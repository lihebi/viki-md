# Awesome Window Manager

# Shortcuts

Control

* `Mod-C-r`: restart
* `Mod-S-q`: quit
* `Mod-r`: run prompt
* `Mod-return`: open terminal emulator

Client

* `Mod-m`: maximize client
* `Mod-n`: minimize client
* `Mod-f`: full screen
* `mod-<mouse-right>`: resize in float mode on not maxized client
* `mod-<mouse-left>`: move

Navigation

* `Mod-j`: Focus next client
* `Mod-k`: Focus previous client

Move tag

* `Mod-S [1-9]`: move current panel to tag [1-9]
* `Mod-C [1-9]`: join/remove tag [1-9] from current selection. Will display windows of every tag.
* `Mod-C-S [1-9]`: **COPY/REMOVE** current window to panel [1-9]. Close each of them will result in close all.
* `mod-o`: move to next screen





## Multi Monotors

Query Monitors

```
xrandr -q
```

output this:

```
Screen 0: minimum 8 x 8, current 1280 x 1024, maximum 32767 x 32767
HDMI1 connected 1280x1024+0+0 (normal left inverted right x axis y axis) 376mm x 301mm
   1280x1024     60.02*+  75.02  
   1152x864      75.00  
   1024x768      75.08    60.00  
   800x600       75.00    60.32  
   640x480       75.00    60.00  
   720x400       70.08  
VGA1 connected 1280x1024+0+0 (normal left inverted right x axis y axis) 376mm x 301mm
   1280x1024     60.02*+  75.02  
   1152x864      75.00  
   1024x768      75.08    60.00  
   800x600       75.00    60.32  
   640x480       75.00    60.00  
   720x400       70.08  
VIRTUAL1 disconnected (normal left inverted right x axis y axis)
```

Do it:

```
xrandr --output VGA1 --mode 1280x1024 --left-of HDMI1
```

turn one down:

```
xrandr --output VGA --off
```
