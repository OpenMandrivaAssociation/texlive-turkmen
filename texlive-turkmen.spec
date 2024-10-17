Name:		texlive-turkmen
Version:	17748
Release:	2
Summary:	Babel support for Turkmen
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/turkmen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turkmen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turkmen.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turkmen.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for Turkmen in babel, but
integration with babel is not available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/turkmen/turkmen.ldf
%doc %{_texmfdistdir}/doc/latex/turkmen/README
%doc %{_texmfdistdir}/doc/latex/turkmen/turkmen.pdf
#- source
%doc %{_texmfdistdir}/source/latex/turkmen/turkmen.dtx
%doc %{_texmfdistdir}/source/latex/turkmen/turkmen.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
