# Linux File System

# Partition

## fdisk

```
sudo fdisk -l [/dev/sda]
sudo fdisk /dev/sda
```

## e2label
Attach label for ex2/3/4.

```
sudo e2label /dev/sda2 [label]
```

list all partition together with their labels

```
ls -l /dev/disk/by-label/
```

# Mount & Umount

When mount many partition for installation, umount all of them by:

```
umount -R /mnt
```

Umount a busy partition:

```
umount -l /dev/sda1
```

# File descriptor

* `/dev/stdxxx`
* `/dev/fd/(012)`

* `0`: stdin
* `1`: stdout
* `2`: stderr
