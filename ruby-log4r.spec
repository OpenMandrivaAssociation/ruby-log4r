%define rname log4r
%define name ruby-%{rname}
%define version 1.0.5
%define release %mkrel 6

Summary: Powerful Logging Library for Ruby
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://log4r.sourceforge.net/
Source0: http://ovh.dl.sourceforge.net/sourceforge/%{rname}/%{rname}-%{version}.tar.bz2
License: GPL
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby
BuildRequires: ruby
BuildArch: noarch

%description
Log4r is a comprehensive and flexible logging library written in Ruby for use
in Ruby programs. It features a hierarchical logging system of any number of
levels, custom level names, logger inheritance, multiple output destinations,
execution tracing, custom formatting, thread safteyness, XML and YAML
configuration, and more.

%prep
%setup -q -n %{rname}-%{version}
sed -i "s|CONFIG\[\"sitelibdir\"\]|\"%{buildroot}\"+CONFIG[\"sitelibdir\"]|" install.rb

%build

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
ruby install.rb 

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/log4r*
%doc INSTALL LICENSE README changelog doc examples tests

