Ubuntu
=============

lightdm
---------------

The default display manager is lightdm.

To stop it:

```
sudo /etc/init.d/lightdm stop
sudo /etc/init.d/lightdm start
```

Trouble Shooting
-------------------------------

When use `startx`, it can be too slowly due that there exists `~/.XAuthority`. DELETE IT!!!

Change Grub to text mode
------------------------

`/etc/default/grub`, change

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

to

```
GRUB_CMDLINE_LINUX_DEFAULT="text"
```

Then run

```
sudo update-grub
```

No need to delete lightdm entry in `/etc/init.d`, lightdm will check if it is in text mode.

