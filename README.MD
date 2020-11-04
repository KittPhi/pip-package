# How to create a pip package and host on private github repo
[Instructions to create pip-package on github](https://dev.to/rf_schubert/how-to-create-a-pip-package-and-host-on-private-github-repo-58pa)

> `packages=['algorithms']` variable must be same name as subfolder. Eg. name='algorithms', packages=['algorithms']
> `setup.py` must be in root directory of project.
> `__init__.py` must be in folder of each functions folder.

pippackage
├── algorithms
│   └── __init__.py
├── README.MD
└── setup.py

```python
# setup.py
from setuptools import setup

setup(
    name='algorithms',
    version='0.0.1',
    description='Hello world pip package from private github repo',
    url='https://github.com/KittPhi/pip-package.git',
    author='Kitt Phi',
    author_email='kittphi@gmail.com',
    license='unlicense',
    packages=['algorithms'],
    zip_safe=False
)

#test.py
from pippackage import algorithms

algorithms.hello_world()
```

# Installing with pip:
python3.7 -m pip install git+https://github.com/KittPhi/pip-package.git --upgrade

# Uninstall pip-package:
python3.7 -m pip uninstall -y pip-package

# test.py
from pippackage import pippackage

pippackage.hello_word()

sudo apt install tree && tree

pippackage
├── hello_world
│   ├── __init__.py
└── setup.py

