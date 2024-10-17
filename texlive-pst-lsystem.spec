Name:		texlive-pst-lsystem
Version:	49556
Release:	2
Summary:	Create images based on a L-system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pst-lsystem
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lsystem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lsystem.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-lsystem is a PSTricks based package for creating images
based on a L-system. A L-system (Lindenmayer system) is a set
of rules which can be used to model the morphology of a variety
of organisms or fractals like the Kochflake or Hilbert curve.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-lsystem
%{_texmfdistdir}/tex/generic/pst-lsystem
%{_texmfdistdir}/dvips/pst-lsystem
%doc %{_texmfdistdir}/doc/generic/pst-lsystem

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
