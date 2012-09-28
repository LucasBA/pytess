#!/usr/bin/env python

import os
from distutils.core import setup, Extension

# remove warning flags; they generate excessive warnings with swig
from distutils.sysconfig import get_config_vars
(opt,) = get_config_vars('OPT')
opts = [x for x in opt.split() if "-W" not in x]
os.environ["OPT"] = " ".join(opts)

include_dirs = ['/usr/local/include',"/usr/include/tesseract"]
swig_opts = ["-c++"] + ["-I" + d for d in include_dirs]
swiglib = os.popen("swig -swiglib").read()[:-1]

sources = []

tess = Extension('_tess',
        swig_opts = swig_opts,
        include_dirs = include_dirs,
        libraries = ["tesseract"],
        sources=['tess.i']+sources)

setup (name = 'tess',
       version = '0.0',
       author      = "tmb",
       description = "Tesseract API bindings",
       ext_modules = [tess],
       py_modules = ["tess"],
       )
