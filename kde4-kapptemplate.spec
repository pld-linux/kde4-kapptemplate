#
# TODO:
# - add man files
#
%define		orgname		kapptemplate
%define		_state		stable
%define		qtver		4.8.1

Summary:	KDE application framework generator
Summary(pl.UTF-8):	Generator szkieletu dla aplikacji KDE
Name:		kde4-kapptemplate
Version:	4.14.3
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	6b43a11be78d7b5fb8a2ee83f0e7c311
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	perl
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdesdk-kapptemplate
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modular shell script that will automatically create a framework for
either a normal KDE 3.x application, a KPart application, a KPart
plugin, or convert an existing application.

%description -l pl.UTF-8
Modularny skrypt, który potrafi automatycznie wygenerować szkielet
katalogów dla zwykłej aplikacji pod KDE 3.x, aplikacji KPart, wtyczki
KPart lub skonwertować istniejącą aplikację.

%prep
%setup -q -n %{orgname}-%{version}
%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang	kapptemplate	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kapptemplate.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kapptemplate
%{_datadir}/config.kcfg/kapptemplate.kcfg
%{_desktopdir}/kde4/kapptemplate.desktop
%dir %{_datadir}/apps/kdevappwizard
%{_datadir}/apps/kdevappwizard/templates
%{_datadir}/apps/kdevappwizard/template_previews
%{_iconsdir}/*/*x*/apps/kapptemplate.*
