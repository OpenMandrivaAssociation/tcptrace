Name:		tcptrace
Version:	6.6.7
Release:	%mkrel 6
Summary:	Tool for analysis of TCP dump files
Group:		Monitoring
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
URL:		http://jarok.cs.ohiou.edu/software/tcptrace/tcptrace.html
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

