%define name           ibmi-dotfiles
%define release        0
%define version        1.0
%define git_completion https://github.com/git/git/blob/master/contrib/completion/git-completion.bash
%define git_prompt     https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh

Name:       %{name}
Version:    %{version}
Release:    %{release}
Requires:   /QOpenSys/pkgs/bin/find /QOpenSys/pkgs/bin/wget
Source:     %{name}-%{version}.tar.gz
Summary:    Shell configuration files for IBM i.
License:    MIT

%description
Shell configuration files for IBM i.

%prep
%setup

%install
mkdir -p %{buildroot}/QOpenSys/pkgs/bin
install -m 755 ./script/bootstrap %{buildroot}/QOpenSys/pkgs/bin/ibmi-dotfiles
mkdir -p %{buildroot}/QOpenSys/etc/ibmi-dotfiles
wget %{git_completion} -P %{buildroot}/QOpenSys/etc/ibmi-dotfiles/
wget %{git_prompt} -P %{buildroot}/QOpenSys/etc/ibmi-dotfiles/
cp -r ./* %{buildroot}/QOpenSys/etc/ibmi-dotfiles

%files
%defattr(-, qsys, *none)
/QOpenSys/pkgs/bin/ibmi-dotfiles
/QOpenSys/etc/ibmi-dotfiles

%changelog
* Sun Jun 14 2020 Joshua Hall <josh@sobo.red> - 1.0-ibmi-dotfiles
- Support git bash completion and prompt

