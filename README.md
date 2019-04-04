# SVP-PythonPro
Tue Mar 12 15:29:54 2019 +0530

SGVP 394600 | 15:51 12Mar19
Python Projects


JSR! ONS!

SGVP 392000 | 16:17 7Mar19..


Yahoooo!!! 16:27 7Mar
1) git init
2) git reomote add origin "git@github.com:P-N-S/SVP-CPro.git"


3) git pull origin master
ue@DESKTOP-MRH2TK7 MINGW64 /e/GDB Tech 13Feb19/MyGitHub-7Mar19 (master)
$ git pull origin master
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 7 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (7/7), done.
From github.com:P-N-S/SVP-CPro
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> origin/master
 
 
 SGVP409300 | 4 Apr 19
 
 These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Forward-port local commits to the updated upstream head
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

 https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html
 
 Git task 	Notes 	Git commands
Tell Git who you are 	Configure the author name and email address to be used with your commits.

Note that Git strips some characters (for example trailing periods) from user.name.
	git config --global user.name "Sam Smith"

git config --global user.email sam@example.com
Create a new local repository 	  	

git init

Check out a repository 	Create a working copy of a local repository: 	

git clone /path/to/repository

For a remote server, use: 	

git clone username@host:/path/to/repository

Add files 	Add one or more files to staging (index): 	

git add <filename>

git add *

Commit 	Commit changes to head (but not yet to the remote repository): 	

git commit -m "Commit message"

Commit any files you've added with git add, and also commit any files you've changed since then: 	

git commit -a

Push 	Send changes to the master branch of your remote repository: 	

git push origin master

Status 	List the files you've changed and those you still need to add or commit: 	

git status

Connect to a remote repository 	If you haven't connected your local repository to a remote server, add the server to be able to push to it: 	git remote add origin <server>
List all currently configured remote repositories: 	git remote -v
Branches 	Create a new branch and switch to it: 	

git checkout -b <branchname>

Switch from one branch to another: 	

git checkout <branchname>

List all the branches in your repo, and also tell you what branch you're currently in: 	

git branch

Delete the feature branch: 	

git branch -d <branchname>

Push the branch to your remote repository, so others can use it: 	

git push origin <branchname>

Push all branches to your remote repository: 	

git push --all origin

Delete a branch on your remote repository: 	

git push origin :<branchname>

Update from the remote repository 	Fetch and merge changes on the remote server to your working directory: 	git pull
To merge a different branch into your active branch: 	

git merge <branchname>

View all the merge conflicts:

View the conflicts against the base file:

Preview changes, before merging:
	git diff

git diff --base <filename>

git diff <sourcebranch> <targetbranch>

After you have manually resolved any conflicts, you mark the changed file: 	

git add <filename>

Tags 	You can use tagging to mark a significant changeset, such as a release: 	

git tag 1.0.0 <commitID>

CommitId is the leading characters of the changeset ID, up to 10, but must be unique. Get the ID using: 	

git log

Push all tags to remote repository: 	

git push --tags origin

Undo local changes 	If you mess up, you can replace the changes in your working tree with the last content in head:

Changes already added to the index, as well as new files, will be kept.
	

git checkout -- <filename>

Instead, to drop all your local changes and commits, fetch the latest history from the server and point your local master branch at it, do this: 	

git fetch origin

git reset --hard origin/master

Search 	Search the working directory for foo(): 	git grep "foo()"
