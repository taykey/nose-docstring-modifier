__author__ = 'maroun'
__version__ = '0.0.6'

import os
import re

from nose.plugins import Plugin


class DocstringModifier(Plugin):
    """
    This plugin enables you to display attributes next to the original
    docstring.

    Usage examples:
      > nosetest --with-docstring-modifier --prefix=id,section --suffix=type
      > nosetest --with-docstring-modifier --replace=('a','A') --first-line
    """

    name = 'docstring-modifier'

    def describeTest(self, running_test):

        # meta information about running test
        test = running_test.test.__dict__.get('test', None)
        if not test:
            return

        # get prefixes and suffixes
        prefix_list = self.conf.options.prefix
        suffix_list = self.conf.options.suffix
        prefix = self._get_affix(prefix_list, test)
        suffix = self._get_affix(suffix_list, test)

        # modify docstring if necessary
        docstring = test.__doc__
        if not docstring:
            docstring = str(running_test).split('.')[-1]
        else:
            docstring = self._get_first_line(docstring)
            docstring = self._get_replaced_docstring(docstring)

        return '{} {} {}'.format(prefix, docstring, suffix).strip()

    def options(self, parser, env=os.environ):
        super(DocstringModifier, self).options(parser, env)

        parser.add_option(
            '--prefix',
            help='Append to this flag list of attributes you want to be printed'
                 'before the original docstring, comma separated')
        parser.add_option(
            '--suffix',
            help='Append to this flag list of attributes you want to be printed'
                 'after the original docstring, comma separated')
        parser.add_option(
            '--replace',
            help="Replace characters in original docstring, for example:"
                 "--replace=('a','A')")
        parser.add_option(
            '--first-line', action="store_true",
            help='Prints only the first line of the docstring'
        )

    @staticmethod
    def _get_affix(func_dict, running_test):
        """
        Returns list containing affixes that will be appended to docstring.

        :param func_dict: list of affix keywords
        :type func_dict: list
        :param running_test: contains meta information about the current test
        :return: a list containing wanted affixes depending on 'affix_type'
        """
        if not func_dict:
            return ''

        func_dict = func_dict.split(',')

        affix = [running_test.func_dict.get(key, None) for key in func_dict]
        affix = filter(None, affix)

        if not affix:
            return ''

        return '(' + ', '.join(filter(len, map(str, affix))) + ')'

    def _get_replaced_docstring(self, docstring):
        """
        Returns modified docstring if --replace is enabled, original otherwise.

        :return: modified docstring
        """
        if not self.conf.options.replace:
            return docstring

        pattern = re.compile("^\('(.+)','(.+)\'\)$")
        match = pattern.match(self.conf.options.replace)
        if not match:
            return docstring

        return docstring.replace(match.group(1), match.group(2))

    def _get_first_line(self, docstring):
        """
        Returns first line of the docstring if --first-line is enabled, original
        otherwise.

        :return: first line of docstring
        """
        if self.conf.options.first_line:
            return docstring.split('\n', 1)[0]

        return ' '.join(docstring.split())