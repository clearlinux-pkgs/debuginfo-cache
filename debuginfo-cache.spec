Name     : debuginfo-cache
Version  : 1
Release  : 2
Source10 : https://download.clearlinux.org/releases/27110/clear/x86_64/debug/glibc-debuginfo-2.28-230.x86_64.rpm
Source20 : https://download.clearlinux.org/releases/27110/clear/x86_64/debug/xz-debuginfo-5.2.4-51.x86_64.rpm
Summary  : Prepopulated debuginfo lookaside cache
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : /usr/bin/rpm2cpio
BuildRequires : cpio

%define debug_package %{nil}


%description
Precached debuginfo


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/debuginfo
pushd %{buildroot}/usr/share/debuginfo
rpm2cpio %{SOURCE10} | cpio -i -d -u
rpm2cpio %{SOURCE20} | cpio -i -d -u
popd

%files
%defattr(-,root,root,-)
/usr/share/debuginfo