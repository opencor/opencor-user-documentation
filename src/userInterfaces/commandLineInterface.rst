.. _userInterfaces_commandLineInterface:

==============================
 Command Line Interface (CLI)
==============================

Help
----

::

   $ ./OpenCOR -h
   Usage: OpenCOR [-a|--about] [-c|--command [<plugin>]::<command> <options>] [-e|--exclude <plugins>] [-h|--help] [-i|--include <plugins>] [-p|--plugins] [-r|--reset] [-s|--status] [-v|--version] [<files>]
    -a, --about     Display some information about OpenCOR
    -c, --command   Send a command to one or all the CLI plugins
    -e, --exclude   Exclude the given plugin(s)
    -h, --help      Display this help information
    -i, --include   Include the given plugin(s)
    -p, --plugins   Display all the CLI plugins
    -r, --reset     Reset all your settings
    -s, --status    Display the status of all the plugins
    -v, --version   Display the version of OpenCOR

About
-----

::

   $ ./OpenCOR -a
   OpenCOR Version 0.6
   macOS High Sierra (10.13)
   Copyright 2011-2018

   OpenCOR is a cross-platform modelling environment, which can be used to organise, edit, simulate and analyse CellML files.

Command
-------

::

   $ ./OpenCOR -c ::help
   Commands supported by the CellMLTextView plugin:
    * Display the commands supported by the CellMLTextView plugin:
         help
    * Export a CellML Text <file> to CellML:
         export <file>
    * Import a CellML <file> to the CellML Text format:
         import <file>

   Commands supported by the CellMLTools plugin:
    * Display the commands supported by the CellMLTools plugin:
         help
    * Export <file> to a <predefined_format> or a <user_defined_format_file>:
         export <file> <predefined_format>|<user_defined_format_file>
      <predefined_format> can take one of the following values:
         cellml_1_0: to export a CellML 1.1 file to CellML 1.0

::

   $ ./OpenCOR -c CellMLTools::help
   Commands supported by the CellMLTools plugin:
    * Display the commands supported by the CellMLTools plugin:
         help
    * Export <file> to a <predefined_format> or a <user_defined_format_file>:
         export <file> <predefined_format>|<user_defined_format_file>
      <predefined_format> can take one of the following values:
         cellml_1_0: to export a CellML 1.1 file to CellML 1.0

Exclude
-------

::

   $ ./OpenCOR -e Core HelpWindow Unknown
    - Core: cannot be directly excluded.
    - HelpWindow: excluded from the GUI version of OpenCOR.
    - Unknown: unknown plugin.

Include
-------

::

   $ ./OpenCOR -i Core HelpWindow Unknown
    - Core: cannot be directly included.
    - HelpWindow: included to the GUI version of OpenCOR.
    - Unknown: unknown plugin.

Plugins
-------

::

   $ ./OpenCOR -p
   The following CLI plugins are available:
    - CellMLTextView: a plugin to edit CellML files using the CellML Text format.
    - CellMLTools: a plugin to access various CellML-related tools.

Reset
-----

::

   $ ./OpenCOR -r
   All your settings have been reset.

Status
------

::

   $ ./OpenCOR -s
   The following plugins are available:
    - CellMLAPI: the plugin is loaded and fully functional.
    - CellMLEditingView: the plugin is loaded and fully functional.
    - CellMLSupport: the plugin is loaded and fully functional.
    - CellMLTextView: the plugin is loaded and fully functional.
    - CellMLTools: the plugin is loaded and fully functional.
    - Compiler: the plugin is loaded and fully functional.
    - Core: the plugin is loaded and fully functional.
    - EditingView: the plugin is loaded and fully functional.
    - EditorWidget: the plugin is loaded and fully functional.
    - LLVMClang: the plugin is loaded and fully functional.
    - MathMLViewerWidget: the plugin is loaded and fully functional.
    - QScintilla: the plugin is loaded and fully functional.
    - QScintillaSupport: the plugin is loaded and fully functional.
    - Qwt: the plugin is loaded and fully functional.
    - StandardSupport: the plugin is loaded and fully functional.

Version
-------

::

   $ ./OpenCOR -v
   OpenCOR Version 0.6
