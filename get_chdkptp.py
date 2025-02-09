import os
import io
import shutil
from zipfile import ZipFile

try:
    import urllib.request
    from urllib.request import urlopen # Python 3.x
except ImportError:
    from urllib2 import urlopen # Python 2


REVISION = 664  # Version used in original submodule
SVN_URL_BASE = "https://app.assembla.com/spaces/chdkptp/subversion/source/"
SVN_URL = SVN_URL_BASE + "{0}/trunk?_format=zip&format=html".format(REVISION)

chdkptp_srcdir = os.path.join('chdkptp', 'vendor', 'chdkptp')


def get_chdkptp_source(outdir):

    if os.path.exists(outdir):
        shutil.rmtree(outdir)

    dl = urlopen(SVN_URL)
    data = io.BytesIO(dl.read())
    with ZipFile(data, 'r') as z:
        os.mkdir(outdir)
        z.extractall(path=outdir)
