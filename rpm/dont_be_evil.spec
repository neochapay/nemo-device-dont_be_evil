Name:       nemo-device-dont_be_evil
Summary:    Config files for Pine64
Version:    0.10
Release:    0
BuildArch:  noarch
Group:      System/Base
License:    BSD
URL:        https://github.com/neochapay/nemo-device-dont_be_evil
Source0:    %{name}-%{version}.tar.bz2

Requires:   mesa-dri-lima-driver >= 19.3
Requires:   mesa-dri-swrast-driver >= 19.3
Requires:   mesa-dri-sun4i-driver >= 19.3
Requires:   qt5-plugin-platform-eglfs

Requires:  kernel-dont_be_evil >= 5.6
Requires:  kernel-dont_be_evil-modules
Requires:  dontbeevil-firmware
Requires:  qt5-feedback-haptics-ffmemless

Requires:  sensorfw-qt5 >= 0.11.4

Requires:  gpsd >= 3.19
Requires:  geoclue-provider-gpsd3
Requires:  alsa-utils
Requires:  pulseaudio-module-keepalive
Requires:  qt5-qtmultimedia-plugin-mediaservice-gstmediacapture
Requires:  qt5-plugin-generic-evdev
Requires:  mce-plugin-libhybris-nondroid

#provide services for startup user session
Requires:   systemd-config-mer
Requires:   nemo-mobile-session-common

#provide keyboard
Requires:   maliit-plugins

# WiFi/BT regulator DB
Requires:   wireless-regdb
Requires:   bluez5-tools

#Camera:
Requires: v4l-utils

#OHM
Requires:  policy-settings-common
Requires:  swi-prolog-library
Requires:  ohm-configs-default
Requires:  ohm-plugin-route
Requires:  ohm-plugin-media
Requires:  ohm-plugin-signaling
Requires:  ohm-plugin-accessories
Requires:  ohm
Requires:  ohm-plugin-resolver
Requires:  ohm-plugins-dbus
Requires:  ohm-plugin-profile
Requires:  ohm-plugin-ruleengine
Requires:  ohm-plugins-misc
Requires:  ohm-plugin-core
Requires:  ohm-plugin-dspep

%description
This package contains the config files specifided for
PinePhone64.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT
rm -rf tmp/
mkdir -p tmp/

#create list of files
echo "%defattr(-,root,root,-)" > tmp/sparse.files
cd sparse/
find . \( -type f -o -type l \) -print | sed 's/^.//' | sed 's/\/etc/%config \/etc/g' > ../tmp/sparse.files
cd ../

#sparce copy
cp -r sparse/* $RPM_BUILD_ROOT/

%files -f tmp/sparse.files
%defattr(-,root,root,-)
