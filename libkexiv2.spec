#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkexiv2
Version  : 20.08.2
Release  : 22
URL      : https://download.kde.org/stable/release-service/20.08.2/src/libkexiv2-20.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.2/src/libkexiv2-20.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.2/src/libkexiv2-20.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: libkexiv2-data = %{version}-%{release}
Requires: libkexiv2-lib = %{version}-%{release}
Requires: libkexiv2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : pkg-config
BuildRequires : pkgconfig(exiv2)

%description
EXIV2 Library interface for KDE
-- AUTHORS ------------------------------------------------------------

%package data
Summary: data components for the libkexiv2 package.
Group: Data

%description data
data components for the libkexiv2 package.


%package dev
Summary: dev components for the libkexiv2 package.
Group: Development
Requires: libkexiv2-lib = %{version}-%{release}
Requires: libkexiv2-data = %{version}-%{release}
Provides: libkexiv2-devel = %{version}-%{release}
Requires: libkexiv2 = %{version}-%{release}

%description dev
dev components for the libkexiv2 package.


%package lib
Summary: lib components for the libkexiv2 package.
Group: Libraries
Requires: libkexiv2-data = %{version}-%{release}
Requires: libkexiv2-license = %{version}-%{release}

%description lib
lib components for the libkexiv2 package.


%package license
Summary: license components for the libkexiv2 package.
Group: Default

%description license
license components for the libkexiv2 package.


%prep
%setup -q -n libkexiv2-20.08.2
cd %{_builddir}/libkexiv2-20.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602613112
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602613112
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkexiv2
cp %{_builddir}/libkexiv2-20.08.2/COPYING %{buildroot}/usr/share/package-licenses/libkexiv2/133efad5329acf364135c569ac01ec084c3d4647
cp %{_builddir}/libkexiv2-20.08.2/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libkexiv2/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/libkexiv2-20.08.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/libkexiv2/c08668a6ace9b36ba46940609040748161b03a37
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/libkexiv2.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KExiv2/KExiv2/KExiv2
/usr/include/KF5/KExiv2/KExiv2/KExiv2Data
/usr/include/KF5/KExiv2/KExiv2/KExiv2Previews
/usr/include/KF5/KExiv2/KExiv2/RotationMatrix
/usr/include/KF5/KExiv2/kexiv2/kexiv2.h
/usr/include/KF5/KExiv2/kexiv2/kexiv2data.h
/usr/include/KF5/KExiv2/kexiv2/kexiv2previews.h
/usr/include/KF5/KExiv2/kexiv2/libkexiv2_export.h
/usr/include/KF5/KExiv2/kexiv2/rotationmatrix.h
/usr/include/KF5/libkexiv2_version.h
/usr/lib64/cmake/KF5KExiv2/KF5KExiv2Config.cmake
/usr/lib64/cmake/KF5KExiv2/KF5KExiv2ConfigVersion.cmake
/usr/lib64/cmake/KF5KExiv2/KF5KExiv2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KExiv2/KF5KExiv2Targets.cmake
/usr/lib64/libKF5KExiv2.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KExiv2.so.15.0.0
/usr/lib64/libKF5KExiv2.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkexiv2/133efad5329acf364135c569ac01ec084c3d4647
/usr/share/package-licenses/libkexiv2/c08668a6ace9b36ba46940609040748161b03a37
/usr/share/package-licenses/libkexiv2/ff3ed70db4739b3c6747c7f624fe2bad70802987
