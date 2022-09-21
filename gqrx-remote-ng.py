#!/usr/bin/env python

import tkinter as tk
from gqrxremote import GqrxRemote

"""
Remote application that interacts with gqrx using rigctl protocol.
Gqrx partially implements rigctl since version 2.3.

Please refer to:
http://gqrx.dk/
http://gqrx.dk/doc/remote-control
http://sourceforge.net/apps/mediawiki/hamlib/index.php?title=Documentation

Author: Rafael Marmelo <rafael@defying.me>
License: MIT License

Copyright (c) 2014 Rafael Marmelo
"""


# entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = GqrxRemote(root)
    app.mainloop()
