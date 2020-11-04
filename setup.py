from setuptools import setup

setup(
    name='pippackage',
    version='0.0.1',
    description='Hello world pip package from private github repo',
    url='https://github.com/KittPhi/pip-package.git',
    author='Kitt Phi',
    author_email='kittphi@gmail.com',
    license='unlicense',
    packages=['pippackage'],
    zip_safe=False
)