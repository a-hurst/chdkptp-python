# chdkptp-python

Python bindings for [chdkptp](https://www.assembla.com/spaces/chdkptp/wiki)
usign the [lupa package](https://github.com/scoder/lupa) to wrap its Lua functions. A fork of the original [chdkptp.py](https://github.com/jbaiter/chdkptp.py) project updated for compatibility with Python 3.x and recent versions of chdkptp.

## Installation

Currently, installation has only been tested on Linux and is unlikely to work on other platforms without tweaks. You will need a C compiler and the development version of libusb in order to install the package.

Once libusb and its headers have been installed, you can install Lupa and chdkptp-python using the following commands:

```bash
LUPA_WITH_LUA_DLOPEN=true pip install --no-binary lupa lupa
pip install https://github.com/a-hurst/chdkptp-python/archive/refs/heads/master.zip
```

Note that Lupa needs to be built and installed manually in order to support chdkptp as the pre-built wheels on PyPI currently do not support loading dynamic C libraries.

## Credits

Credit to Johannes Baiter for creating the chdkptp.py library, as well as the following earlier chdkptp.py forks for their various fixes and patches to the original code!

- https://github.com/contextual-dev/chdkptp.py
- https://github.com/dodald/chdkptp.py
- https://github.com/neogranadina/chdkptp.py
- https://github.com/fabrykato/chdkptp.py
- https://github.com/meelash/chdkptp.py