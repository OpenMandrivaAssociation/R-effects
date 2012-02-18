%define modulename effects
%define realver 2.0-10
%define r_library %{_libdir}/R/library

Summary:	Effects Displays for R
Name:		R-cran-%{modulename}
Version:	%(echo %{realver} | tr '-' '.')
Release:	%mkrel 2
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	R-cran-colorspace
Requires:	R-base
Requires:	R-cran-colorspace
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This R package provides graphical and tabular effect displays, e.g., 
of interactions, for linear generalized linear, multinomial-logit, 
and proportional-odds logit models.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
