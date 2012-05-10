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

