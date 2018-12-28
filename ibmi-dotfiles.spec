%define name       ibmi-dotfiles
%define release    0
%define version    0.3

Name:       %{name}
Version:    %{version}
Release:    %{release}
Requires:   /QOpenSys/pkgs/bin/find
Source:     %{name}-%{version}.tar.gz
Summary:    Shell configuration files for IBM i.
License:    MIT

%description
Shell configuration files for IBM i.

%prep
%setup -q

%install
mkdir -p %{buildroot}/QOpenSys/pkgs/bin
install -m 755 ./ibmi-dotfiles/script/bootstrap %{buildroot}/QOpenSys/pkgs/bin/ibmi-dotfiles
mkdir -p %{buildroot}/QOpenSys/etc/ibmi-dotfiles
cp -r ./ibmi-dotfiles/* %{buildroot}/QOpenSys/etc/ibmi-dotfiles

%files
%defattr(-, qsys, *none)
/QOpenSys/pkgs/bin/ibmi-dotfiles
/QOpenSys/etc/ibmi-dotfiles

%changelog
# let skip this for now
