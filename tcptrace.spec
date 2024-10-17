Name:		tcptrace
Version:	6.6.7
Release:	7
Summary:	Tool for analysis of TCP dump files
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
URL:		https://jarok.cs.ohiou.edu/software/tcptrace/tcptrace.html
Source:		http://jarok.cs.ohiou.edu/software/tcptrace/download/%{name}-%{version}.tar.gz
BuildRequires:	libpcap-devel
%description
tcptrace is a tool written by Shawn Ostermann at Ohio University, for
analysis of TCP dump files. It can take as input the files produced by
several popular packet-capture programs, including tcpdump, snoop,
etherpeek, HP Net Metrix, and WinDump. tcptrace can produce several
different types of output containing information on each connection seen,
such as elapsed time, bytes and segments sent and received, retransmissions,
round trip times, window advertisements, throughput, and more. It can
also produce a number of graphs for further analysis.

%prep
%setup -q

%build
%configure
%make

%install
%{__rm} -Rf %{buildroot}
export CHOWNPROG='echo "**** chown "'
export CHGRPPROG='echo "**** chgrp "'
%makeinstall MANDIR=%{buildroot}%{_mandir} BINDIR=%{buildroot}%{_bindir}

%files
%doc ARGS CHANGES COPYING COPYRIGHT FAQ INSTALL README WWW THANKS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*



%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 6.6.7-6mdv2010.0
+ Revision: 445384
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 6.6.7-5mdv2009.1
+ Revision: 298411
- rebuilt against libpcap-1.0.0

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 6.6.7-4mdv2009.0
+ Revision: 261436
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 6.6.7-3mdv2009.0
+ Revision: 254265
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tvignaud@mandriva.com> 6.6.7-1mdv2008.1
+ Revision: 168289
- fix no-buildroot-tag

* Tue Aug 14 2007 Nicolas Vigier <nvigier@mandriva.com> 6.6.7-1mdv2008.0
+ Revision: 63307
- Import tcptrace

