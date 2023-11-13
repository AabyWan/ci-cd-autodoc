from setuptools import setup, find_packages

setup(
    name='demolib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # list your dependencies here
    ],
    tests_require=[
        'pytest',
    ],
    test_suite='tests',
)