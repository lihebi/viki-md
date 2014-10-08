# Node Package Manage

```
npm install <xxx> --save
npm install <xxx> --save-dev
```

# NVM

```
nvm install 0.10 # install latest 0.10.x release
nvm use 0.10 # use 0.10 as current(but not last)
nvm ls # list all available locally
nvm ls-remote # list all on remote server
nvm alias default 0.10 # set 0.10 as default
```

# NPM Publish my own package

## 1. create a repo
including `package.json`, `index.js`.
Can use `npm init` to create package.json.

## 2. test
In another folder, run

```
npm install ../hebi-cloudstore
```

to install, and then test

## 3. register and login
register on npm website.

Then in commandline:

```
npm adduser
```

## 4. publish

```
npm publish
```
