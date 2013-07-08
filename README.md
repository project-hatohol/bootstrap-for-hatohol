Bootstrap for Hatohol
=====================

The files in this repository are for build bootstrap RPM packages for
Hatohol web UI client.

How to make RPM files
---------------------

    $ rpmbuild -D "_topdir ${PWD}" -ba SPECS/bootstrap-for-hatohol.spec

