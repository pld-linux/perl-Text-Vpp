%include	/usr/lib/rpm/macros.perl
Summary:	Text-Vpp perl module
Summary(pl):	Modu³ perla Text-Vpp
Name:		perl-Text-Vpp
Version:	1.11
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Vpp-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/Vpp
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz
%attr(755,root,root) %{_bindir}/vpp

%{perl_sitelib}/Text/Vpp.pm
%{perl_sitelib}/auto/Text/Vpp
%{perl_sitearch}/auto/Text/Vpp

%{_mandir}/man[13]/*
