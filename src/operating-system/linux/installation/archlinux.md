# Arch Linux Installation Steps

## Partition

```
gdisk /dev/sda
```

```
n -> 1 -> enter -> +200M -> EF00 # /boot
n -> <enter> -> <enter> -> +100G -> 8300<enter> # /
n -> <enter> -> <enter> -> +200G -> 8300<enter> # /home
```

```
mkfs.ext4 /dev/sda2
mkfs.ext4 /dev/sda3
mkfs.fat -F32 /dev/sda1
```

mount them.

## Install Base System

```
vim /etc/pacman.d/mirrorlist
pacstrap -i /mnt base
genfstab -U -p /mnt >> /mnt/etc/fstab
```

## Chroot and Configure

```
arch-chroot /mnt
vi /etc/locale.gen
locale-gen
echo LANG=your_locale > /etc/locale.conf
echo computer_name > /etc/hostname
mkinitcpio -p linux
passwd

# A hostname is a unique name created to identify a machine on a network
# hostname myhostname # => set temporary until reboot
ln -sf /usr/share/zoneinfo/zone/subzone /etc/localtime
```

## Grub

```
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=arch_grub --recheck --debug
```

## Network

```
ip link
systemctl enable dhcpcd@interface_name.service
```

Install `ifconfig`:

```
pacman -S net-tools
```

## Xorg

```
pacman -S xorg
pacman -S xorg-xinit # provide startx
pacman -S xf86-video-intel
pacman -Ss twm, xclock, xterm
startx
pkill X
```

## Utils

```
pacman -S mlocate # updatedb and locate
```

## After Installation

Chinese Font

```
pacman -Ss wqy
```

Natual scrolling for xorg

```
xmodmap -e "pointer = 1 2 3 5 4"
```

### xcompmgr & transset

```
sudo pacman -S xcompmgr transset-df
```

Add to .shrc

```
# because when X is not started, run transset will result in error.
# In the true terminal, $TERM is set as "linux"
# When use terminal emulator, $TERM is set as name specified by the emulator.
# So it can be used in every emulator, including "xterm" and "urxvt"
[ $TERM != "linux" ] && transset-df -a > /dev/null
```

start a composite manager(xcompmgr for example). Just add this to `.xinitrc`

```
xcompmgr -c &
```

## Pacman

### AUR

1. download tar ball
2. tar zxvf
3. cd & makepkg -s
4. pacman -U xxx.tar.xz
