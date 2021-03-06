# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = ideuy.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import logging
import sys

from ideuy import __version__
from ideuy.vector import filter_by_aoi

__author__ = "Damián Silvani"
__copyright__ = "Damián Silvani"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Filter by AOI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("aoi_vector", help="Path to AOI vector file")
    parser.add_argument("--type",
                        "-t",
                        default="national",
                        choices=["national", "urban"],
                        help="Type of grid")
    parser.add_argument("--output",
                        "-o",
                        required=True,
                        help="Path to output GeoJSON vector file")

    parser.add_argument(
        "--grid-vector",
        default=None,
        help="Path to grid vector file. This overrides --type if specified.")

    parser.add_argument("--version",
                        action="version",
                        version="ideuy {ver}".format(ver=__version__))
    parser.add_argument("-v",
                        "--verbose",
                        dest="loglevel",
                        help="set loglevel to INFO",
                        action="store_const",
                        const=logging.INFO)
    parser.add_argument("-vv",
                        "--very-verbose",
                        dest="loglevel",
                        help="set loglevel to DEBUG",
                        action="store_const",
                        const=logging.DEBUG)

    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel,
                        stream=sys.stdout,
                        format=logformat,
                        datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)

    filter_by_aoi(args.aoi_vector,
                  output=args.output,
                  type_id=args.type,
                  grid_vector=args.grid_vector)


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
