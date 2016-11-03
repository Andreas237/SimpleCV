# Author:       Andreas Slovacek
# Date:         28 October 2016



from multiprocessing import Pool, TimeoutError
import time
import os


import pandas as pd
import numpy as np
import scipy as sp
import sklearn as skl

# Simple CV needs update.
#   1) Updated 'Print ""' to 'Print("")' in base.py             PASSED ERROR
#   2) Update 'import urllib2' to 'urllib.request'              PASSED ERROR
#       and references replaced
#   3) Update 'import SocketServer' to 'import socketserver'    PASSED ERROR
#   4) No module 'pygame' (had to install for myself)
#   

import SimpleCV



