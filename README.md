# IBM i Dotfiles

## Requirements
These dotfiles require that the
[IBM i Open Source Environment](https://sobo.red/ibmi-rpms) (yum) be installed.

## IBM i Dotfiles Installation

### Add SoBored RPM Repo to yum
Use your favorite text editor and create the file `/QOpenSys/etc/yum/repos.d/sobored.repo` with these contents:

```
[sobored]
name=sobored
baseurl=http://rpms.sobo.red/ibmi/
enabled=1
gpgcheck=0
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

### Copy IBM i Dotfiles to specific directory.

Please use the full path here. Relative paths are untested.

```
ibmi-dotfiles --install-path /desired/install/path
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

