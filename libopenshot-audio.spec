Summary:	Audio library used by OpenShot
Name:		libopenshot-audio
Version:	0.1.2
Release:	1
License:	GPL v3+
Group:		Libraries
URL:		http://openshot.org/
Source0:	https://github.com/OpenShot/libopenshot-audio/archive/v%{version}.tar.gz
# Source0-md5:	f002b5cdaf91cdd7f482b528da5e02be
Patch0:		%{name}-build.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	freetype-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel

%description
OpenShot Audio Library (libopenshot-audio) is an open-source project
powered by JUCE, and enables high-quality audio editing and playback
for libopenshot.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1

%build
install -d build

cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libopenshot-audio.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenshot-audio.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/openshot-audio-test-sound
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/libopenshot-audio.so
%{_mandir}/man1/openshot-audio-test-sound.1*
