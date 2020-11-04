from setuptools import setup

setup(
    name='pip-package',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:KittPhi/pip-package.git',
    author='Raphael Schubert',
    author_email='raphael.schubert@digitalbankscorp.com',
    license='unlicense',
    packages=['pip-package'],
    zip_safe=False
)