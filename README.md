ML Spec Library
========================

A library for reading and writing MLSpec metadata files.

Schema requirements:
- Each schema version must have a file called ``base.yaml`` in it.
- All schemas must inherit from this file. Multiple generations are possible, but at the root of the inheritence must be this file.

Installation:
- #TODO

Testing:
- Go to the root directory of MLSpecLib and run ``nose2``




---------------------------
Library structure and tools are derived from the work of Kenneth Reitz:

- `Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.
- If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.
