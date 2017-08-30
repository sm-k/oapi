import re
from setuptools import setup, find_packages
from codecs import open
from os import path

d = path.abspath(path.dirname(__file__))

# Get a long description from the README file
with open(
    path.join(
        d,
        'README.rst'
    ),
    encoding='utf-8'
) as f:
    long_description = ''.join(
        re.split(
            r'(^\s*To\s*install::\s*$)',
            f.read(),
            flags=re.IGNORECASE+re.MULTILINE
        )[1:]
    )

setup(
    name='openswallow',

    version='2.0.0',

    description="A python library for generating Marshmallow Schemas from a Swagger (Open API) 2.0 JSON Schema.",
    long_description=long_description,

    # The project's main homepage.
    url='https://bitbucket.com/davebelais/openswallow.git',

    # Author details
    author='David Belais',
    author_email='david@belais.me',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='mdm mercury',

    packages=find_packages(),
    # packages=[], # explicitly set packages
    # py_modules=[], # Single-file module names

    # dependencies
    # See https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'future>=0.15.2',
        'marshmallow>=2.13.6'
    ],

    # pip install -e .[dev,test]
    extras_require={
        'dev': [
            'pytest>=2.9.0'
        ],
        'test': [
            'pytest>=2.9.0'
        ],
    },

    package_data={},

    # See http://docs.python.org/3.5/distutils/setupscript.html#installing-additional-files
    data_files=[],

    entry_points={
        'console_scripts': [],
    }
)