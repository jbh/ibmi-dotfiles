# Dotfiles
IBM i Dotfiles

## Requirements
These dotfiles require that the
[IBM i Open Source Environment](https://sobo.red/ibmi-rpms) be installed. You
will also need to install `findutils`.

**Install findutils**

```
yum install findutils
```

## Dotfiles Installation
```
ssh <username>@<ibmi-ip>
mkdir /home/<username>/git && cd $_
git clone git@github.com:jbh/ibmi-dotfiles.git
./ibmi-dotfiles/script/bootstrap
```

The bootstrap script will step you through installing the dotfiles. If a dotfile
already exists, you will be prompted and asked to overwrite, backup, or skip the
file.
