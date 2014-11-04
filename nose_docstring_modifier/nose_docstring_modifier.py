__author__ = 'maroun'


import os

from nose.plugins import Plugin


class DocstringModifier(Plugin):
    """
    This plugin enables you to display attributes next to the original
    docstring.

    Usage examples:
      > python main.py --with-docstring-modifier --prefix=id --suffix=type
      > python main.py --with-docstring-modifier --replace=a,A --suffix=id
    """

    name = 'docstring-modifier'

    def describeTest(self, running_test):

        # meta information about running test
        test = running_test.test.__dict__.get('test', None)
        if not test:
            return

        prefix_kws = self.__dict__.get('prefix', '')
        suffix_kws = self.__dict__.get('suffix', '')

        prefix = self._get_affix(prefix_kws, test)
        suffix = self._get_affix(suffix_kws, test)

        docstring = self._get_docstring(test)

        return '{} {} {}'.format(prefix, docstring, suffix).strip()

    def options(self, parser, env=os.environ):
        super(DocstringModifier, self).options(parser, env)

        def set_attrs(option, opt_str, value, parser):
            setattr(self, option.dest, value.split(','))

        parser.add_option(
            '--prefix',
            help='Append to this flag list of attributes you want to be printed'
                 'before the original docstring, comma separated',
            type=str,
            action='callback',
            callback=set_attrs)
        parser.add_option(
            '--suffix',
            help='Append to this flag list of attributes you want to be printed'
                 'after the original docstring, comma separated',
            type=str,
            action='callback',
            callback=set_attrs)
        parser.add_option(
            '--replace',
            help='Replace characters in original docstring, for example:'
                 '--replace=a,A',
            type=str,
            action='callback',
            callback=set_attrs)

    def _get_affix(self, affix_kws, running_test):
        """
        Returns list containing affixes that will be appended to docstring.
        :param affix_kws: affix_kws
        :type affix_kws: list
        :param running_test: contains meta information about the current test
        :return: a list containing wanted affixes depending on 'affix_type'
        """
        affix = [running_test.keywords.get(key, '') for key in affix_kws]

        # remove empty strings resulted from unexisting keys
        affix = filter(len, map(str, affix))
        affix_str = ', '.join(affix)

        return '(' + affix_str + ')' if affix_str else ''

    def _get_docstring(self, running_test):
        """
        Returns modified docstring if --replace is toggled, original otherwise.
        :return: modified docstring
        """
        docstring = running_test.__doc__
        if hasattr(self, 'replace') and len(self.replace) == 2:
            return docstring.replace(self.replace[0], self.replace[1])

        return docstring