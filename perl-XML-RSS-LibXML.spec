%define upstream_name    XML-RSS-LibXML
%define upstream_version 0.3102
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.3102
Release:	1
Epoch:		1

Summary:	Represent A Non-Trivial RSS Element
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/XML-RSS-LibXML-0.3102.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(DateTime::Format::Mail)
BuildRequires:	perl(DateTime::Format::W3CDTF)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::LibXML::XPathContext)

BuildArch:	noarch

%description
XML::RSS::LibXML uses XML::LibXML (libxml2) for parsing RSS instead of
XML::RSS' XML::Parser (expat), while trying to keep interface compatibility
with XML::RSS.

XML::RSS is an extremely handy tool, but it is unfortunately not exactly
the most lean or efficient RSS parser, especially in a long-running
process. So for a long time I had been using my own version of RSS parser
to get the maximum speed and efficiency - this is the re-packaged version
of that module, such that it adheres to the XML::RSS interface.

Use this module when you have severe performance requirements working with
RSS files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.310.100-1mdv2011
+ Revision: 690334
- update to new version 0.3101
- update to new version 0.3100

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1:0.310.0-2
+ Revision: 658902
- rebuild for updated spec-helper

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.310.0-1mdv2011.0
+ Revision: 551209
- bump epoch
- update to 0.3100

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.3004-2mdv2010.0
+ Revision: 440769
- rebuild

* Thu Mar 05 2009 Michael Scherer <misc@mandriva.org> 0.3004-1mdv2009.1
+ Revision: 348894
- import perl-XML-RSS-LibXML



