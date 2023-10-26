%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

Name:     hid-asus-kmod
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Kernel module providing hid-asus from ChimeraOS
License:  GPLv2
URL:      https://github.com/ChimeraOS/
VCS:      {{{ git_dir_vcs }}}
Source:   {{{ git_dir_pack }}}
Source1:  https://raw.githubusercontent.com/ChimeraOS/linux/master/drivers/hid/hid-asus.c
Source2:  https://raw.githubusercontent.com/ChimeraOS/linux/master/drivers/hid/hid-ids.h

BuildRequires: kmodtool

%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Kernel module providing hid-asus from ChimeraOS

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

{{{ git_dir_setup_macro }}}
cp %{SOURCE1} .
cp %{SOURCE2} .

for kernel_version  in %{?kernel_versions} ; do
  mkdir -p _kmod_build_${kernel_version%%___*}
  cp -a hid-asus.c hid-ids.h Makefile _kmod_build_${kernel_version%%___*}/
done

%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} VERSION=v%{version} modules
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/hid-asus.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/hid-asus.ko
done
%{?akmod_install}

%changelog
{{{ git_dir_changelog }}}
