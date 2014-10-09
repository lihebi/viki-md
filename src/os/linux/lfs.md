# Linux From Scratch In Action

# Partition

Total used: 500G

* `sda1`: `/boot`, 200M
* `sda4`: extended. Include all logical partition. 500G
* `sda5`: `/`, 50G
* `sda6`: `/usr`, 10G. Provide a server for a thin client or diskless workstation.
* `sda7`: `/opt`, 20G. Useful in BLFS when install large packages like GNOME.
* `sda8`: `/tmp`, 4G. useful if configuring a thin client. Rarely used.
* `sda9`: `/usr/src`, 80G. Useful for provide location to store BLFS source files and share them across LFS build
* `sda10`: `/home`, 350G

Format: all partitions use `ext4`.

```
sudo mkfs -v -t ext4 /dev/sda1
```

Mount partition

```
sudo mkdir -pv /mnt/lfs
sudo mount -v -t ext4 /dev/sda5 /mnt/lfs
sudo mkdir -pv /mnt/usr
sudo mount -v -t ext4 /dev/sda6 /mnt/usr
#...
```

# Download Packages

```
mkdir -v $LFS/sources
chmod -v a+wt $LFS/sources # writable and sticky(many write but only owner can delete)
wget -i wget-list -P $LFS/sources # wget-list can be downloaded from LFS website
```

# Final Preparation

```
sudo mkdir -v $LFS/tools
ln -sv $LFS/tools / # <=> ln -sv /mnt/lfs/tools /tools
```

Add lfs user and group:

```
groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs
passwd lfs
chown -v lfs $LFS/tools
chown -v lfs $LFS/sources
su - lfs
```

Set up env for lfs

```
cat > ~/.bash_profile << "EOF"
exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash
EOF
```

```
cat > ~/.bashrc << "EOF"
set +h
umask 022
LFS=/mnt/lfs
LC_ALL=POSIX
LFS_TGT=$(uname -m)-lfs-linux-gnu
PATH=/tools/bin:/bin:/usr/bin
export LFS LC_ALL LFS_TGT PATH
EOF
```

```
source ~/.bash_profile
```

Dual Core:

```
export MAKEFLAGS='-j 2'
```

or just build with

```
make -j2
```

# Build Temporary System

## Binutils

```sh
cd $LFS/sources
tar xvf binutils-2.24.tar.gz # what about patch?
mkdir -v ../binutils-build
```
