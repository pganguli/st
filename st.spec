Name:           st
Version:        0.9
Release:        1%{?dist}
Summary:        simple terminal

License:        MIT
URL:            https://github.com/pganguli/st

BuildRequires:  make gcc pkgconfig
BuildRequires:  libXft-devel libX11-devel fontconfig-devel freetype-devel
Requires:       libXft ncurses-base

Source0:        %{url}/archive/refs/tags/%{version}-pgan.tar.gz

%description
st is a simple terminal implementation for X.

%prep
%setup -n %{name}-%{version}-pgan

%build
%make_build

%install
install -D -p -m 755 st %{buildroot}%{_bindir}/st
install -D -p -m 644 st.1 %{buildroot}%{_mandir}/man1/st.1

%files
%doc README
%license LICENSE
%{_bindir}/st
%{_mandir}/man1/st.1*

%changelog
* Thu Jan 12 2023 Prateek Ganguli <prateek.ganguli@gmail.com> - 0.9-1
- Initial version of the package
