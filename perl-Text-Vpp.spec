%include	/usr/lib/rpm/macros.perl
Summary:	Text-Vpp perl module
Summary(pl):	Modu³ perla Text-Vpp
Name:		perl-Text-Vpp
Version:	1.15
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Vpp-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Vpp perl module.

%description -l pl
Modu³ perla Text-Vpp.

%prep
%setup -q -n Text-Vpp-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/vpp
%{perl_sitelib}/Text/Vpp.pm
%{perl_sitelib}/auto/Text/Vpp
%{_mandir}/man[13]/*
