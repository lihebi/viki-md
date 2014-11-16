Node Package Manage
===================

Tips
-------------------------

```
npm install <xxx> --save
npm install <xxx> --save-dev
```

NPM Publish my own package
--------------------------

### 1. create a repo
including `package.json`, `index.js`.
Can use `npm init` to create package.json.

### 2. test
In another folder, run

```
npm install ../hebi-cloudstore
```

to install, and then test

### 3. register and login
register on npm website.

Then in commandline:

```
npm adduser
```

### 4. publish

```
npm publish
```
