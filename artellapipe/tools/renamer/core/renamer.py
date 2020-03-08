#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to rename DCC objects in an easy way
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe

# Defines ID of the tool
TOOL_ID = 'artellapipe-tools-renamer'

# We skip the reloading of this module when launching the tool
no_reload = True


class RenamerTool(artellapipe.Tool, object):
    def __init__(self, *args, **kwargs):
        super(RenamerTool, self).__init__(*args, **kwargs)


class RenamerToolset(artellapipe.Toolset, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(RenamerToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from artellapipe.tools.renamer.widgets import renamer

        renamer_widget = renamer.ArtellaRenamerWidget(
            config=self._config, settings=self._settings, parent=self)
        return [renamer_widget]
