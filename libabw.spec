#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libabw
Version  : 0.1.2
Release  : 1
URL      : https://dev-www.libreoffice.org/src/libabw-0.1.2.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libabw-0.1.2.tar.xz
Summary  : A library for reading and writing AbiWord(tm) documents
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libabw-bin
Requires: libabw-lib
Requires: libabw-license
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
Requires: libabw-license

%description bin
bin components for the libabw package.


%package dev
Summary: dev components for the libabw package.
Group: Development
Requires: libabw-lib
Requires: libabw-bin
Provides: libabw-devel

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
Requires: libabw-license

%description lib
lib components for the libabw package.


%package license
Summary: license components for the libabw package.
Group: Default

%description license
license components for the libabw package.


%prep
%setup -q -n libabw-0.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534617263
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534617263
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libabw
cp COPYING.MPL %{buildroot}/usr/share/doc/libabw/COPYING.MPL
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
/usr/lib64/libabw-0.1.so.1.0.2

%files license
%defattr(-,root,root,-)
/usr/share/doc/libabw/COPYING.MPL