#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that allow to rename DCC nodes in an easy way
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe
from artellapipe.libs.naming.core import naminglib

from tpRenamer.core import renamer


class ArtellaRenamer(artellapipe.Tool, object):

    def __init__(self, project, config):
        super(ArtellaRenamer, self).__init__(project=project, config=config)

    def ui(self):
        super(ArtellaRenamer, self).ui()

        self._renamer_widget = ArtellaRenamerWidget()
        self.main_layout.addWidget(self._renamer_widget)


class ArtellaRenamerWidget(renamer.RenamerWidget, object):

    NAMING_LIB = naminglib.ArtellaNameLib

    def __init__(self, config=None, parent=None):
        super(ArtellaRenamerWidget, self).__init__(config=config, parent=parent)

        self.auto_rename_widget.edit_btn.setVisible(False)