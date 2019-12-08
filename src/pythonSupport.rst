.. _pythonSupport:

================
 Python support
================

OpenCOR comes bundled with `Python <https://python.org/>`__, providing `Python <https://python.org/>`__ support to OpenCOR.
The following `Python <https://python.org/>`__ packages are included:

- `Matplotlib <https://matplotlib.org/>`__: a `Python <https://python.org/>`__ 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms;
- `NumPy <https://numpy.org/>`__: the fundamental package for scientific computing with `Python <https://python.org/>`__; and
- `SciPy <https://scipy.org/>`__: a `Python <https://python.org/>`__-based ecosystem of open-source software for mathematics, science and engineering.

Some code illustrating the use of the OpenCOR `Python <https://python.org/>`__ module and wrappers can be found `here <https://github.com/opencor/opencor/blob/master/models/tests/python/lorenz.py>`__.

Install a Python package
------------------------

Additional `Python <https://python.org/>`__ packages can be installed either from the :ref:`CLI <userInterfaces_commandLineInterface>` (using the ``jupyterconsole[.bat]`` :ref:`script <userInterfaces_commandLineInterfacePythonRelatedScriptsJupyterconsole>`) or through the :ref:`GUI <userInterfaces_graphicalUserInterface>` (using the :ref:`Python Console window <plugins_miscellaneous_pythonConsoleWindow>` plugin):

.. code-block::

   !pip install package_name

Python module
-------------

A `Python <https://python.org/>`__ module, ``opencor``, is available and can be used to handle simulations in OpenCOR:

- ``open_simulation(file_name_or_url)``: open and return the simulation for the given local or remote `CellML <https://cellml.org/>`__ file, `SED-ML <https://sed-ml.github.io/>`__ file or `COMBINE archive <https://co.mbine.org/documents/archive>`__.
- ``close_simulation(simulation_object)``: close the given simulation.
- ``simulation()``: return the current simulation.

  **Note:** ``simulation()`` is only available when using the :ref:`Python Console window <plugins_miscellaneous_pythonConsoleWindow>` plugin.

Python wrappers
---------------

The following OpenCOR classes have some `Python <https://python.org/>`__ wrappers that can be used to handle a simulation, some simulation data, some simulation results, a data store and a data store variable:

- ``Simulation``:

  - ``valid()``: return whether the simulation is valid.
  - ``run()``: run the simulation.
  - ``reset(all = True)``: reset all the model parameters (``all = True``) or only the state model parameters (``all = False``).
  - ``clear_results()``: clear the simulation results.
  - ``issues()``: return a list of issues with the simulation.

- ``SimulationData``:

  - ``set_starting_point(starting_point, recompute)``: set the starting point.
  - ``set_ending_point(ending_point)``: set the ending point.
  - ``set_point_interval(point_interval)``: set the point interval.
  - ``set_ode_solver(ode_solver_name)``: set the ODE solver using the given ODE solver name.
  - ``set_nla_solver(nla_solver_name)``: set the NLA solver using the given NLA solver name.
  - ``constants()``: return the constants values.
  - ``rates()``: return the rates values.
  - ``states()``: return the states values.
  - ``algebraic()``: return the algebraic values.

    **Note:** neither ``set_ode_solver()`` nor ``set_nla_solver()`` currently updates the :ref:`GUI <userInterfaces_graphicalUserInterface>`.

- ``SimulationResults``:

  - ``data_store()``: return the associated data store.
  - ``voi()``: return the values for variable of integration.
  - ``constants()``: return the constants values as a `Python dictionary <https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries>`__.
  - ``rates()``: return the rates values as a `Python dictionary <https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries>`__.
  - ``states()``: return the states values as a `Python dictionary <https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries>`__.
  - ``algebraic()``: return the algebraic values as a `Python dictionary <https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries>`__.

- ``DataStore``:

  - ``voi()``: return the variable of integration.
  - ``variables()``: return the variables as a `Python dictionary <https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries>`__.
  - ``voi_and_variables()``: return the variable of integration and variables as a `Python dictionary <https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries>`__.

- ``DataStoreVariable``:

  - ``value(position, run = -1)``: return the value at the given position and for the given run (``run = -1`` corresponds to the last run).
  - ``values(run = -1)``: return the values for the given run (``run = -1`` corresponds to the last run) as a `NumPy array <https://numpy.org/doc/1.17/reference/generated/numpy.array.html>`__.
