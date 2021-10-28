# -*- coding: utf-8 -*-
#
# User documentation for OpenCOR build configuration file
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'User documentation for OpenCOR'
copyright = u'University of Auckland'
author = u'University of Auckland'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['.']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: https://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'UserdocumentationforOpenCORdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'UserdocumentationforOpenCOR.tex', u'User documentation for OpenCOR',
     u'University of Auckland', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Userdocumentationforopencor', u'User documentation for OpenCOR',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'UserdocumentationforOpenCOR', u'User documentation for OpenCOR',
     author, 'UserdocumentationforOpenCOR', 'User documentation for OpenCOR.',
     'Miscellaneous'),
]

# -- Lexer for the CellML Text format -------------------------------------

from pygments.lexer import RegexLexer, include, words
from pygments.token import Token, STANDARD_TYPES
from sphinx.highlighting import lexers

CellmlText = Token.CellmlText
CellmlTextComment = Token.CellmlTextComment
CellmlTextKeyword = Token.CellmlTextKeyword
CellmlTextCellmlKeyword = Token.CellmlTextCellmlKeyword
CellmlTextNumber = Token.CellmlTextNumber
CellmlTextOperator = Token.CellmlTextOperator
CellmlTextParameterBlock = Token.CellmlTextParameterBlock
CellmlTextParameterCellmlKeyword = Token.CellmlTextParameterCellmlKeyword
CellmlTextParameterKeyword = Token.CellmlTextParameterKeyword
CellmlTextParameterNumber = Token.CellmlTextParameterNumber
CellmlTextParameterSiUnitKeyword = Token.CellmlTextParameterSiUnitKeyword
CellmlTextPunctuation = Token.CellmlTextPunctuation
CellmlTextString = Token.CellmlTextString
CellmlTextSiUnitKeyword = Token.CellmlTextSiUnitKeyword

CELLMLTEXT_TYPES = {
    CellmlText: 'ct',
    CellmlTextComment: 'ctc',
    CellmlTextKeyword: 'ctk',
    CellmlTextCellmlKeyword: 'ctck',
    CellmlTextNumber: 'ctn',
    CellmlTextOperator: 'cto',
    CellmlTextParameterBlock: 'ctpb',
    CellmlTextParameterCellmlKeyword: 'ctpck',
    CellmlTextParameterKeyword: 'ctpk',
    CellmlTextParameterNumber: 'ctpn',
    CellmlTextParameterSiUnitKeyword: 'ctpsuk',
    CellmlTextPunctuation: 'ctp',
    CellmlTextString: 'cts',
    CellmlTextSiUnitKeyword: 'ctsuk'
}

STANDARD_TYPES.update(CELLMLTEXT_TYPES)

class cellmlTextLexer(RegexLexer):
    tokens = {
        'root': [
            # Single and multiline comments

            (r'//(\n|[\w\W]*?[^\\]\n)', CellmlTextComment),
            (r'/(\\\n)?[*][\w\W]*?[*](\\\n)?/', CellmlTextComment),
            (r'/(\\\n)?[*][\w\W]*', CellmlTextComment),

            # Keywords

            (words((
                # CellML Text keywords

                'and', 'as', 'between', 'case', 'comp', 'def', 'endcomp',
                'enddef', 'endsel', 'for', 'group', 'import', 'incl', 'map',
                'model', 'otherwise', 'sel', 'unit', 'using', 'var', 'vars',

                # MathML arithmetic operators

                'abs', 'ceil', 'exp', 'fact', 'floor', 'ln', 'log', 'pow',
                'root', 'sqr', 'sqrt',

                # MathML logical operators

                'and', 'or', 'xor', 'not',

                # MathML calculus elements

                'ode',

                # MathML min/max operators

                'min', 'max',

                # MathML gcd/lcm operators

                'gcd', 'lcm',

                # MathML trigonometric operators

                'sin', 'cos', 'tan', 'sec', 'csc', 'cot',
                'sinh', 'cosh', 'tanh', 'sech', 'csch', 'coth',
                'asin', 'acos', 'atan', 'asec', 'acsc', 'acot',
                'asinh', 'acosh', 'atanh', 'asech', 'acsch', 'acoth',

                # MathML constants

                'true', 'false', 'nan', 'pi', 'inf', 'e',

                # Extra operators

                'rem'
            ), suffix=r'\b'), CellmlTextKeyword),

            # CellML keywords

            (words((
                # Miscellaneous

                'base', 'encapsulation', 'containment'
            ), suffix=r'\b'), CellmlTextCellmlKeyword),

            # SI units

            (words((
                # Standard units

                'ampere', 'becquerel', 'candela', 'celsius', 'coulomb',
                'dimensionless', 'farad', 'gram', 'gray', 'henry', 'hertz',
                'joule', 'katal', 'kelvin', 'kilogram', 'liter', 'litre',
                'lumen', 'lux', 'meter', 'metre', 'mole', 'newton', 'ohm',
                'pascal', 'radian', 'second', 'siemens', 'sievert', 'steradian',
                'tesla', 'volt', 'watt', 'weber'
            ), suffix=r'\b'), CellmlTextSiUnitKeyword),

            # Miscellaneous

            include('whitespaces'),
            (r'(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?', CellmlTextNumber),
            (r'[a-zA-Z_]\w*', CellmlText),
            (r'[+\-*/=<>]', CellmlTextOperator),
            (r'[().,;:]', CellmlTextPunctuation),
            (r'"[^\\"\n]+"', CellmlTextString),
            (r'\{', CellmlTextParameterBlock, 'parameterBlock')
        ],
        'parameterBlock': [
            # Parameter keywords

            (words((
                # Unit keywords

                'pref', 'expo', 'mult', 'off',

                # Variable keywords

                'init', 'pub', 'priv'
            ), suffix=r'\b'), CellmlTextParameterKeyword),

            # Parameter CellML keywords

            (words((
                # Unit prefixes

                'yotta', 'zetta', 'exa', 'peta', 'tera', 'giga', 'mega', 'kilo',
                'hecto', 'deka', 'deci', 'centi', 'milli', 'micro', 'nano',
                'pico', 'femto', 'atto', 'zepto', 'yocto',

                # Public/private interfaces

                'in', 'out', 'none'
            ), suffix=r'\b'), CellmlTextParameterCellmlKeyword),

            # Parameter SI units

            (words((
                # Standard units

                'ampere', 'becquerel', 'candela', 'celsius', 'coulomb',
                'dimensionless', 'farad', 'gram', 'gray', 'henry', 'hertz',
                'joule', 'katal', 'kelvin', 'kilogram', 'liter', 'litre',
                'lumen', 'lux', 'meter', 'metre', 'mole', 'newton', 'ohm',
                'pascal', 'radian', 'second', 'siemens', 'sievert', 'steradian',
                'tesla', 'volt', 'watt', 'weber'
            ), suffix=r'\b'), CellmlTextParameterSiUnitKeyword),

            # Miscellaneous

            include('whitespaces'),
            (r'(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?', CellmlTextParameterNumber),
            (r'[a-zA-Z_]\w*', CellmlTextParameterBlock),
            (r'[\-]', CellmlTextParameterBlock),
            (r'[,:]', CellmlTextParameterBlock),
            (r'\.\.\.', CellmlTextParameterBlock),
            (r'\}', CellmlTextParameterBlock, '#pop')
        ],
        'whitespaces': [
            # Whitespaces

            (r'\n', CellmlText),
            (r'\s+', CellmlText),
            (r'\\\n', CellmlText)
        ]
    }

lexers['cellmlText'] = cellmlTextLexer()
