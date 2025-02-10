import os
import io
import sys
import shutil
import subprocess as sub
from zipfile import ZipFile

try:
    import urllib.request
    from urllib.request import urlopen # Python 3.x
except ImportError:
    from urllib2 import urlopen # Python 2


REVISION = 962  # Latest binary release
SVN_URL_BASE = "https://app.assembla.com/spaces/chdkptp/subversion/source/"
SVN_URL = SVN_URL_BASE + "{0}/trunk?_format=zip&format=html".format(REVISION)


def get_chdkptp_source(outdir):

    if os.path.exists(outdir):
        shutil.rmtree(outdir)

    dl = urlopen(SVN_URL)
    data = io.BytesIO(dl.read())
    with ZipFile(data, 'r') as z:
        os.mkdir(outdir)
        z.extractall(path=outdir)


def apply_patches(srcdir, patchfile):
    sub.check_call(['patch', '-d', srcdir, '-i', patchfile, '-p', '1'])


def build_static_lua(srcdir):
    orig_path = os.getcwd()
    misc_path = os.path.join(srcdir, 'misc')
    os.chdir(misc_path)
    cmd = ['bash', 'setup-ext-libs.bash', '-nogui']
    p = sub.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr)
    p.communicate()
    if p.returncode != 0:
        raise RuntimeError("Error building static Lua")
    os.chdir(orig_path)
