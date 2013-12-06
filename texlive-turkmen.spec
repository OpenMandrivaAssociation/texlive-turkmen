# revision 17748
# category Package
# catalog-ctan /language/turkmen
# catalog-date 2010-04-06 13:44:40 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-turkmen
Version:	0.2
Release:	6
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 757157
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719816
- texlive-turkmen
- texlive-turkmen
- texlive-turkmen

