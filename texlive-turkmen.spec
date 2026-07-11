%global tl_name turkmen
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Babel support for Turkmen
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/turkmen
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turkmen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turkmen.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turkmen.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for Turkmen in babel, but integration with
babel is not available.

