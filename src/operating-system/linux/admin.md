# Admin in Linux

# User Manage

## `adduser` versus `useradd`

`useradd` is low-level command. `adduser` is friendly, often used in Debian.
In many system, `adduser` is the same as `useradd`.
They refer to the same man page.

### useradd(important)

```sh
useradd -D # list default setting
useradd hebi # add the user
useradd hebi -m -groups sudo # -m: create home
useradd -aG sudo hebi # add another group "sudo" for hebi

usermod -s /bin/bash hebi

useradd -d /home/kevin -s /bin/bash -m kevin
```

Groups:

* `wheel`: Administration group, commonly used to give access to the sudo and su utilities
