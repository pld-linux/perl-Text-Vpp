%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Vpp
Summary:	Text::Vpp - Perl extension for a versatile text pre-processor
Name:		perl-Text-Vpp
Version:	1.16
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class enables to preprocess a file a bit like cpp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
