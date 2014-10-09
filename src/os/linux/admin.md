# Admin in Linux

# User Manage

## `adduser` versus `useradd`

`adduser` is low-level command. `useradd` is friendly.
In many system, `adduser` is the same as `useradd`.
They refer to the same man page.

### useradd

```
useradd -D # list default setting
useradd hebi # add the user
useradd hebi -m -groups sudo # -m: create home
useradd -aG sudo hebi # add another group "sudo" for hebi

usermod -s /bin/bash hebi

useradd -d /home/kevin -s /bin/bash -m kevin
```
