Name:       nemo-device-dont_be_evil
Summary:    Config files for Pine64
Version:    0.3
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
Requires:  qt5-feedback-haptics-ffmemless

Requires:  sensorfw-qt5 >= 0.11.4

Requires:  gpsd >= 3.19
Requires:  geoclue-provider-gpsd3
Requires:  alsa-utils

#provide services for startup user session
Requires:   systemd-config-mer
Requires:   nemo-mobile-session-common

#provide keyboard
Requires:   maliit-plugins


%description
This package contains the config files specifided for
PinePhone64.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT

#sparce copy
cp -r sparse/* $RPM_BUILD_ROOT/

%files
%defattr(-,root,root,-)
%{_sysconfdir}/modules-load.d/fuse.conf
%{_sysconfdir}/modules-load.d/r8723bs.conf
%{_sysconfdir}/sysconfig
%{_sysconfdir}/systemd
%{_sysconfdir}/default
%{_sysconfdir}/gpsd
%{_sysconfdir}/pulse
%{_sysconfdir}/sensorfw

/lib/systemd/
/lib/udev/
/var/lib/nemo-pulseaudio-parameters
/lib/qt5/plugins/feedback/qtfeedback-dontbeevil.ini
/share/ngfd/plugins.d/ngf-vibra-dontbeevil.ini

%{_bindir}/unmute-sound-card.sh
%{_bindir}/enable-modem.sh
%{_bindir}/disable-modem.sh

%config %{_sysconfdir}/eglfs-config.json
%config %{_sysconfdir}/sysconfig/statefs/system.conf
%config /var/lib/environment/compositor/dont_be_evil.conf
%config /var/lib/environment/nemo/60-dontbeevil-vibra.conf
%config /var/lib/environment/ofono/*.conf
