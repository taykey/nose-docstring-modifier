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

        prefix = self._get_affix(self.args.get('prefix', None), test)
        suffix = self._get_affix(self.args.get('suffix', None), test)

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

    @staticmethod
    def _get_affix(keywords, running_test):
        """
        Returns list containing affixes that will be appended to docstring.

        :param keywords: list of affix keywords
        :type keywords: list
        :param running_test: contains meta information about the current test
        :return: a list containing wanted affixes depending on 'affix_type'
        """
        if not keywords:
            return ''

        affix = [str(running_test.keywords.get(key, '')) for key in keywords]
        return '(' + ', '.join(filter(len, affix)) + ')'

    def _get_docstring(self, running_test):
        """
        Returns modified docstring if --replace is toggled, original otherwise.

        :return: modified docstring
        """
        docstring = running_test.__doc__
        replace_args = self.args.get('replace', '')

        if len(replace_args) == 2:
            return docstring.replace(replace_args[0], replace_args[1])

        return docstring