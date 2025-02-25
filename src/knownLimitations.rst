.. _knownLimitations:

===================
 Known limitations
===================

The following limitations have been noticed when using OpenCOR on our `supported platforms <https://opencor.ws/supportedPlatforms.html>`__.

Windows, Linux and macOS
------------------------

- By default, OpenCOR uses the system's language for menus, message boxes, etc., as long as it is either English or French (please `contact us <https://opencor.ws/contactUs.html>`__ if you would like OpenCOR to support other languages).
  If the system uses another language, OpenCOR will default to English.
  Otherwise, if you specify English or French then please be aware that system messages, diaogs, etc. will still be displayed using the system's language.
- OpenCOR uses the `CellML API <https://github.com/cellmlapi/cellml-api/>`__, which is known to have the following limitations:

  - It leaks memory, although it should not be a "problem" in most cases.
  - It may incorrectly (in)validate certain `CellML <https://cellml.org/>`__ files.

- OpenCOR comes with :ref:`pythonSupport`, which requires OpenCOR to be installed in a directory that does not contain spaces.

Windows and Linux
-----------------

- A scaled display will, on `Linux <https://en.wikipedia.org/wiki/Linux>`__, result in some aspects of OpenCOR being rendered at the wrong size (e.g., icons will be smaller and scroll bars bigger).
  On `Windows <https://en.wikipedia.org/wiki/Windows>`__, OpenCOR should scale itself automatically, although it will look more or less blurry depending on your display scaling and screen resolution.
  In case OpenCOR does not scale itself, turn off *Fix scaling for apps*:

    .. image:: pics/windowsSettings01.png
       :align: center
       :scale: 25%

    .. image:: pics/windowsSettings02.png
       :align: center
       :scale: 25%

    .. image:: pics/windowsSettings03.png
       :align: center
       :scale: 25%

  or better, locate your copy of OpenCOR, right click on ``[OpenCOR]\bin\OpenCOR.exe``, click on the ``Properties`` menu item, and have the high DPI scaling performed by the system:

    .. image:: pics/opencorProperties01.png
       :align: center
       :scale: 25%

    .. image:: pics/opencorProperties02.png
       :align: center
       :scale: 25%

Windows
-------

- The :ref:`File Browser window <plugins_organisation_fileBrowserWindow>` plugin may, on some systems, result in OpenCOR being slow to respond at startup.
  This has nothing to do with OpenCOR, but most likely with a `Windows <https://en.wikipedia.org/wiki/Microsoft_Windows>`__ shell add-on.

Linux
-----

- OpenCOR is supported on `Ubuntu 20.04 LTS (Focal Fossa) <https://en.wikipedia.org/wiki/Ubuntu_version_history#Ubuntu_20.04_LTS_(Focal_Fossa)>`__ and later.
  However, OpenCOR's `Python <https://python.org/>`__ requires a specific version of `libffi <https://sourceware.org/libffi/>`__ which may or may not be present on a later version of Ubuntu.
  For this reason, OpenCOR comes with its own copy of `libffi <https://sourceware.org/libffi/>`__, but this means that OpenCOR's scripts must set ``LD_LIBRARY_PATH``, so that OpenCOR's `Python <https://python.org/>`__ can find `libffi <https://sourceware.org/libffi/>`__.
  This means that, on some later versions of Ubuntu, to run ``[OpenCOR]/bin/OpenCOR`` directly will result in the :ref:`Python Console window <plugins_miscellaneous_pythonConsoleWindow>` plugin not to work (since ``LD_LIBRARY_PATH`` is not set, which means that our copy of `libffi <https://sourceware.org/libffi/>`__ cannot be found).

macOS
-----

- Starting with `macOS Mojave <https://en.wikipedia.org/wiki/MacOS_Mojave>`__, macOS has a `Dark Mode <https://support.apple.com/HT208976>`__, which is not supported by OpenCOR.
