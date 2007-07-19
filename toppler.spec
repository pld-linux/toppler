Summary:	'Jump and run' game
Summary(pl.UTF-8):	Gra z rodzaju 'skacz i biegnij'
Name:		toppler
Version:	1.1.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/toppler/%{name}-%{version}.tar.gz
# Source0-md5:	15ee44094e6a4e2a4f5f9b661f3fb617
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
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

%description -l pl.UTF-8
W tej grze gracz pomaga małemu, sprytnemu, zielonemu zwierzątku
wyłączyć pewnego rodzaju "diabelskie" mechanizmy. "Wyłącznik siły"
jest ukryty gdzieś w wysokiej wieży. Na jego drodze do celu musi
unikać wielu dziwnych robotów które strzegą wieży. Wszystko to brzmi
jak zwykła gra z rodzaju "skacz i biegnij". To czym różni się ta gra
od innych tego typu jest to, że spacerujesz wokół wieży, która obraca
się na ekranie, tak więc widoczne jest tylko 180°.

%prep
%setup -q
%patch0 -p1

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
