# -*- coding: utf-8

from distutils.core import setup

setup(
    name="pyruby",
    version="1.0.0",
    description="Some Ruby for your Python",
    author="Daniel Fernandes Martins",
    author_email="daniel.tritone@gmail.com",
    url="http://github.com/danielfm/pyruby",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Ruby",
        "Topic :: Software Development :: Interpreters"],
    platforms=[
        "Any"],
    license="BSD",

    package_dir={'': 'src'},
    packages=[''],
)
