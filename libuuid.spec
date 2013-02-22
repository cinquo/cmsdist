### RPM external libuuid 2.22.2
Source: http://www.kernel.org/pub/linux/utils/util-linux/v2.22/util-linux-%{realversion}.tar.gz
%define keep_archives true

%prep
%setup -n util-linux-%{realversion}

%build
./configure $([ $(uname) == Darwin ] && echo --disable-shared) \
            --libdir=%{i}/lib64 \
            --prefix="%{i}" \
            --build="%{_build}" \
            --host=%{_host} \
            --disable-silent-rules \
            --disable-tls \
            --disable-rpath \
            --disable-libblkid \
            --disable-libmount \
            --disable-mount \
            --disable-losetup \
            --disable-fsck \
            --disable-partx \
            --disable-mountpoint \
            --disable-fallocate \
            --disable-unshare \
            --disable-eject \
            --disable-agetty \
            --disable-cramfs \
            --disable-wdctl \
            --disable-switch_root \
            --disable-pivot_root \
            --disable-kill \
            --disable-utmpdump \
            --disable-rename \
            --disable-login \
            --disable-sulogin \
            --disable-su \
            --disable-schedutils \
            --disable-wall \
            --disable-makeinstall-setuid \
            --enable-libuuid \
            --disable-uuidd

make %{makeprocesses}

%install
# There is no make install action for the libuuid libraries only
mkdir -p %{i}/lib64
cp -p %{_builddir}/util-linux-%{realversion}/.libs/libuuid.a* %{i}/lib64
%ifos linux
cp -p %{_builddir}/util-linux-%{realversion}/.libs/libuuid.so* %{i}/lib64
%endif
mkdir -p %{i}/include
make install-uuidincHEADERS

%define drop_files %{i}/man
