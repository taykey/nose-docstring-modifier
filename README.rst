This plugin enables you to modify docstring of tests based on their attributes, the project is available on `GitHub <https://github.com/taykey/nose-docstring>`_.

==========
Installing
==========

You can install `nose-docstring-modifier` plugin using pip:

.. code-block:: shell

    $ pip install nose-docstring-modifier

=====
Using
=====

Given the following test function:

.. code-block:: python

    @attr(section='MySection', type='functional+', module='MyModule', id=1)
    def test_function(self):
        """
        This is the original docstring
        """
        ok_(True)

running it with nosetest using nose-docstring-modifier plugin:

.. code-block:: shell

    nosetest --with-docstring-modifier --prefix=id,section --suffix=type --replace=s,S

will print

.. code-block:: shell

    (1, MySection) ThiS iS the original docString (functional+) ... ok
