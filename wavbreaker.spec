%define name wavbreaker
%define version 0.9
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Gtk+ program to split WAV files between songs
License:	GPL
Group:		Sound
URL:		http://wavbreaker.sf.net/
Source0:	http://downloads.sourceforge.net/wavbreaker/%{name}-%{version}.tar.bz2
Suggests:       moodbar
BuildRequires:	gtk+2-devel 
BuildRequires:  libxml2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:	desktop-file-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall
%find_lang %name

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

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
