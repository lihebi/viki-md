# Buffer tmp for viki articles.


`xrdb .Xresources` to let the config for xterm take into effect.

# Github

```
git config --global credential.helper cache # cache 15 min by default
git config --global credential.helper 'cache --timeout=3600' # set in sec
```


# terminal simulator

## xcompmgr & transset

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

# vim

```
:setfiletype python
```

# python

Dictionary is arbitrary sorted.
To get a sorted dict, use collections.OrderedDict.
It remembers the order in which the elements have been inserted.

```python
import collections
od = collections.OrderedDict(sorted(d.items()))
```
