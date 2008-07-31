%define module  Term-ReadLine-Perl
%define name    perl-%{module}
%define version 1.0302
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface to readline libraries
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a quick implementation of the minimal interface to Readline
libraries. The implementation is made in Perl (mostly) by Jeffrey
Friedl. The only thing this library does is to make it conformant (and
add some minimal changes, like using Term::ReadKey if present, and
correct work under xterm). 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# useless in non-interactive context

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Term

