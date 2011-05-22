PyRuby - Some Ruby for your Python!
===================================

PyRuby is a simple way to leverage the power of Ruby to make your Python code
more readable and beautiful.

Please note that PyRuby is still in early stage of development. **Use it at your
own risk.**


Features
--------

* Full Ruby 1.9 compatibility
* Pure Python, no native libraries required
* Small footprint


Installation
------------

The easiest way to download and install PyRuby is via `PyPI`_::

    $ pip install pyruby

Follow `these instructions <http://www.pip-installer.org/en/latest/installing.html>`_
to install `Pip`_ if you don't have it already.


Usage
-----

All you have to do is import the ``ruby`` module::

    import ruby

From now on you should be able to write Ruby code within a regular Python
module. An example::

    1.upto(10) { |n| puts n }


Mixing Python and Ruby code in the same module
``````````````````````````````````````````````

After importing the ``ruby`` module you might want to restore the default
behavior.

To do that, just import the ``python`` module and you're done::

    import ruby

    def ruby_add(a, b)
      a + b
    end

    import python

    def python_add(a, b):
      return ruby_add(a, b)

    print python_add(3, 4) // -> 7

As you could see, it's even possible to seamlessly call Ruby code from Python
and vice-versa.


.. _Ruby: http://ruby-lang.org
.. _PyPI: http://pypi.python.org/pypi
.. _Pip: http://www.pip-installer.org
