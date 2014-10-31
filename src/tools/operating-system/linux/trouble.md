# trouble in linux

## glibc 2.14+(2.19) in debian

add to sourcelist

```
deb http://ftp.debian.org/debian sid main
```

then update

```
sudo apt-get update
sudo apt-get install libc6
```

verify the change

```
ls -l `locate libc.so.6
```

remove the line in sourcelist, or the whole system will update to version sid.
