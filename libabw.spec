#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libabw
Version  : 0.1.3
Release  : 7
URL      : https://dev-www.libreoffice.org/src/libabw-0.1.3.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libabw-0.1.3.tar.xz
Summary  : A library for reading and writing AbiWord(tm) documents
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libabw-bin = %{version}-%{release}
Requires: libabw-lib = %{version}-%{release}
Requires: libabw-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : doxygen
BuildRequires : gperf
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-generators-0.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(zlib)

%description
INSTALLATION:
Unix/Linux
==========
Installation on Unix/Linux should be simple. Simply execute the following
sequence of commands:

%package bin
Summary: bin components for the libabw package.
Group: Binaries
Requires: libabw-license = %{version}-%{release}

%description bin
bin components for the libabw package.


%package dev
Summary: dev components for the libabw package.
Group: Development
Requires: libabw-lib = %{version}-%{release}
Requires: libabw-bin = %{version}-%{release}
Provides: libabw-devel = %{version}-%{release}
Requires: libabw = %{version}-%{release}

%description dev
dev components for the libabw package.


%package doc
Summary: doc components for the libabw package.
Group: Documentation

%description doc
doc components for the libabw package.


%package lib
Summary: lib components for the libabw package.
Group: Libraries
Requires: libabw-license = %{version}-%{release}

%description lib
lib components for the libabw package.


%package license
Summary: license components for the libabw package.
Group: Default

%description license
license components for the libabw package.


%prep
%setup -q -n libabw-0.1.3
cd %{_builddir}/libabw-0.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592622976
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1592622976
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libabw
cp %{_builddir}/libabw-0.1.3/COPYING.MPL %{buildroot}/usr/share/package-licenses/libabw/9744cedce099f727b327cd9913a1fdc58a7f5599
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/abw2html
/usr/bin/abw2raw
/usr/bin/abw2text

%files dev
%defattr(-,root,root,-)
/usr/include/libabw-0.1/libabw/AbiDocument.h
/usr/include/libabw-0.1/libabw/libabw.h
/usr/lib64/libabw-0.1.so
/usr/lib64/pkgconfig/libabw-0.1.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libabw/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libabw-0.1.so.1
/usr/lib64/libabw-0.1.so.1.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libabw/9744cedce099f727b327cd9913a1fdc58a7f5599
