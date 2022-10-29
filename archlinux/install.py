import os
import sys

def operation_help():
    print("help")
    print("setfont")
    print("partitionDisk")
    print("updateSystemTime")
    print("changeMirrorChina")
    print("Please make sure you are root")

def operation_setfont():
    os.system("setfont /usr/share/kbd/consolefontsLatGrkCry-12x22.psfu.gz")

def operation_updateSystemTime():
    os.system("timedatectl set-ntp true")
    os.system("timedatectl status")

def operation_partitionDisk():
    def getPartition():
        partitions = {}
        partitions['root_partition'] = '/dev/' + input("Please type your root_partition: /dev/")
        partitions['swap_partition'] = '/dev/' + input("Please type your swap_partition: /dev/")
        partitions['efi_system_partition'] = '/dev/' + input("Please type your efi_system_partition: /dev/")
        return partitions


    def mountPartitions(isGetPartition, partitions={}):
        if isGetPartition == False:
            partitions = getPartition()
        print("mount %s /mnt" % partitions['root_partition'])
        os.system("mount %s /mnt" % partitions['root_partition'])
        print("swapon %s" % partitions['swap_partition'])
        os.system("swapon %s" % partitions['swap_partition'])
        print("mount --mkdir %s /mnt/boot" % partitions['efi_system_partition'])
        os.system("mkfs.fat -F 32 %s" % partitions['efi_system_partition'])
        
    if input("Please make sure it`s partitioned(y/N): ") == 'y':
        os.system("clear")
        os.system("fdisk -l")
        partitions = getPartition()
        if input("Formatting the partitions now(y/N): ") == 'y':
            print("mkfs.ext4 %s" % partitions['root_partition'])
            os.system("mkfs.ext4 %s" % partitions['root_partition'])
            print("mkswap %s" % partitions['swap_partition'])
            os.system("mkswap %s" % partitions['swap_partition'])
            print("mkfs.fat -F 32 %s" % partitions['efi_system_partition'])
            os.system("mkfs.fat -F 32 %s" % partitions['efi_system_partition'])
            if input("Mounting the partitions now(y/N)") == 'y':
                mountPartitions(True, partitions)
            else:
                return
        if input("Mounting the partitions now(y/N)") == 'y':
            mountPartitions(False)
    else:
        return

def operation_changeMirrorChina():
    pass

# Install archlinux from
# https://wiki.archlinux.org/title/Installation_guide
operation = sys.argv[1]

if operation == 'help':
    operation_help()
elif operation == 'setfont':
    operation_setfont()
elif operation == 'partitionDisk':
    operation_partitionDisk()
elif operation == 'changeMirrorChina':
    operation_changeMirrorChina()
elif operation == 'updateSystemTime':
    operation_updateSystemTime()
else:
    print("Please type help to select which operation")
