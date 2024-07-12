"""
Generating and plotting on HC plane.

The class ``HCplots`` is used for plotting the HC plane and
for creating the bases of other plot formats that can be useful for
diagnostics, interpretation, and analysis with PECCARY.
"""

import numpy as np
import matplotlib.pylab as plt

from . import utils

__all__ = ["plotBoundsHC","HCplane"]

def plotBoundsHC(ax, n=5, nsteps=1000, **kwargs):
    """
    Plots region boundary lines on HC plane

    Parameters
    ----------
    ax : Matplotlib axis
        Axis on which to plot empty HC curves
    n : int, optional
        Embedding dimension/pattern length, by default 5
    nsteps : int, optional
        Number of steps to use for generating HC bounding curves,
        by default 1000
    **kwargs : dict, optional
        Style arguments passed to ``matplotlib.pyplot.plot``,
        if none given uses PECCARY defaults
    """
    minH, minC, maxH, maxC = utils.calcHCplane(n=n, nsteps=nsteps) # H and C values for HC min/max curves
    minHVal = utils.HminPer(n=n) # Min. H value for periodic fnct
    maxHVal = utils.HmaxPer(n=n) # Max. H value for periodic fnct
    argMinH_CminCurve = np.argmin(np.abs(minH-minHVal)) # Min. H value argument for H values for min HC curve
    argMinH_CmaxCurve = np.argmin(np.abs(maxH-minHVal)) # Min. H value argument for H values for max HC curve
    argMaxH_CminCurve = np.argmin(np.abs(minH-maxHVal)) # Max. H value argument for H values for min HC curve
    argMaxH_CmaxCurve = np.argmin(np.abs(maxH-maxHVal)) # Max. H value argument for H values for max HC curve

    if 'lw' not in kwargs.keys():
        kwargs['lw'] = 1.
    if 'ls' not in kwargs.keys():
        kwargs['ls'] = '--'
    if 'color' not in kwargs.keys():
        kwargs['color'] = 'k'
    if 'alpha' not in kwargs.keys():
        kwargs['alpha'] = 0.5

    ax.plot(np.array([minHVal,minHVal]), np.array([minC[argMinH_CminCurve], maxC[argMinH_CmaxCurve]]), **kwargs)
    ax.plot(np.array([maxHVal,maxHVal]), np.array([minC[argMaxH_CminCurve], maxC[argMaxH_CmaxCurve]]), **kwargs)
    ax.plot(np.array([minHVal,maxHVal]), np.array([maxC[argMinH_CmaxCurve], maxC[argMaxH_CmaxCurve]]), **kwargs)

def HCplane(H=None, C=None, ax=None, n=5, nsteps=1000, fontsize=12, showAxLabels=True, showBoundaries=True, annotatePlane=False, 
            savePlot=False, savePath='', kwargsFig={'figsize':(8,6)}, kwargsHC={'ls':'-','color':'k','zorder':0}, kwargsBnds={}, kwargsPts={}, annotateFontsize=None):
    """
    Creates a blank HC plane with maximum and minimum curves for the given embedding dimension

    Parameters
    ----------
    ax : Matplotlib axis
        Axis on which to plot empty HC curves
    n : int, optional
        Embedding dimension/pattern length, by default 5
    nsteps : int, optional
        Number of steps to use for generating HC bounding curves,
        by default 1000
    fontsize : integer or float, optional
        Fontsize of axis labels, by default 12
    showAxLabels : bool, optional
        Show pre-defined axis labels, by default True
    showBoundaries : bool, optional
        Show HC plane boundary lines, by default True
    annotatePlane : bool, optional
        Annotate HC plane regions, by default False
    savePlot : bool, optional
        Saves HC plot if set to True, by default False
    savePath : str, optional
        Path to save plot if savePlot set to True, by default ''
        Note: Use only forward slashes in savePath
    kwargsFig : dict, optional
        Style arguments for HC plane figure and axis passed to 
        ``matplotlib.pyplot.subplots``, if none given uses PECCARY defaults
    kwargsHC : dict, optional
        Style arguments for HC plane envelope lines passed to 
        ``matplotlib.pyplot.plot``, if none given uses PECCARY defaults
    kwargsBnds : dict, optional
        Style arguments for region boundary lines passed to 
        ``matplotlib.pyplot.plot``, if none given uses PECCARY defaults
    kwargsPts : dict, optional
        Style arguments for [H,C] values plotted on HC-plane with 
        ``matplotlib.pyplot.scatter``, if none given uses PECCARY defaults
    annotateFontsize : float, optional
        Fontsize for HC plane regions annotations, by default None
    """
    # Calculate HC plane envelope
    Cminx, Cminy, Cmaxx, Cmaxy = utils.calcHCplane(n=n, nsteps=nsteps)

    # Check if an existing axis has been inputted
    # Otherwise, create figure and subplot
    if ax is None:
        fig, ax = plt.subplots(1,1,**kwargsFig)
        returnAx = True
    else:
        returnAx = False

    # Plot HC envelope
    ax.plot(Cminx,Cminy,**kwargsHC)
    ax.plot(Cmaxx,Cmaxy,**kwargsHC)

    # Check whether or not to plot HC plane boundaries
    if showBoundaries:
        plotBoundsHC(ax, **kwargsBnds)
    else:
        pass

    # Check whether or not to include HC plane annotation
    if annotatePlane:
        if annotateFontsize is None:
            annotateFontsize = fontsize
        else:
            pass
        ax.text(0.30,0.27,'periodic',rotation=46., fontdict={'fontsize':annotateFontsize-4, 'color':'grey'})
        ax.text(0.35,0.24,'regular',rotation=35., fontdict={'fontsize':annotateFontsize-1})
        ax.text(0.56,0.36,'complex', fontdict={'fontsize':annotateFontsize-1})
        ax.text(0.76,0.09,'stochastic',rotation=-53., fontdict={'fontsize':annotateFontsize-1})
    else:
        pass

    # Check whether H and C values have been inputted
    # If so, plot them
    if (H is None) or (C is None):
        pass
    else:
        ax.scatter(H, C, **kwargsPts)

    # Check whether to include axis labels
    if showAxLabels:
        ax.set_xlabel(r"Normalized Permutation Entropy, $H$", fontsize=fontsize)
        ax.set_ylabel(r"Statistical Complexity, $C$", fontsize=fontsize)
        ax.tick_params(axis='both', labelsize=fontsize-2)
    else:
        pass
    
    # Check whether to save plot
    if savePlot:
        ax.set(xlim=(0,1.0), ylim=(0,0.45))
        ax.set_xticks(np.arange(0,1.1,0.1))
        ax.set_yticks(np.arange(0,0.45,0.05))
        if savePath.endswith('/'):
            savefile=savePath + 'HCn5_blank'
        else:
            savefile=savePath + '/HCn5_blank'
        plt.savefig(savefile+'.png')
    elif returnAx:
        return fig, ax