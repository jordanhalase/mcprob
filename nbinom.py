#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom
from matplotlib.ticker import PercentFormatter
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

if __name__ == '__main__':

    # Durability values gathered from
    # https://minecraft.gamepedia.com/Durability

    unbreaking0 = [(32, 'gold', 'Gold'),
                   (59, 'saddlebrown', 'Wood'),
                   (131, 'slategray', 'Stone'),
                   (250, 'deepskyblue', 'Iron')]

    unbreaking1 = [(1561, 'cyan', 'Diamond'),
                   (2031, 'firebrick', 'Netherite')]

    # Probability values gathered from
    # https://minecraft.gamepedia.com/Unbreaking

    probability = [(1/2, ':', 'I'), (1/3, '--', 'II'), (1/4, '-', 'III')]

    x = np.arange(32, 1150)

    fig, (ax0, ax1) = plt.subplots(2, 1)
    fig.set_figwidth(16)
    fig.set_figheight(12)

    for ut in unbreaking0:
        for pt in probability:
            y = 100*nbinom.pmf(x, ut[0], pt[0], loc=ut[0])
            ax0.plot(x, y, color=ut[1], linestyle=pt[1]) #, label=f'{ut[2]} {pt[2]}')

    for ut in unbreaking0:
        ax0.plot(ut[0], 0, marker='d', color=ut[1], markersize=8)

    x = np.arange(1561, 8650)

    for ut in unbreaking1:
        for pt in probability:
            y = 100*nbinom.pmf(x, ut[0], pt[0], loc=ut[0])
            ax1.plot(x, y, color=ut[1], linestyle=pt[1]) #, label=f'{ut[2]} {pt[2]}')

    for ut in unbreaking1:
        ax1.plot(ut[0], 0, marker='d', color=ut[1], markersize=8)

    lines0 = []
    for ut in unbreaking0:
        lines0.append(mpatches.Patch(color=ut[1], label=ut[2]))
    lines0.append(mlines.Line2D([], [], color='black', marker='d', linewidth=0, label='Unenchanted (100%)'))
    for pt in probability:
        lines0.append(mlines.Line2D([], [], color='black', linestyle=pt[1], linewidth=2, label=f'Unbreaking {pt[2]}'))

    lines1 = []
    for ut in unbreaking1:
        lines1.append(mpatches.Patch(color=ut[1], label=ut[2]))

    ax0.legend(handles=lines0, shadow=True, fancybox=True)
    ax1.legend(handles=lines1, shadow=True, fancybox=True)

    ax0.yaxis.set_major_formatter(PercentFormatter())
    ax1.yaxis.set_major_formatter(PercentFormatter())

    fig.text(0.5, 0.04, 'Number of tool uses', ha='center', fontsize=18)
    fig.text(0.04, 0.5, 'Chance of breaking', va='center', fontsize=18, rotation='vertical')

    fig.text(0.5, 0.94, 'Negative Binomial Distributions of Unbreaking Enchantment Levels for Tools in Minecraft', ha='center', fontsize=20, fontweight='bold')

    fig.text(0.96, 0.04, 'Created by Jordan Halase', ha='right', fontweight='light')

    ax1.annotate('Diamond tools always last significantly longer than netherite when\nenchanted to one level higher until netherite at Unbreaking III',
            xy=(8124, 0.26),
            xytext=(7800, 0.64),
            arrowprops=dict(facecolor='black', shrink=0.05),
            xycoords='data',
            horizontalalignment='right')

    ax1.annotate('Diamond III lasts longer than netherite II most of the time\nbut has a ~1 in 5 chance of breaking before netherite II',
            xy=(6244, 0.3),
            xytext=(6244, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            xycoords='data',
            horizontalalignment='center')

    fig.savefig('mc_tool_nbinom.png')
