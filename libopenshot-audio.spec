Summary:	Audio library used by OpenShot
Name:		libopenshot-audio
Version:	0.3.3
Release:	1
License:	GPL v3+
Group:		Libraries
URL:		http://openshot.org/
Source0:	https://github.com/OpenShot/libopenshot-audio/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	09cb1afa4f6243f10d23dd9789d6a852
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

%build
install -d build

cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# Looks like some Java junk
%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/API

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_libdir}/libopenshot-audio.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenshot-audio.so.9

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/OpenShotAudio
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/libopenshot-audio.so
%attr(755,root,root) %{_bindir}/openshot-audio-demo
%{_mandir}/man1/openshot-audio-demo.1*
