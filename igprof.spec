### RPM external igprof 5.9.3
Source0: http://www.hpl.hp.com/research/linux/atomic_ops/download/libatomic_ops-7.2alpha4.tar.gz
Source1: http://download.savannah.gnu.org/releases/libunwind/libunwind-1.0.1.tar.gz
Source2: http://downloads.sourceforge.net/igprof/igprof-%{realversion}.tar.gz
BuildRequires: cmake
Patch0: igprof-5.9.3-fix-gcc47
Patch1: igprof-5.9.3-fix-python
Patch2: igprof-5.9.3-fix-jemalloc

%prep
%setup -T -b 0 -n libatomic_ops-7.2alpha4
%setup -D -T -b 1 -n libunwind-1.0.1
%setup -D -T -b 2 -n igprof-%{realversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%ifnos darwin
cd ../libatomic_ops*
./configure --prefix=%i
make %makeprocesses install

cd ../libunwind*
./configure CFLAGS="-g -O3" CPPFLAGS="-I%i/include" --prefix=%i --disable-block-signals
make %makeprocesses install

cd ../igprof*
cmake -DCMAKE_INSTALL_PREFIX=%i -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="-I%i/include -g -O3" .
make %makeprocesses
%endif

%install
%ifnos darwin
make %makeprocesses install
%define drop_files %i/share/man
%endif
