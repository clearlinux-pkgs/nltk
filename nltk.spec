#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nltk
Version  : 3.6.5
Release  : 34
URL      : https://files.pythonhosted.org/packages/3c/7b/22098799815803fad0b74ecb9b2d5befaa4d3bac880ed7c610aeabb69074/nltk-3.6.5.zip
Source0  : https://files.pythonhosted.org/packages/3c/7b/22098799815803fad0b74ecb9b2d5befaa4d3bac880ed7c610aeabb69074/nltk-3.6.5.zip
Summary  : Natural Language Toolkit
Group    : Development/Tools
License  : Apache-2.0
Requires: nltk-bin = %{version}-%{release}
Requires: nltk-license = %{version}-%{release}
Requires: nltk-python = %{version}-%{release}
Requires: nltk-python3 = %{version}-%{release}
Requires: click
Requires: gensim
Requires: joblib
Requires: matplotlib
Requires: numpy
Requires: pyparsing
Requires: python-crfsuite
Requires: regex
Requires: requests
Requires: scikit-learn
Requires: scipy
Requires: tqdm
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : gensim
BuildRequires : joblib
BuildRequires : matplotlib
BuildRequires : numpy
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyparsing
BuildRequires : pytest
BuildRequires : python-crfsuite
BuildRequires : regex
BuildRequires : requests
BuildRequires : scikit-learn
BuildRequires : scipy
BuildRequires : tox
BuildRequires : tqdm
BuildRequires : virtualenv

%description
# Natural Language Toolkit (NLTK)
[![PyPI](https://img.shields.io/pypi/v/nltk.svg)](https://pypi.python.org/pypi/nltk)
![CI](https://github.com/nltk/nltk/actions/workflows/ci.yaml/badge.svg?branch=develop)

%package bin
Summary: bin components for the nltk package.
Group: Binaries
Requires: nltk-license = %{version}-%{release}

%description bin
bin components for the nltk package.


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
Provides: pypi(nltk)
Requires: pypi(click)
Requires: pypi(joblib)
Requires: pypi(regex)
Requires: pypi(tqdm)

%description python3
python3 components for the nltk package.


%prep
%setup -q -n nltk-3.6.5
cd %{_builddir}/nltk-3.6.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633963097
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nltk
cp %{_builddir}/nltk-3.6.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/nltk/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nltk

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nltk/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
