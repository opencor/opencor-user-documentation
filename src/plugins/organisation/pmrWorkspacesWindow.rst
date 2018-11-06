.. _plugins_organisation_pmrWorkspacesWindow:

============================
 PMRWorkspacesWindow plugin
============================

The PMRWorkspacesWindow plugin gives you access to your `PMR <https://models.physiomeproject.org/>`__ workspaces.
By default, it looks as follows:

.. image:: pics/PMRWorkspacesWindowScreenshot01.png
   :align: center
   :scale: 25%

There are three `PMR <https://models.physiomeproject.org/>`__ sites:

- `Primary site <https://models.physiomeproject.org>`__: everything on this site is permanent and persistent.
  It is always up and always stable.
- `Staging site <https://staging.physiomeproject.org>`__: it is used for public testing/preview of PMR developments.
  Data on this site is wiped periodically whenever a new public testing/preview of the PMR software suite is released for the required testing exercise.
- `Teaching site <https://teaching.physiomeproject.org>`__: the functionality of this site should match the primary site, but without the data persistency guarantees.
  While data on this site is also not permanent, any wipes to data stored will be announced on the `cellml-discussion mailing list <https://lists.cellml.org/sympa/info/cellml-discussion>`__.

Both the `primary site <https://models.physiomeproject.org>`__ and the `teaching site <https://teaching.physiomeproject.org>`__ require you to create an account before you can start interacting with them.
On the `staging site <https://staging.physiomeproject.org>`__, your `primary site <https://models.physiomeproject.org>`__ account may work, but if not then you need to create an account (on the `staging site <https://staging.physiomeproject.org>`__).

Tool bar
--------

| |toolbarNewFolder|                         Create a new workspace
| |toolbarOxygenActionsViewRefresh|          Reload the list of workspaces
| |toolbarOxygenCategoriesPreferencesSystem| Preferences for PMR support
| |toolbarLogOn|                             Log on to PMR
| |toolbarLogOff|                            Log off from PMR

.. |toolbarNewFolder| image:: ../../pics/newFolder.png
   :class: toolbar
   :scale: 50%

.. |toolbarOxygenActionsViewRefresh| image:: ../../pics/oxygen/actions/view-refresh.png
   :class: toolbar
   :scale: 50%

.. |toolbarOxygenCategoriesPreferencesSystem| image:: ../../pics/oxygen/categories/preferences-system.png
   :class: toolbar
   :scale: 50%

.. |toolbarLogOn| image:: ../../pics/logOn.png
   :class: toolbar
   :scale: 50%

.. |toolbarLogOff| image:: ../../pics/logOff.png
   :class: toolbar
   :scale: 50%
