[Git官网](http://www.git-scm.com/)

## Git 基础

直接记录快照，而非差异比较
近乎所有操作都在本地执行
时刻保持数据完整性
多数操作仅添加数据
文件的三种状态

* 已修改(midified)
* 已暂存(staged)
* 已提交(committed)
---
## Git文件状态  
Git文件  
    已被版本管理的文件  
已修改  
    在工作目录修改Git文件  
已暂存  
    对已修改的文件执行Git暂存操作，将文件存入暂存区  
已提交  
    将已暂存的文件执行Git提交操作，将文件存入版本库

## Git常用命令
 获得版本库
* git init
* git clone  

查看信息
* git help
* git log
* git diff

版本管理
* git add
* git commit
* git rm

远程协作
* git pull
* git push

创建一个本地的git仓库
<pre><code>
mkdir mygit
cd mygit
git init
</code></pre>

## Git重要命令操练
`git init`  
创建一个空的Git仓库

---
`git add`  
将已修改的文件加入到Git的赞存区当中

---
`git status`  
查看工作区的状态

---
`git -rm --cached <file>...`  
从暂存区回退到已修改状态

---
`git commit`  
从暂存区提交到已提交，直接回车会要求输入提交注释
Git的提交id(commit id)是一个摘要值，这个摘要值实际上是个sha1计算出来的

---
`git config --global user.name "Your Name"`
`git config --global user email "You@example.com"`  
添加用户和用户的邮箱
对于user.name和user.email来说，有3个地方可以设置
1. --system  /etc/gitconfig(几乎不使用，针对整个系统)，优先级最低  
2. --global   ~/.gitconfig(很常用，针对特定的用户),优先级次高
3. --local    .git/config文件中(针对特定项目),优先级最高

---
`git log`  
查看之前的提交记录

---

`git config`  
查看config的全部命令

---
## Git添加、删除、修改与日志  
<pre><code>
/etc/gitconfig --system
~/.gitconfig --global
.git/config --local
</code></pre>
都可以通过git config配置
`git config --global user.name 'Your Name'`  
`git config --global user.email 'You@example.com'`

***要经常使用 `git status`***

---
#### `git rm`和`rm`的区别

`git rm`
1. 删除一个文件
2. 将被删除的文件纳入到暂存区(stage, index)  

若想要恢复被删除的文件，需要进行两个动作
1. `git reset HEAD test2.txt`, 将待删除的文件从暂存区恢复到工作区
2. `git checkout -- text2.txt`将工作区中的修改丢弃掉

`rm`  
将test2.txt删除，这时，被删除的文件并未纳入暂存区当中  
`git rm`和`mv`和`git rm`和`rm`相同

---
#### Git查看提交历史
##### `git log`  
`-p`展开显示每次提交的内容差异  
`-n`仅展示最近的n次更新  
`--stat`仅显示简要的增改行数统计  
`--pretty=oneline`  
`--pretty=format:"%h - %an, %ar:%s"`

##### `git config`的帮助信息  
`git help config`  
`git git config --help`  
`man git-config`  
##### Git初始化新仓库
<pre><code>
mkdir git_traning && cd git_training
git init # 初始化git仓库
</code></pre>
##### 从现有仓库克隆，克隆完整数据， 包括版本信息
<pre><code>
git clone git://github.com/zhanglong/zl.git
git clone git://github.com/zhanglong/zl.git helloworld
</code></pre>
##### 检查当前文件状态
`git status`

---
## `.gitignore`与分支
`vi .gitignore`创建一个gitignore文件，吧需要忽略的文件名或者目录名加入到文件中忽略文件
<pre><code>
*.a # 忽略所有.a结尾的文件
！lib.a但lib.a除外
/TODO #仅仅忽略项目跟目录下的TODO文件，不包括subdir/TODO
build/ #忽略 build/目录下的所有文件
doc/*.txt #会忽略 doc/notes.txt 但不包括 doc/server/arch.txt
</code></pre>

---
## 分支
`git branch`  
列出当前所有的分支  
`git branch new_branch`  
创建一个新的分支  
`git checkout new_branch`  
切换到新的分支  
`git checkout -`  
切换回上一个分支  

---

## 分支重要操作
`git branch`  
查看系统分支  
`git checkout ...`  
切换分支  
`git branch -d`  
删除分支  
`git branch -D`  
忽略改动并且删除分支  
`git checkout -b new_branch4`  
创建一个new_branch4分支并且切换到新的分支  
`git merge new_branch4`  
将new_branch4分支上的修改合并到当前的分支上  
`git branch -v`  
显示出当前所处分支的最近一条提交信息  

---
## 分支的进阶和版本回退
#### fast-forword  
如果可能，合并分支时Git会使用fast-forword模式，在这种模式下，删除分支时会丢掉分支信息
合并时加上`--no-ff`参数会禁用fast-forword，这样会多出一个commit id
`git merge --no-f dev`  
查看log  
`git log --graph`  
#### 版本回退
`git log --graph` 图形显示  
`git log --graph --abbrev-commit`缩写哈希值  
`git log --graph --pretty=online --abbrev-commit`显示一行

#### Git回退版本
###### 回退到上一版本
`git reset --hard HEAD^`  
`git reset --hard HEAD~1`  
`git reset --hard commit_id`  
##### 返回到某一个版本
`git reflog`可以查看所有日志

---
## checkout进阶与stash
`git checkout --test.txt 文件名`  
丢弃掉想对于暂存区中最后一次田间的文件内容所做的变更  
`git reset HEAD test.txt`  
创建一个叫test的分支并立刻切换到它  
`git checkout master`  
切换到一个分支最新的提交点  
`git checkout 9e7f3`  
回退到9e7f3提交点，将处于一个游离的HEAD状态  
`git stash`  
临时保存当前分支的所有状态  
`git stash list`  
列出所有状态  
`git stash save 'hello basic'`  
添加一个说明  
`git stash pop`  
将之前保存的状态恢复过来，然后把该条状态删除掉  
#### 保存工作现场  
保存现场  
`git stash`  
`git stash list`  
恢复现场  
`git stash apply`(stash内容并不删除，需要通过`git stash drop stash{0}`手动删除)  
`git stash pop`(恢复的同时也将stash内容删除)  
`git stash apply stash@{0}`

---
## 标签与diff
#### Git标签
新建标签，标签有两种，轻量级标签(lightweight)与带有附注标签(annotated)  
###### 创建一个轻量级标签
`git tag V1.0.1`  
###### 创建一个带有附注的标签
`git tag -a V1.0.2 -m 'release'`
###### 查看标签
`git tag`
###### 精确查找
`git tag -l 'V'`
###### 删除标签
`git tag -d tag_name`

---
#### 发布系统或者系统里程碑的时候创建标签
`git blame`  
查看文件上次是谁修改的  
`git diff`  
比较工作区和暂存区文件的差别  
`git diff HEAD`  
比较的是最新的提交和工作区的差别  
`git diff --cached`  
比较暂存区和最新的提交的差别  
`git diff --cached commit_id`  

---
## 远程与GitHub
push 推送  
pull拉取，同时会执行合并merge  
pull = getch + merge  

---
## Git远程操作
`git remote show`  
显示远程仓库的别名  
`git remote show origin`  
显示关联的远程仓库的详细信息
1. Gitflow, 一种建议和参考
2. 基于Git分支的开发模型:
    * develop分支(频繁变化的一个分支)
    * test分支(供测试与产品等人员使用的一反而分支变化不是特别频繁)
    * master分支(生产发布分支，变化非常不频繁的一个分支)
    * bugfix(hotfix)分支(生产系统当中出现了紧急BUG，用于紧急修复的分支)

#### git最推荐远程使用SSH的协议
<pre><code>
git remote add origin SSH_URL
git remote origin
</code></pre>
使用SSH上传到github
windows上使用PuTTY，可以使用整个一套的SSH命令
<pre><code>
cd
cd .ssh
vi know_hosts
which ssh-keygen
//生成SSH密钥
ssh-keygen
连续回车
cd .ssh //查看公钥私钥
</code></pre>
将公钥放置在github上setting-Deploy keys

---
## Git协作
`git remote show`  
查看远程信息  
`git pull`  
从远程拉取文件  
`git branch -a`  
列出所有分支，包括远程分支  

---
#### 远程协作模型
`git branch -av`  
把提交信息和最后一次提交的sha1值列出来

---
`git clone URL`  
将远程仓库clone到本地  
`git clone URL gitname`  
将gitname作为文件夹的名字  
`git remote show origin`  
会提示local out of date  
需要执行`git pull`

---
#### fast-forword(快进)
如果修改没有冲突则可以进行快进  

---
不要用
`git add *`这样会忽略`.gitignore`文件，用`git add .`代替

---
关于git分支最佳实践
1. 通常来说，Git分支会有如下几种

    + master分支，用于生产的分支
    + test分支，测试分支
    + develop分支，变化最频繁的分支，开发都在develop上开发
    + hotfix, 如果线下出问题了，立即从master分支拉出一个分支

---
## Git远程分支、别名、gitk与git gui
`gitk`  
进入git自带的图形界面  
***有问题进入Stack Overflow进行搜索，基本都能找到答案***  
`git gui`  
进入gui界面

---
## Git refspec
#### git别名
`git config --global alias.br branch`  
##### 创建别名
可以手写缩写配置文件  
`vi ～/.gitconfig`  
但是不建议手写，用命令的方式来修改  
`git config --global alias.unstage 'reset HEAD'`  
#### 创建分支并却换到该分支  
`git checkout -b develop`  

---
To push the current branch and set the remote as upstream,use
<pre><code>
git push --set-upstream origind develop
git checkout -b develop origin/develop
</code></pre>
#### 新建一个develop追踪来自origin/develop分支
<pre><code>
git push -u origin test
git checkout --track origin/test
</code></pre>
默认起一个和远程分支相同的名字的分支  
`git branch -d develop`  
#### 删除一个本地分支  
`git push`的完整写法:`git push origin src:dest`  
`git push origin: develop`  
将本地的一个空分支push到远程，相当于删除develop分支  
`git push --delete develop`  
新版本的删除远程分支的做法
<pre><code>
git push origin HEAD:develop2
git push origin develop
</code></pre>
`git push origin develop:develop2`  
将本地的develop分支上的内容推送到远程的develop2上，也是push命令最完整的写法  
重命名本地分支比较复杂，先删除远程分支，然后再推送一个新的分支

---
## Git refspec与远程标签
本质上表示本地分支与远程分支的对应关系  
`git remote show origin`  
push 操作的完整命令是`git push origin srcBranch:destBranch`  
`srcBranch`表示本地分支  
`destBranch`表示远程分支  
表示将本地的原分支推送到远程的目标分支  
pull操作的完整命令是`git pull origin srcBranch:destBranch`  
`srcBranch`表示远程分支  
`destBranch`表示本地分支  
表示将远程分支关联到本地分支  

---
HEAD标记:HEAD文件是一个指向当前所在分支的运用标识符，该文件内部并不包含sha-1值，而是一个指向另外一个引用的指针  
当执行`git commit`命令时，git会创建一个commit对象，并且将这个commit对象的parent指针设置为HEAD所指向的引用的sha-1值  
我们对于HEAD修改的任何操作，都会被`git reflog`命令完整的记录下来，如果手工修改HEAD文件，信息不会被记录下来，是非常危险的  
实际上，我们可以通过git底层命令symbolic-ref来实现对HEAD文件内容的修改，但是也不会被保存  
<pre><code>
git symbolic-ref HEAD // 读取HEAD文件
git symbolic-ref HEAD refs/heads/develop // 且还到develop分支
</code></pre>

---
轻量级标签  
`git tag {v1.0}`  
列出所有的标签  
`git tag`  
创建带注释的标签  
`git tag -a v2.0 -m 'v2.0 released'`  
查看标签  
`git show v1.0`  
`git tag -l '?2*'`  
将v1.0标签从本地推送到远程  
`git push origin --tags`  
把两个标签同时推送  
`git push origin --tags`  
将本地所有未推送的标签全部推送到远程  
其他人怎么获取标签?  
`git pull`  
会把所有标签加载到本地

---
## Git远程分支底层剖析
删除远程标签，和删除分支的操作很类似  
将一个空的原标签推送到远程，就把标签删除了  
`git push origin :refs/tags/v6.0`  
删除远程的v6.0标签，其他用户的标签是没有删除的  
`git push origin --delete tag v5.0`  
删除掉v5.0标签，本地仍然有v5.0标签，删除  
`git tag -d v5.0`  
可以删除本地标签  
将本地标签推送到远程的完整写法是  
`git push origin refs/tags/v7.0:refs/tags/v7.0`  
`git fetch origin tag v7.0`  
将远程标签回到本地分支  
`git remote prune origin`  
清除不用的远程分支  
1. 在缺省情况下，refpec会被`git remote add`命令所自动生成，git会获取远端上refs/heads下的所有引用，并将它们写到本地的refs/remote/origin目录下，所以如果远端上有一个master分支，你在本地就可以通过下面集中方式来访问他们的历史记录  
<pre><code>
git log origin/master
git log remotes/origin/master
git log refs/remote/origin/master // 最完整方式
</code></pre>
获取远程分支的信息  
分支信息在`.git/refs`中，远程分支都位于remotes目录下  
轻量级标签不会创建tag对象，不会创建sha-1值  
`git fetch origin master:refs/remote/origin/mymaster`  
拉取一个远程分支，创建一个名字不同的本地远程分支  

---
## Git gc Git裸库与submodule
`git gc`  
Git裸库：没有工作区的Git仓库，一般在服务器端使用Git裸库，做文件传输的中介和代码的托管  
`git init --bare`  
创建一个裸库，没有工作区  
github针对整个帐号的sshkey，在帐号的setting中设置  
`git sumbodule add git@github.com:ssilverch/child.git mymodule`  
将远程的被依赖的库拉取过来之后放在一个事先不存在的目录中，上例将远程的child拉取到本地的mymodule目录中  
如果模块有修改，可以直接用`git pull`拉取同步，需要进入到子模块中执行  
可以在不进入模块目录时，使用  
`git submodule foreach git pull`  
更新所有的子模块  
克隆带有sumbodule的仓库时不能克隆模块
<pre><code>
git clone url your_name
cd mymodule
git submodule init
git submodule update --recursive
</code></pre>
或者用  
`git clone url your_name --revursive`  
可以将子模块一并克隆下来  
#### 删除module
<pre><code>
git rm --cached mydule
rm -rf mydule
git add .
git commit -m 'remove some module'
</code></pre>

---
## Git subtree
与git submoldule要解决的是同样的问题  
`git subtree`  
可以列出subtree常用命令  
`git remote subtree-origin git@github.com:ssilverch/child.git`  
增加一个新的远程库  
`git subtree add --prefix=subtree subtree-origin master --squash`  
调用命令，放在subtree  
`--squash`把远程的多次提交合并为一次提交，远程的提交丢失  
`git subtree pull --prefix-subree subree-origin master --squash`  
更新本地subtree  
`--squash`

---

## Git subtree原理深度剖析，Git cherry-pick
### Git cherry-pick
将对某个分支的修改应用到另外一个分支上  
如在develop分支上修改，发现改错了，需要改到test分支上  
在test分支上使用命令  
`git cherry-pick commit_ID`  
可以将修改应用到test分支上

---
## Git rebase原理深度剖析
rebase含义  
变基，意即改变分支的根基  
衍合  

---
rebase的功能类似merge，不过二者的工作方式有着显著的差异
<pre><code>
git checkout myword
git rebase origin
</code></pre>
rebase 注意事项  
rebase过程中也会出现冲突  
解决冲突后，使用`git add`添加，然后执行  
`git rebase --continue`  
接下来Git会计算应用与下的补丁  
任何时候都可以通过如下命令终止rebase，分支会恢复到rebase开始前的状态  
`git rebase --abort`  
rebase最佳实践  
不要对master分支执行rebase，否则会引起很多问题  
***一般来说，执行rebase的分支都是自己的本地分支，美欧推送到远程版本库***

---
## GitLab安装和部署
GitLab配置信息在 `/etc/gitlab/gitlab.rb`  
1. 配置external_url, 必需配置为域名或者正确的ip地址
2. 配置完之后执行 gitlab-ctl reconfigure，使配置成效

---


