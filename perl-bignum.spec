#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	bignum
Summary:	bignum - Transparent BigNumber support for Perl
Summary(pl.UTF-8):	bignum - przezroczysta obsługa wielkich liczb dla Perla
Name:		perl-bignum
Version:	0.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pnam}-%{version}.tar.gz
# Source0-md5:	0df3a7c83541ff19cab23af7d9394a31
URL:		http://search.cpan.org/dist/bignum/
%if %{with tests}
BuildRequires:	perl-Math-BigInt >= 1.88
BuildRequires:	perl-Math-BigRat >= 0.21
BuildRequires:	perl-Test-Simple >= 0.62
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.88
Requires:	perl-Math-BigRat >= 0.21
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package attempts to make it easier to write scripts that use
BigInts/BigFloats in a transparent way. They use the rewritten version
of Math::BigInt and Math::BigFloat, Math::BigRat (for bigrat) and
optionally Math::BigInt::Lite.

It's a great way for writing impressing onliners, which is almost
enough to justify any Perl package ;)

%description -l pl.UTF-8
Ten pakiet ułatwia pisanie skryptów używających BigInt/BigFloat w
sposób przezroczysty. Używają przepisanej wersji Math::BigInt 
i Math::BigFloat, Math::BigRat (w bigrat) oraz opcjonalnie
Math::BigInt::Lite.

Jest to świetny sposób to pisania jednolinijkowców, które są prawie
wystarczające do usprawiedliwienia dowolnego pakietu perlowego ;)

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
%{perl_vendorlib}/bigint.pm
%{perl_vendorlib}/bignum.pm
%{perl_vendorlib}/bigrat.pm
%dir %{perl_vendorlib}/Math/BigFloat
%{perl_vendorlib}/Math/BigFloat/Trace.pm
%{perl_vendorlib}/Math/BigInt/Trace.pm
%{_mandir}/man3/bigint.3pm*
%{_mandir}/man3/bignum.3pm*
%{_mandir}/man3/bigrat.3pm*
