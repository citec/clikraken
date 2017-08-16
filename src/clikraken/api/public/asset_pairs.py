# -*- coding: utf8 -*-

"""
clikraken.api.public.asset_pairs

This module queries the AssetPairs method of Kraken's API
and outputs the results in a tabular format.

Licensed under the Apache License, Version 2.0. See the LICENSE file.
"""

from clikraken.api.api_utils import query_api
from clikraken.clikraken_utils import _tabulate as tabulate
from clikraken.clikraken_utils import csv


def asset_pairs(args):
    """Get available asset pairs."""

    # Parameters to pass to the API
    api_params = {}

    res = query_api('public', 'AssetPairs', api_params, args)

    # initialize a list to store the parsed assets pairs
    assetlist = []

    for assetpair in res:
        if assetpair.endswith('.d'):
            continue
        assetlist.append([assetpair,
                          res[assetpair]['altname'],
                          res[assetpair]['base'],
                          res[assetpair]['quote']])

    if args.csv:
        assetlist = [{
            'Pair': o[0],
            'Alt Name': o[1],
            'Base': o[2],
            'Quote': o[3],
        } for o in assetlist]
        print(csv(assetlist, headers="keys"))
    else:
        print(tabulate(assetlist, headers=['Pair', 'Alt Name', 'Base', 'Quote']))
        print('--- Total: {} pairs'.format(len(assetlist)))
