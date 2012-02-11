Summary:	A library providing ability to interpret and import visio diagrams
Name:		libvisio
Version:	0.0.14
Release:	1
License:	GPL+ or LGPLv2+ or MPLv1.1
Group:		Libraries
URL:		http://www.freedesktop.org/wiki/Software/libvisio
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
# Source0-md5:	740188f5b72cc290c89bf306461178ad
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	libwpd-devel
BuildRequires:	libwpg-devel

%description
Libvisio is library providing ability to interpret and import visio
diagrams into various applications. You can find it being used in
libreoffice.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools to transform Visio diagrams into other formats
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform Visio diagrams into other formats. Currently
supported: XHTML, raw.

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

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING.*
%attr(755,root,root) %{_libdir}/%{name}-0.0.so.*

%files devel
%doc %{_docdir}/%{name}
%defattr(644,root,root,755)
%{_includedir}/%{name}-0.0
%attr(755,root,root) %{_libdir}/%{name}-0.0.so
%{_pkgconfigdir}/%{name}-0.0.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vsd2raw
%attr(755,root,root) %{_bindir}/vsd2xhtml
