Summary:	A library providing ability to interpret and import Visio diagrams
Summary(pl.UTF-8):     Biblioteka dostarczająca możliwość interpretowania i importowania diagramów Visio
Name:		libvisio
Version:	0.0.14
Release:	1
License:	GPL+ or LGPLv2+ or MPLv1.1
Group:		Libraries
URL:		http://www.freedesktop.org/wiki/Software/libvisio
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
# Source0-md5:	740188f5b72cc290c89bf306461178ad
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	libwpd-devel
BuildRequires:	libwpg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libvisio is library providing ability to interpret and import Visio
diagrams into various applications. You can find it being used in
libreoffice.

%description -l pl.UTF-8
Libvisio to biblioteka dostarczająca możliwość interpretowania
i importowania diagramów Visio do wielu aplikacji. Znajdziesz ją
w libreoffice.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description devel -l pl.UTF-8
Paczka %{name}-devel zawiera biblioteki i pliki nagłówkowe do
tworzenia aplikacji opartych na %{name}.

%package apidocs
Summary:	%{name} API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki %{name}
Group:		Documentation

%description apidocs
API and internal documentation for %{name} library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki %{name}.

%package tools
Summary:	Tools to transform Visio diagrams into other formats
Summary(pl.UTF-8):	Użytki do przekształcania diagramów Visio do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform Visio diagrams into other formats. Currently
supported: XHTML, raw.

%description tools -l pl.UTF-8
Narzędzia do przekształcania diagramów Visio do innych formatów. Aktualnie wspierane:
XHTML, raw.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-werror \

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/%{name}-0.0.so.*.*.*
%ghost %{_libdir}/libvisio-0.0.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/%{name}-0.0.so
%{_includedir}/%{name}-0.0
%{_pkgconfigdir}/%{name}-0.0.pc

%files apidocs
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vsd2raw
%attr(755,root,root) %{_bindir}/vsd2xhtml
