.. _knownLimitations:

===================
 Known limitations
===================

The following limitations have been observed when using OpenCOR on our :ref:`supported platforms <supportedPlatforms>`.

Windows, Linux and macOS
------------------------

- By default, OpenCOR uses the system's language for menus, message boxes, etc., as long as it is either English or French (please `contact us <http://www.opencor.ws/contactUs.html>`__ if you would like OpenCOR to support other languages).
  If your system uses another language, then OpenCOR will default to English.
  Otherwise, if you specify English or French, then please be aware that system messages, message boxes, etc. will still be displayed using your system's language (assuming it is not one of the languages supported by OpenCOR).
- OpenCOR uses the `CellML API <https://github.com/cellmlapi/cellml-api/>`__, which is known to have the following limitations:

  - It will crash OpenCOR if you try to export a `CellML <https://www.cellml.org/>`__ file to a user-defined format that is described in a file that contains valid, but unknown, `XML <https://www.w3.org/XML/>`__.
  - It may incorrectly (in)validate certain `CellML <https://www.cellml.org/>`__ files.

Windows
-------

- OpenCOR's :ref:`File Browser window <plugins_organisation_fileBrowserWindow>` plugin may, on some systems, result in OpenCOR being slow to respond at startup.
  This has nothing to do with OpenCOR, but most likely with a `Windows <https://en.wikipedia.org/wiki/Microsoft_Windows>`__ shell add-on that is installed on your system.
  `This page <http://www.brighthub.com/computing/windows-platform/articles/86552.aspx>`__ may help you address the issue, but if not then you might have to unselect the :ref:`File Browser window <plugins_organisation_fileBrowserWindow>` plugin.
- OpenCOR is a `Qt <https://www.qt.io/>`__-based application that is styled to look as native as possible on `Windows <https://en.wikipedia.org/wiki/Microsoft_Windows>`__, `Linux <https://en.wikipedia.org/wiki/Linux>`__ and `macOS <https://en.wikipedia.org/wiki/MacOS>`__.
  However, on `Windows <https://en.wikipedia.org/wiki/Microsoft_Windows>`__, the style used by `Qt <https://www.qt.io/>`__ is known to have some limitations when it comes to `HiDPI support <http://doc.qt.io/qt-5/highdpi.html#high-dpi-support-in-qt>`__.
  So, should you need such support, we recommend switching to Qt's Fusion style (either by selecting the ``Tools`` | ``Preferences...`` menu or by clicking `here <opencor://openPreferencesDialog>`__).
