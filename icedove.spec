#
# TODO:
# - CHECK all features of enigmail
# - separate spec for enigmail
# - update or remove -myspell.patch
# - package unpackaged files
# - update branding patch!!!
#
# Conditional builds
%bcond_without	enigmail	# don't build enigmail - GPG/PGP support
%bcond_without	gnomeui		# disable gnomeui support
%bcond_without	gnomevfs	# disable GNOME comp. (gconf+libgnome+gnomevfs) and gnomevfs ext.
%bcond_without	gnome		# disable all GNOME components (gnome+gnomeui+gnomevfs)
%bcond_without	ldap		# disable e-mail address lookups in LDAP directories
%bcond_without  lightning   # disable sunbird calendar
#
%if %{without gnome}
%undefine	with_gnomeui
%undefine	with_gnomevfs
%endif
%define		enigmail_ver		1.0.0

Summary:	Icedove - email client
Summary(pl.UTF-8):	Icedove - klient poczty
Name:		icedove
Version:	3.0
Release:	0.3
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		Applications/Networking
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/source/thunderbird-%{version}.source.tar.bz2
# Source0-md5:	9a564ac2489b1b0f9348dc298b913f6c
Source1:	http://www.mozilla-enigmail.org/download/source/enigmail-%{enigmail_ver}.tar.gz
# Source1-md5:	e3a6d379f1a72ac023751bdde2de750a
Source2:	%{name}-branding.tar.bz2
# Source2-md5:	e775b8cb658de32f30b403bc9b7950bf
Source3:	%{name}-rm_nonfree.sh
Source4:	%{name}.desktop
Source5:	%{name}.sh
Source6:	%{name}-enigmail.manifest
Patch0:		%{name}-branding.patch
Patch1:		%{name}-enigmail-shared.patch
Patch2:		%{name}-gcc.patch
Patch3:		%{name}-fonts.patch
Patch4:		%{name}-install.patch
Patch5:		%{name}-myspell.patch
Patch6:		%{name}-prefs.patch
Patch7:		%{name}-breakpad.patch
URL:		http://www.pld-linux.org/Packages/Icedove
%{?with_gnomevfs:BuildRequires:	GConf2-devel >= 1.2.1}
BuildRequires:	automake
BuildRequires:	freetype-devel >= 1:2.1.8
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.0}
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libIDL-devel >= 0.8.0
%{?with_gnomevfs:BuildRequires:	libgnome-devel >= 2.0}
%{?with_gnomeui:BuildRequires:	libgnomeui-devel >= 2.2.0}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	myspell-devel
BuildRequires:	nspr-devel >= 1:4.8
BuildRequires:	nss-devel >= 1:3.12.0
BuildRequires:	pango-devel >= 1:1.1.0
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel >= 2.1
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel
Requires:	myspell-common
Requires:	nspr >= 1:4.6.1
Requires:	nss >= 1:3.11.3
Obsoletes:	mozilla-thunderbird
Obsoletes:	mozilla-thunderbird-dictionary-en-US
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_cpp		-D_FORTIFY_SOURCE=[0-9]+

# iceweasel/icedove/iceape provide their own versions
%define		_noautoreqdep		libgfxpsshar.so libgkgfx.so libgtkxtbin.so libjsj.so libxpcom_compat.so libxpcom_core.so libxpistub.so
%define		_noautoprovfiles	%{_libdir}/%{name}/components
# we don't want these to satisfy xulrunner-devel
%define		_noautoprov		libgtkembedmoz.so libldap50.so libmozjs.so libprldap50.so libssldap50.so libxpcom.so libxul.so
# and as we don't provide them, don't require either
%define		_noautoreq		libgtkembedmoz.so libldap50.so libmozjs.so libprldap50.so libssldap50.so libxpcom.so libxul.so

%description
Icedove is an open-source,fast and portable email client.

%description -l pl.UTF-8
Icedove jest open sourcowym, szybkim i przenośnym klientem poczty.

%package addon-enigmail
Summary:	Extension for the authentication and encryption features provided by GnuPG
Summary(pl.UTF-8):	Rozszerzenie do uwierzytelniania i szyfrowania zapewnianego przez GnuPG
License:	MPL/LGPL
Group:		Applications/Networking
URL:		http://enigmail.mozdev.org/
Requires:	%{name} = %{version}-%{release}
Requires:	gnupg
Obsoletes:	mozilla-thunderbird-addon-enigmail

%description addon-enigmail
Enigmail is an extension to the Icedove mail client which allows users
to access the authentication and encryption features provided by
GnuPG.

Main Features:
- Encrypt/sign mail when sending, decrypt/authenticate received mail
- Support for inline-PGP (RFC 2440) and PGP/MIME (RFC 3156)
- Per-Account based encryption and signing defaults
- Per-Recipient rules for automated key selection, and
  enabling/disabling encryption and signing
- OpenPGP key management interface

%description addon-enigmail -l pl.UTF-8
Enigmail to rozszerzenie klienta pocztowego Icedove pozwalające
użytkownikom na dostęp do uwierzytelniania i szyfrowania zapewnianego
przez GnuPG.

Główne możliwości:
- szyfrowanie/podpisywanie poczty przy wysyłaniu,
  odszyfrowywanie/uwierzytelnianie poczty odebranej
- obsługa inline-PGP (RFC 2440) i PGP/MIME (RFC 3156)
- ustawienia domyślne szyfrowania i podpisywania dla każdego konta
- reguły automatycznego wyboru kluczy i włączenia szyfrowania oraz
  podpisywania dla każdego adresata
- interfejs do zarządzania kluczami OpenPGP

%prep
%setup -q -c -a2
cd comm-1.9.1
%{?with_enigmail:tar xvfz %{SOURCE1} -C mailnews/extensions}
/bin/sh %{SOURCE3}
%patch0 -p2
%{?with_enigmail:%patch1 -p1}
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1
%patch6 -p0
%patch7 -p1

%build
cd comm-1.9.1
export CFLAGS="%{rpmcflags} `%{_bindir}/pkg-config mozilla-nspr --cflags-only-I`"
export CXXFLAGS="%{rpmcflags} `%{_bindir}/pkg-config mozilla-nspr --cflags-only-I`"

cp -f %{_datadir}/automake/config.* mozilla/build/autoconf
cp -f %{_datadir}/automake/config.* mozilla/nsprpub/build/autoconf
cp -f %{_datadir}/automake/config.* directory/c-sdk/config/autoconf

cat << 'EOF' > .mozconfig
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-%{_target_cpu}

# Options for 'configure' (same as command-line options).
ac_add_options --prefix=%{_prefix}
ac_add_options --exec-prefix=%{_exec_prefix}
ac_add_options --bindir=%{_bindir}
ac_add_options --sbindir=%{_sbindir}
ac_add_options --sysconfdir=%{_sysconfdir}
ac_add_options --datadir=%{_datadir}
ac_add_options --includedir=%{_includedir}
ac_add_options --libdir=%{_libdir}
ac_add_options --libexecdir=%{_libexecdir}
ac_add_options --localstatedir=%{_localstatedir}
ac_add_options --sharedstatedir=%{_sharedstatedir}
ac_add_options --mandir=%{_mandir}
ac_add_options --infodir=%{_infodir}
%if %{?debug:1}0
ac_add_options --disable-optimize
ac_add_options --enable-debug
ac_add_options --enable-debug-modules
ac_add_options --enable-debugger-info-modules
ac_add_options --enable-crash-on-assert
%else
ac_add_options --disable-debug
ac_add_options --disable-debug-modules
ac_add_options --disable-logging
ac_add_options --enable-optimize="%{rpmcflags} -Os"
%endif
%if %{with tests}
ac_add_options --enable-tests
%else
ac_add_options --disable-tests
%endif
%if %{with gnomeui}
ac_add_options --enable-gnomeui
%else
ac_add_options --disable-gnomeui
%endif
%if %{with gnomevfs}
ac_add_options --enable-gnomevfs
%else
ac_add_options --disable-gnomevfs
%endif
%if %{with ldap}
ac_add_options --enable-ldap
%else
ac_add_options --disable-ldap
%endif
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-xterm-updates
ac_add_options --enable-ldap
ac_add_options --enable-postscript
ac_add_options --enable-startup-notification
%if %{with lightning}
ac_add_options --enable-calendar
%else
ac_add_options --disable-calendar
%endif
ac_add_options --disable-installer
ac_add_options --disable-jsd
ac_add_options --disable-xprint
ac_add_options --disable-permissions
ac_add_options --disable-pref-extensions
ac_add_options --enable-canvas
ac_add_options --enable-crypto
ac_add_options --enable-default-toolkit="gtk2"
ac_add_options --enable-mathml
ac_add_options --enable-optimize="%{rpmcflags}"
ac_add_options --enable-pango
ac_add_options --enable-reorder
ac_add_options --enable-static
ac_add_options --disable-strip
ac_add_options --disable-strip-libs
ac_add_options --enable-system-cairo
ac_add_options --enable-system-myspell
ac_add_options --enable-svg
ac_add_options --enable-xft
ac_add_options --enable-application=mail
ac_add_options --enable-default-toolkit=cairo-gtk2
ac_add_options --enable-xinerama
ac_add_options --with-system-jpeg
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-zlib
ac_add_options --with-pthreads
ac_add_options --enable-single-profile
ac_add_options --disable-profilesharing
ac_add_options --with-distribution-id=org.pld-linux
#ac_add_options --with-branding=icedove/branding
ac_add_options --with-default-mozilla-five-home=%{_libdir}/%{name}
EOF

%{__make} -f client.mk build \
	STRIP="/bin/true" \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%if %{with enigmail}
cd mailnews/extensions/enigmail
./makemake -r
%{__make} -C ../../../obj-%{_target_cpu}/mailnews/extensions/enigmail \
	STRIP="/bin/true" \
	CC="%{__cc}" \
	CXX="%{__cxx}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_pixmapsdir},%{_desktopdir}} \
	       $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}

cd comm-1.9.1
%{__make} -C obj-%{_target_cpu}/mail/installer stage-package \
	DESTDIR=$RPM_BUILD_ROOT \
	MOZ_PKG_APPDIR=%{_libdir}/%{name} \
	PKG_SKIP_STRIP=1

# move arch independant ones to datadir
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome $RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults $RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/greprefs $RPM_BUILD_ROOT%{_datadir}/%{name}/greprefs
#mv $RPM_BUILD_ROOT%{_libdir}/%{name}/icons $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/isp $RPM_BUILD_ROOT%{_datadir}/%{name}/isp
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/res $RPM_BUILD_ROOT%{_datadir}/%{name}/res
ln -s ../../share/%{name}/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/%{name}/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/%{name}/greprefs $RPM_BUILD_ROOT%{_libdir}/%{name}/greprefs
#ln -s ../../share/%{name}/icons $RPM_BUILD_ROOT%{_libdir}/%{name}/icons
ln -s ../../share/%{name}/isp $RPM_BUILD_ROOT%{_libdir}/%{name}/isp
ln -s ../../share/%{name}/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries

%{__sed} -e 's,@LIBDIR@,%{_libdir},' %{SOURCE5} > $RPM_BUILD_ROOT%{_bindir}/icedove
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/thunderbird
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/mozilla-thunderbird

install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%if %{with enigmail}
_enig_dir=$RPM_BUILD_ROOT%{_libdir}/%{name}/extensions/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
install -d $_enig_dir/chrome
install -d $_enig_dir/components
install -d $_enig_dir/defaults/preferences
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome/enigmail.jar $_enig_dir/chrome
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/components/enig* $_enig_dir/components
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/components/libenigmime.so $_enig_dir/components
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/components/ipc.xpt $_enig_dir/components
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults/preferences/enigmail.js $_enig_dir/defaults/preferences
cp -f mailnews/extensions/enigmail/package/install.rdf $_enig_dir
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults/preferences
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome/enigmail-en-US.jar
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome/enigmail-skin.jar
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome/enigmime.jar
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/components/enig*
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/components/libenigmime.so
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/components/ipc.xpt
cp -f %{SOURCE6} $_enig_dir/chrome.manifest
#cp -f icedove/branding/content/icon64.png $RPM_BUILD_ROOT%{_pixmapsdir}/icedove.png
%endif

# win32 stuff
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/dirver

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans
if [ -d %{_libdir}/%{name}/dictionaries ] && [ ! -L %{_libdir}/%{name}/dictionaries ]; then
	mv -v %{_libdir}/%{name}/dictionaries{,.rpmsave}
fi
for d in chrome defaults greprefs icons isp res; do
	if [ -d %{_libdir}/%{name}/$d ] && [ ! -L %{_libdir}/%{name}/$d ]; then
		install -d %{_datadir}/%{name}
		mv %{_libdir}/%{name}/$d %{_datadir}/%{name}/$d
	fi
done
exit 0

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/icedove
%attr(755,root,root) %{_bindir}/mozilla-thunderbird
%attr(755,root,root) %{_bindir}/thunderbird
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.ini
%dir %{_libdir}/%{name}/components
%attr(755,root,root) %{_libdir}/%{name}/components/*.so
%{_libdir}/%{name}/components/*.js
%{_libdir}/%{name}/components/*.xpt
%attr(755,root,root) %{_libdir}/%{name}/*.so
%attr(755,root,root) %{_libdir}/%{name}/*.sh
%attr(755,root,root) %{_libdir}/%{name}/*-bin
%attr(755,root,root) %{_libdir}/%{name}/mozilla-xremote-client
#%attr(755,root,root) %{_libdir}/%{name}/reg*
%attr(755,root,root) %{_libdir}/%{name}/icedove
%{_libdir}/%{name}/*.txt
#%attr(755,root,root) %{_libdir}/%{name}/x*

# symlinks
%{_libdir}/%{name}/chrome
%{_libdir}/%{name}/defaults
%{_libdir}/%{name}/dictionaries
%{_libdir}/%{name}/greprefs
#%{_libdir}/%{name}/icons
%{_libdir}/%{name}/isp
%{_libdir}/%{name}/res

%{_libdir}/%{name}/dependentlibs.list
#%{_libdir}/%{name}/updater
#%{_libdir}/%{name}/update.locale
#%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/chrome
%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/greprefs
#%{_datadir}/%{name}/icons
%{_datadir}/%{name}/isp
%{_datadir}/%{name}/res

%dir %{_libdir}/%{name}/modules
%{_libdir}/%{name}/modules/*.js*
%dir %{_libdir}/%{name}/modules/activity
%{_libdir}/%{name}/modules/activity/*.js
%dir %{_libdir}/%{name}/modules/gloda
%{_libdir}/%{name}/modules/gloda/*.js

%dir %{_libdir}/%{name}/extensions
%{_libdir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}
%{_libdir}/%{name}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}

%if %{with enigmail}
%files addon-enigmail
%defattr(644,root,root,755)
%{_libdir}/%{name}/extensions/{847b3a00-7ab1-11d4-8f02-006008948af5}
%endif
