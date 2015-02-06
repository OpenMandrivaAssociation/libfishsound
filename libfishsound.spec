%define	name	libfishsound
%define	version	1.0.0
%define release	3

%define	major	1
%define	libname	%mklibname fishsound %{major}
%define develname %mklibname -d fishsound

Summary:	Simple programming interface that wraps Xiph.Org audio codecs
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	http://www.annodex.net/software/libfishsound/download/%{name}-%{version}.tar.gz
License:	BSD-like
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

%package -n	%{develname}
Summary:	Simple programming interface that wraps Xiph.Org audio codecs
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-devel < %version-%release
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d fishsound 1

%description -n	%{develname}
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
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std docdir=./docs/

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc NEWS README COPYING
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README ./doc/docs
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2011.0
+ Revision: 609745
- rebuild

* Sat Mar 27 2010 Funda Wang <fwang@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 528057
- New version 1.0.0

* Wed May 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.2-1mdv2010.0
+ Revision: 380252
- update to new version 0.9.2

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 23 2008 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2009.0
+ Revision: 210332
- New version 0.9.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.7.0-1mdv2008.1
+ Revision: 128578
- kill re-definition of %%buildroot on Pixel's request
- import libfishsound


* Tue Oct 11 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.7.0-1mdk
- initial release
