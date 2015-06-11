#
# Conditional build:
%bcond_without	tests	# "make check"
#
Summary:	OpenPA - portable library for atomic operations
Summary(pl.UTF-8):	OpenPA - przenośna biblioteka operacji atomowych
Name:		openpa
Version:	1.0.4
Release:	2
License:	BSD-like
Group:		Libraries
Source0:	http://trac.mpich.org/projects/openpa/raw-attachment/wiki/Downloads/%{name}-%{version}.tar.gz
# Source0-md5:	3ad998bb26ac84ee7de262db94dd7656
URL:		http://trac.mpich.org/projects/openpa/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of this project is to provide an open source, highly-portable
library that provides atomic primitives (and related constructs) for
high performance, concurrent software. This project is a collaboration
between the Mathematics and Computer Science (MCS) division at Argonne
National Laboratory (ANL) and the HDF Group. The code was originally
derived from work on the MPICH2 project. 

%description -l pl.UTF-8
Celem tego projektu jest dostarczenie mającej otwarte źródła, w dużym
stopniu przenośnej biblioteki zapewniającej podstawowe operacje
atomowe (i związane z nimi konstrukcje) dla wysoko wydajnego
oprogramowania współbieżnego. Ten projekt jest efektem współpracy
między wydziałem MCS (Mathematics and Computer Science - matematyki i
informatyki) w Argonne National Laboratory (ANL) oraz HDF Group. Kod
oryginalnie wywodzi się z projektu MPICH2.

%package devel
Summary:	Header files for OpenPA library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenPA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OpenPA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenPA.

%package static
Summary:	Static OpenPA library
Summary(pl.UTF-8):	Statyczna biblioteka OpenPA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenPA library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenPA.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--disable-silent-rules
%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libopa.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYRIGHT README
%attr(755,root,root) %{_libdir}/libopa.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopa.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopa.so
%{_includedir}/opa_*.h
%{_includedir}/primitives
%{_pkgconfigdir}/openpa.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libopa.a
