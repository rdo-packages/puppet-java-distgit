%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-java
%global commit d36a0f6f1298176dd3ac912f23424c5c54138bf9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-java
Version:        7.3.0
Release:        1%{?alphatag}%{?dist}
Summary:        Installs the correct Java package on various platforms.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-java

Source0:        http://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Installs the correct Java package on various platforms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/java/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/java/



%files
%{_datadir}/openstack-puppet/modules/java/


%changelog
* Fri Apr 01 2022 RDO <dev@lists.rdoproject.org> 7.3.0-1.d36a0f6git
- Update to post 7.3.0 (d36a0f6f1298176dd3ac912f23424c5c54138bf9)



