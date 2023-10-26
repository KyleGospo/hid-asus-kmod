%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     hid-asus
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Kernel module providing hid-asus from ChimeraOS
License:  GPLv2
URL:      https://github.com/ChimeraOS/
VCS:      {{{ git_dir_vcs }}}
Source:   {{{ git_dir_pack }}}

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Kernel module providing hid-asus from ChimeraOS

%prep
{{{ git_dir_setup_macro }}}

%build
install -D -m 0644 LICENSE %{buildroot}%{_datarootdir}/licenses/hid-asus/LICENSE

%files
%license LICENSE

%changelog
{{{ git_dir_changelog }}}
