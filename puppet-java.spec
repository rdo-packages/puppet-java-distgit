%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-java
%global commit 43aa9af1b258abfb671b640867dbafc67681565e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-java
Version:        2.0.0
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
* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 2.0.0-1.43aa9afgit
- Pike update 2.0.0 (43aa9af1b258abfb671b640867dbafc67681565e)


