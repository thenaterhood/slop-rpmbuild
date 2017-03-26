%define name slop
%define version 5.3.27
%define unmangled_version 5.3.27
%define release 1

Summary: slop (Select Operation) is a screen region selection tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPLv3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64 i686
Requires: libXext mesa-libEGL libX11
BuildRequires: make mesa-libEGL-devel libXext cmake gcc-c++ glm-devel
Vendor: naelstrof <naelstrof@gmail.com>
Url: https://github.com/naelstrof/slop/archive/v%{unmangled_version}

%description
slop (Select Operation) is an application that queries for a selection from the user and prints the region to stdout.

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
cmake -DCMAKE_INSTALL_PREFIX="/usr" ./
make

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f install_manifest.txt
%defattr(-,root,root)

%post
ldconfig
