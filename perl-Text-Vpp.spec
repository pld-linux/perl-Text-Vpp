%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Vpp
Summary:	Text::Vpp - Perl extension for a versatile text pre-processor
Summary(pl):	Text::Vpp - perlowe roszerzenie wszechstronnego preprocesora tekstu
Name:		perl-Text-Vpp
Version:	1.16
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class enables to preprocess a file a bit like cpp.

%description -l pl
Ta klasa pozwala na preprocesing plików w sposób nieco podobny do cpp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/vpp
%{perl_vendorlib}/Text/Vpp.pm
%{perl_vendorlib}/auto/Text/Vpp
%{_mandir}/man[13]/*
