#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) 2016 Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2016-07-9
#

"""
"""

from __future__ import print_function, unicode_literals, absolute_import


import sys

from ualfred import Workflow

log = None


def main(wf):
    """Do nothing."""
    log.debug('datadir=%r', wf.datadir)


if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
