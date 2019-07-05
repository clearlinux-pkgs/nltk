#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nltk
Version  : 3.4.4
Release  : 10
URL      : https://files.pythonhosted.org/packages/87/16/4d247e27c55a7b6412e7c4c86f2500ae61afcbf5932b9e3491f8462f8d9e/nltk-3.4.4.zip
Source0  : https://files.pythonhosted.org/packages/87/16/4d247e27c55a7b6412e7c4c86f2500ae61afcbf5932b9e3491f8462f8d9e/nltk-3.4.4.zip
Summary  : Natural Language Toolkit
Group    : Development/Tools
License  : Apache-2.0
Requires: nltk-license = %{version}-%{release}
Requires: nltk-python = %{version}-%{release}
Requires: nltk-python3 = %{version}-%{release}
Requires: gensim
Requires: matplotlib
Requires: numpy
Requires: pyparsing
Requires: python-crfsuite
Requires: requests
Requires: scikit-learn
Requires: scipy
Requires: singledispatch
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : gensim
BuildRequires : matplotlib
BuildRequires : numpy
BuildRequires : pyparsing
BuildRequires : python-crfsuite
BuildRequires : requests
BuildRequires : scikit-learn
BuildRequires : scipy
BuildRequires : singledispatch
BuildRequires : six

%description
# Natural Language Toolkit (NLTK)
[![PyPI](https://img.shields.io/pypi/v/nltk.svg)](https://pypi.python.org/pypi/nltk)
[![Travis](https://travis-ci.org/nltk/nltk.svg?branch=develop)](https://travis-ci.org/nltk/nltk)

%package license
Summary: license components for the nltk package.
Group: Default

%description license
license components for the nltk package.


%package python
Summary: python components for the nltk package.
Group: Default
Requires: nltk-python3 = %{version}-%{release}

%description python
python components for the nltk package.


%package python3
Summary: python3 components for the nltk package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nltk package.


%prep
%setup -q -n nltk-3.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562309289
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nltk
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/nltk/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nltk/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
