xmodmap
================

Expression mode
------------------

```
xmodmap -e "remove Lock = Caps_Lock"
```

Conf file mode
----------------------

use along with `xmodmap ~/.Xmodmap`. No need to write in `~/.xinitrc`, it will apply automatically.

map capslock to control_L

```
remove Lock = Caps_Lock
keysym Caps_Lock = Control_L
add Control = Control_L
```
or

```
keycode 66 = Control_L
clear Lock
add Control = Control_L
```

change capslock and control_L

```
remove Lock = Caps_Lock
remove Control = Control_L
keysym Control_L = Caps_Lock
keysym Caps_Lock = Control_L
add Lock = Caps_Lock
add Control = Control_L
```

Pointer
----------------------

```
pointer = 1 2 3 5 4
```
