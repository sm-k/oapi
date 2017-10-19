
from codecs import open
from os import path

from setuptools import setup, find_packages

# Get a long description from the README file
with open(
    path.join(
        path.dirname(path.abspath(__file__)),
        'README.rst'
    ),
    encoding='utf-8'
) as f:
    long_description = f.read()

setup(
    name='oapi',

    version='0.0.2',

    description='An SDK for parsing OpenAPI (Swagger) 2.0 - 3.0 JSON or YAML specifications.',
    long_description=long_description,

    # The project's main homepage.
    url='https://bitbucket.com/davebelais/oapi.git',

    # Author details
    author='David Belais',
    author_email='david@belais.me',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
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

    keywords='openapi swagger',

    packages=find_packages(),
    # packages=[], # explicitly set packages
    # py_modules=[], # Single-file module names

    # dependencies
    # See https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'serial>=0.0.1',
        'future>=0.15.2',
        'jsonpointer>=1.12',
        'pyyaml>=3.12'
    ],

    # pip install -e .[dev, test]
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
