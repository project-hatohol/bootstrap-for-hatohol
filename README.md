Bootstrap for Hatohol
=====================

The files in this repository are for building bootstrap RPM packages for
Hatohol web UI client.

The bootstrap files are installed on the following directory.
    %{prefix}/libexec/hatohol/client/static
(%{prefix} is typically /usr)

How to make RPM files
---------------------

    $ rpmbuild -D "_topdir ${PWD}" -ba SPECS/bootstrap-for-hatohol.spec

