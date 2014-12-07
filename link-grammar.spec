%define major 4
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	A syntactic parser of English
Name:		link-grammar
Version:	4.8.5
Release:	4
Group:		Office
License:	BSD-like
Url:		http://www.link.cs.cmu.edu/link/
Source0:	http://www.abisource.com/downloads/link-grammar/%{version}/%{name}-%{version}.tar.gz

%description
The Link Grammar Parser is a syntactic parser of English, based
on link grammar, an original theory of English syntax. Given a
sentence, the system assigns to it a syntactic structure, which
consists of a set of labeled links connecting pairs of words.
The parser also produces a "constituent" representation of a
sentence (showing noun phrases, verb phrases, etc.).

%files
%doc LICENSE README
%{_bindir}/*
%{_datadir}/link-grammar/*
%{_mandir}/man1/link-parser.1.*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A syntactic parser of English
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Support files necessary to compile applications with link-grammar
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Libraries and header files necessary to compile applications using
link-grammar.

%files -n %{devname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/link-grammar.pc
%{_includedir}/link-grammar/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

