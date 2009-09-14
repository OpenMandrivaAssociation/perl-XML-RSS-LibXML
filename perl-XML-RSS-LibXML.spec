%define realname   XML-RSS-LibXML
%define version    0.3004
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Represent A Non-Trivial RSS Element
Source:     http://www.cpan.org/modules/by-module/XML/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(DateTime::Format::Mail)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(XML::LibXML::XPathContext)
BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*
