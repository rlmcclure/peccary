# PECCARY
PECCARY (Permutation Entropy and statistiCal Complexity Analysis for astRophYsics) 
is a pure-python package for distinguishing between regular, complex, and stochastic
behavior in timeseries. It is based on the work by 
[Bandt & Pompe (2002)](https://ui.adsabs.harvard.edu/#abs/2002PhRvL..88q4102B/abstract), 
[Rosso et al. (2007)](https://ui.adsabs.harvard.edu/#abs/2007PhRvL..99o4102R/abstract), 
and [Weck et al. (2015)](https://ui.adsabs.harvard.edu/#abs/2015PhRvE..91b3101W/abstract).
In addition to calculating the Permutation Entropy ($H$) and Statistical Complexity
($C$) values, this package also has plotting tools for the $HC$-plane and visualizing the 
resulting $[H,C]$ values for various timeseries.

A detailed summary of the PECCARY method can be found in Hyman, Daniel, & Schaffner (in prep). 
If you make use of PECCARY, please include a citation to Hyman, Daniel, & Schaffner (in prep) 
in any publications.