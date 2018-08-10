.. _plugins_index:

=========
 Plugins
=========

OpenCOR is a plugin-based application.
As can be seen by opening the Plugins dialog (either by selecting the ``Tools`` | ``Plugins...`` menu or by clicking `here <opencor://openPluginsDialog>`__) and by unselecting ``Show only selectable plugins`` (if necessary), OpenCOR comes with different types of plugins:

.. image:: pics/screenshot01.png
   :align: center
   :scale: 25%

You can select which plugins you want to use.
However, plugins that are needed by other plugins (e.g. the Core plugin is needed by the :ref:`PMR window <plugins_organisation_pmrWindow>` plugin) cannot be directly selected.
Instead, they will be automatically selected if and only if they are needed by at least one other plugin.

Most of the selectable plugins come with some kind of a :ref:`GUI <userInterfaces_graphicalUserInterface>`, which is of one of two types:

- **View:** such a plugin (e.g. the :ref:`CellML Annotation view <plugins_editing_cellmlAnnotationView>` and :ref:`Simulation Experiment view <plugins_simulation_simulationExperimentView>` plugins) is used to interact with a file, be it to edit it, simulate it or analyse it.
- **Window:** such a plugin (e.g. the :ref:`PMR window <plugins_organisation_pmrWindow>` and :ref:`Help window <plugins_miscellaneous_helpWindow>` plugins) can be docked around the central area, undocked or hidden, as illustrated :ref:`here <userInterfaces_graphicalUserInterface>`.

As can be imagined, if no plugins are selected, then OpenCOR is an :ref:`empty shell <userInterfaces_graphicalUserInterface_opencorWithNoLoadedPlugins>`.

Data store
----------

Data store plugins are used to store and manipulate data:

.. rst-class:: internal reference

   - :ref:`BioSignalMLDataStore: <plugins_dataStore_biosignalmlDataStore>` a BioSignalML specific data store plugin.
   - :ref:`CSVDataStore: <plugins_dataStore_csvDataStore>` a `CSV <https://en.wikipedia.org/wiki/Comma-separated_values>`__ specific data store plugin.

There is also one non-selectable data store plugin:

- **DataStore:** a plugin that provides core data store facilities.

Editing
-------

Editing plugins are used to edit files:

.. rst-class:: internal reference

   - :ref:`CellMLAnnotationView: <plugins_editing_cellmlAnnotationView>` a plugin to annotate `CellML <https://www.cellml.org/>`__ files.
   - :ref:`CellMLTextView: <plugins_editing_cellmlTextView>` a plugin to edit `CellML <https://www.cellml.org/>`__ files using the :ref:`CellML Text format: <plugins_editing_cellmlTextView_cellmlTextFormat>`.
   - :ref:`RawCellMLView: <plugins_editing_rawCellmlView>` a plugin to edit `CellML <https://www.cellml.org/>`__ files using an `XML <https://www.w3.org/XML/>`__ editor.
   - :ref:`RawSEDMLView: <plugins_editing_rawSedmlView>` a plugin to edit `SED-ML <http://www.sed-ml.org/>`__ files using an `XML <https://www.w3.org/XML/>`__ editor.
   - :ref:`RawTextView: <plugins_editing_rawTextView>` a plugin to edit text-based files using a text editor.

There are also some non-selectable editing plugins:

- **CellMLEditingView:** a plugin that provides core `CellML <https://www.cellml.org/>`__ editing view facilities.
- **EditingView:** a plugin that provides core editing view facilities.
- **SEDMLEditingView:** a plugin that provides core `SED-ML <http://www.sed-ml.org/>`__ editing view facilities.
