#!/usr/bin/env python3

import numpy as np
from mpl_plot import *


breakpoints  = np.array([  1, 46,  86, 116, 136, 151])
coefficients = np.array([1.4, 2., 2.5,  3., 3.5,  4.])


def equivalent_crit_damage(strength_raw):
  strength = strength_raw[:, np.newaxis]
  # Internal crit rolls create a 100-point range which, when adjusted by crit
  # strength, falls across one or more bins on the coefficient table. Our goal
  # is simply to compute the fraction of probability mass that lands in each
  # bin, then use that as a weight for the crit damage coefficients, giving a
  # simplified "crit damage equivalent", which is just the expected critical
  # damage value.
  probability_offset = np.clip(breakpoints - strength - 1, 0, 100.)
  #print(probability_offset)
  #print('---')
  probability_offset_extended = np.concatenate(
    (probability_offset,
     np.broadcast_to(100., (probability_offset.shape[0],1))),
    axis=1)
  #print(probability_offset_extended)
  #print('---')
  probability_mass = np.diff(probability_offset_extended)/100.
  #print(probability_mass)
  #print('---')
  # Probability mass should always sum to one.
  #print(np.sum(probability_mass, axis=1))
  assert(np.all((np.sum(probability_mass, axis=1)-1.0)<0.01))

  probability_weighted_crit_damage = probability_mass * coefficients
  #print(probability_weighted_crit_damage)
  #print('---')

  return np.sum(probability_weighted_crit_damage, axis=1)

#print(equivalent_crit_damage(np.arange(0,120,10)))


def plot_it():
  xs = np.arange(0,120) # caps at 105, but let's visually see the plateau
  ys = equivalent_crit_damage(xs)*100
  (fig,ax) = plt.subplots()
  ax.plot(xs, ys)
  ax.grid(True)
  ax.set_xlabel('Critical Strength')
  ax.set_xlim(0,120)
  ax.set_ylabel('Average Equivalent Critical Damage %')
  fig.tight_layout()
  fig.savefig('Equivalent_crit_damage.png')

  zs = np.diff(ys)
  (fig,ax) = plt.subplots()
  ax.plot(xs[:-1], zs)
  ax.grid(True)
  ax.set_xlabel('Critical Strength')
  ax.set_xlim(0,120)
  ax.set_ylabel('Critical Damage % per Point of Critical Strength')
  fig.tight_layout()
  fig.savefig('Critical_damage_per_strength.png')

plot_it()
