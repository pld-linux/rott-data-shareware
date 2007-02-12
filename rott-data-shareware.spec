#
# _with_local	- local build, without DOS files (non-distributable)
#
Summary:	Rise of the Triad - shareware, one-episode version of data
Summary(pl.UTF-8):   Rise of the Triad - sharewarowa wersja danych, zawierająca jeden epizod
Name:		rott-data-shareware
Version:	1.3
Release:	1
%if 0%{?_with_local:1}
License:	non-distributable, free use
%else
License:	non-commercially distributable if complete, unmodified and not bundled on CD etc.
%endif
Group:		Applications/Games
Source0:	http://filesingularity.timedoctor.org/swdata.zip
# Source0-md5:	0150bf731e703cc91b8c5e21cb9402f3
URL:		http://www.3drealms.com/rott/
BuildRequires:	unzip
Requires:	rott(SHAREWARE)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rise of the Triad - shareware, one-episode version of data.

%description -l pl.UTF-8
Rise of the Triad - sharewarowa wersja danych, zawierająca jeden
epizod.

%prep
%setup -qc
unzip -L ROTTSW13.SHR

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/rott

install *.dmo *.r* *.wad $RPM_BUILD_ROOT%{_datadir}/rott
%{!?_with_local:install *.pck [a-z]*.exe $RPM_BUILD_ROOT%{_datadir}/rott}

mv -f FILE_ID.DIZ file_id.diz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc file_id.diz order.frm vendor.doc
%{_datadir}/rott
