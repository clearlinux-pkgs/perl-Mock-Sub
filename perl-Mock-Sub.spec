#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Mock-Sub
Version  : 1.09
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/S/ST/STEVEB/Mock-Sub-1.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/ST/STEVEB/Mock-Sub-1.09.tar.gz
Summary  : 'Mock package, object and standard subroutines, with unit testing in mind.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Mock-Sub-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Mock::Sub - Mock package, object and standard subroutines, with unit
testing in mind.

%package dev
Summary: dev components for the perl-Mock-Sub package.
Group: Development
Provides: perl-Mock-Sub-devel = %{version}-%{release}
Requires: perl-Mock-Sub = %{version}-%{release}

%description dev
dev components for the perl-Mock-Sub package.


%package perl
Summary: perl components for the perl-Mock-Sub package.
Group: Default
Requires: perl-Mock-Sub = %{version}-%{release}

%description perl
perl components for the perl-Mock-Sub package.


%prep
%setup -q -n Mock-Sub-1.09
cd %{_builddir}/Mock-Sub-1.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mock::Sub.3
/usr/share/man/man3/Mock::Sub::Child.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
