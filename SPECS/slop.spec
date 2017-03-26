%define name slop
%define version 5.3.37
%define unmangled_version 5.3.37
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
BuildArch: x86_64
Requires: glm-devel libXext
BuildRequires: mesa-libEGL-devel libXext cmake gcc-c++ glm-devel
Vendor: naelstrof <naelstrof@gmail.com>
Url: https://github.com/naelstrof/slop/archive/v%{unmangled_version}

%description
slop (Select Operation) is an application that queries for a selection from the user and prints the region to stdout.

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
cmake -DCMAKE_INSTALL_PREFIX="$RPM_BUILD_ROOT/usr/" ./
make

%install
make install
sed -e s:$RPM_BUILD_ROOT::g install_manifest.txt > install_manifest_patched.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files -f install_manifest_patched.txt
%defattr(-,root,root)
