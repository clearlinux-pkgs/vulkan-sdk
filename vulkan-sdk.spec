#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vulkan-sdk
Version  : 1.0.39.0
Release  : 9
URL      : https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers/archive/sdk-1.0.39.0.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers/archive/sdk-1.0.39.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause NCSA
Requires: vulkan-sdk-bin
Requires: vulkan-sdk-lib
BuildRequires : cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glslang
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-dev32
BuildRequires : mesa-dev
BuildRequires : pkgconfig(32gl)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32sm)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xau)
BuildRequires : pkgconfig(32xcb)
BuildRequires : pkgconfig(32xcomposite)
BuildRequires : pkgconfig(32xcursor)
BuildRequires : pkgconfig(32xdmcp)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(32xft)
BuildRequires : pkgconfig(32xinerama)
BuildRequires : pkgconfig(32xmu)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(32xrandr)
BuildRequires : pkgconfig(32xtst)
BuildRequires : pkgconfig(32xv)
BuildRequires : pkgconfig(32xxf86vm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xdmcp)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xft)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xmu)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xtst)
BuildRequires : pkgconfig(xxf86vm)
BuildRequires : python3-dev
Patch1: build.patch

%description
Google C++ Testing Framework
============================
http://code.google.com/p/googletest/

%package bin
Summary: bin components for the vulkan-sdk package.
Group: Binaries

%description bin
bin components for the vulkan-sdk package.


%package dev
Summary: dev components for the vulkan-sdk package.
Group: Development
Requires: vulkan-sdk-lib
Requires: vulkan-sdk-bin
Provides: vulkan-sdk-devel

%description dev
dev components for the vulkan-sdk package.


%package dev32
Summary: dev32 components for the vulkan-sdk package.
Group: Default
Requires: vulkan-sdk-lib32
Requires: vulkan-sdk-bin
Requires: vulkan-sdk-dev

%description dev32
dev32 components for the vulkan-sdk package.


%package lib
Summary: lib components for the vulkan-sdk package.
Group: Libraries

%description lib
lib components for the vulkan-sdk package.


%package lib32
Summary: lib32 components for the vulkan-sdk package.
Group: Default

%description lib32
lib32 components for the vulkan-sdk package.


%prep
%setup -q -n Vulkan-LoaderAndValidationLayers-sdk-1.0.39.0
%patch1 -p1
pushd ..
cp -a Vulkan-LoaderAndValidationLayers-sdk-1.0.39.0 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485731240
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DBUILD_WSI_MIR_SUPPORT=OFF -DBUILD_TESTS=OFF -DBUILD_VKJSON=OFF -DBUILD_LAYERS=OFF
make VERBOSE=1  %{?_smp_mflags}
popd
mkdir clr-build32
pushd clr-build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=32 -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DBUILD_WSI_MIR_SUPPORT=OFF -DBUILD_TESTS=OFF -DBUILD_VKJSON=OFF -DBUILD_LAYERS=OFF
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1485731240
rm -rf %{buildroot}
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build
%make_install
popd
## make_install_append content
mv %{buildroot}/usr/lib %{buildroot}/usr/lib32
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vulkaninfo

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/vulkan/vk_platform.h
%exclude /usr/include/vulkan/vulkan.h
/usr/include/vulkan/vk_icd.h
/usr/include/vulkan/vk_layer.h
/usr/include/vulkan/vk_sdk_platform.h
/usr/include/vulkan/vulkan.hpp
/usr/lib64/libvulkan.so

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libvulkan.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvulkan.so.1
/usr/lib64/libvulkan.so.1.0.39

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvulkan.so.1
/usr/lib32/libvulkan.so.1.0.39
