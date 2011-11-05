# revision 17748
# category Package
# catalog-ctan /language/turkmen
# catalog-date 2010-04-06 13:44:40 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-turkmen
Version:	0.2
Release:	1
Summary:	Babel support for Turkmen
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/turkmen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turkmen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turkmen.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turkmen.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides support for Turkmen in babel, but
integration with babel is not available.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/turkmen/turkmen.ldf
%doc %{_texmfdistdir}/doc/latex/turkmen/README
%doc %{_texmfdistdir}/doc/latex/turkmen/turkmen.pdf
#- source
%doc %{_texmfdistdir}/source/latex/turkmen/turkmen.dtx
%doc %{_texmfdistdir}/source/latex/turkmen/turkmen.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
