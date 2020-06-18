%define name           ibmi-dotfiles
%define release        0
%define version        1.1.1
%define git_completion https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
%define git_prompt     https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh

Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Summary: Shell configuration files for IBM i.
BuildArch: noarch

BuildRequires: curl

Requires: findutils

Source: %{name}-%{version}.tar.gz

%description
Shell configuration files for IBM i.

%prep
%setup

%install
mkdir -p %{buildroot}/QOpenSys/pkgs/bin
install -m 755 ./script/bootstrap %{buildroot}/QOpenSys/pkgs/bin/%{name}
mkdir -p %{buildroot}/QOpenSys/etc/%{name}
/QOpenSys/pkgs/bin/curl %{git_completion} -o %{buildroot}/QOpenSys/etc/ibmi-dotfiles/git-completion.bash
/QOpenSys/pkgs/bin/curl %{git_prompt} -o %{buildroot}/QOpenSys/etc/ibmi-dotfiles/git-prompt.sh
cp -r ./* %{buildroot}/QOpenSys/etc/%{name}

%files
%defattr(-, qsys, *none)
/QOpenSys/pkgs/bin/%{name}
/QOpenSys/etc/%{name}

%changelog
* Wed Jun 17 2020 Joshua Hall <josh@sobo.red> - 1.1.1-ibmi-dotfiles
- Cleaned up spec file
* Wed Jun 17 2020 Joshua Hall <josh@sobo.red> - 1.1.0-ibmi-dotfiles
- Stopped modifying etc to solve permission issues
* Sun Jun 14 2020 Joshua Hall <josh@sobo.red> - 1.0.0-ibmi-dotfiles
- Support git bash completion and prompt

