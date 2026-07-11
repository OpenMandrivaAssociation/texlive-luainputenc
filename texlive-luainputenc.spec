%global tl_name luainputenc
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.973
Release:	%{tl_revision}.1
Summary:	Replacing inputenc for use in LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luainputenc
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luainputenc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luainputenc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luainputenc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LuaTeX operates by default in UTF-8 input; thus LaTeX documents that
need 8-bit character-sets need special treatment. (In fact, LaTeX
documents using UTF-8 with "traditional" -- 256-glyph -- fonts also need
support from this package.) The package, therefore, replaces the LaTeX
standard inputenc for use under LuaTeX. With a current LuaTeX, the
package has the same behaviour with LuaTeX as inputenc has under pdfTeX.

