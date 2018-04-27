# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2016-2018 by the contributors (see AUTHORS file).
    :license: BSD, see LICENSE.txt for details.
"""

from sphinxcontrib_confluencebuilder_util import ConfluenceTestUtil as _
from sphinxcontrib_confluencebuilder_util import EXT_NAME
import os
import unittest


class TestConfluenceCustomFormatting(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.config = _.prepareConfiguration()
        self.config['extensions'].append('sphinx.ext.todo')
        self.config['todo_include_todos'] = True
        self.config['confluence_fmt_todo'] = \
            ['{note:label=|icon=false}', '{note}']
        test_dir = os.path.dirname(os.path.realpath(__file__))
        dataset = os.path.join(test_dir, 'dataset-custom-formatting')
        self.expected = os.path.join(test_dir, 'expected')

        doc_dir, doctree_dir = _.prepareDirectories('custom-formatting')
        app = _.prepareSphinx(dataset, doc_dir, doctree_dir, self.config)
        app.build(force_all=True)

        self.doc_dir = doc_dir
        self.app = app

    def _assertExpectedWithOutput(self, name):
        _.assertExpectedWithOutput(
            self, 'custom-%s' %name, self.expected, self.doc_dir)

    def test_custom_todo(self):
        self._assertExpectedWithOutput('todo')
