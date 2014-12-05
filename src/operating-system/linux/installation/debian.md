# GNU/Debian Installation

# Get ISO

Get ISO for CD.

# Burn on USB

```
cp debian.iso /dev/sdb
sync
```

# Install

Follow Instructions.

# After Installation config

## sources.list

Search for a online generator for sources.list, and then

```
apt-get update
```

## wifi

```
apt-get install wireless-tools
apt-get install network-manager
apt-get install wpasupplicant # for wpa2 auth
apt-get install net-tools
apt-get install ethtool # for ifconfig
```

Install driver for PCI device

When issue `lspci`, I saw

```
Network controller: Intel Corporation Centrino Wireless-N 1000 [Condor Peak]
```

And search for `wifi debian`, on the wiki, match it to `iwlwifi`, so:

```
apt-cache search iwlwifi
apt-get install firmware-iwlwifi
```

Then reload module:

```
modprobe -r iwlwifi ; modprobe iwlwifi
```

## sudo

```
apt-get install sudo
export EDITOR=vim
visudo
```

Add to `/etc/sudoers` by `visudo`:

```
hebi ALL=(ALL:ALL) ALL
```

## Awesome

```
apt-get install awesome
```

It will appear in lightdm's menu automatically(`/user/share/xessions/awesome.desktop`)

Make it default, in `/etc/lightdm/lihgtdm.conf`:

```
[SeatDefaults]
user-session=awesome
```

## Use Text Terminal!

Default runlevel is 2, in `/etc/inittab`:

```
id:2:initdefault:
```

In `/etc/rc2.d`:

```
mv S18lightdm K18lightdm
update-rc.d lightdm defaults
```

It will be renamed automatically to K01lightdm

## xmodmap

in `~/.xinitrc`:

```
xmodmap -e "pointer = 1 2 3 5 4" # natural scrolling
# CapsLock to Control
xmodmap -e "keycode 66 = Control_L"
xmodmap -e "clear Lock"
xmodmap -e "add Control = Control_L"
```

## default browser

```
update-alternatives --config gnome-www-browser # maybe x-www-browser
```
