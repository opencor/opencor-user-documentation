.. _plugins_tools_cellmlTools:

====================
 CellMLTools plugin
====================

The CellMLTools plugin consists of various `CellML <https://www.cellml.org/>`__-related tools, which can be accessed both through the :ref:`CLI <userInterfaces_commandLineInterface>` and the :ref:`GUI <userInterfaces_graphicalUserInterface>`.

CellML file export
------------------

A CellML file can be exported to:

- CellML 1.0
- A user-defined format

An export can be initiated by selecting the ``Tools`` | ``CellML File Export To`` menu or by entering the following command:

.. code-block:: shell

   $ ./OpenCOR -c CellMLTools::export myfile.cellml cellml_1_0

to export ``myfile.cellml`` to CellML 1.0, or by entering:

.. code-block:: shell

   $ ./OpenCOR -c CellMLTools::export http://mydomain.com/myfile.cellml myformat.xml

to export ``http://mydomain.com/myfile.cellml`` file using the user-defined format described in ``myformat.xml``.

Some sample user-defined formats can be found in the OpenCOR distribution package. They are for `C <https://raw.githubusercontent.com/opencor/opencor/master/formats/C.xml>`__, `FORTRAN 77 <https://raw.githubusercontent.com/opencor/opencor/master/formats/F77.xml>`__, `MATLAB <https://raw.githubusercontent.com/opencor/opencor/master/formats/MATLAB.xml>`__ and `Python <https://raw.githubusercontent.com/opencor/opencor/master/formats/Python.xml>`__.

**Note:** the CellML 1.0 export is adapted from `Jonathan Cooper's CellML 1.1 to 1.0 converter <https://www.cellml.org/tools/jonathan-cooper-s-cellml-1-1-to-1-0-converter/versionconverter-tar.bz2/view>`__ and therefore has the same limitations.
