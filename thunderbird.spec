# TODO:
# - build with system mozldap
# - do something with *.rdf file, there is file conflict with other lang packages
#
# Conditional builds
%bcond_with	tests		# enable tests (whatever they check)
%bcond_without	gtk3		# GTK+ 3.x instead of 2.x
%bcond_without	ldap		# disable e-mail address lookups in LDAP directories
%bcond_without	lightning	# disable Sunbird/Lightning calendar
%bcond_without	official	# official Thunderbird branding
%bcond_with	crashreporter	# report crashes to crash-stats.mozilla.com
# - disabled shared_js - https://bugzilla.mozilla.org/show_bug.cgi?id=1039964
%bcond_with	shared_js	# shared libmozjs library [broken]
%bcond_with	system_icu	# build with system ICU (disabled due to crashes with system icu 58.2)
%bcond_without	clang		# build using Clang/LLVM

# UPDATING TRANSLATIONS:
%if 0
rm -vf *.xpi
./builder -g
V=31.4.0
U=http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

%if 0%{?_enable_debug_packages} != 1
%undefine	crashreporter
%endif

%define		nspr_ver	4.13.1
%define		nss_ver		3.28.6

# The actual sqlite version (see RHBZ#480989):
%define		sqlite_build_version %(pkg-config --silence-errors --modversion sqlite3 2>/dev/null || echo ERROR)

Summary:	Thunderbird - email client
Summary(pl.UTF-8):	Thunderbird - klient poczty
Name:		thunderbird
Version:	52.7.0
Release:	1
License:	MPL v2.0
Group:		X11/Applications/Mail
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/source/%{name}-%{version}.source.tar.xz
# Source0-md5:	9c44ccd16cfcca4691ab0ce8aebb4236
Source1:	%{name}.desktop
Source2:	%{name}.sh
Source100:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ar.xpi
# Source100-md5:	bc5bf8ca5ca96d53c6f483f00e0c5fd7
Source101:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ast.xpi
# Source101-md5:	f7c7b5eac40df7efc7d69ef397f30a26
Source102:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/be.xpi
# Source102-md5:	516cab5e1fec3ada1b7486750d69f33c
Source103:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bg.xpi
# Source103-md5:	b308be0641802a3d8b8941104ad813c0
Source104:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source104-md5:	769aad2893f699757de84382d5617dc7
Source105:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/br.xpi
# Source105-md5:	5ac4e263e3ee614f56cc9c6766ba4155
Source106:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ca.xpi
# Source106-md5:	3ec58b6c4f2a2e9e7b431137d8b0a8e6
Source107:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/cs.xpi
# Source107-md5:	791f30ec5147bf9f9928a8bfd2c151a0
Source108:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/da.xpi
# Source108-md5:	d1f27438b7c47b499b4b40efe2c1a79d
Source109:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/de.xpi
# Source109-md5:	b589be5e458eb124e47a2b1047a52593
Source110:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source110-md5:	fb36b1bc5c825bfc165c112af179d378
Source111:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/el.xpi
# Source111-md5:	864963b9b86e348f7e0ac28bc9ba62d3
Source112:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source112-md5:	f6139ef8c388b062380a8d4d0861f561
Source113:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source113-md5:	77c0ae4182a4bd08d23c87effeadafc1
Source114:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source114-md5:	a100e8a7541a4045a61429634eb5ef4f
Source115:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source115-md5:	803b36026cbf20c9a25466d8b3d5adf3
Source116:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/et.xpi
# Source116-md5:	1dccb2024036baad503b813857ccb62c
Source117:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/eu.xpi
# Source117-md5:	35f7c3f537b24da435530795763fa743
Source118:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fi.xpi
# Source118-md5:	6f7d522e592e8b5f99607e42500c4946
Source119:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fr.xpi
# Source119-md5:	3bf10e487c69b4f3ab764d6bb96c3a9c
Source120:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source120-md5:	ada225d2a52e5013dc514a5dc21aa25b
Source121:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source121-md5:	bc287703e3976cd36449b17389e23297
Source122:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gd.xpi
# Source122-md5:	464ec645ecc30e30009774b2d3ee4356
Source123:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gl.xpi
# Source123-md5:	1573e1fde02ac5248704f1332101c2e4
Source124:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/he.xpi
# Source124-md5:	c922c1f81bc6df2b3c1c84143ca14c7d
Source125:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hr.xpi
# Source125-md5:	7fbafdc559d7f57796fcf5faae4432d1
Source126:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source126-md5:	33cb571c32776701ff2f711a5bdca83d
Source127:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hu.xpi
# Source127-md5:	25c71013851eac0b524d9c57ec7e6e39
Source128:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source128-md5:	05aa902556dff9a9d985fc89db5e710d
Source129:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/id.xpi
# Source129-md5:	3e3cbfc09fd00defc233916d3410aa75
Source130:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/is.xpi
# Source130-md5:	b75df41c13fa291e6e049560e17f60a0
Source131:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/it.xpi
# Source131-md5:	3749eaa8a0bb48eca2da5cd6bc21b436
Source132:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ja.xpi
# Source132-md5:	365931e8cb36e0a39663f89b1d6df2da
Source133:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/kab.xpi
# Source133-md5:	35a1ff4f11e9df970f122fbd205c94ab
Source134:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ko.xpi
# Source134-md5:	06f55a131a5508a8dc4148e4825fd288
Source135:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/lt.xpi
# Source135-md5:	e32c35eafdce217fc33f73cab87cc805
Source136:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source136-md5:	81f5104e09b4b95ea2442448a33cf519
Source137:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nl.xpi
# Source137-md5:	e6c86bd68826b1bc23711c2754873502
Source138:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source138-md5:	d4f0102a7801eb3067ded4c8a47eed2e
Source139:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source139-md5:	982c7455134cfe8e1d8429bf7e8ec486
Source140:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source140-md5:	00efda408ecf7f011f9c0e55e5318ab6
Source141:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source141-md5:	738309a9f80d3134ae016c08faaf4a6c
Source142:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source142-md5:	0667d2d66c78dde7f44061c167554c9f
Source143:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/rm.xpi
# Source143-md5:	fe9e0203c31158ded5c7865ba8b52376
Source144:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ro.xpi
# Source144-md5:	5d5958043eb4331f6856ac2586820725
Source145:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ru.xpi
# Source145-md5:	dcb6cc11909cbcde49daf292973fdc1c
Source146:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/si.xpi
# Source146-md5:	9512694d78a4e01b40b0ab92af14b372
Source147:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sk.xpi
# Source147-md5:	90387224477355843866c1107b8f49c9
Source148:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sl.xpi
# Source148-md5:	c60d923681185bd4148cf8512502a126
Source149:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sq.xpi
# Source149-md5:	4057bb45b9b3051ad628779ec5a463e3
Source150:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sr.xpi
# Source150-md5:	e87b4aa01bca3cd3206c035a2e23d263
Source151:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source151-md5:	3dca966cd3ce95addf428ae082d6b12e
Source152:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ta-LK.xpi
# Source152-md5:	b6d52e9706f190105c02ffe6e2189f79
Source153:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/tr.xpi
# Source153-md5:	b7922e27bf46672e2cbc1dcc8075bf4f
Source154:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/uk.xpi
# Source154-md5:	56bc903cc698940776fa93103bdc9805
Source155:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/vi.xpi
# Source155-md5:	08727cb3108a2363455a2c2c9f023c44
Source156:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source156-md5:	70b082298a14e811d0739c8a82d56a75
Source157:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source157-md5:	ac2be57e51f02f2604fc979dbc839589
Patch0:		prefs.patch
Patch1:		no-subshell.patch
Patch2:		enable-addons.patch
URL:		http://www.mozilla.org/projects/thunderbird/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf2_13 >= 2.13
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.10
%{?with_clang:BuildRequires:	clang}
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	fontconfig-devel >= 2.7.0
BuildRequires:	freetype-devel >= 1:2.1.8
BuildRequires:	glib2-devel >= 1:2.22
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.18.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.4.0}
BuildRequires:	hunspell-devel
BuildRequires:	libatomic-devel
BuildRequires:	libevent-devel
BuildRequires:	libffi-devel > 3.0.9
%{?with_system_icu:BuildRequires:	libicu-devel >= 58.1}
BuildRequires:	libiw-devel
# requires libjpeg-turbo implementing at least libjpeg 6b API
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel >= 2:1.6.25
BuildRequires:	libstdc++-devel
BuildRequires:	libvpx-devel >= 1.5.0
BuildRequires:	mozldap-devel
BuildRequires:	nspr-devel >= 1:%{nspr_ver}
BuildRequires:	nss-devel >= 1:%{nss_ver}
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	pixman-devel >= 0.19.2
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7
BuildRequires:	python-virtualenv
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.17.0
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	virtualenv
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXt-devel
%ifarch %{ix86} %{x8664}
BuildRequires:	yasm >= 1.0.1
%endif
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.3
Requires(post):	mktemp >= 1.5-18
Requires:	dbus-glib >= 0.60
Requires:	glib2 >= 1:2.22
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.18.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.4.0}
Requires:	libpng >= 2:1.6.25
Requires:	libvpx >= 1.5.0
Requires:	myspell-common
Requires:	nspr >= 1:%{nspr_ver}
Requires:	nss >= 1:%{nss_ver}
Requires:	pango >= 1:1.22.0
Requires:	sqlite3 >= %{sqlite_build_version}
Requires:	startup-notification >= 0.8
Requires:	libjpeg-turbo
Obsoletes:	icedove
Obsoletes:	mozilla-thunderbird
Obsoletes:	mozilla-thunderbird-dictionary-en-US
Conflicts:	thunderbird-lang-resources < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_cpp		-D_FORTIFY_SOURCE=[0-9]+

%if %{with clang}
%define		filterout		-fvar-tracking-assignments
%endif

# firefox/thunderbird/seamonkey provide their own versions
%define		_noautoprovfiles	%{_libdir}/%{name}/components

# we don't want these to satisfy packages depending on xulrunner
%define		_noautoprov		libmozalloc.so libmozjs.so libxul.so
# and as we don't provide them, don't require either
%define		_noautoreq		libmozalloc.so libmozjs.so libxul.so

%define		topdir		%{_builddir}/thunderbird-%{version}
%define		objdir		%{topdir}/obj-%{_target_cpu}

%description
Thunderbird is an open-source, fast and portable email client.

%description -l pl.UTF-8
Thunderbird jest mającym otwarte źródła, szybkim i przenośnym klientem
poczty.

%package addon-lightning
Summary:	An integrated calendar for Thunderbird
Summary(pl.UTF-8):	Zintegrowany kalendarz dla Thunderbird
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}
Obsoletes:	icedove-addon-lightning

%description addon-lightning
Lightning is an calendar extension to Thunderbird email client.

%description addon-lightning -l pl.UTF-8
Lightning to rozszerzenie do klienta poczty Thunderbird dodające
funkcjonalność kalendarza.

%package lang-ar
Summary:	Arabic resources for Thunderbird
Summary(pl.UTF-8):	Arabskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ar
Obsoletes:	mozilla-thunderbird-lang-ar
BuildArch:	noarch

%description lang-ar
Arabic resources for Thunderbird.

%description lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Thunderbirda.

%package lang-ast
Summary:	Asturian resources for Thunderbird
Summary(pl.UTF-8):	Asturskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ast
Obsoletes:	mozilla-thunderbird-lang-ast
BuildArch:	noarch

%description lang-ast
Asturian resources for Thunderbird.

%description lang-ast -l pl.UTF-8
Asturskie pliki językowe dla Thunderbirda.

%package lang-be
Summary:	Belarusian resources for Thunderbird
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-be
Obsoletes:	mozilla-thunderbird-lang-be
BuildArch:	noarch

%description lang-be
Belarusian resources for Thunderbird.

%description lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Thunderbirda.

%package lang-bg
Summary:	Bulgarian resources for Thunderbird
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-bg
Obsoletes:	mozilla-thunderbird-lang-bg
BuildArch:	noarch

%description lang-bg
Bulgarian resources for Thunderbird.

%description lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Thunderbirda.

%package lang-bn
Summary:	Bengali (Bangladesh) resources for Thunderbird
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Thunderbirda (wersja dla Bangladeszu)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-bn
Obsoletes:	mozilla-thunderbird-lang-bn
BuildArch:	noarch

%description lang-bn
Bengali (Bangladesh) resources for Thunderbird.

%description lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Thunderbirda (wersja dla Bangladeszu).

%package lang-br
Summary:	Breton resources for Thunderbird
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-br
Obsoletes:	mozilla-thunderbird-lang-br
BuildArch:	noarch

%description lang-br
Breton resources for Thunderbird.

%description lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Thunderbirda.

%package lang-ca
Summary:	Catalan resources for Thunderbird
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ca
Obsoletes:	mozilla-thunderbird-lang-ca
BuildArch:	noarch

%description lang-ca
Catalan resources for Thunderbird.

%description lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Thunderbirda.

%package lang-cs
Summary:	Czech resources for Thunderbird
Summary(pl.UTF-8):	Czeskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-cs
Obsoletes:	mozilla-thunderbird-lang-cs
BuildArch:	noarch

%description lang-cs
Czech resources for Thunderbird.

%description lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Thunderbirda.

%package lang-da
Summary:	Danish resources for Thunderbird
Summary(pl.UTF-8):	Duńskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-da
Obsoletes:	mozilla-thunderbird-lang-da
BuildArch:	noarch

%description lang-da
Danish resources for Thunderbird.

%description lang-da -l pl.UTF-8
Duńskie pliki językowe dla Thunderbirda.

%package lang-de
Summary:	German resources for Thunderbird
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-de
Obsoletes:	mozilla-thunderbird-lang-de
BuildArch:	noarch

%description lang-de
German resources for Thunderbird.

%description lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Thunderbirda.

%package lang-dsb
Summary:	Lower Sorbian resources for Thunderbird
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-dsb
Lower Sorbian resources for Thunderbird.

%description lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Thunderbirda.

%package lang-el
Summary:	Greek resources for Thunderbird
Summary(pl.UTF-8):	Greckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-el
Obsoletes:	mozilla-thunderbird-lang-el
BuildArch:	noarch

%description lang-el
Greek resources for Thunderbird.

%description lang-el -l pl.UTF-8
Greckie pliki językowe dla Thunderbirda.

%package lang-en_GB
Summary:	English (British) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-en_GB
Obsoletes:	mozilla-thunderbird-lang-en_GB
BuildArch:	noarch

%description lang-en_GB
English (British) resources for Thunderbird.

%description lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Thunderbirda.

%package lang-en_US
Summary:	English (American) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-en_US
Obsoletes:	mozilla-thunderbird-lang-en_US
BuildArch:	noarch

%description lang-en_US
English (American) resources for Thunderbird.

%description lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Thunderbirda.

%package lang-es_AR
Summary:	Spanish (Andorra) resources for Thunderbird
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Andory)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-es_AR
Obsoletes:	mozilla-thunderbird-lang-es_AR
BuildArch:	noarch

%description lang-es_AR
Spanish (Andorra) resources for Thunderbird.

%description lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Andory).

%package lang-es
Summary:	Spanish (Spain) resources for Thunderbird
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Hiszpanii)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-es
Obsoletes:	mozilla-thunderbird-lang-es
BuildArch:	noarch

%description lang-es
Spanish (Spain) resources for Thunderbird.

%description lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Hiszpanii).

%package lang-et
Summary:	Estonian resources for Thunderbird
Summary(pl.UTF-8):	Estońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-et
Obsoletes:	mozilla-thunderbird-lang-et
BuildArch:	noarch

%description lang-et
Estonian resources for Thunderbird.

%description lang-et -l pl.UTF-8
Estońskie pliki językowe dla Thunderbirda.

%package lang-eu
Summary:	Basque resources for Thunderbird
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-eu
Obsoletes:	mozilla-thunderbird-lang-eu
BuildArch:	noarch

%description lang-eu
Basque resources for Thunderbird.

%description lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Thunderbirda.

%package lang-fi
Summary:	Finnish resources for Thunderbird
Summary(pl.UTF-8):	Fińskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-fi
Obsoletes:	mozilla-thunderbird-lang-fi
BuildArch:	noarch

%description lang-fi
Finnish resources for Thunderbird.

%description lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Thunderbirda.

%package lang-fr
Summary:	French resources for Thunderbird
Summary(pl.UTF-8):	Francuskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-fr
Obsoletes:	mozilla-thunderbird-lang-fr
BuildArch:	noarch

%description lang-fr
French resources for Thunderbird.

%description lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Thunderbirda.

%package lang-fy
Summary:	Frisian resources for Thunderbird
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-fy
Obsoletes:	mozilla-thunderbird-lang-fy
BuildArch:	noarch

%description lang-fy
Frisian resources for Thunderbird.

%description lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Thunderbirda.

%package lang-ga
Summary:	Irish resources for Thunderbird
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ga
Obsoletes:	mozilla-thunderbird-lang-ga
BuildArch:	noarch

%description lang-ga
Irish resources for Thunderbird.

%description lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Thunderbirda.

%package lang-gd
Summary:	Gaelic resources for Thunderbird
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-gd
Obsoletes:	mozilla-thunderbird-lang-gd
BuildArch:	noarch

%description lang-gd
Gaelic resources for Thunderbird.

%description lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Thunderbirda.

%package lang-gl
Summary:	Galician resources for Thunderbird
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-gl
Obsoletes:	mozilla-thunderbird-lang-gl
BuildArch:	noarch

%description lang-gl
Galician resources for Thunderbird.

%description lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Thunderbirda.

%package lang-he
Summary:	Hebrew resources for Thunderbird
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-he
Obsoletes:	mozilla-thunderbird-lang-he
BuildArch:	noarch

%description lang-he
Hebrew resources for Thunderbird.

%description lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Thunderbirda.

%package lang-hr
Summary:	Croatian resources for Thunderbird
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-hr
Obsoletes:	mozilla-thunderbird-lang-hr
BuildArch:	noarch

%description lang-hr
Croatian resources for Thunderbird.

%description lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Thunderbirda.

%package lang-hsb
Summary:	Upper Sorbian resources for Thunderbird
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-hsb
Upper Sorbian resources for Thunderbird.

%description lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Thunderbirda.

%package lang-hu
Summary:	Hungarian resources for Thunderbird
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-hu
Obsoletes:	mozilla-thunderbird-lang-hu
BuildArch:	noarch

%description lang-hu
Hungarian resources for Thunderbird.

%description lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Thunderbirda.

%package lang-hy
Summary:	Armenian resources for Thunderbird
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-hy
Obsoletes:	mozilla-thunderbird-lang-hy
BuildArch:	noarch

%description lang-hy
Armenian resources for Thunderbird.

%description lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Thunderbirda.

%package lang-id
Summary:	Indonesian resources for Thunderbird
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-id
Obsoletes:	mozilla-thunderbird-lang-id
BuildArch:	noarch

%description lang-id
Indonesian resources for Thunderbird.

%description lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Thunderbirda.

%package lang-is
Summary:	Icelandic resources for Thunderbird
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-is
Obsoletes:	mozilla-thunderbird-lang-is
BuildArch:	noarch

%description lang-is
Icelandic resources for Thunderbird.

%description lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Thunderbirda.

%package lang-it
Summary:	Italian resources for Thunderbird
Summary(pl.UTF-8):	Włoskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-it
Obsoletes:	mozilla-thunderbird-lang-it
BuildArch:	noarch

%description lang-it
Italian resources for Thunderbird.

%description lang-it -l pl.UTF-8
Włoskie pliki językowe dla Thunderbirda.

%package lang-ja
Summary:	Japanese resources for Thunderbird
Summary(pl.UTF-8):	Japońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ja
Obsoletes:	mozilla-thunderbird-lang-ja
BuildArch:	noarch

%description lang-ja
Japanese resources for Thunderbird.

%description lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Thunderbirda.

%package lang-kab
Summary:	Kabyle resources for Thunderbird
Summary(pl.UTF-8):	Kabylskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-kab
Kabyle resources for Thunderbird.

%description lang-kab -l pl.UTF-8
Kabylskie pliki językowe dla Thunderbirda.

%package lang-ko
Summary:	Korean resources for Thunderbird
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ko
Obsoletes:	mozilla-thunderbird-lang-ko
BuildArch:	noarch

%description lang-ko
Korean resources for Thunderbird.

%description lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Thunderbirda.

%package lang-lt
Summary:	Lithuanian resources for Thunderbird
Summary(pl.UTF-8):	Litewskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-lt
Obsoletes:	mozilla-thunderbird-lang-lt
BuildArch:	noarch

%description lang-lt
Lithuanian resources for Thunderbird.

%description lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Thunderbirda.

%package lang-nb
Summary:	Norwegian Bokmaal resources for Thunderbird
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-nb
Obsoletes:	mozilla-thunderbird-lang-nb
BuildArch:	noarch

%description lang-nb
Norwegian Bokmaal resources for Thunderbird.

%description lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Thunderbirda.

%package lang-nl
Summary:	Dutch resources for Thunderbird
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-nl
Obsoletes:	mozilla-thunderbird-lang-nl
BuildArch:	noarch

%description lang-nl
Dutch resources for Thunderbird.

%description lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Thunderbirda.

%package lang-nn
Summary:	Norwegian Nynorsk resources for Thunderbird
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-nn
Obsoletes:	mozilla-thunderbird-lang-nn
BuildArch:	noarch

%description lang-nn
Norwegian Nynorsk resources for Thunderbird.

%description lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Thunderbirda.

%package lang-pa
Summary:	Panjabi resources for Thunderbird
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-pa
Obsoletes:	mozilla-thunderbird-lang-pa
BuildArch:	noarch

%description lang-pa
Panjabi resources for Thunderbird.

%description lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Thunderbirda.

%package lang-pl
Summary:	Polish resources for Thunderbird
Summary(pl.UTF-8):	Polskie pliki językowe dla Thunderbirda
Group:		I18n
URL:		http://www.thunderbird.pl/
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-pl
Obsoletes:	mozilla-thunderbird-lang-pl
BuildArch:	noarch

%description lang-pl
Polish resources for Thunderbird.

%description lang-pl -l pl.UTF-8
Polskie pliki językowe dla Thunderbirda.

%package lang-pt_BR
Summary:	Portuguese (Brazil) resources for Thunderbird
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-pt_BR
Obsoletes:	mozilla-thunderbird-lang-pt_BR
BuildArch:	noarch

%description lang-pt_BR
Portuguese (Brazil) resources for Thunderbird.

%description lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Thunderbirda.

%package lang-pt
Summary:	Portuguese (Portugal) resources for Thunderbird
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Thunderbirda (wersja dla Portugalii)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-pt
Obsoletes:	mozilla-thunderbird-lang-pt
BuildArch:	noarch

%description lang-pt
Portuguese (Portugal) resources for Thunderbird.

%description lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Thunderbirda (wersja dla Portugalii).

%package lang-rm
Summary:	Romansh resources for Thunderbird
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-rm
Obsoletes:	mozilla-thunderbird-lang-rm
BuildArch:	noarch

%description lang-rm
Romansh resources for Thunderbird.

%description lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Thunderbirda.

%package lang-ro
Summary:	Romanian resources for Thunderbird
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ro
Obsoletes:	mozilla-thunderbird-lang-ro
BuildArch:	noarch

%description lang-ro
Romanian resources for Thunderbird.

%description lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Thunderbirda.

%package lang-ru
Summary:	Russian resources for Thunderbird
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ru
Obsoletes:	mozilla-thunderbird-lang-ru
BuildArch:	noarch

%description lang-ru
Russian resources for Thunderbird.

%description lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Thunderbirda.

%package lang-si
Summary:	Sinhala resources for Thunderbird
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-si
Obsoletes:	mozilla-thunderbird-lang-si
BuildArch:	noarch

%description lang-si
Sinhala resources for Thunderbird.

%description lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Thunderbirda.

%package lang-sk
Summary:	Slovak resources for Thunderbird
Summary(pl.UTF-8):	Słowackie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sk
Obsoletes:	mozilla-thunderbird-lang-sk
BuildArch:	noarch

%description lang-sk
Slovak resources for Thunderbird.

%description lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Thunderbirda.

%package lang-sl
Summary:	Slovene resources for Thunderbird
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sl
Obsoletes:	mozilla-thunderbird-lang-sl
BuildArch:	noarch

%description lang-sl
Slovene resources for Thunderbird.

%description lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Thunderbirda.

%package lang-sq
Summary:	Albanian resources for Thunderbird
Summary(pl.UTF-8):	Albańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sq
Obsoletes:	mozilla-thunderbird-lang-sq
BuildArch:	noarch

%description lang-sq
Albanian resources for Thunderbird.

%description lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Thunderbirda.

%package lang-sr
Summary:	Serbian resources for Thunderbird
Summary(pl.UTF-8):	Serbskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sr
Obsoletes:	mozilla-thunderbird-lang-sr
BuildArch:	noarch

%description lang-sr
Serbian resources for Thunderbird.

%description lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Thunderbirda.

%package lang-sv
Summary:	Swedish resources for Thunderbird
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sv
Obsoletes:	mozilla-thunderbird-lang-sv
BuildArch:	noarch

%description lang-sv
Swedish resources for Thunderbird.

%description lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Thunderbirda.

%package lang-ta_LK
Summary:	Tamil (Sri Lanka) resources for Thunderbird
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Thunderbirda (wersja dla Sri Lanki)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ta_LK
Obsoletes:	mozilla-thunderbird-lang-ta_LK
BuildArch:	noarch

%description lang-ta_LK
Tamil (Sri Lanka) resources for Thunderbird.

%description lang-ta_LK -l pl.UTF-8
Tamilskie pliki językowe dla Thunderbirda (wersja dla Sri Lanki).

%package lang-tr
Summary:	Turkish resources for Thunderbird
Summary(pl.UTF-8):	Tureckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-tr
Obsoletes:	mozilla-thunderbird-lang-tr
BuildArch:	noarch

%description lang-tr
Turkish resources for Thunderbird.

%description lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Thunderbirda.

%package lang-uk
Summary:	Ukrainian resources for Thunderbird
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-uk
Obsoletes:	mozilla-thunderbird-lang-uk
BuildArch:	noarch

%description lang-uk
Ukrainian resources for Thunderbird.

%description lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Thunderbirda.

%package lang-vi
Summary:	Vietnamese resources for Thunderbird
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-vi
Obsoletes:	mozilla-thunderbird-lang-vi
BuildArch:	noarch

%description lang-vi
Vietnamese resources for Thunderbird.

%description lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Thunderbirda.

%package lang-zh_CN
Summary:	Simplified Chinese resources for Thunderbird
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-zh_CN
Obsoletes:	mozilla-thunderbird-lang-zh_CN
BuildArch:	noarch

%description lang-zh_CN
Simplified Chinese resources for Thunderbird.

%description lang-zh_CN -l pl.UTF-8
Chińskie (uproszczone) pliki językowe dla Thunderbirda.

%package lang-zh_TW
Summary:	Traditional Chinese resources for Thunderbird
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-zh_TW
Obsoletes:	mozilla-thunderbird-lang-zh_TW
BuildArch:	noarch

%description lang-zh_TW
Traditional Chinese resources for Thunderbird.

%description lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Thunderbirda.

%prep
unpack() {
	local args="$1" file="$2"
	cp -p $file .
}
%define __unzip unpack
%setup -q %(seq -f '-a %g' 100 157 | xargs)
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cat << EOF > .mozconfig
mk_add_options MOZ_OBJDIR=%{objdir}

%if %{with clang}
export CC="clang"
export CXX="clang++"
%else
export CC="%{__cc}"
export CXX="%{__cxx}"
%endif
export CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="%{rpmcxxflags} -D_FILE_OFFSET_BITS=64"

%if %{with crashreporter}
export MOZ_DEBUG_SYMBOLS=1
%endif

# Options for 'configure' (same as command-line options).
ac_add_options --prefix=%{_prefix}
%if %{?debug:1}0
ac_add_options --disable-optimize
ac_add_options --enable-debug
ac_add_options --enable-debug-modules
ac_add_options --enable-debugger-info-modules
ac_add_options --enable-crash-on-assert
%else
ac_add_options --disable-debug
ac_add_options --enable-optimize="%{rpmcflags}"
%endif
ac_add_options --disable-strip
ac_add_options --disable-install-strip
%if %{with tests}
ac_add_options --enable-tests
ac_add_options --enable-mochitest
%else
ac_add_options --disable-tests
%endif
%if %{with lightning}
ac_add_options --enable-calendar
%else
ac_add_options --disable-calendar
%endif
%if %{with crashreporter}
ac_add_options --enable-crashreporter
%else
ac_add_options --disable-crashreporter
%endif
#ac_add_options --disable-elf-hack
ac_add_options --disable-gconf
ac_add_options --disable-gnomeui
ac_add_options --disable-necko-wifi
ac_add_options --disable-updater
ac_add_options --enable-alsa
ac_add_options --enable-application=mail
ac_add_options --enable-chrome-format=omni
ac_add_options --enable-default-toolkit=%{?with_gtk3:cairo-gtk3}%{!?with_gtk3:cairo-gtk2}
ac_add_options --enable-gio
%if %{with ldap}
ac_add_options --enable-ldap
%else
ac_add_options --disable-ldap
%endif
%{?with_official:ac_add_options --enable-official-branding}
ac_add_options --enable-readline
%{?with_shared_js:ac_add_options --enable-shared-js}
ac_add_options --enable-startup-notification
ac_add_options --enable-system-cairo
ac_add_options --enable-system-ffi
ac_add_options --enable-system-hunspell
ac_add_options --enable-system-sqlite
ac_add_options --enable-url-classifier
ac_add_options --with-default-mozilla-five-home=%{_libdir}/%{name}
ac_add_options --with-distribution-id=org.pld-linux
ac_add_options --with-pthreads
ac_add_options --with-system-bz2
ac_add_options --with%{!?with_system_icu:out}-system-icu
ac_add_options --with-system-jpeg
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-zlib
ac_add_options --with-x
EOF

mkdir -p %{objdir}/config
ln -sf %{topdir}/mozilla/config/*.mk %{objdir}/config

%{__make} -j1 -f client.mk build \
	AUTOCONF=/usr/bin/autoconf2_13 \
	MOZ_MAKE_FLAGS="%{_smp_mflags}"

%if %{with crashreporter}
# create debuginfo for crash-stats.mozilla.com
%{__make} -j1 -C obj-%{_target_cpu} buildsymbols
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/plugins,%{_datadir}/%{name},%{_pixmapsdir},%{_desktopdir}}

cd %{objdir}
%{__make} -C mail/installer stage-package \
	DESTDIR=$RPM_BUILD_ROOT \
	installdir=%{_libdir}/%{name} \
	PKG_SKIP_STRIP=1

cp -a dist/thunderbird/* $RPM_BUILD_ROOT%{_libdir}/%{name}/

# Enable crash reporter for Thunderbird application
%if %{with crashreporter}
%{__sed} -i -e 's/\[Crash Reporter\]/[Crash Reporter]\nEnabled=1/' $RPM_BUILD_ROOT%{_libdir}/%{name}/application.ini

# Add debuginfo for crash-stats.mozilla.com
install -d $RPM_BUILD_ROOT%{_exec_prefix}/lib/debug%{_libdir}/%{name}
cp -a dist/%{name}-%{version}.en-US.linux-*.crashreporter-symbols.zip $RPM_BUILD_ROOT%{_prefix}/lib/debug%{_libdir}/%{name}
%endif

%{__sed} -e 's,@LIBDIR@,%{_libdir},' %{SOURCE2} > $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p dist/thunderbird/chrome/icons/default/default48.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

# use system dict
%{__rm} -rv $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/hyphenation

# move arch independant ones to datadir
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome $RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults $RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/isp $RPM_BUILD_ROOT%{_datadir}/%{name}/isp
ln -s ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/%{name}/extensions $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions
ln -s ../../share/%{name}/isp $RPM_BUILD_ROOT%{_libdir}/%{name}/isp

# mozldap
%{__sed} -i '/lib\(ldap\|ldif\|prldap\)60.so/d' $RPM_BUILD_ROOT%{_libdir}/%{name}/dependentlibs.list
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/lib{ldap,ldif,prldap}60.so

# remove unecessary stuff
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/removed-files

cd ..
for a in *.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions/langpack-$basename@thunderbird.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans
if [ -d %{_libdir}/%{name}/extensions ] && [ ! -L %{_libdir}/%{name}/extensions ]; then
	install -d %{_datadir}/%{name}
	if [ -e %{_datadir}/%{name}/extensions ]; then
		mv %{_datadir}/%{name}/extensions{,.rpmsave}
	fi
	mv -v %{_libdir}/%{name}/extensions %{_datadir}/%{name}/extensions
fi
if [ -d %{_libdir}/%{name}/dictionaries ] && [ ! -L %{_libdir}/%{name}/dictionaries ]; then
	mv -v %{_libdir}/%{name}/dictionaries{,.rpmsave}
fi
for d in chrome defaults icons isp modules res; do
	if [ -d %{_libdir}/%{name}/$d ] && [ ! -L %{_libdir}/%{name}/$d ]; then
		install -d %{_datadir}/%{name}
		mv %{_libdir}/%{name}/$d %{_datadir}/%{name}/$d
	fi
done
exit 0

%post
%update_desktop_database_post
# make temporary HOME, as it attempts to touch files in $HOME/.mozilla
# dangerous if you run this with sudo with keep_env += HOME
# also TMPDIR could be pointing to sudo user's homedir so we reset that too.
export HOME=$(mktemp -d)
unset TMPDIR TMP || :
umask 022
%{_libdir}/%{name}/thunderbird -register
rm -rf $HOME

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins

%if %{with gtk3}
%dir %{_libdir}/%{name}/gtk2
%attr(755,root,root) %{_libdir}/%{name}/gtk2/libmozgtk.so
%attr(755,root,root) %{_libdir}/%{name}/libmozgtk.so
%endif
%attr(755,root,root) %{_libdir}/%{name}/liblgpllibs.so
%{?with_shared_js:%attr(755,root,root) %{_libdir}/%{name}/libmozjs.so}
%attr(755,root,root) %{_libdir}/%{name}/libmozsandbox.so
%attr(755,root,root) %{_libdir}/%{name}/libxul.so
%attr(755,root,root) %{_libdir}/%{name}/*.sh
%attr(755,root,root) %{_libdir}/%{name}/*-bin
%attr(755,root,root) %{_libdir}/%{name}/plugin-container
%attr(755,root,root) %{_libdir}/%{name}/thunderbird

%{_libdir}/%{name}/application.ini
%{_libdir}/%{name}/blocklist.xml
%{_libdir}/%{name}/dependentlibs.list
%{_libdir}/%{name}/omni.ja
%{_libdir}/%{name}/platform.ini
%{!?with_system_icu:%{_libdir}/%{name}/icudt58l.dat}

%dir %{_libdir}/%{name}/fonts
%{_libdir}/%{name}/fonts/EmojiOneMozilla.ttf

%if %{with crashreporter}
%attr(755,root,root) %{_libdir}/%{name}/crashreporter
%{_libdir}/%{name}/crashreporter.ini
%{_libdir}/%{name}/Throbber-small.gif
%endif

%dir %{_libdir}/%{name}/distribution
%dir %{_libdir}/%{name}/distribution/extensions

# symlinks
%{_libdir}/%{name}/chrome
%{_libdir}/%{name}/defaults
%{_libdir}/%{name}/dictionaries
%{_libdir}/%{name}/extensions
%{_libdir}/%{name}/hyphenation
%{_libdir}/%{name}/isp

%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/chrome
%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/isp

%dir %{_datadir}/%{name}/extensions
%{_datadir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}.xpi

%if %{with lightning}
%files addon-lightning
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/app.ini
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/chrome.jar
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/chrome.manifest
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/defaults
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/install.rdf
%dir %{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/components
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/components/*.js
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/components/*manifest
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/components/*.xpt
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/modules
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/calendar-js
%dir %{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/timezones
%{_libdir}/%{name}/distribution/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}/timezones/zones.json
%endif

%files lang-ar
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ar@thunderbird.mozilla.org.xpi

%files lang-ast
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ast@thunderbird.mozilla.org.xpi

%files lang-be
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-be@thunderbird.mozilla.org.xpi

%files lang-bg
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-bg@thunderbird.mozilla.org.xpi

%files lang-bn
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-bn-BD@thunderbird.mozilla.org.xpi

%files lang-br
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-br@thunderbird.mozilla.org.xpi

%files lang-ca
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ca@thunderbird.mozilla.org.xpi

%files lang-cs
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-cs@thunderbird.mozilla.org.xpi

%files lang-da
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-da@thunderbird.mozilla.org.xpi

%files lang-de
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-de@thunderbird.mozilla.org.xpi

%files lang-dsb
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-dsb@thunderbird.mozilla.org.xpi

%files lang-el
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-el@thunderbird.mozilla.org.xpi

%files lang-en_GB
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-en-GB@thunderbird.mozilla.org.xpi

%files lang-en_US
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-en-US@thunderbird.mozilla.org.xpi

%files lang-es_AR
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-es-AR@thunderbird.mozilla.org.xpi

%files lang-es
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-es-ES@thunderbird.mozilla.org.xpi

%files lang-et
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-et@thunderbird.mozilla.org.xpi

%files lang-eu
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-eu@thunderbird.mozilla.org.xpi

%files lang-fi
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-fi@thunderbird.mozilla.org.xpi

%files lang-fr
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-fr@thunderbird.mozilla.org.xpi

%files lang-fy
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-fy-NL@thunderbird.mozilla.org.xpi

%files lang-ga
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ga-IE@thunderbird.mozilla.org.xpi

%files lang-gd
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-gd@thunderbird.mozilla.org.xpi

%files lang-gl
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-gl@thunderbird.mozilla.org.xpi

%files lang-he
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-he@thunderbird.mozilla.org.xpi

%files lang-hr
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-hr@thunderbird.mozilla.org.xpi

%files lang-hsb
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-hsb@thunderbird.mozilla.org.xpi

%files lang-hu
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-hu@thunderbird.mozilla.org.xpi

%files lang-hy
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-hy-AM@thunderbird.mozilla.org.xpi

%files lang-id
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-id@thunderbird.mozilla.org.xpi

%files lang-is
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-is@thunderbird.mozilla.org.xpi

%files lang-it
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-it@thunderbird.mozilla.org.xpi

%files lang-ja
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ja@thunderbird.mozilla.org.xpi

%files lang-kab
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-kab@thunderbird.mozilla.org.xpi

%files lang-ko
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ko@thunderbird.mozilla.org.xpi

%files lang-lt
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-lt@thunderbird.mozilla.org.xpi

%files lang-nb
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-nb-NO@thunderbird.mozilla.org.xpi

%files lang-nl
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-nl@thunderbird.mozilla.org.xpi

%files lang-nn
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-nn-NO@thunderbird.mozilla.org.xpi

%files lang-pa
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-pa-IN@thunderbird.mozilla.org.xpi

%files lang-pl
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-pl@thunderbird.mozilla.org.xpi

%files lang-pt_BR
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-pt-BR@thunderbird.mozilla.org.xpi

%files lang-pt
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-pt-PT@thunderbird.mozilla.org.xpi

%files lang-rm
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-rm@thunderbird.mozilla.org.xpi

%files lang-ro
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ro@thunderbird.mozilla.org.xpi

%files lang-ru
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ru@thunderbird.mozilla.org.xpi

%files lang-si
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-si@thunderbird.mozilla.org.xpi

%files lang-sk
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-sk@thunderbird.mozilla.org.xpi

%files lang-sl
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-sl@thunderbird.mozilla.org.xpi

%files lang-sq
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-sq@thunderbird.mozilla.org.xpi

%files lang-sr
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-sr@thunderbird.mozilla.org.xpi

%files lang-sv
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-sv-SE@thunderbird.mozilla.org.xpi

%files lang-ta_LK
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ta-LK@thunderbird.mozilla.org.xpi

%files lang-tr
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-tr@thunderbird.mozilla.org.xpi

%files lang-uk
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-uk@thunderbird.mozilla.org.xpi

%files lang-vi
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-vi@thunderbird.mozilla.org.xpi

%files lang-zh_CN
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-zh-CN@thunderbird.mozilla.org.xpi

%files lang-zh_TW
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-zh-TW@thunderbird.mozilla.org.xpi
