# -*- coding: utf-8 -*-

"""Command line interface for the bioregistry."""

import click

from .miriam import get_miriam_df
from .obofoundry import get_obofoundry_df
from .ols import get_ols_df
from ..utils import secho

__all__ = [
    'download',
]


@click.command()
def download():
    """Download/update the external entries in the Bioregistry."""
    secho('Downloading MIRIAM')
    get_miriam_df(force_download=True)

    secho('Downloading OBO Foundry')
    get_obofoundry_df(force_download=True)

    secho('Downloading OLS')
    get_ols_df(force_download=True)


if __name__ == '__main__':
    download()
