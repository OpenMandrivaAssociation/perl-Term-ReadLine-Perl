%define upstream_name    Term-ReadLine-Perl
%define upstream_version 1.0303

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Epoch:		1

Summary:	Perl interface to readline libraries
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

BuildArch:	noarch

%description
This is a quick implementation of the minimal interface to Readline
libraries. The implementation is made in Perl (mostly) by Jeffrey
Friedl. The only thing this library does is to make it conformant (and
add some minimal changes, like using Term::ReadKey if present, and
correct work under xterm). 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# useless in non-interactive context

%install
%makeinstall_std

%files
%doc CHANGES README
%{perl_vendorlib}/Term

%changelog
* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.30.300-1mdv2010.1
+ Revision: 461031
- bmping epoch
- update to 1.0303

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0302-6mdv2010.0
+ Revision: 430579
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.0302-5mdv2009.0
+ Revision: 258507
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0302-4mdv2009.0
+ Revision: 246520
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0302-2mdv2008.1
+ Revision: 136360
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0302-2mdv2008.0
+ Revision: 86952
- rebuild


* Mon May 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0302-1mdv2007.0
- New release 1.0302

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0208-2mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0208-1mdk
- New release 1.0208

* Wed Mar 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0207-2mdk
- fix summary
- fix directory ownership

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0207-1mdk
- New release 1.0207
- spec cleanup

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0203-2mdk
- Fix url
- Make rpmbuildupdate happy

* Tue Feb 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0203-1mdk
- from Maxim Heijndijk <cchq@wanadoo.nl> :
	- Initial wrap.

