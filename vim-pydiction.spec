Summary:	Dictionary file of Python modules for use with vim's completion
Summary(pl.UTF-8):	Plik słownikowy modułów Pythona do użycia z dopełnianiem identyfikatorów vima
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
Requires:	vim-rt >= 6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pydiction is a special dictionary file of Python modules for use with
vim's completion feature. pydiction.py is a program that generates the
pydiction file and you can use it to add your project's own modules to
it.

%description -l pl.UTF-8
pydiction jest specjalizowanym plikiem słownika modułów Pythona do
użycia z funkcjonalnością dopełniania identyfikatorów w vimie.
pydiction.py jest programem służącym do generowania pliku słownika
pydiction, umożliwiającym dodawanie do słownika własnych modułów.

%prep
%setup -q -n pydiction-%{version}

mv pydiction.py pydiction.py.dos
sed 's/
//' < pydiction.py.dos > pydiction.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pydiction}

install pydiction.py	$RPM_BUILD_ROOT%{_bindir}
install pydiction	$RPM_BUILD_ROOT%{_datadir}/pydiction

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE.txt
%attr(755,root,root) %{_bindir}/pydiction.py
%{_datadir}/pydiction
