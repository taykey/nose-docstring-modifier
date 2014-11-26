__author__ = 'maroun'


import os
import io

import nose_docstring_modifier.nose_docstring_modifier

from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

requires = [
    'nose',
]


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst', 'CHANGES.txt')

setup(name='nose-docstring-modifier',
      version=nose_docstring_modifier.__version__,
      description='Enables you to modify docstring of tests based on '
                  'their attributes',
      long_description=long_description,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing",
          "License :: OSI Approved :: Apache Software License",
      ],
      author='Maroun Maroun',
      author_email='maroun@taykey.com',
      url='https://github.com/taykey/nose-docstring-modifier',
      packages=find_packages(),
      keywords='nosetest docstring',
      include_package_data=True,
      zip_safe=False,
      entry_points={
        'nose.plugins.0.10': [
            'nose_docstring_modifier = nose_docstring_modifier:DocstringModifier'
            ]
        },
      install_requires=requires)