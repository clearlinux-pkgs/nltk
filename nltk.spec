#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nltk
Version  : 3.4
Release  : 5
URL      : https://files.pythonhosted.org/packages/6f/ed/9c755d357d33bc1931e157f537721efb5b88d2c583fe593cc09603076cc3/nltk-3.4.zip
Source0  : https://files.pythonhosted.org/packages/6f/ed/9c755d357d33bc1931e157f537721efb5b88d2c583fe593cc09603076cc3/nltk-3.4.zip
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
Requires: requests
Requires: scikit-learn
Requires: scipy
Requires: singledispatch
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : singledispatch
BuildRequires : six

%description
natural language processing.  NLTK requires Python 2.7, 3.4, 3.5, 3.6, or 3.7.

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
%setup -q -n nltk-3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542839341
python3 setup.py build

%install
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
