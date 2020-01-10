Name:           libid3tag
Version:        0.15.1b
Release:        17%{?dist}
Summary:        ID3 tag manipulation library
Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.underbit.com/products/mad/
Source0:        http://downloads.sourceforge.net/mad/%{name}-%{version}.tar.gz
Patch0:         libid3tag-0.15.1b-fix_overflow.patch
BuildRequires:  zlib-devel >= 1.1.4
# For autoreconf
BuildRequires:  libtool

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
ID3 tag library development files.


%prep
%setup -q
%patch0 -p0 -b .CVE-2008-2109
touch NEWS AUTHORS ChangeLog
autoreconf -i -f

# *.pc originally from the Debian package.
cat << \EOF > %{name}.pc
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: id3tag
Description: ID3 tag manipulation library
Requires:
Version: %{version}
Libs: -lid3tag
Cflags:
EOF


%build
%configure --disable-static
# configure strips -g, -O2 from CFLAGS, override it here
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
install -Dpm 644 %{name}.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/id3tag.pc


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/libid3tag.so.*

%files devel
%{_includedir}/id3tag.h
%{_libdir}/libid3tag.so
%{_libdir}/pkgconfig/id3tag.pc


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.15.1b-17
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.15.1b-16
- Mass rebuild 2013-12-27

* Mon Mar 25 2013 Hans de Goede <hdegoede@redhat.com> - 0.15.1b-15
- Run autoreconf for aarch64 support (rhbz#925768)
- Make build honor RPM_OPT_FLAGS

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 13 2010 Todd Zullinger <tmz@pobox.com> - 0.15.1b-10
- Rebuild to ensure n-v-r is greater than F-12 branch
- Fix Source0 URL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Todd Zullinger <tmz@pobox.com> - 0.15.1b-7
- Fix %%patch incantation for new rpm

* Fri May 09 2008 Todd Zullinger <tmz@pobox.com> - 0.15.1b-6
- fix for CVE-2008-2109 (#445812)

* Tue Feb 12 2008 Todd Zullinger <tmz@pobox.com> - 0.15.1b-5
- rebuild for gcc 4.3

* Mon Aug  6 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1b-4
- License: GPLv2+

* Mon Aug 28 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1b-3
- Rebuild.

* Mon Feb 13 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1b-2
- Rebuild.

* Wed Nov  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1b-1
- Don't ship static libraries.
- Embed *.pc in specfile to keep it in sync with the build.
- Build with dependency tracking disabled.

* Thu May 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.15.1-3.b
- Rebuild.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.15.1-2.b
- rebuilt

* Wed Feb 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.15.1-0.fdr.1.b
- Update to 0.15.1b.

* Wed Oct 29 2003 Ville Skytta <ville.skytta at iki.fi> - 0:0.15.0-0.fdr.2.b
- Rebuild.

* Sun Sep 28 2003 Dams <anvil[AT]livna.org> 0:0.15.0-0.fdr.1.b.0.94
- Remove comment after scriptlets

* Mon Jun 30 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.15.0-0.fdr.1.b
- Update to 0.15.0b.
- Split separate from the old mad package to follow upstream.
- -devel requires zlib-devel and pkgconfig.

* Thu Apr 24 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.14.2-0.fdr.3.b
- Fix missing "main" package dependencies in *-devel.
- Include patch from Debian, possibly fixes #187 comment 7, and adds
  pkgconfig files for libraries.

* Sun Apr 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.14.2-0.fdr.2.b
- Split into mad, libmad, -devel, libid3tag and -devel packages (#187).
- Provide mp3-cmdline virtual package and alternative.
- Build shared library.

* Fri Apr  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.14.2-0.fdr.1.b
- Update to current Fedora guidelines.
- Exclude %%{_libdir}/*.la.

* Thu Feb 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.14.2b-1.fedora.1
- First Fedora release, based on Matthias Saou's work.

* Fri Sep 27 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuild for Red Hat Linux 8.0 (missing because of license issues).
- Spec file cleanup.

* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com> 0.14.2b-3
- ship libid3tag too

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Mon Jan 28 2002 Bill Nottingham <notting@redhat.com>
- split libmad off into a separate package
