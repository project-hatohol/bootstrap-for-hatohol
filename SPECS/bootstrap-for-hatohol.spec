Name: bootstrap-for-hatohol
Version: 2.3.2
# PH means Project Hatohol's build
Release: 1PH
License: APLv2
Group: Development/Libraries
Summary: Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created and maintained by Mark Otto and Jacob Thornton.
URL: http://twitter.github.io/bootstrap/
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Source0: bootstrap.zip

%description
Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and
easier web development, created and maintained by Mark Otto and Jacob Thornton.

%prep
%setup -q -n bootstrap

%install
DEST_DIR=%{buildroot}/%{_prefix}/libexec/hatohol/client/static
install -d $DEST_DIR/css
install -m 755 css/* $DEST_DIR/css
install -d $DEST_DIR/js
install -m 755 js/* $DEST_DIR/js
install -d $DEST_DIR/img
install -m 755 img/* $DEST_DIR/img

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/libexec/hatohol/client/*

%changelog
* Mon Jul 08 2013 Kazuhiro Yamato <kazuhiro.yamato@miraclelinux.com>
- Inital RPM spec. file by Project Hatohol.
