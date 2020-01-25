%define		status		stable
%define		pearname	Horde_Alarm
Summary:	%{pearname} - Horde alarm libraries
Name:		php-horde-Horde_Alarm
Version:	1.0.8
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	e6ab0f6fa6f1819674401d56a6f720e3
URL:		https://github.com/horde/horde/tree/master/framework/Alarm/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.593
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Date < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Db
Suggests:	php-horde-Horde_Log
Suggests:	php-horde-Horde_Mail
Suggests:	php-horde-Horde_Mime
Suggests:	php-horde-Horde_Notification
Suggests:	php-horde-Horde_Perms
Suggests:	php-horde-Horde_Prefs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an interface to deal with reminders, alarms and
notifications through a standardized API. The following notification
methods are available at the moment: standard Horde notifications,
popups, emails, sms.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Alarm
%{php_pear_dir}/Horde/Alarm.php
%{php_pear_dir}/data/Horde_Alarm
