%define name	gtkgep
%define version	0.2.3
%define release 8

Name: 	 %{name}
Summary: Real-time guitar effects
Version: %{version}
Release: %{release}
Source0:		%{name}-%{version}.tar.bz2
URL:		http://gtkgep.prv.pl
License:	GPL
Group:		Sound
BuildRequires:	gtk+1.2-devel
Obsoletes:	%{_lib}gtkgep0
%description
GtkGEP turns your computer into a realtime effects processor. You can plug
your guitar into the computer and play with cool distortion effects, for
example. It has a modular plugin structure, with standard plugins including
distortion, overdrive, delay, reverb, equalizers, and a flanger. It works in
16-bit resolution, in mono mode, and with frequencies from 11khz to 44khz.
The sound quality is very good.

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
rm -f %{buildroot}/%_libdir/*.a

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
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
%doc README COPYING
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%dir %{_libdir}/%name-%version
%dir %{_libdir}/%name-%version/plugins
%{_libdir}/%name-%version/plugins/*.so

