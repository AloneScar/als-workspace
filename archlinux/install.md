### Verify Boot Mode

```
# ls /sys/firmware/efi/efivars
```

if there is nothing output, please find another tutorial.

## Networking

To prohibit mirror list updated.

```
# systemctl stop reflector.service
```

This step is important, if not, it will be updated your mirror list and you need type it by yourself.

```
# iwctl
# iwctl device list // Get station name -> wlan0
# station wlan0 scan // Scan surrounding wifi
# station wlan0 get-networks // Get surrounding wifi_name
# station wlan0 connect wifi_name // Connect wifi, then type password.
# exit

```
## Edit pacman mirror source
```
# vim /etc/pacman.d/mirrorlist
```

Search `ustc` and note of the two lines.

```
# pacman -Syy
```

## Partition
Use `cfdisk` to partition

```
# fdisk -l // Get disk name -> /dev/partition
# cfdisk disk_name
```

Divided into three areas

- EFI System: 300 MB
- Linux swap: `Physical memory`/2
- Linux filesystem: `Remaining memory`

## Format Partition

```
# fdisk -l // Get disk name -> /dev/partition
# mkfs.ext4 /dev/root_partition
# mkswap /dev/swap_partition
# mkfs.fat -F 32 /dev/efi_system_partition
```

## Mount Partition

```
# mount /dev/root_partition /mnt
# mount --mkdir /dev/efi_system_partition /mnt/boot
# swapon /dev/swap_partition
```

## Install System
### Install linux kernel and some neccessary softwares
```
# pacstrap /mnt linux linux-firmware base base-devel neovim bash-completion intel-ucode grub efibootmgr networkmanager
```

## Generate a table file for the file system

```
# genfstab -U /mnt >> /mnt/etc/fstab
# cat /mnt/etc/fstab
```

## Enter the new system

```
# arch-chroot /mnt
```

## Set time zone

```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc
```

## Set system language

```
# vim /etc/locale.gen
```

`en_US.UTF-8 UTF-8` note off this line

```
# locale-gen
# nvim /etc/locale.conf
```

type `LANG=en_US.UTF-8`

## Networking settings
### Hosts settings

```
# nvim /etc/hostname
```

Type your hostname.

```
# vim /etc/hosts

127.0.0.1   localhost
::1         localhost
127.0.1.1   archlinux.localdomain archlinux
```

`archlinux` is the name of above\`s hostname.

### Enable NetworkManager

```
# systemctl enable NetworkManager
```
Then you can connect wifi use this later.

## Set root password

```
# passwd
```

## Add user

```
# useradd -m -G wheel -s /bin/bash username
# EDITOR=nvim visudo
%wheel ALL=(ALL) ALL note of this line
passwd username
```

## Add archlinuxcn repository

```
# vim /etc/pacman.conf
Note off the end of the file which has multilib and include line.
Then add this under the line
[archlinuxcn]
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
# pacman -Syy
# pacman -S archlinuxcn-keyring
```

## Add startup items

```
# grub-install --target=x86_64-efi --efi-directory=/boot
# grub-mkconfig -o /boot/grub/grub.cfg
```

## Reboot

```
# exit
# umount -R /mnt
# reboot
```

## Connect wifi
```
# nmtui
```

Select `Activate a connection`

## That\`s all, the simplest archlinux has been installed well
