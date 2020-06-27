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
These dotfiles require that the
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

`ibmi-dotfiles` are used from the command line. BASH suggested, as these dotfiles are configured for BASH.

### Copy IBM i Dotfiles to current user's home directory.

```
ibmi-dotfiles
```

## Note for those that used beta versions

> Please note that the repo URL has changed: `http://rpms.sobo.red/ibmi/`.
This must be updated in `/QOpenSys/etc/yum/repos.d/sobored.repo`

Since I've changed the architecture to noarch, you'll probably have to:

```
yum clean metadata
yum remove ibmi-dotfiles
yum install ibmi-dotfiles
```

