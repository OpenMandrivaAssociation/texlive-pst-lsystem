%global tl_name pst-lsystem
%global tl_revision 49556

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02
Release:	%{tl_revision}.1
Summary:	Create images based on a L-system
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-lsystem
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lsystem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-lsystem.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
pst-lsystem is a PSTricks based package for creating images based on a
L-system. A L-system (Lindenmayer system) is a set of rules which can be
used to model the morphology of a variety of organisms or fractals like
the Kochflake or Hilbert curve.

