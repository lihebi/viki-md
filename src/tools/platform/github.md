Git
======================================

Small Tips
--------------------------------------

* `github search stars:>100`: search for most starred projects on github
* `git diff`: see what is changed but not staged
* `git diff --cached`: see what is staged that will go into next commit
* `git rm a.txt`: remove it from tracked files **AND** remove the file in current dir
* `git rm --cached a.txt`: remove it from tracked files only. Keep it in current dir

Configure
--------------------------------------

* `git config --list`: check your setting
* `git config user.name`: check user.name setting

User Identity

```
git config --global user.email 'xxx@xxx'
git config --global user.name 'xxx'
```

Credential

```
git config --global credential.helper cache # cache 15 min by default
git config --global credential.helper 'cache --timeout=3600' # set in sec
```

a better log

```
git config --global alias.lg \
"log --color --graph
--pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'
--abbrev-commit"
```

Concepts
--------------------------------------

* 工作区(working directory): 你当前看到的目录
* 暂存区(staging area): git add 后,将会放到此处,commit会放到版本库.
* 版本库(git directory): `.git`文件夹中的内容

Local Operations
--------------------------------------

### stage file

* `git add -u`: add all deleted files for commitment. It will NOT add untracked file.

### Commit file

### checkout file

remote
--------------------------------------

### add & remove

```
git remote add origin https://github.com/lihebi/xxx.git
git remote rename pb paul # will change remote branch names automatically
git remote rm paul
```

### check

* `git remote`: list all remotes as shortnames
* `git remote -v`: show the URL that git has stored for the shortname
* `git remote show origin`: show detail for origin remote

### fetch

fetch all info that pb has but I don't.

```
git fetch pb
```

now pb's master branch is accessible locally as `pb/master`. Merge it into your branch.

fetch only download. Never merge for you.

`git pull` will do merge.

### push

```
git push
git push origin master
git push -u origin master
```

关于`-u`的解释

使用git push -u origin master以后就可以直接使用不带别的参数的git pull从之前push到的分支来pull。

加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，
还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。

所以说,第一次push的时候还是加上`-u`,以后才能用`git push origin master`用的放心.


分支
--------------------------------------

### Create and Delete

* `git branch` # 列出所有分支
* `git branch xxx` # 新建
* `git checkout [branch]` # 切换
* `git push origin [branch]`
* `git checkout -b [branch]` # 新建并切换
* `git branch -d [branch]` # 删除本地分支
* `git branch -D <branch>` # 强制删除没有被merge的分支
* `git push origin --delete [branch]` # 删除remote的分支


不能delete current branch.
在项目的`settings`中可以改变`default branch`
然后再

```
git push origin —delete master
```

### merge

* `git merge [branch]`: merge [branch] into current branch.

### 本地分支和远程分支

创建时关联

```
git checkout -b dev origin/dev
```

后期关联

```
git branch --set-upstream dev origin/dev
```


### 图形查看分支情况

```
git log --graph
```

tag
--------------------------------------

* `git tag`: 查看tag
* `git tag -l 'v1.4.2.*'`: list only what we want
* `git show <tagname>`: 查看一次tag的详细信息
* `git tag v1.0`: tag current branch's last commit
* `git tag v1.0 <commit ID>`: tag specific commit(need only the first several bits)
* `git tag -a v1.0 -m 'this is a tag'`: annotated tags. `-a` for tag name, `-m` for tag commit
* `git tag -d v1.0`: delete tag
* `git push origin v1.0`: push tag to remote
* `git push origin --tags`: push all tags to remote

若标签已经推送到远程,则删除:

```
git tag -d v1.0
git push origin :refs/tags/v1.0
```

版本回退
--------------------------------------

### change last commit
* `git commit --amend`: editor open with the pervious commit. It will overwrite the previous one.

Can be used for add more file for last commit:

```
git add forgotten_file
git commit --amend
```

### discard changes in working directory (DANGEROUS!!)

使用`HEAD`(版本库)中最新的内容替换此文件。已添加到缓存区和新文件不受影响。

```
git checkout -- [filename]
```

### Unstage a file

```
git reset HEAD <filename>
```

### 丢弃本地所有的改动与提交

到服务器上获取最新版本，并将本地主分支指向它。

```
git fetch origin
git reset --hard origin/master
```

### 整个本地版本库重置

```
# 获取commit id
git log
git log --pretty=oneline --abbrev-commit
# 执行reset
git reset --hard <tag/branch/commit id> # commit ID 不必写全,写前几个字母就行了.
```

`git push`后，`reset —hard`再`push`会出错。提示要`git pull`

也可以使用相对版本.`HEAD`是当前版本.`HEAD^`是上一个版本.`HEAD^^`是上上个版本.`HEAD~100`上上100个版本.

```
git reset --hard HEAD^
```

后悔了,还是把reset之前的状态找回来把.

```
git reflog # 列出每一次命令的commit 和 id
git reset --head <commit ID>
```

.gitignore
--------------------------------------

```
# a comment
*.a
!lib.a
/TODO # root TODO file, not sub/TODO file
build/ # all files in build dir
doc/*.txt # all txt file in doc dir. not doc/sub/a.txt
doc/**/*.txt # all txt file in doc dir recursively.
```

submodule
--------------------------------------

```
git submodule add xxx
git submodule init
git submodule update
```

pull request
--------------------------------------

1. fork
2. git clone https://github.com/lihebi/xxx
3. cd xxx
4. git remote add upstream https://github.com/origin/xxx.git
5. git fetch upstream
6. git merge upstream/master
7. git add .
8. git commit -m ‘xxx’
9. git push origin master
10. in my repo, create pull request

搭建git服务器
--------------------------------------

### 搭建

```
sudo apt-get install git
sudo adduser git
```

收集用户的公钥(`id_rsa.pub`),导入`/home/git/.ssh/authorized_keys`,一行一个

初始化git仓库

```
cd /srv
sudo git init --bare sample.git
sudo chown -R git:git sample.git
```

在`/etc/password`中设置git用户不允许登陆shell

### 使用

```
git clone git@server:/srv/sample.git
```
