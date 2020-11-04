from setuptools import setup

setup(
    name='hello_world',
    version='0.0.1',
    description='Hello world pip package from private github repo',
    url='https://github.com/KittPhi/pip-package.git',
    author='Kitt Phi',
    author_email='kittphi@gmail.com',
    license='unlicense',
    packages=['hello_world'],
    zip_safe=False
)