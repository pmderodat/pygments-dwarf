#! /usr/bin/env python

from setuptools import setup

setup(
    name = 'pygments-dwarf',
    version = '0.1',
    py_modules = ['pygments_dwarf'],

    install_requires = ['pygments'],

    entry_points = {
        'pygments.lexers': 'dwarflexer = pygments_dwarf:DWARFLexer',
    },

    author = 'Pierre-Marie de Rodat',
    author_email = 'pmderodat@kawie.fr',
    description = 'Pygments lexer for objdump\'s DWARF DIEs output',
    keywords = 'pygments dwarf objdump',
)
