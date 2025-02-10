import os
import subprocess

from setuptools.command.install import install as InstallCommand
from setuptools import setup

from get_chdkptp import get_chdkptp_source, apply_patches, build_static_lua

PKG_ROOT = os.path.dirname(os.path.abspath(__file__))
CHDKPTP_PATH = os.path.join(PKG_ROOT, 'chdkptp', 'vendor', 'chdkptp')
CHDKPTP_PATCH = os.path.join(PKG_ROOT, 'chdkptp_module.diff')


class CustomInstall(InstallCommand):
    def run(self):
        os.symlink(os.path.join(CHDKPTP_PATH, 'config-sample-linux.mk'),
                   os.path.join(CHDKPTP_PATH, 'config.mk'))
        subprocess.check_call(['make', '-C', CHDKPTP_PATH])
        InstallCommand.run(self)


get_chdkptp_source(CHDKPTP_PATH)
apply_patches(CHDKPTP_PATH, CHDKPTP_PATCH)
build_static_lua(CHDKPTP_PATH)

setup(
    name='chdkptp.py',
    version="0.1.3",
    description=("Python bindings for chdkptp"),
    author="Johannes Baiter",
    url="http://github.com/jbaiter/chdkptp.py.git",
    author_email="johannes.baiter@gmail.com",
    license='GPL',
    packages=['chdkptp'],
    package_data={"chdkptp": ["vendor/chdkptp/chdkptp.so",
                              "vendor/chdkptp/lua/*.lua"]},
    install_requires=[
        "lupa >= 1.1",
    ],
    cmdclass={'install': CustomInstall}
)
