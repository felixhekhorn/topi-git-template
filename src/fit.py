"""Contains the necessary tools to fit a dataset."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Step 1: Determine the starting velocity and starting angle of the test dataset `data/A-test.txt`.

## 1. Load data file using https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy-loadtxt .
##    The first column corresponds to the abscissa x and the second column to the ordinate y.

## 2. Define the model: Look to the example on SciPy (the link below)

## 3. Fit using https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html#curve-fit

## 4. Calculate the initial velocity and initial angle from the model parameter.
##    (Yes, this is a math exercise ;-) )

# Step 2: Plot the data and your fit into one diagram.

## The most popular library for making plots is matplotlib:
## Homepage: https://matplotlib.org/
## A Quick start example can be found here: https://matplotlib.org/stable/users/explain/quick_start.html
## A list with tutorials can be found here: https://matplotlib.org/stable/tutorials/index.html
## - Save the final plot in the `plots/` directory as `.pdf`
## - Note it is often convenient to not commit generated files to repositories, but their recipe instead!
##   (That is why there is a `.gitignore` file in the folder.)
