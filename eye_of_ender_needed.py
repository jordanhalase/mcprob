#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from scipy.stats import binom

def main():

    # Probability of an eye of ender slot already being filled
    p = 0.1

    # Probability of needing to fill an eye of ender slot ourselves
    q = 1 - p

    # Number of eye of ender slots
    n = 12

    # Slot range (inclusive)
    x = np.arange(6, n + 1)

    # Probability (percentage)
    y = 100*binom.cdf(x, n, q)

    fig, ax = plt.subplots(1, 1)
    bar_color = 'seagreen'
    text_color = 'seagreen'

    ax.bar(x, y, width=0.9, color=bar_color)
    ax.yaxis.set_major_formatter(PercentFormatter())
    plt.ylim(top=110)

    for i, v in enumerate(y):
        ax.text(i + 6, v + 1, f'{v:.1f}%', horizontalalignment='center',
            fontweight='bold', color=text_color)

    plt.title('Eyes of ender needed to complete an end portal')
    ax.set_xlabel('Number of eyes of ender')
    ax.set_ylabel('Probability of being enough')

    fig.text(0.96, 0.04, 'github.com/jordanhalase/mcprob', ha='right',
        fontweight='light', fontsize=8, color='gray')

    fig.savefig('eye_of_ender_needed.png')

if __name__ == '__main__':
    main()