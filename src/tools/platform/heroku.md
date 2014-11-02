# Heroku

# Install

download `Tollbelt` and install.

In linux, use the standalone script to install. After that, add in `~/.zshrc`:

```
export PATH="/usr/local/heroku/bin:$PATH"
```

# Usage

```
heroku login
```

# test locally
`npm install` install the dependencies. heroku will install them in the cloud
`foreman start web` start app locally
or `foreman start`

# change & commit & push
make a change

```
git add .
git commit -m 'xxx'
git push heroku master
heroku open
```

## Procfile

a text file in the root directory of your application,
to explicitly declare what command should be executed to start your app.
All heroku command should have a `Procfile` in the current dir.
In this cae, Procfile contains `web: node index.js`

## scale the app
`heroku ps` check the current running app. need a Procfile too.
`heroku ps:scale web=2` change dyno to 2
`heroku ps:scale web=1` change back

# Examples

## Node Example

clone the example nodejs app

```
git clone https://github.com/heroku/node-js-getting-started.git
```

heroku recognizes nodejs app by package.json.

`cd` into the folder, then deploy:

```
heroku create # generate a random name and set up the app in the cloud
# we can use `heroku create <name>` to specify the name we want
git push heroku master # push to the app in the cloud
heroku ps:scale web=1 # make sure at least one instance of the app is running.
heroku open # open browser to see result
```

To view log

```
heroku logs -tail
```

## PHP example

```
heroku login
mkdir php
cd php
touch index.php
touch composer.json

git init
git add .
git commit -m ‘first’

heroku create # have a random name
heroku create byname # custom name

git push heroku master

heroku open
```

# Trouble Shooting

    Heroku 'Permission denied (publickey) fatal: Could not read from remote repository'

```
ssh-keygen -t rsa
heroku keys:add
```

or just

```
ssh-add ~/.ssh/id_rsa
#and, to confirm it's been added to the known list of keys
ssh-add -l
```

to see the list of keys

```
heroku keys
```
