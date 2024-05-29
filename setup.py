from setuptools import setup, find_packages

setup(
    name='api_tests',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pytest'
    ],
)
