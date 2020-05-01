"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

#with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#    long_description = f.read()
long_description = "See website for more info."

def fix_setuptools():
    """Work around bugs in setuptools.                                                                                                                                                        

    Some versions of setuptools are broken and raise SandboxViolation for normal                                                                                                              
    operations in a virtualenv. We therefore disable the sandbox to avoid these                                                                                                               
    issues.                                                                                                                                                                                   
    """
    try:
        from setuptools.sandbox import DirectorySandbox
        def violation(operation, *args, **_):
            print("SandboxViolation: %s" % (args,))

        DirectorySandbox._violation = violation
    except ImportError:
        pass

# Fix bugs in setuptools.                                                                                                                                                                     
fix_setuptools()



setup(
    name='formatStringExploiter',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.2.0',

    description='Script to ease the exploitation of format string vulnerabilities.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/BannSec/formatStringExploiter',

    # Author details
    author='Michael Bann',
    author_email='self@bannsecurity.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console'
    ],

    # What does your project relate to?
    keywords='exploitation format string',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=["formatStringExploiter"],#find_packages(exclude=['contrib', 'docs', 'tests']),
    # Pinning to pwntools dev since stable doesn't work with python3
    install_requires=['pwntools @ https://github.com/Gallopsled/pwntools/archive/dev.zip','prettytable','sphinx_rtd_theme','sphinx','pytest','recommonmark','sphinxcontrib-napoleon'],
)

