# Arch Linux Installation Steps

# Partition

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

# Install Base System

```
vim /etc/pacman.d/mirrorlist
pacstrap -i /mnt base
genfstab -U -p /mnt >> /mnt/etc/fstab
```

# Chroot and Configure

```
arch-chroot /mnt
vi /etc/locale.gen
locale-gen
```
