from glob import glob
 
from distutils.core import setup
from setuptools import find_packages
 
setup(
    name='photometric_stereo',
    version='0.1.0',
    url = '',
    description='photometric stereo algorithms',
    author='kensuke uchida',
    author_email='',
    packages=find_packages(),
    python_requires='>=3.7.*'
)