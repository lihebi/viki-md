# xinit

`~/.xinitrc`

keyboard remapping

```
# natural scrolling
xmodmap -e "pointer = 1 2 3 5 4"
```

input method

```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
fcitx&
```

xterm configure load

```
xrdb ~/.Xresources
```

xcompmgr for enhanced display

```
xcompmgr -c &
```

screensaver

```
xscreensaver &
```

Window Manager

```
exec awesome
```
