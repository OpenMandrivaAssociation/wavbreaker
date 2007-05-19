%define name wavbreaker
%define version 0.6.1
%define release %mkrel 3

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/*
%_datadir/%name
%doc AUTHORS README ChangeLog NEWS
