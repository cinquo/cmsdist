### RPM external p5-params-validate 1.00
## INITENV +PATH PERL5LIB %i/lib/perl5
%define downloadn Params-Validate
Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{downloadn}-%{realversion}.tar.gz
Requires: p5-module-build

%prep
%setup -n %downloadn-%realversion

%build
LC_ALL=C; export LC_ALL
perl Build.PL --install_base %i
./Build

%install
./Build install
