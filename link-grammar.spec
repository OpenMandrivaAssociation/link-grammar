%define name	link-grammar
%define version	4.2.5
%define cvs	%nil
%define release	2

%define lib_major       4
%define lib_name        %mklibname link-grammar%{lib_major}

Summary:	A syntactic parser of English
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		Office
License:	BSD-like
Source:		%{name}-%{version}.tar.bz2
Patch1:		link-grammar-4.1.2-automake.patch.bz2
Buildroot:	%_tmppath/%{name}-%{version}-root
URL:		http://www.link.cs.cmu.edu/link/
# Patched release:
# URL:		http://www.abisource.com/downloads/link-grammar/

#Requires:
BuildRequires:	automake1.9

%description
The Link Grammar Parser is a syntactic parser of English, based
on link grammar, an original theory of English syntax. Given a
sentence, the system assigns to it a syntactic structure, which
consists of a set of labeled links connecting pairs of words.
The parser also produces a "constituent" representation of a
sentence (showing noun phrases, verb phrases, etc.).

%package -n %{lib_name}
Summary:	A syntactic parser of English
Group:		System/Libraries

%description -n %{lib_name}
The Link Grammar Parser is a syntactic parser of English, based
on link grammar, an original theory of English syntax. Given a
sentence, the system assigns to it a syntactic structure, which
consists of a set of labeled links connecting pairs of words.
The parser also produces a "constituent" representation of a
sentence (showing noun phrases, verb phrases, etc.).

%package -n %{lib_name}-devel
Summary:	Support files necessary to compile applications with link-grammar
Group:		 Development/C
Requires:	%{lib_name} = %{version}
Requires:	link-grammar
Provides:	link-grammar-devel

%description -n %{lib_name}-devel
Libraries and header files necessary to compile applications using
link-grammar.

%prep

%setup -q -n %{name}-%{version}

%build
# cvs build, run autogen.sh:
#./autogen.sh
%configure
# 4.1.1: parallel make is broken
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
%make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT/%{_libdir} -name \*.la -exec rm -f \{\} \;

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -fr $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif


%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root)%{_bindir}/*
%{_datadir}/link-grammar/*

%files -n %{lib_name}
%defattr(644,root,root,755)
%{_libdir}/lib*.so.%{lib_major}
%{_libdir}/lib*.so.%{lib_major}.*

%files -n %{lib_name}-devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/link-grammar.pc
%{_includedir}/link-grammar/*
