This plugin enables you to modify docstring of tests based on their attributes.

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

========
Features
========

* Works with multiprocess plugin:

.. code-block:: shell

    nosetest --processes=10 -- process-restartworker with-docstring-modifier --prefix=id

spreads test run among 10 processes, appending `id` attribute to each test.

=======
History
=======

0.0.4 (2014-11-06)
------------------
* Code design changes

0.0.3 (2014-11-05)
------------------
* Multiprocessing support

0.0.2 (2014-11-04)
------------------
* Initial release