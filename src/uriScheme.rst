.. _uriScheme:

============
 URI scheme
============

OpenCOR has its own `URI scheme <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__, which gets registered the first time OpenCOR is run.
The scheme takes the form:

::

  opencor://[pluginName.]command[/argument1[|argument2|argument3|...|argumentN]]

It can be used in a Web browser, as well as in a Web document (e.g. the :ref:`plugins_index` page).
Both ``pluginName`` and ``command`` are case insensitive while it depends for ``argument1``, ``argument2``, ``argument3``, ..., ``argumentN``.

The following commands are supported by OpenCOR itself:

- ``openPluginsDialog``: open the Plugins dialog.

  - Example: |openPluginsDialog|_.

.. |openPluginsDialog| replace:: ``opencor://openPluginsDialog``
.. _openPluginsDialog: opencor://openPluginsDialog

- ``openPreferencesDialog``: open the Preferences dialog.

  - Example: |openPreferencesDialog|_.

.. |openPreferencesDialog| replace:: ``opencor://openPreferencesDialog``
.. _openPreferencesDialog: opencor://openPreferencesDialog

- ``openAboutDialog``: open the About dialog.

  - Example: |openAboutDialog|_.

.. |openAboutDialog| replace:: ``opencor://openAboutDialog``
.. _openAboutDialog: opencor://openAboutDialog

- ``openFile``: open a file, which path/URL is given as an argument.

  - Example #1: |openFile01|_ to open ``/home/user/file``.
  - Example #2: |openFile02|_ to open ``https://models.physiomeproject.org/.../cell-model.sedml``.

.. |openFile01| replace:: ``opencor://openFile//home/user/file``
.. _openFile01: opencor://openFile//home/user/file

.. |openFile02| replace:: ``opencor://openFile/https://models.physiomeproject.org/.../cell-model.sedml``
.. _openFile02: opencor://openFile/https://models.physiomeproject.org/workspace/49e/rawfile/0a252e033bdf5e65d5a6490c9d3ade9035fef04e/experiments/cell-model.sedml

- ``openFiles``: open several files, which path/URL is given as arguments, separated by ``|``.

  - Example #1: |openFiles01|_ to open ``/home/user/file1`` and ``/home/user/file2``.
  - Example #2: |openFiles02|_ to open ``/home/user/file1`` and ``/home/user/file2``.

.. |openFiles01| replace:: ``opencor://openFiles//home/user/file1|/home/user/file2``
.. _openFiles01: opencor://openFiles//home/user/file1|/home/user/file2

.. |openFiles02| replace:: ``opencor://openFiles/https://models.physiomeproject.org/.../cell-model.xml|https://models.physiomeproject.org/.../cell-model.sedml``
.. _openFiles02: opencor://openFiles/https://models.physiomeproject.org/workspace/49e/rawfile/0a252e033bdf5e65d5a6490c9d3ade9035fef04e/experiments/cell-model.xml|https://models.physiomeproject.org/workspace/49e/rawfile/0a252e033bdf5e65d5a6490c9d3ade9035fef04e/experiments/cell-model.sedml
