# Buffer tmp for viki articles.


`xrdb .Xresources` to let the config for xterm take into effect.

git config --global credential.helper cache # cache 15 min by default
git config --global credential.helper 'cache --timeout=3600' # set in sec


# terminal simulator

## xcompmgr & transset

```
sudo pacman -S xcompmgr transset-df
```

Add to .shrc

```
transset-df -a > /dev/null
```

start a composite manager(xcompmgr for example)

```
xcompmgr -c &
```
