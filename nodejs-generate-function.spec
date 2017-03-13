%{?scl:%scl_package nodejs-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global srcname generate-function

%global commit0 3d5fc8de5859be95f58e3af9bfb5f663edd95149
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-%{srcname}
Version:        2.0.0
Release:        3%{?dist}
Summary:        Module that helps you write generated functions in Node

License:        MIT
URL:            https://github.com/mafintosh/generate-function
# license is included in next not released version
Source0:        https://github.com/mafintosh/%{srcname}/archive/%{commit0}.tar.gz#/%{srcname}-%{shortcommit0}.tar.gz
Source1:        https://raw.githubusercontent.com/mafintosh/generate-function/master/LICENSE

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tape)
%endif

%description
%{summary}.

%prep
%setup -n %{pkg_name}-%{version} -qn %{srcname}-%{commit0}
cp -p %{SOURCE1} .
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
tape test.js
%endif

%files
%doc README.md example.js
%license LICENSE
%{nodejs_sitelib}/%{srcname}

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-3
- Rebuild for rhscl

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.0-1
- Initial packaging
