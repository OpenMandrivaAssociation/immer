%define devname %mklibname immer -d

Name: immer
Version: 0.8.1
Release: 1
Source0: https://github.com/arximboldi/immer/archive/refs/tags/v%{version}.tar.gz
Summary: Library of persistent and immutable data structures written in C++
URL: https://github.com/arximboldi/immer
License: BSL-1.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildArch: noarch

%description
immer is a library of persistent and immutable data structures written in C++.
These enable whole new kinds of architectures for interactive and concurrent
programs of striking simplicity, correctness, and performance.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C++

%description -n %{devname}
Development files (Headers etc.) for %{name}.

immer is a library of persistent and immutable data structures written in C++.
These enable whole new kinds of architectures for interactive and concurrent
programs of striking simplicity, correctness, and performance.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
