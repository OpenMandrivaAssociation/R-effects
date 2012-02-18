%global packname  effects
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.1_0
Release:          1
Summary:          Effect Displays for Linear, Generalized Linear, Multinomial-Logit, Proportional-Odds Logit Models and mixed-effects models
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-0.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-lattice R-grid R-nlme R-MASS R-nnet R-colorspace 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-lattice R-grid R-nlme R-MASS R-nnet R-colorspace
%rename R-cran-effects

%description
Graphical and tabular effect displays, e.g., of interactions, for linear
generalized linear, multinomial-logit, and proportional-odds logit models.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
