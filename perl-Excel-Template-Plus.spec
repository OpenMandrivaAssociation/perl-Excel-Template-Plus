%define upstream_name    Excel-Template-Plus
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Testing module for use with Excel::Template::Plus
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Excel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Excel::Template)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Param)
BuildRequires:	perl(Spreadsheet::ParseExcel)
BuildRequires:	perl(Template)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module is an extension of the Excel::Template module, which allows the
user to use various "engines" from which you can create Excel files through
Excel::Template.

The idea is to use the existing (and very solid) excel file generation code
in Excel::Template, but to extend its more templatey bits with more
powerful options.

The only engine currently provided is the Template Toolkit engine, which
replaces Excel::Template's built in template features (the LOOP, and IF
constructs) with the full power of TT. This is similar to the module
Excel::Template::TT, but expands on that even further to try and create a
more extensive system.

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
%doc ChangeLog META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 654320
- rebuild for updated spec-helper

* Sat Jan 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 627237
- import perl-Excel-Template-Plus

