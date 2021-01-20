#!/usr/bin/python

from scipy.stats import nbinom

import numpy as np
import matplotlib.pyplot as plt

# Simple simulation for cases where diamond at Unbreaking III break
# before netherite at Unbreaking II
#
# The math involves a simple sum of random variables compared against zero
# but the simulation provides a convenient sanity check.

if __name__ == '__main__':

    trials = 1000000

    # Diamond at Unbreaking III
    rv1 = nbinom.rvs(1561, 1/4, size=trials) + 1561

    # Netherite at Unbreaking II
    rv2 = nbinom.rvs(2031, 1/3, size=trials) + 2031

    c = [0, 0]
    for i in range(trials):
        if rv1[i] < rv2[i]:
            c[0] += 1
        else:
            c[1] += 1

    print(c[0]/(c[0]+c[1]))
