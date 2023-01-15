from setuptools import setup

name = "types-tensorflow"
description = "Typing stubs for tensorflow"
long_description = '''
## Typing stubs for tensorflow

This is a PEP 561 type stub package for the `tensorflow` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`tensorflow`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/tensorflow. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `ebde125d700e9b3197f0473e3db3060a631f32b2`.
'''.lstrip()

setup(name=name,
      version="2.11.0.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/tensorflow.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['numpy>=1.20'],
      packages=['tensorflow-stubs'],
      package_data={'tensorflow-stubs': ['__init__.pyi', 'core/framework/variable_pb2.pyi', 'dtypes.pyi', 'math.pyi', 'sparse.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
