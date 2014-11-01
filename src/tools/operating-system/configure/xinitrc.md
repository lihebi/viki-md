# xinit

`~/.xinitrc`

keyboard remapping

```
# natural scrolling
xmodmap -e "pointer = 1 2 3 5 4"
# caps_lock to ctrl
xmodmap -e "keycode 66 = Control_L"
xmodmap -e "clear Lock"
xmodmap -e "add Control = Control_L"
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
