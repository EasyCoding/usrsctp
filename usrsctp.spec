%global commit0 f4925bd5ebb2db38263eef0ec816bf393293cf9c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20201017

Name: usrsctp
Version: 1.0.0
Release: 0.1.%{date}git%{shortcommit0}%{?dist}

License: BSD
Summary: Portable SCTP userland stack
URL: https://github.com/sctplab/%{name}
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: gcc

%description
SCTP is a message oriented, reliable transport protocol with direct support
for multihoming that runs on top of IP or UDP, and supports both v4 and v6
versions.

Like TCP, SCTP provides reliable, connection oriented data delivery with
congestion control. Unlike TCP, SCTP also provides message boundary
preservation, ordered and unordered message delivery, multi-streaming and
multi-homing. Detection of data corruption, loss of data and duplication
of data is achieved by using checksums and sequence numbers. A selective
retransmission mechanism is applied to correct loss or corruption of data.

In this manual the socket API for the SCTP User-land implementation will be
described. It is based on RFC 6458. The main focus of this document is on
pointing out the differences to the SCTP Sockets API. For all aspects of the
sockets API that are not mentioned in this document, please refer to RFC
6458. Questions about SCTP itself can hopefully be answered by RFC 4960.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
%meson \
    -Dwerror=false \
    -Dsctp_debug=false \
    -Dsctp_inet=true \
    -Dsctp_inet6=true \
    -Dsctp_build_programs=false
%meson_build

%check
%meson_test

%install
%meson_install

%files
%doc README.md Manual.md
%license LICENSE.md
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Oct 30 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-0.1.20201017gitf4925bd
- Initial SPEC release.
