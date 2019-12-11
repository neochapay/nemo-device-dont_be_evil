Name:       nemo-device-dont_be_evil
Summary:    Config files for Pine64
Version:    0.1
Release:    0
BuildArch:  noarch
Group:      System/Base
License:    BSD
URL:        https://github.com/neochapay/nemo-device-dont_be_evil
Source0:    %{name}-%{version}.tar.bz2

Requires:   mesa-llvmpipe-dri-lima-driver
Requires:   mesa-llvmpipe-dri-swrast-driver
Requires:   mesa-llvmpipe-dri-sun4i-driver
Requires:   qt5-plugin-platform-eglfs

Requires:  kernel-dont_be_evil-modules
Requires:  dontbeevil-firmware

%description
This package contains the config files specifided for
PinePhone64.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/statefs/
mkdir -p $RPM_BUILD_ROOT/etc/modules-load.d/
mkdir -p $RPM_BUILD_ROOT/var/lib/environment/compositor

install -p -c -m644 configs/fuse.conf $RPM_BUILD_ROOT/etc/modules-load.d/
install -p -c -m644 configs/r8723bs.conf $RPM_BUILD_ROOT/etc/modules-load.d/
install -p -c -m644 configs/system.conf $RPM_BUILD_ROOT/etc/sysconfig/statefs/
install -p -c -m644 configs/eglfs-config.json $RPM_BUILD_ROOT/etc/
install -p -c -m644 configs/dont_be_evil.conf $RPM_BUILD_ROOT/var/lib/environment/compositor/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/modules-load.d/fuse.conf
%{_sysconfdir}/modules-load.d/r8723bs.conf

%config %{_sysconfdir}/eglfs-config.json
%config %{_sysconfdir}/sysconfig/statefs/system.conf
%config /var/lib/environment/compositor/dont_be_evil.conf
