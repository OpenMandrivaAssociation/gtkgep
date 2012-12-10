%define name	gtkgep
%define version	0.2.3
%define release 7

%define major 0
%define libname %mklibname %name %major

Name: 	 %{name}
Summary: Real-time guitar effects
Version: %{version}
Release: %{release}
Source0:		%{name}-%{version}.tar.bz2
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
%makeinstall_std
rm -f $RPM_BUILD_ROOT/%_libdir/*.a

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=GTK Guitar Effects
Comment=Realtime effects
Categories=Audio;
EOF

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop

%files -n %libname
%defattr(-,root,root)
%dir %{_libdir}/%name-%version
%dir %{_libdir}/%name-%version/plugins
%{_libdir}/%name-%version/plugins/*.so



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-7mdv2011.0
+ Revision: 619288
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.3-6mdv2010.0
+ Revision: 429337
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-5mdv2009.0
+ Revision: 246688
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.2.3-3mdv2008.1
+ Revision: 131730
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import gtkgep


* Fri Apr 08 2005 Olivier Thauvin <nanardon@mandrake.org> 0.2.3-3mdk
- %%mklibname
- amd64 fix

* Tue Jul 15 2003 Austin Acton <aacton@yorku.ca> 0.2.3-2mdk
- DIRM

* Mon Feb 17 2003 Austin Acton <aacton@yorku.ca> 0.2.3-1mdk
- initial package
