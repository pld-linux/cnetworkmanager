Summary:	Command-line client for NetworkManager
Name:		cnetworkmanager
Version:	0.8.4
Release:	1
License:	GPL v2+
Group:		Networking/Admin
Source0:	http://vidner.net/martin/software/cnetworkmanager/%{name}-%{version}.tar.gz
# Source0-md5:	8f3eccaeff900cd68e19785f13c813ab
URL:		http://vidner.net/martin/software/cnetworkmanager/
BuildRequires:	dbus-devel
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
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	sysconfdir=%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/cnetworkmanager
%dir %{_datadir}/cnetworkmanager
%attr(755,root,root) %{_datadir}/cnetworkmanager/cnetworkmanager
%attr(755,root,root) %{_datadir}/cnetworkmanager/pbkdf2.py
/etc/dbus-1/system.d/cnetworkmanager.conf
/etc/dbus-1/system.d/cnetworkmanager-06.conf
