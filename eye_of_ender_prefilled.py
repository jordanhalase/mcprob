#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from scipy.stats import binom

def main():

    # Probability of an eye of ender slot already being filled
    p = 0.1

    # Number of eye of ender slots
    n = 12

    # Slot range (inclusive)
    x = np.arange(0, n//2 + 1)

    # Probability (percentage)
    y = 100*binom.pmf(x, n, p)

    fig, ax = plt.subplots(1, 1)
    bar_color = 'seagreen'
    text_color = 'seagreen'

    ax.bar(x, y, width=0.9, color=bar_color)
    ax.yaxis.set_major_formatter(PercentFormatter())
    plt.ylim(top=42)

    for i, v in enumerate(y):
        ax.text(i, v + 1, f'{v:.03g}%', horizontalalignment='center',
            fontweight='bold', color=text_color)

    plt.title('Eyes of ender already filled in an end portal')
    ax.set_xlabel('Eyes of ender already filled')
    ax.set_ylabel('Probability')

    fig.text(0.96, 0.04, 'github.com/jordanhalase/mcprob', ha='right',
        fontweight='light', fontsize=8, color='gray')

    fig.savefig('eye_of_ender_prefilled')

if __name__ == '__main__':
    main()