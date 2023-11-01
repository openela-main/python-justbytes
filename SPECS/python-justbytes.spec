%global srcname justbytes

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{srcname}
Version:        0.14
Release:        2%{?dist}
Summary:        Library for handling computation with address ranges in bytes

License:        LGPLv2+
URL:            http://pypi.python.org/pypi/justbytes
Source0:        https://pypi.io/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
A library for handling computations with address ranges. The library also offers\
a configurable way to extract the representation of a value.

%description %{_description}

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-hypothesis
BuildRequires:  python2-justbases
BuildRequires:  python2-six
Requires:       python2-justbases
Requires:       python2-six

%description -n python2-%{srcname} %{_description}

Python 2 version.
%endif # with python2

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-justbases
BuildRequires:  python3-six
Requires:       python3-justbases
Requires:       python3-six

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf justbytes.egg-info

%build
%if %{with python2}
%py2_build
%endif # with python2
%py3_build

%install
%if %{with python2}
%py2_install
%endif # with python2
%py3_install

%check
%if %{with python2}
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v tests
%endif # with python2
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v tests

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/justbytes/
%{python2_sitelib}/justbytes-%{version}-*.egg-info/
%endif # with python2

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/justbytes/
%{python3_sitelib}/justbytes-%{version}-*.egg-info/

%changelog
* Wed May 06 2020  Dennis Keefe <dkeefe@redhat.com> - 0.14-2
- Update to 0.14
- Resolves: rhbz#1824225
 
* Fri Jun 08 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.11-2
- Conditionalize the python2 subpackage

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11-1
- Update to 0.11

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10-2
- Rebuild for Python 3.6

* Wed Aug 10 2016 mulhern <amulhern@redhat.com> - 0.10
- New release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 23 2016 mulhern <amulhern@redhat.com> - 0.6
- Initial release
