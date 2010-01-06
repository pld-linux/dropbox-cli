Summary:	Dropbox Linux CLI
Name:		dropbox-cli
Version:	20100106
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://dl.getdropbox.com/u/43645/dbcli.py
# Source0-md5:	76babc858d10330650e105a4abb11ee6
URL:		http://wiki.dropbox.com/DropboxAddons/DropboxLinuxCLI
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dropbox Linux CLI.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/dropbox-cli

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dropbox-cli
