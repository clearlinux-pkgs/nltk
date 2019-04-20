#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nltk
Version  : 3.4.1
Release  : 8
URL      : https://files.pythonhosted.org/packages/73/56/90178929712ce427ebad179f8dc46c8deef4e89d4c853092bee1efd57d05/nltk-3.4.1.zip
Source0  : https://files.pythonhosted.org/packages/73/56/90178929712ce427ebad179f8dc46c8deef4e89d4c853092bee1efd57d05/nltk-3.4.1.zip
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
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : singledispatch
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
natural language processing.  NLTK requires Python 2.7, 3.5, 3.6, or 3.7.

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
%setup -q -n nltk-3.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555528980
export LDFLAGS="${LDFLAGS} -fno-lto"
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
