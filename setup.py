#!/usr/bin/env python3

import sys
import os
from setuptools import setup
from distutils.sysconfig import get_python_lib

import yass

# Warn if we are installing over top of an existing installation. This can
# cause issues where files that were deleted from a more recent YASS are
# still present in site-packages.
overlay_warning = False
existing_path = None

if 'install' in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "yass"))
        if os.path.exists(existing_path):
            # We note the need for the warning here, but present it after the
            # command is run, so it's more likely to be seen.
            overlay_warning = True
            break


def _(fname):
    """
    Utility function to read the README file.
    Used to fill the *long_description* field.

    It's nice, because now
        * we have a top level README file, and
        * it's easier to type in the README file than to put a raw string in below

    :param fname: README file name
    :type fname: str
    :return: README file content
    :rtype: str
    """
    with open(os.path.join(os.path.dirname(__file__), fname)) as readme:
            content = readme.read() or ''  # prevent ``content = None``
    return content

setup(
    name=yass.__lname__,
    version=yass.__version__,
    author=yass.__author__,
    author_email=yass.__author_email__,
    description='{name} is a plugin-powered search engine based subdomainer'.format(name=yass.__uname__),
    long_description=_('README'),
    license='Apache License, Version 2.0',
    keywords='subdomain crawling information-gathering',
    url=yass.__source_url__,
    scripts=['bin/yass'],
    packages=['yass'],
    install_requires=['pyquery >=1.2.9', 'colorama'],
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Pentesters',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security',
    ]
)

if overlay_warning:
    sys.stderr.write("""
========
WARNING!
========
You have just installed {name} over top of an existing
installation, without removing it first. Because of this,
your install may now include extraneous files from a
previous version that have since been removed from
{name}. This is known to cause a variety of problems.
You should manually remove the
{existing_path}
directory and re-install {name}.
""".format(name=yass.__uname__, existing_path=existing_path))
