Name:		agnes
Version:	1.1
Release:	1%{?dist}
Summary:	Agnes went for a walk.

Group:		Amusements/Games
License:	BSD
URL:		http://agnes.agnes.agnes/
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	javac
Requires:	jar

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc



%changelog
* Fri Oct 18 2013 Sri Sankaran <sri@redhat.com> 1.1-1
- new package built with tito


