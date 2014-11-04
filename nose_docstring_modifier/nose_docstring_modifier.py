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
    args = dict()

    def describeTest(self, running_test):

        # meta information about running test
        test = running_test.test.__dict__.get('test', None)
        if not test:
            return

        prefix = self._get_affix('prefix', test)
        suffix = self._get_affix('suffix', test)

        docstring = self._get_docstring(test)

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
            help='Replace characters in original docstring, for example:'
                 '--replace=a,A'
        )

    def configure(self, options, conf):
        super(DocstringModifier, self).configure(options, conf)

        if options.prefix:
            self.args['prefix'] = options.prefix.split(',')
        if options.suffix:
            self.args['suffix'] = options.suffix.split(',')
        if options.replace:
            self.args['replace'] = options.replace.split(',')

    def _get_affix(self, affix_type, running_test):
        """
        Returns list containing affixes that will be appended to docstring.
        :param affix_type: 'suffix' or 'prefix'
        :type affix_type: str
        :param running_test: contains meta information about the current test
        :return: a list containing wanted affixes depending on 'affix_type'
        """
        affix = list()

        if not affix_type in self.args.keys():
            return ''

        for key in self.args[affix_type]:
            affix.append(running_test.keywords.get(key, ''))

        # remove empty strings resulted from unexisting keys
        affix = filter(len, map(str, affix))

        return ', '.join(affix)

    def _get_docstring(self, running_test):
        """
        Returns modified docstring if --replace is toggled, original otherwise.
        :return: modified docstring
        """
        docstring = running_test.__doc__
        if 'replace' in self.args.keys() and len(self.args['replace']) == 2:
            return docstring.replace(self.args['replace'][0],
                                     self.args['replace'][1])
        return docstring