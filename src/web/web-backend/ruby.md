
# RVM

## Install

```sh
curl -L https://get.rvm.io | bash -s stable --autolibs=enabled —ruby —rails

# make sure dvm is up-to-date
rvm get head
```

## Install ruby

```sh
# install a version of ruby
rvm install ruby-1.9.3-p125
# the same as
dvm install 1.9.3 # dvm will fetch the latest patched version
```

## Use ruby

```sh
rvm list
# use
rvm use ruby-1.9.3-p125
# the same as
rvm 1.9.3
# make 1.9.3 your default
rvm 1.9.3 --default
# the same as
rvm --default use 1.9.3
```
