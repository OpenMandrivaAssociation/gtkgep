%define name	gtkgep
%define version	0.2.3
%define release %mkrel 3

%define major 0
%define libname %mklibname %name %major

Name: 	 %{name}
Summary: Real-time guitar effects
Version: %{version}
Release: %{release}
Source:		%{name}-%{version}.tar.bz2
URL:		http://gtkgep.prv.pl
License:	GPL
Group:		Sound
BuildRequires:	gtk+1.2-devel

%description
GtkGEP turns your computer into a realtime effects processor. You can plug
your guitar into the computer and play with cool distortion effects, for
example. It has a modular plugin structure, with standard plugins including
distortion, overdrive, delay, reverb, equalizers, and a flanger. It works in
16-bit resolution, in mono mode, and with frequencies from 11khz to 44khz.
The sound quality is very good.

%package -n %libname
Summary: Libraries from %name
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n %libname
Libraries from %name

%prep
%setup -q

%build
libtoolize --force
aclocal
automake
autoconf
%configure
perl -p -i -e 's;/usr/local/lib;%_libdir;g' gtkgep_main.c
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT/%_libdir/*.a
rm -f $RPM_BUILD_ROOT/%_libdir/*/*.la

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="sound_section.png" needs="x11" title="GTK Guitar Effects" longtitle="Realtime effects" section="Multimedia/Sound"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%post -n %libname -p /sbin/ldconfig
		
%postun
%clean_menus

%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/%name
%{_menudir}/%name
%{_libdir}/%name-%version

%files -n %libname
%defattr(-,root,root)
%dir %{_libdir}/%name-%version
%dir %{_libdir}/%name-%version/plugins
%{_libdir}/%name-%version/plugins/*.so
%{_libdir}/%name-%version/plugins/*.la
%{_libdir}/lib*.la

