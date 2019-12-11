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

Requires:  kernel-dont_be_evil
Requires:  kernel-dont_be_evil-modules
Requires:  dontbeevil-firmware

%description
This package contains the config files specifided for
PinePhone64.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT

#sparce copy
cp -r sparce/* $RPM_BUILD_ROOT/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/modules-load.d/fuse.conf
%{_sysconfdir}/modules-load.d/r8723bs.conf
%{_sysconfdir}/systemd

/lib/systemd/

%config %{_sysconfdir}/eglfs-config.json
%config %{_sysconfdir}/sysconfig/statefs/system.conf
%config /var/lib/environment/compositor/dont_be_evil.conf
