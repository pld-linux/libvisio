#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	A library providing ability to interpret and import Visio diagrams
Summary(pl.UTF-8):	Biblioteka umożliwiająca interpretowanie i importowanie diagramów Visio
Name:		libvisio
Version:	0.1.5
Release:	3
License:	MPL v2.0
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/libvisio/%{name}-%{version}.tar.xz
# Source0-md5:	691522167fe3b0c94becfe5d957883be
URL:		http://www.freedesktop.org/wiki/Software/libvisio
BuildRequires:	boost-devel >= 1.36
BuildRequires:	doxygen
BuildRequires:	gperf >= 3
BuildRequires:	libicu-devel
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libvisio is library providing ability to interpret and import Visio
diagrams into various applications. You can find it being used in
libreoffice.

%description -l pl.UTF-8
Libvisio to biblioteka umożliwiająca interpretowanie i importowanie
diagramów Visio do wielu aplikacji. Jest wykorzystywana przez
libreoffice.

%package devel
Summary:	Development files for libvisio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvisio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libicu-devel
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.0
Requires:	zlib-devel

%description devel
This package contains the header files for developing applications
that use libvisio.

%description devel -l pl.UTF-8
Pen pakiet zawiera pliki nagłówkowe do tworzenia aplikacji opartych na
bibliotece libvisio.

%package static
Summary:	Static libvisio library
Summary(pl.UTF-8):	Statyczna biblioteka libvisio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvisio library.

%description static -l pl.UTF-8
Statyczna biblioteka libvisio.

%package apidocs
Summary:	API documentation for libvisio library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libvisio
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for libvisio library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libvisio.

%package tools
Summary:	Tools to transform Visio diagrams into other formats
Summary(pl.UTF-8):	Programy przekształcania diagramów Visio do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform Visio diagrams into other formats. Currently
supported: XHTML, raw.

%description tools -l pl.UTF-8
Narzędzia do przekształcania diagramów Visio do innych formatów.
Aktualnie obsługiwane są XHTML i raw.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libvisio-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvisio-0.1.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisio-0.1.so
%{_includedir}/libvisio-0.1
%{_pkgconfigdir}/libvisio-0.1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libvisio-0.1.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/%{name}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vsd2raw
%attr(755,root,root) %{_bindir}/vsd2text
%attr(755,root,root) %{_bindir}/vsd2xhtml
%attr(755,root,root) %{_bindir}/vss2raw
%attr(755,root,root) %{_bindir}/vss2text
%attr(755,root,root) %{_bindir}/vss2xhtml
