Summary:	Dictionary file of Python modules for use with vim's completion
Summary(pl):	Plik s³ownikowy modu³ów Pythona do u¿ycia z dope³nianiem identyfikatorów vima
Name:		vim-pydiction
Version:	0.5
Release:	2
License:	GPL v2
Group:		Development/Tools
# renamed from http://www.vim.org/scripts/download_script.php?src_id=2668
Source0:	pydiction-0.5.tar.gz
# Source0-md5:	f7189a21c88d2dd9fbdd2a2a7dd2b981
URL:		http://www.vim.org/scripts/script.php?script_id=850
%pyrequires_eq	python
%pyrequires_eq	python-modules
Requires:	python-numpy
Requires:	vim >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
pydiction is a special dictionary file of Python modules for use with
vim's completion feature. pydiction.py is a program that generates the
pydiction file and you can use it to add your project's own modules to
it.

%description -l pl
pydiction jest specjalizowanym plikiem s³ownika modu³ów Pythona do
u¿ycia z funkcjonalno¶ci± dope³niania identyfikatorów w vimie.
pydiction.py jest programem s³u¿±cym do generowania pliku s³ownika
pydiction, umo¿liwiaj±cym dodawanie do s³ownika w³asnych modu³ów.

%prep
%setup -q -n pydiction-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pydiction}

mv pydiction.py pydiction.py.dos
sed 's/
//' < pydiction.py.dos > pydiction.py

install pydiction.py	$RPM_BUILD_ROOT%{_bindir}
install pydiction	$RPM_BUILD_ROOT%{_datadir}/pydiction

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE.txt
%attr(755,root,root) %{_bindir}/pydiction.py
%{_datadir}/pydiction
