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

### [BASH](system)

The BASH environment on IBM i comes unconfigured by default, which is the motivation
behind `ibmi-dotfiles` and the default dotfiles it installs. The default dotfiles
installed by `ibmi-dotfiles` are meant to be nearly barebones and a jumping
off point. There's a lot one can do with dotfiles, and below are some of the
key features that come with what is installed by `ibmi-dotfiles`.

#### [.aliases](system/aliases.symlink)

Aliases on command line are just shortcuts for other commands.

`ibmi-dotfiles` aliases:

- `reload` is short for `source ~/.bash_profile`, which will reload your dotfiles
- `ls`, `dir`, `vdir`, `grep`, `fgrep`, and `egrep` are all aliases with `--color=auto`
included, which will use dircolors to color directories, symlinks, files, etc in the
output list
- `ll` is short for `ls -alF`
- `la` is short for `ls -A`
- `l` is short for `ls -CF`
- `..` is short for `cd ..`
- `...` is short for `cd ../..`
- `....` is short for `cd ../../..` and so on and so on for this alias.

#### [.functions](system/functions.symlink)

Functions, when defined in dotfiles and sourced in BASH, can be treated as simple
scripts. For example, `mkcdr` will take an option of a path, create it, and cd
to it.

`ibmi-dtofiles` functions:

- `mkcdr <path>` will create the path defined and cd to it
- `extract <zip>.[tar.bz2,tar.gz,bz2,rar,gz,tar,tbz2,tgz,zip,Z,7z]` will unpack nearly
any zip
- `h <path>` will go to a path relative to the home directory
- `d <path>` will go to a path relative to the development directory, currently set to
`~/Development` and can be changed

#### [.history](system/history.symlink)

The default history is small. `ibmi-dotfiles` defines a much larger history
and makes sure history is appending and not overwriting, so the history
will include many commands over a long period of time.

#### [.path](system/path.symlink)

`ibmi-dotfiles` makes sure to include anything it can in the $PATH, so you can have
access to `zendphp7`, `QOpenSys`, and other binaries. `~/.local/bin` is included in
the path, and this is a nice place to include custom scripts you've written and would
like to run conveniently through command line.

#### [.prompt](system/prompt.symlink)

Your BASH prompt is what appears before every command that your write. Most systems
come with a useful prompt that gives information about your user and the system
you're using. The default one on IBM i appears like so:

```
bash4.4$
```

While good enough, this doesn't tell us much. `ibmi-dotfiles` will make your prompt
appear like so:

```
username@hostname:current_dir (git-branch-if-in-git-repo)$
```

Or, with actual values:

```
josh@DEVLPAR:project-dir (master)$
```

You can do a lot with your prompt.
[Learn more](https://www.maketecheasier.com/8-useful-and-interesting-bash-prompts/).

#### [.vars](system/vars.symlink)

This is where you should put all your environment variables. For now, there are
a few included in the inital install, like `JAVA_HOME`, `TERM`, and `PAGER`.

#### [.inputrc](system/inputrc.symlink)

The inputrc is usually included under `/etc/inputrc` on most systems
and doesn't require any customization. IBM i does not have this yet,
so `ibmi-dotfiles` includes a default one in your home directory.
This will fix some bugs, like the home/end/delete keys not working
on command line.

#### [Terminal size and globstar](system/before_dotfiles.symlink)

- `shopt -s checkwinsize` will check the window size each resize and reset $LINES and $COLUMNS
accordingly
- `shopt -s globstar` will allow us use `**` in path names to expand the path and check all
directories/subdirectories

### [Vim](system/vimrc.symlink)

Vim is a powerful text editor, especially when you start customizing it.
Some features included from `ibmi-dotfiles` are:

- Fixed backspace
- Relative line numbers
- `jk` as a shortcut for `esc`

## Note for those that used beta versions

> Please note that the repo URL has changed: `http://rpms.sobo.red/ibmi/`.
This must be updated in `/QOpenSys/etc/yum/repos.d/sobored.repo`

Since I've changed the architecture to noarch, you'll probably have to:

```
yum clean metadata
yum remove ibmi-dotfiles
yum install ibmi-dotfiles
```

