Summary:	'Jump and run' game
Summary(pl):	Gra w stylu 'skacz i biegnij'
Name:		toppler
Version:	1.0.4
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/toppler/%{name}-%{version}.tar.gz
# Source0-md5:	086326a22d6ed7874fde9fcac71fa1db
#Source1:	%{name}.desktop
URL:		http://toppler.sourceforge.net/
BuildRequires:  SDL-devel >= 1.2
BuildRequires:  SDL_mixer-devel >= 1.2
BuildRequires:	gettext-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In this game you have to help a cute little green animal switch off
some kind of "evil" mechanism. The "power off switch" is hidden
somewhere in high towers. On your way to the target you need to avoid
a lot of strange robots that guard the tower. That sounds all like a
normal jump and run game. What makes this game different is that you
walk arond the tower which is revolving on the screen, so that you
only see the 180° that are currently visible.

%description -l pl

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
