Summary:	Gtk+ program to split WAV files between songs
Name:	wavbreaker
Version:	0.16
Release:	2
License:	GPLv2+
Group:	Sound
Url:		https://wavbreaker.sf.net/
Source0:	https://github.com/thp/wavbreaker/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:	wavbreaker-0.16-supply-valid-content_rating-for-AppData.patch
Patch1:	wavbreaker-0.16-replace-custom-cue-parsing-with-libcue.patch
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcue)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(vorbisfile)
Recommends:	gstreamer1.0-moodbar
Recommends:	moodbar

%description
This application's purpose in life is to take a wave file and break it up into
multiple wave files.  It makes a clean break at the correct position to burn
the files to an audio cd without any dead air between the tracks.

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/wavcli
%{_datadir}/applications/net.sourceforge.%{name}.desktop
%{_datadir}/metainfo/net.sourceforge.%{name}.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/net.sourceforge.%{name}.svg
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/wavcli.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}
