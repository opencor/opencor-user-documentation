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
       ...;
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

Blah...
