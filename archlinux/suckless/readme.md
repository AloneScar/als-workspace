# suckless

## dwm

## st
1. Download `Simple Terminal`

```
git clone https://git.suckless.org/st
```

2. Download Diff
```
axel http://st.suckless.org/patches/alpha/st-alpha-20220206-0.8.5.diff
axel http://st.suckless.org/patches/anysize/st-anysize-20220718-baa9357.diff
```

3. Patch Diff
```
patch < st-anysize-20220718-baa9357.diff
patch < st-alpha-20220206-0.8.5.diff
```

4. Install
```
sudo make install clean
mv my_st/config.h your_st/config.h
sudo make install clean
```

## slstatus

## dmenu
