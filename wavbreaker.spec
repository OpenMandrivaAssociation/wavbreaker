Name:		wavbreaker
Version:	0.15
Release:	1
Summary:	Gtk+ program to split WAV files between songs
License:	GPLv2+
Group:		Sound
URL:		http://wavbreaker.sf.net/
Source0:	https://github.com/thp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(alsa)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	desktop-file-utils
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(libmpg123)
Recommends:     gstreamer1.0-moodbar
Suggests:       moodbar

%description
This application's purpose in life is to take a wave file and break it up into
multiple wave files.  It makes a clean break at the correct position to burn
the files to an audio cd without any dead air between the tracks.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc AUTHORS README.md
%license COPYING
%_bindir/wavbreaker
%_bindir/wavgen
%_bindir/wavinfo
%_bindir/wavmerge
%_datadir/applications/net.sourceforge.wavbreaker.desktop
%_iconsdir/hicolor/scalable/apps/net.sourceforge.%name.svg
%_mandir/man1/wavbreaker.1.*
%_mandir/man1/wavinfo.1.*
%_mandir/man1/wavmerge.1.*
