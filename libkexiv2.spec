#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkexiv2
Version  : 22.08.3
Release  : 45
URL      : https://download.kde.org/stable/release-service/22.08.3/src/libkexiv2-22.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.3/src/libkexiv2-22.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.08.3/src/libkexiv2-22.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: libkexiv2-data = %{version}-%{release}
Requires: libkexiv2-lib = %{version}-%{release}
Requires: libkexiv2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : exiv2-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev

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
%setup -q -n libkexiv2-22.08.3
cd %{_builddir}/libkexiv2-22.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667857357
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1667857357
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkexiv2
cp %{_builddir}/libkexiv2-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkexiv2/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkexiv2-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkexiv2/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
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
/usr/share/package-licenses/libkexiv2/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkexiv2/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
