%define major       4
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname -d %{name}

Summary:	A syntactic parser of English
Name:		link-grammar
Version:	4.7.6
Release:	1
Group:		Office
License:	BSD-like
URL:		http://www.link.cs.cmu.edu/link/
Source0:	http://www.abisource.com/downloads/link-grammar/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	ant
BuildRequires:	java-openjdk
BuildRequires:	java-devel-openjdk

%description
The Link Grammar Parser is a syntactic parser of English, based
on link grammar, an original theory of English syntax. Given a
sentence, the system assigns to it a syntactic structure, which
consists of a set of labeled links connecting pairs of words.
The parser also produces a "constituent" representation of a
sentence (showing noun phrases, verb phrases, etc.).

%package -n %{libname}
Summary:	A syntactic parser of English
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{develname}
Summary:	Support files necessary to compile applications with link-grammar
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel
Obsoletes:	%{_lib}link-grammar4-devel

%description -n %{develname}
Libraries and header files necessary to compile applications using
link-grammar.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc LICENSE README
%{_bindir}/*
%{_datadir}/link-grammar/*
%{_mandir}/man1/link-parser.1.*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/link-grammar.pc
%{_includedir}/link-grammar/*



%changelog
* Thu May 10 2012 Matthew Dawkins <mattydaw@mandriva.org> 4.7.6-1
+ Revision: 798109
- new version 4.7.6
- cleaned up spec
- removed old patch

* Mon Apr 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.7.5-1
+ Revision: 792840
- file not found fix
- BR:java-devel-openjdk
- BR:java-openjdk
- version update 4.7.5

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 4.2.5-2mdv2009.0
+ Revision: 217192
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
- normalize call to ldconfig in %%post/%%postun

* Tue Mar 25 2008 Emmanuel Andry <eandry@mandriva.org> 4.2.5-2mdv2008.1
+ Revision: 189872
- Fix groups
- protect major

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 13 2007 Jérôme Soyer <saispo@mandriva.org> 4.2.5-1mdv2008.1
+ Revision: 108495
- New release 4.2.4

* Wed Sep 05 2007 Jérôme Soyer <saispo@mandriva.org> 4.2.4-1mdv2008.0
+ Revision: 80232
- New release 4.2.4
- Import link-grammar




* Sat Apr 15 2006 Jerome Soyer <saispo@mandriva.org> 4.2.2-1mdk
- 4.2.2

* Thu Aug 04 2005 Marcel Pol <mpol@mandriva.org> 4.1.3-1mdk
- 4.1.3

* Tue Jul 26 2005 Marcel Pol <mpol@mandriva.org> 4.1.2-0.20050726cvs.2mdk
- fix description and summary (Gaetan Lehmann)
- fix license

* Tue Jul 26 2005 Marcel Pol <mpol@mandriva.org> 4.1.2-0.20050726cvs.1mdk
- cvs release of 4.1.2-20050726cvs
- buildrequires automake1.9
- P1, run versioned automake and aclocal

* Tue May 17 2005 Marcel Pol <mpol@mandriva.org> 4.1.1-1mdk
- Initial version
