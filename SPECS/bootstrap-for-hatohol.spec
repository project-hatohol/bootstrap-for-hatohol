Name: bootstrap-for-hatohol
Version: 3.1.0
# PH means Project Hatohol's build
Release: 1PH
License: MIT
Group: Development/Libraries
Summary: Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created and maintained by Mark Otto and Jacob Thornton.
URL: http://getbootstrap.com/
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Source0: bootstrap-%{version}.zip

%description
Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and
easier web development, created and maintained by Mark Otto and Jacob Thornton.

%prep
%setup -q -n bootstrap-%{version}

%install
DEST_DIR=%{buildroot}/%{_prefix}/libexec/hatohol/client/static
install -d $DEST_DIR/css
install -m 755 dist/css/* $DEST_DIR/css
install -d $DEST_DIR/js
install -m 755 dist/js/* $DEST_DIR/js
install -d $DEST_DIR/fonts
install -m 755 dist/fonts/* $DEST_DIR/fonts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/libexec/hatohol/client/*

%changelog
* Wed Feb 12 2014 Takuro Ashie <ashie@clear-code.com>
- Update to Bootstrap 3.1.0
* Mon Jul 08 2013 Kazuhiro Yamato <kazuhiro.yamato@miraclelinux.com>
- Inital RPM spec. file by Project Hatohol.
