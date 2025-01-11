%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     system76-driver
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  akmod module for System76 laptops
License:  GPLv2
URL:      https://github.com/ssweeny/system76-driver-akmod

Source:   %{url}/archive/refs/heads/main.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Kernel module for controlling the hotkeys and fans on some System76 laptops.

%prep
%setup -q -c system76-driver-akmod-main

%build
install -D -m 0644 system76-driver-akmod-main/%{name}.conf %{buildroot}%{_modulesloaddir}/%{name}.conf

%files
%doc system76-driver-akmod-main/README.md
%license system76-driver-akmod-main/LICENSE
%{_modulesloaddir}/%{name}.conf

%changelog
{{{ git_dir_changelog }}}
