### ualfred

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ischaojie/ualfred/ci.yml?branch=master&style=flat-square)
[![codecov](https://codecov.io/gh/ischaojie/ualfred/branch/master/graph/badge.svg?token=FPBE0LGDCO)](https://codecov.io/gh/ischaojie/ualfred)
[![PyPI](https://img.shields.io/pypi/v/ualfred?style=flat-square)](https://pypi.org/project/ualfred/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ualfred?style=flat-square)

Modern [Alfred](https://www.alfredapp.com/) workflow library for Python3.

> **Note**
>
> This project is based on [deanishe/alfred-workflow](https://github.com/deanishe/alfred-workflow), and make it compatible with Python3.
>
> Currently, the test passed on Python3.7~3.11.

Install `uaflred` directly into your workflow with:

```bash
pip install --target=/path/to/my/workflow ualfred
```

For full usage documentation, see the origin project [docs](https://www.deanishe.net/alfred-workflow/). And don't forget to replace import statements from `workflow` to `ualfred`:
```python
# replace this:
# from workflow import *
# to
from ualfred import *
```
