# Buffer tmp for viki articles.

## Database

### concepts

* `attribute`: column name
* `relation scheme`: a set of attributes
* `tuple`: S is a scheme. A tuple over S is an assignment of values to attributes of S.
* `superkey`: a set of attributes that identify tuples uniquely
* `key`: a minimal set of attributes that form a superkey
    * a key can have multiple attributes, for example, `{CourseCode, StudentID}`.
    * a relation can have multiple keys. `r(A,B,C,D,E)` can have `{A,B,C}` and `{B,D}` as its key
* `primary key`: impose an ordering of tuples in a relation. Only one primary key.
* `foreign key`: a foreign key should be a primary key in some other relations.

### operations

* `selection operator`: select tuples of r that satisfy condition c

```katex
\rho_c(r)
```

* `projection operator`: retains only X columns. X can be AC, to choose column A and C from r to form a new table.

```katex
\prod_X(r) = {x[X]:x\inr}
```

| A | B | C |
| :---: | :---: | :---: |
| 1 | 2 | 4 |
| 5 | 4 | 2 |
| 5 | 6 | 2 |
| 7 | 8 | 3 |


# demo for 7

```
printf ("hello world\n");
```

**HELLO** *7*
hello `world` !

# awesome

* `mod-o`: move to next screen

* `mod-<mouse-right>`: resize in float mode on not maxized client
* `mod-<mouse-left>`: move

# atom

`~/.atom/keymap.cson`

```
'.editor':
  'ctrl-n': 'core:move-down'
  'ctrl-p': 'core:move-up'
  'ctrl-b': 'core:move-left'
  'ctrl-f': 'core:move-right'
  'ctrl-d': 'core:delete'
  'ctrl-h': 'core:backspace'
```

# git

add all deleted files for commitment:

```
git add -u
```

it will not add untracked files, so I still need:

```
git add .
```

# js

```
data.replace(/\\"/g, '"');
```

# glibc 2.14+(2.19) in debian

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

# acpi

```
acpi -i
```

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

# ffmpeg
m4a to mp3

```
ffmpeg -v 5 -y -i input.m4a -acodec libmp3lame -ac 2 -ab 192k output.mp3
```

`fc-list` 查看字体名称
`fc-match <mono>` 查看字体信息（应该）


# ruby

```
rvm list known
rvm install 2.1
rvm use 2.1
rvm --default use 2.1.1
```

