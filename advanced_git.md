# Advanced git

re-visit the basics and build upo them

### to learn
* [interactive rebase](#interactive-rebase)
* [cherry picking](#cherry-picking)
* [reflog](#reflog)
* [submodules](#submodules)
* [search and find](#search-and-find)

### interactive rebase
* a tool to optimise and clean up commit history
    * change a commit message
    * delete commits
    * reorder commits
    * combine multiple commits into a single new one
    * edit/split an existing commit into multiple new ones
* **Disclaimer:** Do not use interactive rebase on commits that have been pushed/shared on a remote repository. Use it to clean your local commit history before merging it to a shared team branch
#### the flow
* what should the _base_ be?
    * how far back in history do you want to go?
* assume you want to go back 3 commits in time 
 
    ~~~bash
    git rebase -i HEAD~3
    ~~~

* in the editor,  _determine_, do not _perform_ the actions that are required
    * do not change the commit data in this step
* perform the ctions you want
* verify that said changes occurred
#### example 1: change a commit message
* a fictitious workspace; idea is to change a commit message
    * there are seven commits viz
        1. de135b4 (HEAD -> main) improve headline for `imprint`
        2. 7b2317c change page structure
        3. 6bcf266 (origin/feature/login) optimise markup structure in index page
        4. 2b504be (origin/staging) change headlines for `About` and `Imprint`
        5. 0023cdd add simple `robots.txt`
        6. 113adcc add jquery javascript resource
        7. fcd6199 initial commit
* run `git log` to see what git log contains

~~~bash
git log --oneline
~~~

* determine how far back in history you want to go. in this case, three commits before `HEAD` (the latest one). zero-based indexing; `HEAD` is zero. three commits before the latest means `HEAD~3` (_tilde_, not _hyphen_). you move to the commit right before the one you want to change

~~~bash
git rebase -i HEAD~3
~~~

expect a window to pop up; it will have the following, among other pieces of information

~~~text
pick 6bcf266 optimise markup structure in index page
pick 7b2317c change page structure
pick de135b4 improve headline for imprint

# Rebase 2b504be..de135b4 onto 2b504be (3 commands)
#
# Commands:
# p, pick <commit> = use commit
...
~~~

* tell git what you want to do; do not do it, yet. say we want to change the commit message of the commit `6bcf266`

~~~text
reword 6bcf266 optimise markup structure in index page
pick 7b2317c change page structure
pick de135b4 improve headline for imprint
...
~~~

the first action keyword in the first line changes from `pick` to `reword` because we want to change the commit message of that commit
* save your work and close the window. expect an editor window to pop up; here is where you edit the commit message
* edit the commit message in the editor window that pops up

~~~text
optimise mark-up structure of the index page to reflect latest changes
~~~

* save your work and close the window. you will be redirected to you terminal window
* check git log again

~~~bash
git log --oneline
~~~

expect the changes to show in the output on terminal

~~~text
ce22112 (HEAD -> main) improve headline for imprint
2d42208 change page structure
eb972b4 (origin/feature/login) optimise mark-up structure of the index page to reflect latest changes
2b504be (origin/staging) change headlines for About and Imprint
0023cdd add simple robots.txt
113adcc add jquery javascript resource
fcd6199 initial commit
~~~

notice the following
 * the commit message has changed
 * commit hashes for `HEAD`, `HEAD~1` and `HEAD~2` have changed
#### example 2: combine two commits 
* same fictitious workspace; idea is to combine commits `HEAD~2` and `HEAD~3`
* determine how far back in history you want to go; in this case, four commits before `HEAD` (the latest one)

~~~bash
git rebase -i HEAD~4
~~~ 

* replace `pick` with `squash` on the `HEAD~2` (commit `eb972b4`)

~~~text
pick 2b504be change headlines for About and Imprint
squash eb972b4 optimise markup structure in index page
pick 7b2317c change page structure
pick de135b4 improve headline for imprint
...
~~~

`squash` combines a commit with its immediate parent; in this case, commit `2b504be`; it destorys them and creates a new one
* save your work and close the window
* in the editor that pops up, put in a commit message for the new commit that will be created

~~~text
combine eb972b4 and 2b504be
~~~

* save your work and close the window
* check git log again

~~~bash
git log --oneline
~~~

expect the changes to show in the output on terminal

~~~text
6d37ff0 (HEAD -> main) improve headline for imprint
4376d4d change page structure
59505fd combine eb972b4 and 2b504be
0023cdd add simple robots.txt
113adcc add jquery javascript resource
fcd6199 initial commit
~~~

notice the following
 * the commit message has changed
 * commits `eb972b4` and `2b504be` are not there anymore; instead, there is commit `59505fd`
 * commit hashes for `HEAD`, `HEAD~1` and `HEAD~2` have changed
### cherry picking
* commits are integrated on a branch level
    * think `git merge` or `git rebase` etc
    * idea is to converge branches into the `HEAD` of the main branch (`main` or `master`)
* however, you might want to integrate single, specific commits rather than all
    * cherry picking allows you to select individual commits and integrate them into the `HEAD` of the `main` branch
* **Disclaimer**: Do not get too excited; do not use cherry picking liberally. Use branch-level commits as a rule/standard, not an exception
* instances where cherry picking is used
    * commit is made to the wrong branch; select that commit and place it in the proper branch
    * 
#### flow
* switch to/checkout the target branch. this is the branch you want a commit to be on
* copy the commit hash of the commit to cherry pick 
* run `git cherry-pick`; pass said commit hash as an argument to the command
* verify that changes occurred 
#### example 1: commit `6d37ff0 (HEAD -> main) ...` should be on `feature/newsletter` not `main`
* recall the previous [example](#example-2-combine-two-commits)
    * the workspace viz

    ~~~text
    6d37ff0 (HEAD -> main) improve headline for imprint
    4376d4d change page structure
    59505fd combine eb972b4 and 2b504be
    0023cdd add simple robots.txt
    113adcc add jquery javascript resource
    fcd6199 initial commit
    ~~~

* turns out that commit `6d37ff0 (HEAD -> main) ...` should be on branch `feature`, not `main`
* checkout (go to) `feature/newsletter`

~~~bash
git checkout feature/newsletter
~~~

* copy the commit hash of the commit to select
* pass the commit hash to `git cherry-pick`

~~~bash
git cherry-pick 6d37ff0
~~~

* check git log again

~~~bash
git log --oneline
~~~

expect the changes to show in the output on terminal

~~~text
b198c6d (HEAD -> feature/newsletter) improve headline for imprint
4376d4d change page structure
59505fd combine eb972b4 and 2b504be
0023cdd add simple robots.txt
113adcc add jquery javascript resource
fcd6199 initial commit
~~~

notice the following
 * commit message for `HEAD` has changed
 * `HEAD` now points to `feature/newsletter`
 * commmit message did not change
* **Optional**: reset `HEAD` to main
    * checkout `main`

    ~~~bash
    git checkout main
    ~~~

    * reset `HEAD`
    
    ~~~bash
    git reset --hard HEAD~1
    ~~~
* `main` is clean and `feature/newsletter` has the cherry-picked commit
### reflog
* `ref`erence `log`book. git's journal
* logs every movement of the `HEAD` pointer
* `HEAD` pointer moves with every commit, merge, rebase, checkout, reset etc
*  instances where reflog is useful
    * four commits on a branch. you think that you do not need the latest two. you use `git reset`. you realise it is a mistake. you panic
    * `feature` branch. you think you do not need it. you delete it. it is at this moment you know you f'd up. you panic
#### example 1: throw away `1bc896d` and `4376d4d`
* recall the previous [example](#example-1-commit-6d37ff0-head---main--should-be-on-featurenewsletter-not-main)
    * the workspace viz

    ~~~text
    1bc896d (HEAD -> main) remove typos
    4376d4d change page structure
    59505fd combine eb972b4 and 2b504be
    0023cdd add simple robots.txt
    113adcc add jquery javascript resource
    fcd6199 initial commit
    ~~~

* the mistake: remove `1bc896d` and `4376d4d` so that `59505fd` becomes `HEAD`
* make sure you are on the `main` branch
* copy the commit hash of `HEAD~2`
* pass said hash to `git reset`

~~~bash
git reset --hard 59505fd
~~~

expect the following message

~~~text
HEAD is now at 59505fd combine eb972b4 and 2b504be
~~~

* check git log again
    * _it was at that moment that he knew he f'd up_
    * panic time ...
<img src='https://images.app.goo.gl/LTMPzDxecXsD8wSR8' alt='https://images.app.goo.gl/rjf3qosQVGb6WqH29'/>

* view the reflog

~~~bash
git reflog
~~~

notice how everything is ordered chronologically; the state before the mistake is logged too. we can use its commit hash to restore it
* copy the commit hash of the state before the mistake reset; in this case `1bc896d`
* two options
    * `git reset 1bc896d`. restores said state to the current branch
    * create a new branch; pass said hash to command
* use the latter option; create a branch called `happy-ending`

~~~bash
git branch happy-ending 1bc896d
~~~

the branch `happy-ending` starts at the state `1bc896d`
#### delete then restore branch `feature`
* recall the previous [example](#example-1-throw-away-1bc896d-and-4376d4d)
    * the workspace viz

    ~~~text
    59505fd (HEAD -> main) combine eb972b4 and 2b504be
    0023cdd add simple robots.txt
    113adcc add jquery javascript resource
    fcd6199 initial commit
    ~~~

    * recall, from [this example](#example-1-commit-6d37ff0-head---main--should-be-on-featurenewsletter-not-main) that there is a branch called `feature/newsletter`
* idea is to delete and restore said branch
* delete the branch

~~~bash
git branch --delete feature/newsletter
~~~

* check git log; branch is not there anymore
* view reflog; info we need is available
* copy the relavant commit hash
* create a new branch and have it start at the state of said hash, inthis case, `b198c6d`

~~~bash
git branch feature-recovered/newsletter b198c6d
~~~

* check git log again; the branch `feature-recovered/newsletter` starts at the state `b198c6d`
### submodules
* copy-pasting third-party code has downsides; here are two
    * external code mixes with your own files
    * updating the external code is a manual process
    * this is where submdules come in
* submodule is a repository inside a repository
    * repository with full specs and functionality of a repo
    * resides in a parent repo
    * contents of files in submodule are on the author's repo, not the parent repo
    * submodule stores remote URL, path and checked-out revision
    * said files are accessible to us; we do not bear the cost of having them 
#### example 1: create a submodule within a fictitious project file
* assume a project has the following file structure
```console
/
|_/public
    |_/assets
|_/src
    |_/components
        |_/Controllers
            |_/Create.tsx
            |_/Read.tsx
            |_/Update.tsx
        |_/Navbar
            |_/RightContent.tsx
            |_/Search.tsx
            |_/Navbar.tsx
    |_/hooks
        |_/useAPIData.tsx
        |_/useAuth.tsx
    |_/pages
        |_/_app.tsx
        |_/index.tsx
        |_/[id]
            |_/submit.tsx
            |_/showContent.tsx
    |_/node_modules
|_/README.md
|_/.gitignore
```
* say we need a module from a third party and that we must add it to the project wholesale (cannot use a CDN or _import_ or _require_ directly)
* create a directory called `lib` in `public` (assume you are at `/`)

~~~bash
mkdir public/lib
~~~

* navigate into the directory

~~~bash
cd public/lib
~~~

* copy the link to the third-party resource
* create a submodule; pass the link to the command `git submodule add`

~~~bash
git submodule add https://github.com/path/to/third/party/resource
~~~

* inspect the file structure
    * directory `lib` is created inside `public`
    * there is a `.gitmodules` dir; it contains the path and URL to the third-party source
    * the `.git` dir contains the path and URL to the third-party source also
    * said dir contains the files from the third-party source
    * the third-party dir, there is 
        * a `.git` dir (use `ls -a`; it's hidden)
        * relevant files that we will use in the fictitious project
* check the status of the project

~~~bash
git status
~~~

notice that git takes the operation as a modification like any other; said modification must be committed to the main branch
* commit changes

~~~bash
git commit -m 'add <name-of-submodule> library as a submodule'
~~~
* **Advice**: do not edit the configs iside any `git` file
#### example 2: clone a project that has a submodule
* in this example, we will clone [Apache Airflow](https://airflow.apache.org/)
* navigate into a clean/empty directory
* create a git repo

~~~bash
git init
~~~

* clone Airflow's [github repo](https://github.com/apache/airflow)

~~~bash
git clone https://github.com/apache/airflow.git
~~~

* open the files in a [gui](https://en.wikipedia.org/wiki/Graphical_user_interface)

~~~bash
open .
~~~

* inspect the files at `/github/actions`
    * all those dirs are submodules
    * they are empty because a project does not contain its submodules files. it contains the remote URL and path to said submodule files

* in terminal run this

~~~bash
cd airflow
git submodule update --init --recursive
~~~

several cloning processes begin. submodule folders are now populated

* **Alternative method**: there is a flag/option that allows automatic population of third-party files during cloning

~~~bash
git clone --recurse-submodules https://github.com/apache/airflow.git
~~~

### checked-out revisions
* a submodule can have many committed revisions; you can have one and only one at a time in your working directory
* submodule repos are checked out on a specific commit, not a branch
    * one can add as many commits to a branch as they want
    * however, the submodule has features and functionalities that users require to be stable (starting to see where _stable version_ comes from)
### search and find
* the git log is a great source of information w.r.t. changes to the repo
* there are a lot of records; what to do when you want specific data/entry?
    * easy! filter the log
* parameters to use during filtering
    * date: `--before` and `--after`
    * message: `grep`
    * author: `--author`
    * file: `-- <filename`>
    * branch: `-- branch-branchName`
* use the [Ruby on Rails open repository](https://github.com/asyraffff/Open-Source-Ruby-and-Rails-Apps) as a punching bag
* data logged after 14-May-2023

~~~bash
git log --after="2023-5-15"
~~~

* data logged between 01-May-2023 and 14-May-2023

~~~bash
git log --after="2023-5-15" --before="2023-05-01"
~~~

* data that contains the word 'refactor'

~~~bash
git log --grep="refactor"
~~~

* data generated by user "Kamichi"

~~~bash
git log --author="Kamichi"
~~~

* data logged after 14-May-2023 by user "Kamichi"

~~~bash
git log --after="2023-5-15" --author="Kamichi"
~~~

* data files named "README.md"

~~~bash
git log -- README.md
~~~

the `--` in the command above allows git to know that you are asking for a file, not a branch

* data logged in "main" but not in "feature/newsletter"

~~~bash
git log feature/newsletter..main
~~~
