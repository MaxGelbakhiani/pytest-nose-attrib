from setuptools import setup
import pytest_nose_attrib

setup(
    name='pytest-nose-attrib',
    description='pytest plugin to use nose @attrib marks decorators'
                'and pick tests based on attributes and'
                'partially uses nose-attrib plugin approach',
    version=pytest_nose_attrib.version,
    author='Maksim Gelbakhiani',
    author_email='Max.Gelbakhiani@gmail.com',
    url='https://github.com/MaxGelbakhiani/pytest-nose-attrib',
    packages=['pytest_nose_attrib'],
    entry_points={'pytest11': ['attr = pytest_nose_attrib.plugin']},
    install_requires=['pytest>=2.2'],
    license="MIT License",
    package_data={'pytest_attrib': ["VERSION"]},
)
