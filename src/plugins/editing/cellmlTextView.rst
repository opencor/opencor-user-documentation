.. _plugins_editing_cellmlTextView:

=======================
 CellMLTextView plugin
=======================

The CellMLTextView plugin can be used to edit `CellML <https://www.cellml.org/>`__ files using a text editor that supports the :ref:`CellML Text format <plugins_editing_cellmlTextView_cellmlTextFormat>`.
If you open a `CellML <https://www.cellml.org/>`__ file, then it will look something like:

.. image:: pics/CellMLTextViewScreenshot01.png
   :align: center
   :scale: 25%

Apart from using a specific format, the view has the same features as the :ref:`Raw CellML <plugins_editing_rawCellMLView>` view with one exception: currently, ``CellML Validation`` only validates against the :ref:`CellML Text format <plugins_editing_cellmlTextView_cellmlTextFormat>`.

Compatibility with COR
----------------------

People familiar with `COR <http://www.opencor.ws/cor/index.html>`__ will find that the :ref:`CellML Text format <plugins_editing_cellmlTextView_cellmlTextFormat>` is compatible with the COR format, although it supports additional features:

- :ref:`Comments <plugins_editing_cellmlTextView_comments>`;
- The ``import`` element (i.e. support for `CellML 1.1 <https://www.cellml.org/specifications/cellml_1.1>`__);
- The ``cmeta:id`` attribute on all CellML elements (i.e. support for CellML annotation);
- The ``degree`` qualifier for the ``diff`` element (i.e. support for higher-order derivatives);
- The ``notanumber`` and ``infinity`` constants; and
- An unlimited number of group types (in `COR <http://www.opencor.ws/cor/index.html>`__, a group can only specify one ``encapsulation`` and/or one ``containment`` type).

However, note that the COR format has some limitations that are also present in the :ref:`CellML Text format <plugins_editing_cellmlTextView_cellmlTextFormat>`:

- The ``reaction`` element is not supported (its use is not only discouraged, but it has also been removed from `CellML 2.0 <https://www.cellml.org/specifications/cellml_2.0>`__, the next version of CellML);
- A ``piecewise`` statement can only be used as part of a top-level ``eq`` statement, and nested ``piecewise`` statements are not allowed (the latter is not a limitation *per se* since an equation can always be rewritten without the need for nested ``piecewise`` statements; more importantly, it is easier to read and maintain an equation that uses only one top-level ``piecewise`` statement); and
- A ``component`` element may contain a set of ``math`` elements, but its rendering is such that when serialised back, only one ``math`` element will remain, with all the equations in that one and unique ``math`` element.

.. _plugins_editing_cellmlTextView_comments:

Comments
--------

You can (un)comment a piece of code by pressing ``Ctrl``\ +\ ``/``.
If no text is selected or if it consists of one or several full lines, then the comment will be rendered as ``// XXX``, e.g.

.. code-block:: cellmlText

   def model my_model as
       // A single line comment
       ...
   enddef;

Alternatively, if one or several lines are partially selected, then the comment will be rendered as ``/* XXX */``, e.g.

.. code-block:: cellmlText

   def model my/*_super_duper*/_model as
       ...
   enddef;

Note that ``/* XXX */`` comments are only for convenience and are not serialised back to CellML.
Indeed, such comments can be inserted anywhere, including within an equation, e.g.

.. code-block:: cellmlText

   ode(V, time) = -(i_Na+i_K+i_Leak/*+i_Stim*/)/Cm;

It is therefore difficult, if not impossible, to determine where such comments should be included when serialised back.

``// XXX`` comments can also be inserted anywhere, but unlike ``/* XXX */`` comments they are serialised back.
However, the rendering of certain elements using the :ref:`CellML Text format <plugins_editing_cellmlTextView_cellmlTextFormat>` is such that when serialised back, ``// XXX`` comments may be included in the parent element of those elements, and either before or after those elements, depending on the situation.

.. _plugins_editing_cellmlTextView_cellmlTextFormat:

CellML Text format
------------------

The CellML Text format offers, for the large part, a one-to-one mapping to the CellML format with the view of making it easier to create and edit CellML files.

Model structure
~~~~~~~~~~~~~~~

To define a model of name ``my_model``, we would use:

.. code-block:: cellmlText

   def model my_model as
       ...
   enddef;

The model definition sits between ``as`` and ``enddef;``, and can consist of :ref:`imports <plugins_editing_cellmlTextView_imports>`, :ref:`unit definitions <plugins_editing_cellmlTextView_unitDefinitions>`, :ref:`component definitions <plugins_editing_cellmlTextView_componentDefinitions>`, :ref:`group definitions <plugins_editing_cellmlTextView_groupDefinitions>` and :ref:`mapping definitions <plugins_editing_cellmlTextView_mappingDefinitions>`.

.. _plugins_editing_cellmlTextView_imports:

Imports
~~~~~~~

To define an import for units and components defined in a CellML file, which `URI <https://en.wikipedia.org/wiki/Uniform_resource_identifier>`__ is ``my_imported_model_uri``, we would use:

.. code-block:: cellmlText

   def import using "my_imported_model_uri" for
       ...
   enddef;

To import a unit originally named ``my_reference_unit`` and renamed ``my_imported_unit`` in our model, we would use:

.. code-block:: cellmlText

   unit my_imported_unit using unit my_reference_unit;

Similarly, to import a component originally named ``my_reference_component`` and renamed ``my_imported_component`` in our model, we would use:

.. code-block:: cellmlText

   comp my_imported_component using comp my_reference_component;

Putting everything together, we would have:

.. code-block:: cellmlText

   def import using "my_imported_model_uri" for
       unit my_imported_unit using unit my_reference_unit;
       comp my_imported_component using comp my_reference_component;
   enddef;

.. _plugins_editing_cellmlTextView_unitDefinitions:

Unit definitions
~~~~~~~~~~~~~~~~

To define a base unit of name ``my_base_unit``, we would use:

.. code-block:: cellmlText

   def unit my_base_unit as base unit;

To define a unit of name ``my_unit``, based on some other units, we would use:

.. code-block:: cellmlText

   def unit my_unit as
       unit my_other_unit {...};
       unit second {...};
       unit litre {...};
       unit volt {...};
       ...
   enddef;

``my_other_unit`` refers to a user-defined unit while ``second`` is an `SI <https://en.wikipedia.org/wiki/International_System_of_Units>`__ base unit, ``litre`` a convenience unit and ``volt`` an `SI <https://en.wikipedia.org/wiki/International_System_of_Units>`__ derived unit .
The following `SI <https://en.wikipedia.org/wiki/International_System_of_Units>`__ base (in bold) and derived units, as well as convenience units (in italics), can be used:

.. table::
   :class: units

   +------------+------------+--------------+----------+---------+-----------------+
   | **ampere** | becquerel  | **candela**  | celsius  | coulomb | *dimensionless* |
   +------------+------------+--------------+----------+---------+-----------------+
   |   farad    |   *gram*   |     gray     |  henry   |  hertz  |      joule      |
   +------------+------------+--------------+----------+---------+-----------------+
   |   katal    | **kelvin** | **kilogram** | *liter*  | *litre* |      lumen      |
   +------------+------------+--------------+----------+---------+-----------------+
   |    lux     | **meter**  |  **metre**   | **mole** | newton  |       ohm       |
   +------------+------------+--------------+----------+---------+-----------------+
   |   pascal   |   radian   |  **second**  | siemens  | sievert |    steradian    |
   +------------+------------+--------------+----------+---------+-----------------+
   |   tesla    |    volt    |     watt     |  weber   |         |                 |
   +------------+------------+--------------+----------+---------+-----------------+

Additional information can be provided within curly brackets.
Thus, ``prefix``, ``exponent``, ``multiplier`` and ``offset`` values of :math:`p`, :math:`e`, :math:`m` and :math:`o` can be used on a unit :math:`u` to define a new unit equal to :math:`m \cdot (p \cdot u)^e+o`.
For example, to define ``my_unit`` as being equal to :math:`3 \cdot (milli \cdot my\_other\_unit)^{-1}+7`, we would use:

.. code-block:: cellmlText

   def unit my_unit as
       unit my_other_unit {pref: milli, expo: -1, mult: 3, off: 7};
   enddef;

By default, ``pref``, ``expo``, ``mult`` and ``off`` have a value of :math:`0`, :math:`1.0`, :math:`1.0` and :math:`0.0`, respectively.
``pref`` can either be an integer or have any of the following values:

.. table::
   :class: prefixes

   +-------+-----------------+-------+------------------+
   | yotta | :math:`10^{24}` | deci  | :math:`10^{-1}`  |
   +-------+-----------------+-------+------------------+
   | zetta | :math:`10^{21}` | centi | :math:`10^{-2}`  |
   +-------+-----------------+-------+------------------+
   |  exa  | :math:`10^{18}` | milli | :math:`10^{-3}`  |
   +-------+-----------------+-------+------------------+
   | peta  | :math:`10^{15}` | micro | :math:`10^{-6}`  |
   +-------+-----------------+-------+------------------+
   | tera  | :math:`10^{12}` | nano  | :math:`10^{-9}`  |
   +-------+-----------------+-------+------------------+
   | giga  | :math:`10^{9}`  | pico  | :math:`10^{-12}` |
   +-------+-----------------+-------+------------------+
   | mega  | :math:`10^{6}`  | femto | :math:`10^{-15}` |
   +-------+-----------------+-------+------------------+
   | kilo  | :math:`10^{3}`  | atto  | :math:`10^{-18}` |
   +-------+-----------------+-------+------------------+
   | hecto | :math:`10^{2}`  | zepto | :math:`10^{-21}` |
   +-------+-----------------+-------+------------------+
   | deka  | :math:`10^{1}`  | yocto | :math:`10^{-24}` |
   +-------+-----------------+-------+------------------+

.. _plugins_editing_cellmlTextView_componentDefinitions:

Component definitions
~~~~~~~~~~~~~~~~~~~~~

To define a component of name ``my_component``, we would use:

.. code-block:: cellmlText

   def comp my_component as
       ...
   enddef;

The component definition sits between ``as`` and ``enddef;``, and can consist of :ref:`unit definitions <plugins_editing_cellmlTextView_unitDefinitions>`, :ref:`variable definitions <plugins_editing_cellmlTextView_variableDefinitions>`, :ref:`mathematical equations <plugins_editing_cellmlTextView_mathematicalEquations>`.

.. _plugins_editing_cellmlTextView_variableDefinitions:

Variable definitions
~~~~~~~~~~~~~~~~~~~~

To define a variable of name ``my_variable`` and of unit ``my_unit``, we would use:

.. code-block:: cellmlText

   var my_variable: my_unit {...};

Additional information can be provided within curly brackets: an initial value, a public interface and/or a private interface.
For example, to initialise ``my_variable`` to :math:`3` and set its public and private interfaces to ``in`` and ``out``, respectively, we would use:

.. code-block:: cellmlText

   var my_variable: my_unit {init: 3, pub: in, priv: out};

By default, ``init`` has no value (i.e. the variable is not initialised) while ``pub`` and ``priv`` have a value of ``none`` (i.e. the variable belongs to the current component and is not visible to other components in the model).
``init`` can either take a real number as a value or the name of a variable defined in the current component.
Both ``pub`` and ``priv`` can take any of the following values: ``none``, ``in`` or ``out``.

.. _plugins_editing_cellmlTextView_mathematicalEquations:

Mathematical equations
~~~~~~~~~~~~~~~~~~~~~~

Blah...

.. _plugins_editing_cellmlTextView_groupDefinitions:

Group definitions
~~~~~~~~~~~~~~~~~

Blah...

.. _plugins_editing_cellmlTextView_mappingDefinitions:

Mapping definitions
~~~~~~~~~~~~~~~~~~~

Blah...

.. _plugins_editing_cellmlTextView_metadata:

Metadata
~~~~~~~~

Blah...

CLI support
-----------

Blah...
