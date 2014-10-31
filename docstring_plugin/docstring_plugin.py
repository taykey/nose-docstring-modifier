__author__ = 'maroun'


import os

from nose.plugins import Plugin


class DocString(Plugin):
    """
    This plugin enables you to display attributes next to the original
    docstring.

    Usage example:
         > python main.py --with-docstring --prefix=platform,id --suffix=type
    """

    args = dict()

    def describeTest(self, running_test):
        prefix_info = list()
        suffix_info = list()

        keywords = running_test.test.__dict__['test'].keywords

        for prefix in self.args['prefix']:
            self.prefix_info.append(keywords.get(prefix, ''))

        # remove empty strings resulted from unexusting keys
        self.prefix_info = filter(len, map(str, self.prefix_info))
        prefix = ', '.join(self.prefix_info)

        for suffix in self.args['suffix']:
            suffix_info.append(keywords.get(suffix, ''))

        suffix_info = filter(len, map(str, suffix_info))
        suffix = ', '.join(suffix_info)

        # prevent list mutation
        self.prefix_info = list()
        self.suffix_info = list()

        return '({}) {} ({})'.format(prefix,
                                     running_test.test.__dict__['test'].__doc__,
                                     suffix)

    def options(self, parser, env=os.environ):
        super(DocString, self).options(parser, env)

        parser.add_option(
            '--prefix', default='id,platform',
            help='Append to this flag list of attributes you want to be printed'
                 'before the original docstring, separated by COMMA')
        parser.add_option(
            '--suffix', default='section,type,module',
            help='Append to this flag list of attributes you want to be printed'
                 'after the original docstring, separated by COMMA')
        parser.add_option(
            '--replace',
            help='Replace characters in original docstring, for example:'
                 '--replace(a, A)'
        )

    def configure(self, options, conf):
        super(DocString, self).configure(options, conf)

        self.args['prefix'] = options.prefix.split(',')
        self.args['suffix'] = options.suffix.split(',')