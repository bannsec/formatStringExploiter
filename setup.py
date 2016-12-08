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
            print "SandboxViolation: %s" % (args,)

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
    version='0.1.3',

    description='Script to ease the exploitation of format string vulnerabilities.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/owlz/formatStringExploiter',

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

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        #'Topic :: Software Development :: ',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console'
    ],

    # What does your project relate to?
    keywords='exploitation format string',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=["formatStringExploiter"],#find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['pwntools','prettytable','sphinx_rtd_theme','sphinx','pytest','recommonmark','sphinxcontrib-napoleon']

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sharePlayer.notifications': ['*.mp3'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={
    #    'console_scripts': [
    #        'sharePlayer = sharePlayer.sharePlayer:main',
    #    ],
    #},

)

