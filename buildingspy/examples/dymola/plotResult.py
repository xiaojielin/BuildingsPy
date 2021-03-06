#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# import from future to make Python2 behave like Python3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
from io import open
# end of from future import


def main():
    ''' Main method that plots the results
    '''
    from buildingspy.io.outputfile import Reader
    import matplotlib.pyplot as plt
    import os

    # Optionally, change fonts to use LaTeX fonts
    # from matplotlib import rc
    # rc('text', usetex=True)
    # rc('font', family='serif')

    # Read results
    ofr1 = Reader(os.path.join("buildingspy", "examples", "dymola",
                               "case1", "PIDHysteresis.mat"), "dymola")
    ofr2 = Reader(os.path.join("buildingspy", "examples", "dymola",
                               "case2", "PIDHysteresis.mat"), "dymola")
    (time1, T1) = ofr1.values("cap.T")
    (time1, y1) = ofr1.values("con.y")
    (time2, T2) = ofr2.values("cap.T")
    (time2, y2) = ofr2.values("con.y")

    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(211)

    ax.plot(time1 / 3600, T1 - 273.15, 'r', label='$T_1$')
    ax.plot(time2 / 3600, T2 - 273.15, 'b', label='$T_2$')
    ax.set_xlabel('time [h]')
    ax.set_ylabel('temperature [$^\circ$C]')
    ax.set_xticks(list(range(25)))
    ax.set_xlim([0, 24])
    ax.legend()
    ax.grid(True)

    ax = fig.add_subplot(212)
    ax.plot(time1 / 3600, y1, 'r', label='$y_1$')
    ax.plot(time2 / 3600, y2, 'b', label='$y_2$')
    ax.set_xlabel('time [h]')
    ax.set_ylabel('y [-]')
    ax.set_xticks(list(range(25)))
    ax.set_xlim([0, 24])
    ax.legend()
    ax.grid(True)

    # Save figure to file
    plt.savefig('plot.pdf')
    plt.savefig('plot.png')

    # To show the plot on the screen, uncomment the line below
    # plt.show()


# Main function
if __name__ == '__main__':
    main()
