.. _plugins_tools_cellmlTools:

====================
 CellMLTools plugin
====================

The CellMLTools plugin consists of various `CellML <https://cellml.org/>`__-related tools, which can be accessed both through the :ref:`CLI <userInterfaces_commandLineInterface>` and the :ref:`GUI <userInterfaces_graphicalUserInterface>`.

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

   $ ./OpenCOR -c CellMLTools::export https://mydomain.com/myfile.cellml myformat.xml

to export ``https://mydomain.com/myfile.cellml`` file using the user-defined format described in ``myformat.xml``.

Some sample user-defined formats can be found in the OpenCOR distribution package.
They are for `C <https://raw.githubusercontent.com/opencor/opencor/master/formats/C.xml>`__, `FORTRAN 77 <https://raw.githubusercontent.com/opencor/opencor/master/formats/F77.xml>`__, `MATLAB <https://raw.githubusercontent.com/opencor/opencor/master/formats/MATLAB.xml>`__ and `Python <https://raw.githubusercontent.com/opencor/opencor/master/formats/Python.xml>`__.

| **Note #1:** the CellML 1.0 export is adapted from `Jonathan Cooper's CellML 1.1 to 1.0 converter <https://cellml.org/tools/jonathan-cooper-s-cellml-1-1-to-1-0-converter/versionconverter-tar.bz2/view>`__ and therefore has the same limitations.
| **Note #2:** the sample user-defined formats come from the `CellML API <https://github.com/cellmlapi/cellml-api/>`__ and should be used with caution.

Validate CellML file
--------------------

The validation of a `CellML <https://cellml.org/>`__ file can be done by entering the following command:

.. code-block:: shell

   $ ./OpenCOR -c CellMLTools::validate myfile.cellml

Both errors and warnings, if any, get listed and an exit code value of ``0`` means that the `CellML <https://cellml.org/>`__ file is valid, i.e. no errors were found.
