%define	name	libfishsound
%define	version	0.7.0
%define	release	1

%define	major	1
%define	libname	%mklibname fishsound %{major}

Summary:	Simple programming interface that wraps Xiph.Org audio codecs
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	http://www.annodex.net/software/libfishsound/download/%{name}-%{version}.tar.bz2
License:	BSD
Group:		System/Libraries
URL:		http://www.annodex.net/software/libfishsound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	oggvorbis-devel speex-devel

%description
FishSound (libfishsound) provides a simple programming interface for
decoding and encoding audio data using the Xiph.Org codecs Vorbis and
Speex. libfishsound is a wrapper around the existing codec libraries
and provides a consistent, higher-level programming interface. It
has been designed for use in a wide variety of applications; it has
no direct dependencies on Annodex or Ogg encapsulation, though it is
most commonly used in conjunction with liboggz to decode or encode Ogg
encapsulated Vorbis or Speex files.

%package -n	%{libname}
Summary:	Simple programming interface that wraps Xiph.Org audio codecs
Group:		System/Libraries
Obsoletes:	%{name}
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
FishSound (libfishsound) provides a simple programming interface for
decoding and encoding audio data using the Xiph.Org codecs Vorbis and
Speex. libfishsound is a wrapper around the existing codec libraries
and provides a consistent, higher-level programming interface. It
has been designed for use in a wide variety of applications; it has
no direct dependencies on Annodex or Ogg encapsulation, though it is
most commonly used in conjunction with liboggz to decode or encode Ogg
encapsulated Vorbis or Speex files.

%package -n	%{libname}-devel
Summary:	Simple programming interface that wraps Xiph.Org audio codecs
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
FishSound (libfishsound) provides a simple programming interface for
decoding and encoding audio data using the Xiph.Org codecs Vorbis and
Speex. libfishsound is a wrapper around the existing codec libraries
and provides a consistent, higher-level programming interface. It
has been designed for use in a wide variety of applications; it has
no direct dependencies on Annodex or Ogg encapsulation, though it is
most commonly used in conjunction with liboggz to decode or encode Ogg
encapsulated Vorbis or Speex files.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall docdir=./docs/

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc NEWS README COPYING
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README ./doc/docs
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

