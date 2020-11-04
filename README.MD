# pip-package
[Instructions to create pip-package on github](https://dev.to/rf_schubert/how-to-create-a-pip-package-and-host-on-private-github-repo-58pa)

git commit -am "updated setup.py and created my_cool_test_method"

# Installing with pip:
python3.7 -m pip install git+https://github.com/KittPhi/pip-package.git

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

