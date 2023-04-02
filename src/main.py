# SPDX-License-Identifier: GPL-3.0-only

import sys

from .application import TelegraphApplication


def main(version):
    """The application's entry point."""
    app = TelegraphApplication()
    return app.run(sys.argv)
