#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	bignum
Summary:	bignum - Transparent BigNumber support for Perl
Summary(pl):	bignum - przezroczysta obs³uga wielkich liczb dla Perla
Name:		perl-bignum
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	b3a08efe68348b1de4f8927e2a81f88a
%if %{with tests}
BuildRequires:	perl-Math-BigInt >= 1.65
BuildRequires:	perl(Math::BigFloat) >= 1.39
BuildRequires:	perl-Math-BigRat >= 0.09
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.65
Requires:	perl(Math::BigFloat) >= 1.39
Requires:	perl-Math-BigRat >= 0.09
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package attempts to make it easier to write scripts that use
BigInts/BigFloats in a transparent way. They use the rewritten version
of Math::BigInt and Math::BigFloat, Math::BigRat (for bigrat) and
optionally Math::BigInt::Lite.

It's a great way for writing impressing onliners, which is almost
enough to justify any Perl package ;)

%description -l pl
Ten pakiet u³atwia pisanie skryptów u¿ywaj±cych BigInt/BigFloat w
sposób przezroczysty. U¿ywaj± przepisanej wersji Math::BigInt 
i Math::BigFloat, Math::BigRat (w bigrat) oraz opcjonalnie
Math::BigInt::Lite.

Jest to ¶wietny sposób to pisania jednolinijkowców, które s± prawie
wystarczaj±ce do usprawiedliwienia dowolnego pakietu perlowego ;)

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README TODO
%{perl_vendorlib}/big*.pm
%{perl_vendorlib}/Math/Big*/Trace.pm
%{_mandir}/man3/*
