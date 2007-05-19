%define name wavbreaker
%define version 0.8.0
%define release %mkrel 1

Summary:	Gtk+ program to split WAV files between songs
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://huli.org/wavbreaker/%{name}-%{version}.tar.bz2
URL:		http://huli.org/wavbreaker/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
Prefix:		%{_prefix}
BuildRequires:	gtk+2-devel 
BuildRequires:  libxml2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:	desktop-file-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
This application's purpose in life is to take a wave file and break it up into
multiple wave files.  It makes a clean break at the correct position to burn
the files to an audio cd without any dead air between the tracks.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%{update_desktop_database}

%postun
%{clean_menus}
%{clean_desktop_database}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*
%_iconsdir/hicolor/16x16/apps/%name.png
%_iconsdir/hicolor/22x22/apps/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_mandir/man1/*
