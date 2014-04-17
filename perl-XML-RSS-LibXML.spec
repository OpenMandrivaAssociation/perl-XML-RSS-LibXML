%define upstream_name    XML-RSS-LibXML
%define upstream_version 0.3104
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		1

Summary:	Represent A Non-Trivial RSS Element

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)
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
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


