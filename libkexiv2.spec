#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkexiv2
Version  : 24.08.0
Release  : 73
URL      : https://download.kde.org/stable/release-service/24.08.0/src/libkexiv2-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/libkexiv2-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/libkexiv2-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: libkexiv2-data = %{version}-%{release}
Requires: libkexiv2-lib = %{version}-%{release}
Requires: libkexiv2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qt6
BuildRequires : exiv2-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libkexiv2-24.08.0
cd %{_builddir}/libkexiv2-24.08.0
pushd ..
cp -a libkexiv2-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724434565
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724434565
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkexiv2
cp %{_builddir}/libkexiv2-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkexiv2/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkexiv2-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkexiv2/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/libkexiv2.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KExiv2Qt6/KExiv2/KExiv2
/usr/include/KExiv2Qt6/KExiv2/KExiv2Data
/usr/include/KExiv2Qt6/KExiv2/KExiv2Previews
/usr/include/KExiv2Qt6/KExiv2/RotationMatrix
/usr/include/KExiv2Qt6/kexiv2/kexiv2.h
/usr/include/KExiv2Qt6/kexiv2/kexiv2data.h
/usr/include/KExiv2Qt6/kexiv2/kexiv2previews.h
/usr/include/KExiv2Qt6/kexiv2/libkexiv2_export.h
/usr/include/KExiv2Qt6/kexiv2/rotationmatrix.h
/usr/include/KExiv2Qt6/libkexiv2_version.h
/usr/lib64/cmake/KExiv2Qt6/KExiv2Qt6Config.cmake
/usr/lib64/cmake/KExiv2Qt6/KExiv2Qt6ConfigVersion.cmake
/usr/lib64/cmake/KExiv2Qt6/KExiv2Qt6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KExiv2Qt6/KExiv2Qt6Targets.cmake
/usr/lib64/libKExiv2Qt6.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKExiv2Qt6.so.5.1.0
/usr/lib64/libKExiv2Qt6.so.0
/usr/lib64/libKExiv2Qt6.so.5.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkexiv2/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkexiv2/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
