"""Contains the necessary tools to generate a dataset."""

import argparse
from dataclasses import dataclass
import pathlib
import numpy as np

EARTH_GRAVITY = 1.0  # [a.u.]
"""Acceleration on earth due to gravity."""
# ↑ for simplicity we use arbitrary units every where - how to restore SI units?


@dataclass(frozen=True)
# ↑ this is the `dataclass` decorator, whose documentation can be found
# here: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass .
# Data class are a convenient way to define a class, which mainly
# just holds some attributes.
class Hill:
    """The hill from which the jumpers fly off.

    .. code::
            ^
            --------------> x
            |
            |     <- offset
            |\
            | \
            |  \
    """

    offset: float
    """Vertical offset of slope - should be negative."""
    slope: float
    """Slope of the hill - should be negative."""

    def y(self, x: float) -> float:
        """Returns shape of the hill."""
        return self.offset + self.slope * x


HILL = Hill(offset=-2.0, slope=-1.0)
"""The present hill."""


@dataclass(frozen=True)
class SkiJump:
    """The true jumping trajectory."""

    v0: float
    """Initial velocity."""
    alpha: float
    """Initial angle."""

    def y(self, x: float) -> float:
        """Return the trajectory."""
        # Work here in Step 1!
        raise NotImplementedError()

    @classmethod
    # ↑ this is the `classmethod` decorator, whose documentation can be found
    # here: https://docs.python.org/3/library/functions.html#classmethod .
    # Class methods can be often used as alternative constructors, as the `cls` argument here points
    # to the class (in this case `SkiJump`) itself.
    def from_json_file(cls, path: pathlib.Path):
        """Read configuration from JSON file."""
        # Work here in Step 1!
        raise NotImplementedError()

    def landing(self, hill: Hill) -> float:
        """Returns the intersection of the trajectory and the hill."""
        # Work here in Step 1!
        raise NotImplementedError()

    def sample(self, hill: Hill, n: int) -> tuple[np.ndarray, np.ndarray]:
        """Discretize trajectory with `n` points until the landing.

        Parameters
        ----------
            hill :
                Jumping location
            n :
                number of points

        Returns
        -------
            xs :
                x points
            ys :
                y points
        """
        # Work here in Step 3!
        # 1. Compute the landing point
        # 2. Generate `n` equally space x points between the landing point and 0. using
        #    [`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy-linspace)
        xs = np.array([])
        # 3. Compute the trajectory for each x point
        ys = np.array([])
        return xs, ys


if __name__ == "__main__":
    # Python provides the argparse library to provide simple command line interfaces.
    # The official tutorial can be found here: https://docs.python.org/3/howto/argparse.html#argparse-tutorial
    # To see it in action just execute this file: `$ python src/generate.py -h` (the `-h` opens immediately the help page)
    parser = argparse.ArgumentParser(
        description="Generate data files from a given configuration."
    )
    parser.add_argument(
        "input", help="Jumping configuration file - should end in .json"
    )
    parser.add_argument("output", help="Target file for output - should end in .txt")
    parser.add_argument("-n", type=int, default=10, help="Number of points")
    args = parser.parse_args()
    # 1. Read the configuration
    my_obj = SkiJump.from_json_file(args.input)
    # 2. Sample
    my_xs, my_ys = my_obj.sample(HILL, args.n)
    # 3. Dump the x points and the y points into the file `args.output` using
    #    [`numpy.savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy-savetxt).
    #    Make x the first column and y the second column.
