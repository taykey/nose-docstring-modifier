__author__ = 'maroun'


import os

from nose.plugins import Plugin


class DocString(Plugin):

    def describeTest(self, test):
        return '{0} # {1}'.format(test.test.__dict__['test'].keywords['id'],
        test.test.__dict__['test'].__doc__)


    def options(self, parser, env=os.environ):
        super(DocString, self).options(parser, env)

        parser.add_option(
            '--prefix', default='id',
            help='Append to this flag list of attributes you want to be printed'
                 'before the original docstring')
        parser.add_option(
            '--suffix', default=None,
            help='Append to this flag list of attributes you want to be printed'
                 'after the original docstring')

    def configure(self, options, conf):
        super(DocString, self).configure(options, conf)
        # TODO: parse options
        pass
