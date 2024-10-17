Name:		texlive-luainputenc
Version:	20491
Release:	2
Summary:	Replacing inputenc for use in LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luainputenc
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luainputenc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luainputenc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luainputenc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LuaTeX operates by default in UTF-8 input; thus LaTeX documents
that need 8-bit character-sets need special treatment. (In
fact, LaTeX documents using UTF-8 with "traditional" -- 256-
glyph -- fonts also need support from this package.) The
package, therefore, replaces the LaTeX standard inputenc for
use under LuaTeX. With a current LuaTeX,the package has the
same behaviour with LuaTeX as inputenc has under pdfTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/luainputenc/luainputenc.lua
%{_texmfdistdir}/tex/lualatex/luainputenc/luainputenc.sty
%{_texmfdistdir}/tex/lualatex/luainputenc/lutf8.def
%{_texmfdistdir}/tex/lualatex/luainputenc/lutf8x.def
%doc %{_texmfdistdir}/doc/lualatex/luainputenc/NEWS
%doc %{_texmfdistdir}/doc/lualatex/luainputenc/README
%doc %{_texmfdistdir}/doc/lualatex/luainputenc/inputenc.sty.diff
%doc %{_texmfdistdir}/doc/lualatex/luainputenc/luainputenc.pdf
%doc %{_texmfdistdir}/doc/lualatex/luainputenc/test.tex
#- source
%doc %{_texmfdistdir}/source/lualatex/luainputenc/Makefile
%doc %{_texmfdistdir}/source/lualatex/luainputenc/luainputenc.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
