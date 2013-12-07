# revision 20491
# category Package
# catalog-ctan /macros/luatex/latex/luainputenc
# catalog-date 2010-11-19 16:55:42 +0100
# catalog-license pd
# catalog-version 0.973
Name:		texlive-luainputenc
Version:	0.973
Release:	3
Summary:	Replacing inputenc for use in LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luainputenc
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luainputenc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luainputenc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luainputenc.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.973-2
+ Revision: 753583
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.973-1
+ Revision: 718922
- texlive-luainputenc
- texlive-luainputenc
- texlive-luainputenc
- texlive-luainputenc

