# IBM i Dotfiles

IBM i Dotfiles is a command line tool used to create configuration files,
otherwise known as dotfiles, in the home directory of your user on IBM i.
Dotfiles are used to configure BASH, vim, git, and many other command
line tools. You can create a beautiful BASH prompt, alias commands,
build helpful functions, set environment variables, customize vim,
and the list goes on and on.

Use these dotfiles as a jumping off point. Customize them to your heart's
desire to create a comfortable and efficient BASH environment on IBM i
for your user. **These dotfiles are installed in your home directory
and will not effect anyone else on the system.**

## Requirements
This software requires that the
[IBM i Open Source Environment](https://sobo.red/ibmi-rpms) (yum) be installed.

## IBM i Dotfiles Installation

### Add SoBored RPM Repo to yum
Make sure to have `yum-utils` isntalled in order to run `yum-config-manager`:

```
yum install yum-utils
```

Then:

```
yum-config-manager --add-repo http://rpms.sobo.red/ibmi/
```

Just to be safe, make sure you clean your metadata:

```
yum clean metadata
```

### Install `ibmi-dotfiles` via yum

```
yum install ibmi-dotfiles
```

## IBM i Dotfiles Usage

`ibmi-dotfiles` is used from the command line. BASH suggested, as these dotfiles are configured for BASH.

### Copy IBM i Dotfiles to current user's home directory.

```
ibmi-dotfiles
```

> Be sure to logout and log back in for the dotfiles to take effect. The installed dotfiles
come with a helpful alias, `reload`, that you can use after logging in again to reload your
dotfiles after editing them instead of having to logout/login each time.

## Features

### [Git](git)


#### [.gitconfig](git/gitconfig.symlink)

The git config not only sets your name and email during installation, but it also comes with
some helpful aliases like `co`, `ci`, `st`, `br`, `hist`, and others. I particularly like the
`hist` alias, as it prints a much prettier and understandable history of commits.

```bash
git co <branch-name>       # git checkout <branch-name> 
git co -b <branch-name>    # git checkout -b <branch-name>
git ci -m "Commit message" # git commit -m "Commit message"
git st                     # git status -sb
git br                     # git branch
git br -d <branch-name>    # git branch -d <branc-name>
git hist                   # git log --pretty=format:\"%h %ad | %s%d [%a]\" --graph --date=short
```

The git config also sets push to simple, and it can be used for much more.
[Learn more](https://git-scm.com/docs/git-config).

#### [.gitignore](git/gitignore.symlink)

The installed dotfiles come with a global gitignore file. This can potentially become annoying
if for some reason you want to track a `.DS_Store` file (not recommended), but all of the files
in it are standardly ignored. Just keep it in mind if ever a directory is ignored and you cannot
figure out why.


#### [Git prompt and git bash completion](system/after_dotfiles.symlink)

Installing `ibmi-dotfiles` through yum also installs `git-completion` and `git-prompt`.

`git-completion` is used to complete git commands, like checkout, on command line.
For example, while writing `git checkout <branch-name>`, you can tab-complete the branch
name. Double-tapping tab will list any branch names matching what you've typed so far,
so you can easily search through branches while typing the branch name.

`git-prompt` is used to add git information to your BASH
[prompt](system/prompt.symlink).
With these default dotfiles, the prompt will show the current branch name and its status.
[Learn more](https://digitalfortress.tech/tutorial/setting-up-git-prompt-step-by-step/)
about what you can do with your git prompt.

### BASH


## Note for those that used beta versions

> Please note that the repo URL has changed: `http://rpms.sobo.red/ibmi/`.
This must be updated in `/QOpenSys/etc/yum/repos.d/sobored.repo`

Since I've changed the architecture to noarch, you'll probably have to:

```
yum clean metadata
yum remove ibmi-dotfiles
yum install ibmi-dotfiles
```

