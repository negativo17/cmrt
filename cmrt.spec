Name:           cmrt
Epoch:          1
Version:        1.0.6
Release:        1%{?dist}
Summary:        Media GPU kernel manager for Intel G45 & HD Graphics family
License:        MIT
URL:            https://01.org/linuxmedia/vaapi

Source0:        https://github.com/intel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-configure.patch

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(libdrm) >= 2.4.23
BuildRequires:  pkgconfig(libva) >= 0.34

%description
One solution to expose Intel’s Gen GPU’s high performance through high level
language.

%package devel
Summary:        Development files for the C for Media Runtime
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description devel
%{name}-devel contains the files necessary to build packages that use the
%{name} library.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure
%make_build

%install
%make_install 
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%license AUTHORS COPYING
%doc NEWS README
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_libdir}/lib%{name}.so.1.1001.0
%{_libdir}/lib%{name}.so.1

%files devel
%{_includedir}/cm_rt.h
%{_includedir}/cm_rt_linux.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libcmrt.pc

%changelog
* Sun May 03 2020 Simone Caronni <negativo17@gmail.com> - 1:1.0.6-1
- First build.
