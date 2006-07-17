%define		_alfa	a
Summary:	'Jump and run' game
Summary(pl):	Gra z rodzaju 'skacz i biegnij'
Name:		toppler
Version:	1.1.2
Release:	0.%{_alfa}.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/toppler/%{name}-%{version}%{_alfa}.tar.gz
Source1:	%{name}.desktop
# Source0-md5:	7950bf692e4cb3e78a4fd486f375fcd2
URL:		http://toppler.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/games

%description
In this game player helps a cute little green animal switch off some
kind of "evil" mechanism. The "power off switch" is hidden somewhere
in high towers. On his way to the target he needs to avoid a lot of
strange robots that guard the tower. That sounds all like a normal
jump and run game. What makes this game different is that you walk
arond the tower which is revolving on the screen, so that you only see
the 180° that are currently visible.

%description -l pl
W tej grze gracz pomaga ma³emu, sprytnemu, zielonemu zwierz±tku
wy³±czyæ pewnego rodzaju "diabelskie" mechanizmy. "Wy³±cznik si³y"
jest ukryty gdzie¶ w wysokiej wie¿y. Na jego drodze do celu musi
unikaæ wielu dziwnych robotów które strzeg± wie¿y. Wszystko to brzmi
jak zwyk³a gra z rodzaju "skacz i biegnij". To czym ró¿ni siê ta gra
od innych tego typu jest to, ¿e spacerujesz wokó³ wie¿y, która obraca
siê na ekranie, tak wiêc widoczne jest tylko 180°.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(2755,root,games) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_pixmapsdir}/%{name}.xpm
%dir %{_var}/games/%{name}
%attr(664,root,games) %{_var}/games/%{name}/%{name}.hsc
