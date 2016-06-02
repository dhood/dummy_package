from setuptools import find_packages
from setuptools import setup

setup(
    name='dummy_package',
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    author='dummy',
    author_email='dummy@osrfoundation.org',
    maintainer='dummy',
    maintainer_email='dummy@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='dummy package for testing',
    long_description='''\
This package provides helper scripts for writing tests that use the ROS launch tool.''',
    license='Apache License, Version 2.0',
    test_suite='test',
)
