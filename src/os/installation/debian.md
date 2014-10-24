# GNU/Debian Installation

# Get ISO

Get ISO for CD.

# Burn on USB

```
cp debian.iso /dev/sdb
sync
```

# Install

Follow Instructions.

# After Installation config

## sources.list

Search for a online generator for sources.list, and then

```
apt-get update
```

## wifi

```
apt-get install wireless-tools
apt-get install network-manager
apt-get install wpasupplicant # for wpa2 auth
apt-get install net-tools
apt-get install ethtool # for ifconfig
```

Install driver for PCI device

When issue `lspci`, I saw

```
Network controller: Intel Corporation Centrino Wireless-N 1000 [Condor Peak]
```

And search for `wifi debian`, on the wiki, match it to `iwlwifi`, so:

```
apt-cache search iwlwifi
apt-get install firmware-iwlwifi
```

Then reload module:

```
modprobe -r iwlwifi ; modprobe iwlwifi
```
