# TODO:
# - build with system mozldap
# - do something with *.rdf file, there is file conflict with other lang packages
#
# Conditional builds
%bcond_with	tests		# enable tests (whatever they check)
%bcond_without	official	# official Thunderbird branding
%bcond_with	crashreporter	# report crashes to crash-stats.mozilla.com
%bcond_with	gold		# use gold instead of default linker
# - disabled shared_js - https://bugzilla.mozilla.org/show_bug.cgi?id=1039964
%bcond_with	shared_js	# shared libmozjs library [broken]
%bcond_without	system_icu	# build without system ICU
%bcond_with	system_cairo	# build with system cairo (not supported in 60.0)
%bcond_without	system_libvpx	# build with system libvpx
%bcond_without	clang		# build using Clang/LLVM
%bcond_with	lowmem		# lower memory requirements
%bcond_with	lowmem2		# even lower memory requirements at cost of build time

# UPDATING TRANSLATIONS:
%if 0
rm -vf *.xpi
./builder -g
V=31.4.0
U=https://releases.mozilla.org/pub/thunderbird/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

%define		_enable_debug_packages	0

%if 0%{?_enable_debug_packages} != 1
%undefine	crashreporter
%endif

%ifarch %{ix86} %{arm} aarch64
%define		with_lowmem	1
%endif

%define		nspr_ver	4.32
%define		nss_ver		3.101

Summary:	Thunderbird - email client
Summary(pl.UTF-8):	Thunderbird - klient poczty
Name:		thunderbird
Version:	128.2.1
Release:	1
License:	MPL v2.0
Group:		X11/Applications/Mail
Source0:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/source/%{name}-%{version}esr.source.tar.xz
# Source0-md5:	e2036ef2a7089a1dbcbe716db4987d8b
Source1:	%{name}.desktop
Source2:	%{name}.sh
Source100:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/af.xpi
# Source100-md5:	72b0c191c011aa6e3009f45b4e891eb9
Source101:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ar.xpi
# Source101-md5:	47385615426a94630e460d32a8f2056f
Source102:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ast.xpi
# Source102-md5:	33d32731e90c771d8eae28c1938ace7c
Source103:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/be.xpi
# Source103-md5:	e91c412c7405abd6bff31d26f181eb64
Source104:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/bg.xpi
# Source104-md5:	209477974075bc31669cd5579d307d3d
Source105:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/br.xpi
# Source105-md5:	0b4e8703e485516bff6abcfab1bb242c
Source106:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ca.xpi
# Source106-md5:	d58ac1550b1031bce39982d06bfc3990
Source107:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/cak.xpi
# Source107-md5:	d06098049b5f21cfec1c2940f8a28e9c
Source108:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/cs.xpi
# Source108-md5:	c311d21db7f30ac09023421d86e8b1f1
Source109:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/cy.xpi
# Source109-md5:	80a194c4452931596150f97f44a03547
Source110:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/da.xpi
# Source110-md5:	d258de7a92a887e7c305cb14d36e844a
Source111:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/de.xpi
# Source111-md5:	9470ac2922deb6874249588492574804
Source112:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/dsb.xpi
# Source112-md5:	10bf51599bd5b383ef48bf2c813a4170
Source113:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/el.xpi
# Source113-md5:	f6f08ef799942420705e3284208e7b61
Source114:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/en-CA.xpi
# Source114-md5:	ad4499e581cbba09269e29d4d78d740e
Source115:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/en-GB.xpi
# Source115-md5:	ddfe2e1ae0cc2903ee209c86e8e60ee6
Source116:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/en-US.xpi
# Source116-md5:	209a6da4adf310fc1741b34d3e0074bd
Source117:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/es-AR.xpi
# Source117-md5:	e25d111408de18c29ff317bc107e8e24
Source118:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/es-ES.xpi
# Source118-md5:	4995042485f3bd169ed4a090c41c9d26
Source119:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/es-MX.xpi
# Source119-md5:	2b319170f9eb18b3631ed3f02a425e1f
Source120:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/et.xpi
# Source120-md5:	9b055e13a207cdca29192c6b4f3b71de
Source121:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/eu.xpi
# Source121-md5:	9bfa1aebdab349a942204c8dd83435cf
Source122:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/fi.xpi
# Source122-md5:	a50bbed4207ebba9e36f7d98b1f032ef
Source123:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/fr.xpi
# Source123-md5:	862cd4e9fa07b397684081392f994e02
Source124:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/fy-NL.xpi
# Source124-md5:	a11fc5d4912a858cb95732b0ae49f62c
Source125:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ga-IE.xpi
# Source125-md5:	43698d9c3ea1b4ab502578185ad33333
Source126:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/gd.xpi
# Source126-md5:	9d401cc495050a03034b6ee270d52d5a
Source127:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/gl.xpi
# Source127-md5:	476129ebafc76eeee7ec324205953d9f
Source128:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/he.xpi
# Source128-md5:	64b6387921c5f32a148631bf160d984b
Source129:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/hr.xpi
# Source129-md5:	d548983445df16bbd00a31840f3b14dc
Source130:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/hsb.xpi
# Source130-md5:	a1da65f4a7663b74e072c77a1f15b97a
Source131:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/hu.xpi
# Source131-md5:	adbb7410b9a8953519c6bd0189eacec6
Source132:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/hy-AM.xpi
# Source132-md5:	1adbad835690e5bd21362d2deae45e2e
Source133:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/id.xpi
# Source133-md5:	ae1a3a6b2541db22b9fa5c4aee86ac00
Source134:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/is.xpi
# Source134-md5:	87adb0979c936422dbe93e84ffac39ff
Source135:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/it.xpi
# Source135-md5:	5b6ff7fba13842dc43593061c545c798
Source136:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ja.xpi
# Source136-md5:	405b2ffa6f8e8ca16d92f7506932b61f
Source137:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ka.xpi
# Source137-md5:	77181591033396f976dd446f16d26d8b
Source138:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/kab.xpi
# Source138-md5:	497dd4121cde2049ef4e7d5c7e35f99d
Source139:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/kk.xpi
# Source139-md5:	c2001b950bd6882923b022bc0f45c03a
Source140:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ko.xpi
# Source140-md5:	ed24a8e3656bc8f0bfe764a444fac50a
Source141:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/lt.xpi
# Source141-md5:	399f83ad6361922d713b0f29e5668e5b
Source142:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/lv.xpi
# Source142-md5:	0ac76ce85f8e30296a0761b273d0459a
Source143:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ms.xpi
# Source143-md5:	9fa33ff60071b40eff27700b49685a81
Source144:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/nb-NO.xpi
# Source144-md5:	bc3dc919903e7d6653dbe589fb609148
Source145:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/nl.xpi
# Source145-md5:	c443e4bd5c40bcb54f3f16d302e970c5
Source146:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/nn-NO.xpi
# Source146-md5:	4e02e52b5a54d3ed4ed07bb0fbb0f710
Source147:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/pa-IN.xpi
# Source147-md5:	d9dc54eaff61e3ffd49be7162e543f0c
Source148:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/pl.xpi
# Source148-md5:	321cf3fc9919b0f19260fabd9a27a658
Source149:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/pt-BR.xpi
# Source149-md5:	07be0b0f0da521228232c30d5f05c22b
Source150:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/pt-PT.xpi
# Source150-md5:	df78e79c826d86aca49e2b546427b128
Source151:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/rm.xpi
# Source151-md5:	021a1e3a45daefb782c3c5da6e7943a6
Source152:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ro.xpi
# Source152-md5:	21084eb8fd2cb6eb4a93721ebdb8195d
Source153:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/ru.xpi
# Source153-md5:	8ef5d93a1638168d2dceb8fdec0098f1
Source154:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/sk.xpi
# Source154-md5:	59fe9d03d78d10bf964fa8ffe7635397
Source155:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/sl.xpi
# Source155-md5:	41b379ca049e603fc9d5c29d495600a6
Source156:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/sq.xpi
# Source156-md5:	b928a5844dea10c3c53559640f79c9d4
Source157:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/sr.xpi
# Source157-md5:	4dd86140710c5fd66a47cde4f7ffadd2
Source158:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/sv-SE.xpi
# Source158-md5:	49563deda397c51e1d562777dd37f2ec
Source159:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/th.xpi
# Source159-md5:	1d8d11858510c89dc89429f4b2488bca
Source160:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/tr.xpi
# Source160-md5:	04eebb7949cfd5c11a98de4c29e83ea2
Source161:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/uk.xpi
# Source161-md5:	bed8c32f3da806cf5b88c1d39becd04d
Source162:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/uz.xpi
# Source162-md5:	bf9259c55602d67b1185e923302aa24d
Source163:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/vi.xpi
# Source163-md5:	033601acdb7aebcc03d5d8d01077f8fc
Source164:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/zh-CN.xpi
# Source164-md5:	6ca717d5c9165cb127fe88f1a93d8493
Source165:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}esr/linux-x86_64/xpi/zh-TW.xpi
# Source165-md5:	f16efb798d04a82f9dbcc9f8917ab3fb
Patch0:		prefs.patch
Patch2:		enable-addons.patch
Patch3:		glibc-2.34.patch
URL:		http://www.mozilla.org/projects/thunderbird/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf2_13 >= 2.13
BuildRequires:	automake
%{?with_gold:BuildRequires:	binutils >= 3:2.20.51.0.7}
%{?with_system_cairo:BuildRequires:	cairo-devel >= 1.10.2-5}
BuildRequires:	cargo >= 1.47.0
%{?with_clang:BuildRequires:	clang >= 8.0}
BuildRequires:	clang-devel >= 8.0
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	fontconfig-devel >= 1:2.7.0
BuildRequires:	freetype-devel >= 1:2.2.1
%{!?with_clang:BuildRequires:	gcc-c++ >= 6:8.1.0}
BuildRequires:	glib2-devel >= 1:2.42
BuildRequires:	gtk+3-devel >= 3.14.0
%ifnarch %arch_with_atomics64
BuildRequires:	libatomic-devel
%endif
BuildRequires:	libevent-devel
BuildRequires:	libffi-devel >= 7:3.0.9
%{?with_system_icu:BuildRequires:	libicu-devel >= 73.1}
BuildRequires:	libiw-devel
# requires libjpeg-turbo implementing at least libjpeg 6b API
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel >= 2:1.6.35
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libwebp-devel >= 1.0.2
%{?with_system_libvpx:BuildRequires:	libvpx-devel >= 1.10.0}
BuildRequires:	libxcb-devel
BuildRequires:	llvm-devel >= 8.0
BuildRequires:	mozldap-devel
BuildRequires:	nodejs >= 12.22.12
BuildRequires:	nspr-devel >= 1:%{nspr_ver}
BuildRequires:	nss-devel >= 1:%{nss_ver}
BuildRequires:	pango-devel >= 1:1.22.0
%ifarch %{arm}
BuildRequires:	perl-modules >= 1:5.006
%endif
BuildRequires:	pixman-devel >= 0.36.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	pulseaudio-devel
BuildRequires:	python3 >= 1:3.8.5-3
BuildRequires:	python3-devel-tools
BuildRequires:	python3-setuptools
BuildRequires:	python3-simplejson
BuildRequires:	python3-virtualenv >= 20
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.025
BuildRequires:	rust >= 1.76.0
BuildRequires:	rust-cbindgen >= 0.26.0
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	unzip
BuildRequires:	virtualenv
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.4.1
BuildRequires:	xz
%ifarch %{ix86} %{x8664}
BuildRequires:	yasm >= 1.0.1
%endif
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.3
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post):	mktemp >= 1.5-18
%{?with_system_cairo:Requires:	cairo >= 1.10.2-5}
Requires:	dbus-libs >= 0.60
Requires:	fontconfig >= 2.7.0
Requires:	freetype >= 1:2.2.1
Requires:	glib2 >= 1:2.42
Requires:	glibc >= 6:2.17
Requires:	gtk+3 >= 3.14.0
Requires:	hicolor-icon-theme
%{?with_system_icu:Requires:	libicu >= 73.2-2}
Requires:	libjpeg-turbo
Requires:	libpng >= 2:1.6.35
Requires:	libstdc++ >= 6:4.8.1
Requires:	libwebp >= 1.0.2
%{?with_system_libvpx:Requires:	libvpx >= 1.10.0}
Requires:	myspell-common
Requires:	nspr >= 1:%{nspr_ver}
Requires:	nss >= 1:%{nss_ver}
Requires:	pango >= 1:1.22.0
Requires:	pixman >= 0.36.0
Requires:	xorg-lib-libxkbcommon >= 0.4.1
Obsoletes:	icedove < 39
Obsoletes:	mozilla-thunderbird < 32
Obsoletes:	mozilla-thunderbird-dictionary-en-US < 2.0
Obsoletes:	thunderbird-addon-lightning < 78.0
Obsoletes:	thunderbird-lang-fa < 91.0
Obsoletes:	thunderbird-lang-si < 91.0
Conflicts:	thunderbird-lang-resources < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_cpp		-D_FORTIFY_SOURCE=[0-9]+

%if %{with clang}
%define		filterout		-fvar-tracking-assignments
%endif

# firefox/thunderbird/seamonkey provide their own versions
%define		_noautoprovfiles	%{_libdir}/%{name}/components

%define		moz_caps		libgkcodecs.so liblgpllibs.so libmozavcodec.so libmozavutil.so libmozalloc.so libmozgtk.so libmozjs.so libmozsandbox.so libmozsqlite3.so libmozwayland.so librnp.so libxul.so
# we don't want these to satisfy packages depending on xulrunner
%define		_noautoprov		%{moz_caps}
# and as we don't provide them, don't require either
%define		_noautoreq		%{moz_caps}

%define		topdir		%{_builddir}/thunderbird-%{version}
%define		objdir		%{topdir}/obj-%{_target_cpu}

%description
Thunderbird is an open-source, fast and portable email client.

%description -l pl.UTF-8
Thunderbird jest mającym otwarte źródła, szybkim i przenośnym klientem
poczty.

%package lang-af
Summary:	Afrikaans resources for Thunderbird
Summary(pl.UTF-8):	Afrykanerskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-af
Afrikaans resources for Thunderbird.

%description lang-af -l pl.UTF-8
Afrykanerskie pliki językowe dla Thunderbirda.

%package lang-ar
Summary:	Arabic resources for Thunderbird
Summary(pl.UTF-8):	Arabskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ar < 39
Obsoletes:	mozilla-thunderbird-lang-ar < 32
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
Obsoletes:	icedove-lang-ast < 39
Obsoletes:	mozilla-thunderbird-lang-ast < 32
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
Obsoletes:	icedove-lang-be < 39
Obsoletes:	mozilla-thunderbird-lang-be < 32
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
Obsoletes:	icedove-lang-bg < 39
Obsoletes:	mozilla-thunderbird-lang-bg < 32
BuildArch:	noarch

%description lang-bg
Bulgarian resources for Thunderbird.

%description lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Thunderbirda.

%package lang-br
Summary:	Breton resources for Thunderbird
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-br < 39
Obsoletes:	mozilla-thunderbird-lang-br < 32
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
Obsoletes:	icedove-lang-ca < 39
Obsoletes:	mozilla-thunderbird-lang-ca < 32
BuildArch:	noarch

%description lang-ca
Catalan resources for Thunderbird.

%description lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Thunderbirda.

%package lang-cak
Summary:	Kaqchikel resources for Thunderbird
Summary(pl.UTF-8):	Pliki językowe kaqchikel dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-cak
Kaqchikel resources for Thunderbird.

%description lang-cak -l pl.UTF-8
Pliki językowe kaqchikel dla Thunderbirda.

%package lang-cy
Summary:	Welsh resources for Thunderbird
Summary(pl.UTF-8):	Walijskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-cy
Welsh resources for Thunderbird.

%description lang-cy -l pl.UTF-8
Walijskie pliki językowe dla Thunderbirda.

%package lang-cs
Summary:	Czech resources for Thunderbird
Summary(pl.UTF-8):	Czeskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-cs < 39
Obsoletes:	mozilla-thunderbird-lang-cs < 32
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
Obsoletes:	icedove-lang-da < 39
Obsoletes:	mozilla-thunderbird-lang-da < 32
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
Obsoletes:	icedove-lang-de < 39
Obsoletes:	mozilla-thunderbird-lang-de < 32
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
Obsoletes:	icedove-lang-el < 39
Obsoletes:	mozilla-thunderbird-lang-el < 32
BuildArch:	noarch

%description lang-el
Greek resources for Thunderbird.

%description lang-el -l pl.UTF-8
Greckie pliki językowe dla Thunderbirda.

%package lang-en_CA
Summary:	English (Canadian) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (kanadyjskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-en_CA
English (Canadian) resources for Thunderbird.

%description lang-en_CA -l pl.UTF-8
Angielskie (kanadyjskie) pliki językowe dla Thunderbirda.

%package lang-en_GB
Summary:	English (British) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-en_GB < 39
Obsoletes:	mozilla-thunderbird-lang-en_GB < 32
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
Obsoletes:	icedove-lang-en_US < 39
Obsoletes:	mozilla-thunderbird-lang-en_US < 32
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
Obsoletes:	icedove-lang-es_AR < 39
Obsoletes:	mozilla-thunderbird-lang-es_AR < 32
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
Obsoletes:	icedove-lang-es < 39
Obsoletes:	mozilla-thunderbird-lang-es < 32
BuildArch:	noarch

%description lang-es
Spanish (Spain) resources for Thunderbird.

%description lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Hiszpanii).

%package lang-es_MX
Summary:	Spanish (Mexico) resources for Thunderbird
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Meksyku)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-es_MX
Spanish (Mexico) resources for Thunderbird.

%description lang-es_MX -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Meksyku).

%package lang-et
Summary:	Estonian resources for Thunderbird
Summary(pl.UTF-8):	Estońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-et < 39
Obsoletes:	mozilla-thunderbird-lang-et < 32
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
Obsoletes:	icedove-lang-eu < 39
Obsoletes:	mozilla-thunderbird-lang-eu < 32
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
Obsoletes:	icedove-lang-fi < 39
Obsoletes:	mozilla-thunderbird-lang-fi < 32
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
Obsoletes:	icedove-lang-fr < 39
Obsoletes:	mozilla-thunderbird-lang-fr < 32
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
Obsoletes:	icedove-lang-fy < 39
Obsoletes:	mozilla-thunderbird-lang-fy < 32
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
Obsoletes:	icedove-lang-ga < 39
Obsoletes:	mozilla-thunderbird-lang-ga < 32
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
Obsoletes:	icedove-lang-gd < 39
Obsoletes:	mozilla-thunderbird-lang-gd < 32
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
Obsoletes:	icedove-lang-gl < 39
Obsoletes:	mozilla-thunderbird-lang-gl < 32
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
Obsoletes:	icedove-lang-he < 39
Obsoletes:	mozilla-thunderbird-lang-he < 32
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
Obsoletes:	icedove-lang-hr < 39
Obsoletes:	mozilla-thunderbird-lang-hr < 32
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
Obsoletes:	icedove-lang-hu < 39
Obsoletes:	mozilla-thunderbird-lang-hu < 32
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
Obsoletes:	icedove-lang-hy < 39
Obsoletes:	mozilla-thunderbird-lang-hy < 32
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
Obsoletes:	icedove-lang-id < 39
Obsoletes:	mozilla-thunderbird-lang-id < 32
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
Obsoletes:	icedove-lang-is < 39
Obsoletes:	mozilla-thunderbird-lang-is < 32
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
Obsoletes:	icedove-lang-it < 39
Obsoletes:	mozilla-thunderbird-lang-it < 32
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
Obsoletes:	icedove-lang-ja < 39
Obsoletes:	mozilla-thunderbird-lang-ja < 32
BuildArch:	noarch

%description lang-ja
Japanese resources for Thunderbird.

%description lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Thunderbirda.

%package lang-ka
Summary:	Georgian resources for Thunderbird
Summary(pl.UTF-8):	Gruzińskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-ka
Georgian resources for Thunderbird.

%description lang-ka -l pl.UTF-8
Gruzińskie pliki językowe dla Thunderbirda.

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

%package lang-kk
Summary:	Kazakh resources for Thunderbird
Summary(pl.UTF-8):	Kazachskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-kk
Kazakh resources for Thunderbird.

%description lang-kk -l pl.UTF-8
Kazachskie pliki językowe dla Thunderbirda.

%package lang-ko
Summary:	Korean resources for Thunderbird
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ko < 39
Obsoletes:	mozilla-thunderbird-lang-ko < 32
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
Obsoletes:	icedove-lang-lt < 39
Obsoletes:	mozilla-thunderbird-lang-lt < 32
BuildArch:	noarch

%description lang-lt
Lithuanian resources for Thunderbird.

%description lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Thunderbirda.

%package lang-lv
Summary:	Latvian resources for Thunderbird
Summary(pl.UTF-8):	Łotewskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-lv
Latvian resources for Thunderbird.

%description lang-lv -l pl.UTF-8
Łotewskie pliki językowe dla Thunderbirda.

%package lang-ms
Summary:	Malay resources for Thunderbird
Summary(pl.UTF-8):	Malajskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-ms
Malay resources for Thunderbird.

%description lang-ms -l pl.UTF-8
Malajskie pliki językowe dla Thunderbirda.

%package lang-nb
Summary:	Norwegian Bokmaal resources for Thunderbird
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-nb < 39
Obsoletes:	mozilla-thunderbird-lang-nb < 32
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
Obsoletes:	icedove-lang-nl < 39
Obsoletes:	mozilla-thunderbird-lang-nl < 32
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
Obsoletes:	icedove-lang-nn < 39
Obsoletes:	mozilla-thunderbird-lang-nn < 32
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
Obsoletes:	icedove-lang-pa < 39
Obsoletes:	mozilla-thunderbird-lang-pa < 32
BuildArch:	noarch

%description lang-pa
Panjabi resources for Thunderbird.

%description lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Thunderbirda.

%package lang-pl
Summary:	Polish resources for Thunderbird
Summary(pl.UTF-8):	Polskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-pl < 39
Obsoletes:	mozilla-thunderbird-lang-pl < 32
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
Obsoletes:	icedove-lang-pt_BR < 39
Obsoletes:	mozilla-thunderbird-lang-pt_BR < 32
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
Obsoletes:	icedove-lang-pt < 39
Obsoletes:	mozilla-thunderbird-lang-pt < 32
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
Obsoletes:	icedove-lang-rm < 39
Obsoletes:	mozilla-thunderbird-lang-rm < 32
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
Obsoletes:	icedove-lang-ro < 39
Obsoletes:	mozilla-thunderbird-lang-ro < 32
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
Obsoletes:	icedove-lang-ru < 39
Obsoletes:	mozilla-thunderbird-lang-ru < 32
BuildArch:	noarch

%description lang-ru
Russian resources for Thunderbird.

%description lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Thunderbirda.

%package lang-sk
Summary:	Slovak resources for Thunderbird
Summary(pl.UTF-8):	Słowackie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sk < 39
Obsoletes:	mozilla-thunderbird-lang-sk < 32
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
Obsoletes:	icedove-lang-sl < 39
Obsoletes:	mozilla-thunderbird-lang-sl < 32
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
Obsoletes:	icedove-lang-sq < 39
Obsoletes:	mozilla-thunderbird-lang-sq < 32
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
Obsoletes:	icedove-lang-sr < 39
Obsoletes:	mozilla-thunderbird-lang-sr < 32
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
Obsoletes:	icedove-lang-sv < 39
Obsoletes:	mozilla-thunderbird-lang-sv < 32
BuildArch:	noarch

%description lang-sv
Swedish resources for Thunderbird.

%description lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Thunderbirda.

%package lang-th
Summary:	Thai resources for Thunderbird
Summary(pl.UTF-8):	Tajskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-th
Thai resources for Thunderbird.

%description lang-th -l pl.UTF-8
Tajskie pliki językowe dla Thunderbirda.

%package lang-tr
Summary:	Turkish resources for Thunderbird
Summary(pl.UTF-8):	Tureckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-tr < 39
Obsoletes:	mozilla-thunderbird-lang-tr < 32
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
Obsoletes:	icedove-lang-uk < 39
Obsoletes:	mozilla-thunderbird-lang-uk < 32
BuildArch:	noarch

%description lang-uk
Ukrainian resources for Thunderbird.

%description lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Thunderbirda.

%package lang-uz
Summary:	Uzbek resources for Thunderbird
Summary(pl.UTF-8):	Uzbeckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
BuildArch:	noarch

%description lang-uz
Uzbek resources for Thunderbird.

%description lang-uz -l pl.UTF-8
zbeckiee pliki językowe dla Thunderbirda.

%package lang-vi
Summary:	Vietnamese resources for Thunderbird
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-vi < 39
Obsoletes:	mozilla-thunderbird-lang-vi < 32
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
Obsoletes:	icedove-lang-zh_CN < 39
Obsoletes:	mozilla-thunderbird-lang-zh_CN < 32
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
Obsoletes:	icedove-lang-zh_TW < 39
Obsoletes:	mozilla-thunderbird-lang-zh_TW < 32
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
%setup -q %(seq -f '-a %g' 100 165 | xargs)
%patch0 -p1
%patch2 -p0
%patch3 -p1

%build
cp -p %{_datadir}/automake/config.* build/autoconf

cat << 'EOF' > .mozconfig
mk_add_options MOZ_OBJDIR=%{objdir}

%if %{with clang}
export CC="clang"
export CXX="clang++"
%else
export CC="%{__cc}"
export CXX="%{__cxx}"
%endif
%ifarch %{ix86}
export CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="%{rpmcxxflags} -D_FILE_OFFSET_BITS=64"
%else
export CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="%{rpmcxxflags} -D_FILE_OFFSET_BITS=64"
%endif

%if %{with lowmem}
export CFLAGS="$CFLAGS -g0"
export CXXFLAGS="$CXXFLAGS -g0"
export MOZ_DEBUG_FLAGS=" "
export LLVM_USE_SPLIT_DWARF=1
export LLVM_PARALLEL_LINK_JOBS=1
export MOZ_LINK_FLAGS="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
export RUSTFLAGS="-Cdebuginfo=0"
%endif

%if %{with crashreporter}
export MOZ_DEBUG_SYMBOLS=1
%endif

# Options for 'configure' (same as command-line options).
ac_add_options --host=%{_target_platform}
ac_add_options --prefix=%{_prefix}
%if %{?debug:1}0
ac_add_options --disable-optimize
ac_add_options --enable-debug
ac_add_options --enable-debug-modules
ac_add_options --enable-debugger-info-modules
ac_add_options --enable-crash-on-assert
%else
ac_add_options --disable-debug
%endif
ac_add_options --disable-strip
ac_add_options --disable-install-strip
%if %{with tests}
ac_add_options --enable-tests
%else
ac_add_options --disable-tests
%endif
%if %{with crashreporter}
ac_add_options --enable-crashreporter
%else
ac_add_options --disable-crashreporter
%endif
%ifarch %{ix86} %{x8664} %{arm}
ac_add_options --disable-elf-hack
%endif
ac_add_options --disable-necko-wifi
ac_add_options --disable-updater
ac_add_options --enable-alsa
ac_add_options --enable-application=comm/mail
ac_add_options --enable-chrome-format=omni
ac_add_options --enable-default-toolkit=cairo-gtk3
%{?with_official:ac_add_options --enable-official-branding}
%{?with_gold:ac_add_options --enable-linker=gold}
%{?with_shared_js:ac_add_options --enable-shared-js}
%{?with_system_cairo:ac_add_options --enable-system-cairo}
ac_add_options --enable-system-pixman
ac_add_options --with-distribution-id=org.pld-linux
ac_add_options --with-system-ffi
ac_add_options --with%{!?with_system_icu:out}-system-icu
ac_add_options --with-system-jpeg
ac_add_options --with-system-libevent
ac_add_options --with%{!?with_system_libvpx:out}-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-webp
ac_add_options --with-system-zlib
ac_add_options --without-wasm-sandboxed-libraries
EOF

%if %{without clang}
# On x86_64 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
MOZ_PARALLEL_BUILD=1
%ifarch %{x8664}
jobs="%{__jobs}"
[ -n "$jobs" -a "$jobs" -gt 4 ] && MOZ_PARALLEL_BUILD=4 || MOZ_PARALLEL_BUILD="$jobs"
%endif
export MOZ_PARALLEL_BUILD
%else
%{?__jobs:export MOZ_PARALLEL_BUILD="%__jobs"}
%endif

export MOZBUILD_STATE_PATH="$(pwd)/.mozbuild"
export MACH_SYSTEM_ASSERTED_COMPATIBLE_WITH_BUILD_SITE=1
export MACH_SYSTEM_ASSERTED_COMPATIBLE_WITH_MACH_SITE=1
AUTOCONF=/usr/bin/autoconf2_13 \
MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=none \
./mach build %{?with_lowmem2:-j1}

%if %{with crashreporter}
# create debuginfo for crash-stats.mozilla.com
%{__make} -j1 -C obj-%{_target_cpu} buildsymbols
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/{extensions,plugins},%{_datadir}/%{name},%{_desktopdir}}

cd %{objdir}
%{__make} -C comm/mail/installer stage-package \
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

cd ..

%{__sed} -e 's,@LIBDIR@,%{_libdir},' %{SOURCE2} > $RPM_BUILD_ROOT%{_bindir}/%{name}

# install icons and desktop file
for i in 16 22 24 32 48 64 128 256; do
	install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/${i}x${i}/apps
	cp -a comm/mail/branding/thunderbird/default${i}.png \
		$RPM_BUILD_ROOT%{_iconsdir}/hicolor/${i}x${i}/apps/thunderbird.png
done
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

# move arch independant ones to datadir
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome $RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults $RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/isp $RPM_BUILD_ROOT%{_datadir}/%{name}/isp
ln -s ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/%{name}/extensions $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions
ln -s ../../share/%{name}/isp $RPM_BUILD_ROOT%{_libdir}/%{name}/isp

# remove unecessary stuff
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/removed-files

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
for d in chrome defaults icons isp modules res; do
	if [ -d %{_libdir}/%{name}/$d ] && [ ! -L %{_libdir}/%{name}/$d ]; then
		install -d %{_datadir}/%{name}
		mv %{_libdir}/%{name}/$d %{_datadir}/%{name}/$d
	fi
done
exit 0

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins

%attr(755,root,root) %{_libdir}/%{name}/glxtest
%attr(755,root,root) %{_libdir}/%{name}/libgkcodecs.so
%attr(755,root,root) %{_libdir}/%{name}/libmozgtk.so
%attr(755,root,root) %{_libdir}/%{name}/liblgpllibs.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavcodec.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavutil.so
%{?with_shared_js:%attr(755,root,root) %{_libdir}/%{name}/libmozjs.so}
%ifarch %{ix86} %{x8664} %{arm} aarch64
%attr(755,root,root) %{_libdir}/%{name}/libmozsandbox.so
%endif
%attr(755,root,root) %{_libdir}/%{name}/libmozsqlite3.so
%attr(755,root,root) %{_libdir}/%{name}/libmozwayland.so
%attr(755,root,root) %{_libdir}/%{name}/librnp.so
%attr(755,root,root) %{_libdir}/%{name}/libxul.so
%attr(755,root,root) %{_libdir}/%{name}/thunderbird-bin
%attr(755,root,root) %{_libdir}/%{name}/pingsender
%attr(755,root,root) %{_libdir}/%{name}/precomplete
%attr(755,root,root) %{_libdir}/%{name}/rnp-cli
%attr(755,root,root) %{_libdir}/%{name}/rnpkeys
%attr(755,root,root) %{_libdir}/%{name}/thunderbird
%attr(755,root,root) %{_libdir}/%{name}/vaapitest

%{_libdir}/%{name}/application.ini
%{_libdir}/%{name}/dependentlibs.list
%{_libdir}/%{name}/omni.ja
%{_libdir}/%{name}/platform.ini
%{!?with_system_icu:%{_libdir}/%{name}/icudt58l.dat}

%dir %{_libdir}/%{name}/fonts
%{_libdir}/%{name}/fonts/TwemojiMozilla.ttf

%if %{with crashreporter}
%attr(755,root,root) %{_libdir}/%{name}/crashreporter
%{_libdir}/%{name}/crashreporter.ini
%{_libdir}/%{name}/Throbber-small.gif
%endif

# symlinks
%{_libdir}/%{name}/chrome
%{_libdir}/%{name}/defaults
%{_libdir}/%{name}/extensions
%{_libdir}/%{name}/isp

%{_desktopdir}/thunderbird.desktop
%{_iconsdir}/hicolor/*/apps/thunderbird.png

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/chrome
%{_datadir}/%{name}/defaults
%dir %{_datadir}/%{name}/extensions
%{_datadir}/%{name}/isp

%files lang-af
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-af@thunderbird.mozilla.org.xpi

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

%files lang-br
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-br@thunderbird.mozilla.org.xpi

%files lang-ca
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ca@thunderbird.mozilla.org.xpi

%files lang-cak
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-cak@thunderbird.mozilla.org.xpi

%files lang-cs
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-cs@thunderbird.mozilla.org.xpi

%files lang-cy
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-cy@thunderbird.mozilla.org.xpi

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

%files lang-en_CA
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-en-CA@thunderbird.mozilla.org.xpi

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

%files lang-es_MX
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-es-MX@thunderbird.mozilla.org.xpi

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

%files lang-ka
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ka@thunderbird.mozilla.org.xpi

%files lang-kab
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-kab@thunderbird.mozilla.org.xpi

%files lang-kk
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-kk@thunderbird.mozilla.org.xpi

%files lang-ko
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ko@thunderbird.mozilla.org.xpi

%files lang-lt
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-lt@thunderbird.mozilla.org.xpi

%files lang-lv
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-lv@thunderbird.mozilla.org.xpi

%files lang-ms
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-ms@thunderbird.mozilla.org.xpi

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

%files lang-th
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-th@thunderbird.mozilla.org.xpi

%files lang-tr
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-tr@thunderbird.mozilla.org.xpi

%files lang-uk
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-uk@thunderbird.mozilla.org.xpi

%files lang-uz
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-uz@thunderbird.mozilla.org.xpi

%files lang-vi
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-vi@thunderbird.mozilla.org.xpi

%files lang-zh_CN
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-zh-CN@thunderbird.mozilla.org.xpi

%files lang-zh_TW
%defattr(644,root,root,755)
%{_datadir}/%{name}/extensions/langpack-zh-TW@thunderbird.mozilla.org.xpi
