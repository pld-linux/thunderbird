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
%define		nss_ver		3.90

Summary:	Thunderbird - email client
Summary(pl.UTF-8):	Thunderbird - klient poczty
Name:		thunderbird
Version:	115.3.0
Release:	1
License:	MPL v2.0
Group:		X11/Applications/Mail
Source0:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/source/%{name}-%{version}.source.tar.xz
# Source0-md5:	d1a72df19949cae096a0122f551f6b05
Source1:	%{name}.desktop
Source2:	%{name}.sh
Source100:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/af.xpi
# Source100-md5:	c9ad58c28167f79eee9a77506b2078a9
Source101:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ar.xpi
# Source101-md5:	fab992ff964ea0249c83db4fa1bd722b
Source102:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ast.xpi
# Source102-md5:	805f72d05f4a1ba030e551d85bcf9906
Source103:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/be.xpi
# Source103-md5:	fe371f217425e6f3b17eefebeaf663b3
Source104:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/bg.xpi
# Source104-md5:	a3a068711a78b6d88c8efa3765283305
Source105:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/br.xpi
# Source105-md5:	6298bb1274eee0c50df4c33a1f97cbf2
Source106:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ca.xpi
# Source106-md5:	d720b300939706abc33ce2bf9d0b11cf
Source107:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/cak.xpi
# Source107-md5:	7ee7baa088036bac9736485379392b79
Source108:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/cs.xpi
# Source108-md5:	9707f8d4ba47be4a4fae091b7dfe1014
Source109:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/cy.xpi
# Source109-md5:	cddb0c96038a0c0c79b9a47ce9267aff
Source110:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/da.xpi
# Source110-md5:	3589842783011ac6485d475013f13ec3
Source111:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/de.xpi
# Source111-md5:	fcbd56b4a62c7215eab25484986e9f33
Source112:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/dsb.xpi
# Source112-md5:	7aa56e774bca787b4ca133a13059bfba
Source113:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/el.xpi
# Source113-md5:	40a86e4e44154a3a618c08b7437b318b
Source114:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/en-CA.xpi
# Source114-md5:	a8046675a0ba7ea348e836a8206b99b6
Source115:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/en-GB.xpi
# Source115-md5:	1f88876c2840782d641834077186b31a
Source116:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/en-US.xpi
# Source116-md5:	61416dba5839f580cd1a372c030498bf
Source117:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/es-AR.xpi
# Source117-md5:	144c45db5157a67549a5d287b69d7273
Source118:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/es-ES.xpi
# Source118-md5:	3afefc7a9b36ee13fd608b6d203949a5
Source119:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/es-MX.xpi
# Source119-md5:	3225cdf5519bab1b01e25eb76e9345d7
Source120:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/et.xpi
# Source120-md5:	10eb632ea2826846584869420845542d
Source121:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/eu.xpi
# Source121-md5:	23f705b99083c76e91a22ee7364fa44f
Source122:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/fi.xpi
# Source122-md5:	e7c1e3a65752623e6d35ea3da0825aea
Source123:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/fr.xpi
# Source123-md5:	925ad8f410c2a49f42ef5869306a6b54
Source124:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/fy-NL.xpi
# Source124-md5:	b8e1764bb8c3e6f2afb9bc84515ae688
Source125:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ga-IE.xpi
# Source125-md5:	0c6a33f59fd10ff99a23b79c94ca7382
Source126:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/gd.xpi
# Source126-md5:	e2f9be32bcc07838a4911c7c7e1802be
Source127:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/gl.xpi
# Source127-md5:	578f1cff28e198218c6e4acdc993d32d
Source128:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/he.xpi
# Source128-md5:	83e6bcce35571b03e7e24feb94b84521
Source129:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/hr.xpi
# Source129-md5:	7c647473d9416e0a07a3cbdbee2fb0f8
Source130:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/hsb.xpi
# Source130-md5:	23bf0960873e692365b91ee25844546c
Source131:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/hu.xpi
# Source131-md5:	988b313087bf3deffeca89305a4141a4
Source132:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/hy-AM.xpi
# Source132-md5:	07cab8def47af3b496846f14e6415c1c
Source133:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/id.xpi
# Source133-md5:	88ee453644362abbca99bf8894ddaa8d
Source134:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/is.xpi
# Source134-md5:	303de9b67a4015ee53ded5ef1b653638
Source135:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/it.xpi
# Source135-md5:	a1a1a87ddbcdda77ba4ae8e830e52a5f
Source136:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ja.xpi
# Source136-md5:	568b99b1c8ae2a8b8674d7c8226c10a1
Source137:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ka.xpi
# Source137-md5:	0a125c011b82e1462146e91d203edc2e
Source138:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/kab.xpi
# Source138-md5:	2ec6d079fe51e7ded4e59716a385ca91
Source139:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/kk.xpi
# Source139-md5:	d8232d55c0b9f6a8d53890c7abec64f2
Source140:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ko.xpi
# Source140-md5:	2c93803317649f5c8fd1e18c6abfab05
Source141:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/lt.xpi
# Source141-md5:	4df4f2f730d857312caa987dad33d2ba
Source142:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/lv.xpi
# Source142-md5:	877bf9c26f5f95988cbad4c24f46a9bb
Source143:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ms.xpi
# Source143-md5:	54afa909cb9072d8ac26fb70fc87da33
Source144:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/nb-NO.xpi
# Source144-md5:	8a9721ed9a75476d771d14796606d3a7
Source145:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/nl.xpi
# Source145-md5:	9332a26943f93618f394983ce99da800
Source146:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/nn-NO.xpi
# Source146-md5:	7f4367460c626f6bf790e78178f477c6
Source147:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/pa-IN.xpi
# Source147-md5:	2476f25273e31061f00ab4f3063f34d2
Source148:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/pl.xpi
# Source148-md5:	344b399e8d3a61273c93e23308fd5291
Source149:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/pt-BR.xpi
# Source149-md5:	9189d7adcb730d97dea7a7a01c57ffc5
Source150:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/pt-PT.xpi
# Source150-md5:	aaac255d71c8d293a9e2d4204eb22e4a
Source151:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/rm.xpi
# Source151-md5:	5056f01c993c69032c6fb480d0e5da0b
Source152:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ro.xpi
# Source152-md5:	e7ba77939682489605ef324e9d1e4220
Source153:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/ru.xpi
# Source153-md5:	cef3b84dc6d056b5083bc4fa3c12adfc
Source154:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/sk.xpi
# Source154-md5:	5c1c7581aa4d79626c006d8eafeac582
Source155:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/sl.xpi
# Source155-md5:	b1943950badef487bbc6ab7246c28e14
Source156:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/sq.xpi
# Source156-md5:	ebff133e9a786cbd6871048c9f4413fa
Source157:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/sr.xpi
# Source157-md5:	af2e6650d1bc54c3ade030e10a1ac34e
Source158:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/sv-SE.xpi
# Source158-md5:	eb8fad8c4e11ae42d3b39f4bf49ef1bb
Source159:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/th.xpi
# Source159-md5:	b5de3c23439b40f1360dab2b883c8355
Source160:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/tr.xpi
# Source160-md5:	d9ceb2345a42c5d093f112eae3deee14
Source161:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/uk.xpi
# Source161-md5:	9ac8baec0032d4257aeea80a99d12add
Source162:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/uz.xpi
# Source162-md5:	66ba1d0e75687e4ef38ed628c21a999e
Source163:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/vi.xpi
# Source163-md5:	b5945a9652d816b6b3a16070d3bc28f0
Source164:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/zh-CN.xpi
# Source164-md5:	1bca9319c2be7b6f08dc980b2e8f45de
Source165:	https://releases.mozilla.org/pub/thunderbird/releases/%{version}/linux-x86_64/xpi/zh-TW.xpi
# Source165-md5:	fc24106eee555ad039ef186e53185f81
Patch0:		prefs.patch
Patch1:		no-subshell.patch
Patch2:		enable-addons.patch
Patch3:		glibc-2.34.patch
URL:		http://www.mozilla.org/projects/thunderbird/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf2_13 >= 2.13
BuildRequires:	automake
%{?with_gold:BuildRequires:	binutils >= 3:2.20.51.0.7}
%{?with_system_cairo:BuildRequires:	cairo-devel >= 1.10.2-5}
BuildRequires:	cargo >= 1.47.0
%{?with_clang:BuildRequires:	clang >= 7.0}
BuildRequires:	clang-devel >= 7.0
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	fontconfig-devel >= 1:2.7.0
BuildRequires:	freetype-devel >= 1:2.2.1
%{!?with_clang:BuildRequires:	gcc-c++ >= 6:8.1.0}
BuildRequires:	glib2-devel >= 1:2.42
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	libatomic-devel
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
BuildRequires:	llvm-devel >= 7.0
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
BuildRequires:	python3-simplejson
BuildRequires:	python3-virtualenv >= 20
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rust >= 1.66.0
BuildRequires:	rust-cbindgen >= 0.24.3
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
Requires:	dbus-glib >= 0.60
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

%define		moz_caps		liblgpllibs.so libmozavcodec.so libmozavutil.so libmozalloc.so libmozgtk.so libmozjs.so libmozsandbox.so libmozsqlite3.so libmozwayland.so librnp.so libxul.so
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

%package lang-bn
Summary:	Bengali (Bangladesh) resources for Thunderbird
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Thunderbirda (wersja dla Bangladeszu)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-bn < 39
Obsoletes:	mozilla-thunderbird-lang-bn < 32
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

%package lang-ta_LK
Summary:	Tamil (Sri Lanka) resources for Thunderbird
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Thunderbirda (wersja dla Sri Lanki)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ta_LK < 39
Obsoletes:	mozilla-thunderbird-lang-ta_LK < 32
BuildArch:	noarch

%description lang-ta_LK
Tamil (Sri Lanka) resources for Thunderbird.

%description lang-ta_LK -l pl.UTF-8
Tamilskie pliki językowe dla Thunderbirda (wersja dla Sri Lanki).

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
%patch1 -p1
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
%attr(755,root,root) %{_libdir}/%{name}/plugin-container
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
