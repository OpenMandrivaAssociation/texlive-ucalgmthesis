Name:		texlive-ucalgmthesis
Version:	52527
Release:	1
Summary:	LaTeX thesis class for University of Calgary Faculty of Graduate Studies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucalgmthesis
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucalgmthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucalgmthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ucalgmthesis.cls is a LaTeX class file that produces documents
according to the thesis guidelines of the University of Calgary
Faculty of Graduate Studies. It uses the memoir class, which
provides very powerful and flexible mechanisms for book design
and layout. All memoir commands for changing chapter and
section headings, page layout, fancy foot- and endnotes,
typesetting poems, etc., can be used. (Memoir is meant as a
replacement for the standard LaTeX classes, so all standard
LaTeX commands such as \chapter, \section, etc., still work.)
Likewise, any of memoir's class options can be passed as
options to ucalgmthesis, in particular 12pt to select 12 point
type (11 point is the default).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ucalgmthesis
%doc %{_texmfdistdir}/doc/latex/ucalgmthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
