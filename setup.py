import os

from setuptools.command.build import build as BuildCommand
from setuptools import setup

from get_chdkptp import (
    get_chdkptp_source, apply_patches, build_static_lua, build_chdkptp
)

PKG_ROOT = os.path.dirname(os.path.abspath(__file__))
CHDKPTP_PATH = os.path.join(PKG_ROOT, 'chdkptp', 'vendor', 'chdkptp')
CHDKPTP_PATCH = os.path.join(PKG_ROOT, 'chdkptp_module.diff')


class CustomBuild(BuildCommand):

    def run(self):

        get_chdkptp_source(CHDKPTP_PATH)
        apply_patches(CHDKPTP_PATH, CHDKPTP_PATCH)

        build_static_lua(CHDKPTP_PATH)
        build_chdkptp(CHDKPTP_PATH)

        BuildCommand.run(self)


setup(
    name='chdkptp.py',
    version="0.1.3",
    description=("Python bindings for chdkptp"),
    author="Johannes Baiter",
    url="http://github.com/jbaiter/chdkptp.py.git",
    author_email="johannes.baiter@gmail.com",
    license='GPL',
    packages=['chdkptp'],
    package_dir={"chdkptp": "chdkptp"},
    package_data={"chdkptp": ["vendor/chdkptp/*.so",
                              "vendor/chdkptp/lua/*.lua"]},
    install_requires=[
        "lupa >= 2.1",
    ],
    cmdclass={'build': CustomBuild}
)
