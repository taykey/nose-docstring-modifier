__author__ = 'maroun'

from nose.tools import ok_
from nose.plugins.attrib import attr
from nose import runmodule


class TestSet(object):

    @attr(section='my_section', type='UI', module='my_module', id=1)
    def test_first_function(self):
        """
        This is the original docstring
        """
        pass


class TestDocstringModifier(object):
    @attr(id=1)
    def test_affix(self):
        """
        This is the original docstring
        """
        nose_run_args = '-v -s -d  --with-docstring-modifier --prefix=id'
        runmodule(argv=nose_run_args)
