%define name           ibmi-dotfiles
%define release        0
%define version        1.1
%define git_completion https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
%define git_prompt     https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh

Name:       %{name}
Version:    %{version}
Release:    %{release}
BuildArch:  noarch
Requires:   /QOpenSys/pkgs/bin/find /QOpenSys/pkgs/bin/curl
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
/QOpenSys/pkgs/bin/curl %{git_completion} -o %{buildroot}/QOpenSys/etc/ibmi-dotfiles/git-completion.bash
/QOpenSys/pkgs/bin/curl %{git_prompt} -o %{buildroot}/QOpenSys/etc/ibmi-dotfiles/git-prompt.sh
cp -r ./* %{buildroot}/QOpenSys/etc/ibmi-dotfiles

%files
%defattr(-, qsys, *none)
/QOpenSys/pkgs/bin/ibmi-dotfiles
/QOpenSys/etc/ibmi-dotfiles

%changelog
* Wed Jun 17 2020 Joshua Hall <josh@sobo.red> - 1.1-ibmi-dotfiles
- Stopped modifying etc to solve permission issues
* Sun Jun 14 2020 Joshua Hall <josh@sobo.red> - 1.0-ibmi-dotfiles
- Support git bash completion and prompt

