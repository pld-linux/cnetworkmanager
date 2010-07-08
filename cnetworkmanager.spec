Summary:	Command-line client for NetworkManager
Name:		cnetworkmanager
Version:	0.21.1
Release:	2
License:	GPL v2+
Group:		Networking/Admin
Source0:	http://vidner.net/martin/software/cnetworkmanager/%{name}-%{version}.tar.gz
# Source0-md5:	3703a43a6d6f3692cb8dbac6372834f2
URL:		http://vidner.net/martin/software/cnetworkmanager/
BuildRequires:	dbus-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	python-dbus
Requires:	python-pygobject
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cnetworkmanager is a command-line client for NetworkManager, intended
to supplement and replace the GUI applets.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/cnetworkmanager
%{py_sitescriptdir}/cnetworkmanager-%{version}-py*.egg-info
%dir %{py_sitescriptdir}/dbusclient
%attr(755,root,root) %{py_sitescriptdir}/dbusclient/*.py[co]
%dir %{py_sitescriptdir}/networkmanager
%attr(755,root,root) %{py_sitescriptdir}/networkmanager/*.py[co]
%dir %{py_sitescriptdir}/networkmanager/applet
%attr(755,root,root) %{py_sitescriptdir}/networkmanager/applet/*.py[co]
%dir %{py_sitescriptdir}/networkmanager/applet/service
%attr(755,root,root) %{py_sitescriptdir}/networkmanager/applet/service/*.py[co]
/etc/dbus-1/system.d/cnetworkmanager.conf
