__author__ = 'maroun'


import os

from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(ROOT, 'README.md')).read()

requires = [
    'nose',
]

setup(name='docstring-affix',
      version='0.0.2',
      description='Enables you to modify docstring of tests based on '
                  'their attributes',
      long_description=README,
      classifiers=[
          "Development Status :: 0 - Beta",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing",
      ],
      author='Maroun Maroun',
      author_email='maroun@taykey.com',
      url='',
      packages=find_packages(),
      keywords='nosetest docstring',
      include_package_data=True,
      zip_safe=False,
      entry_points="""\
      [nose.plugins.0.10]
      docstring-affix = nose_docstring_affix:DocstringAffix
      """,
      install_requires=requires)