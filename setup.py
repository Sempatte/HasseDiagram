#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup
import py2exe
import sys
sys.setrecursionlimit(5000)

setup(name="DoxingFramework",
      include_package_data=True,
      version="1",
      windows=['DiagramaDeHasse.py'],
      options={
          'py2exe': {
              'dll_excludes': ["MSVFW32.dll",
                               "AVIFIL32.dll",
                               "AVICAP32.dll",
                               "ADVAPI32.dll",
                               "CRYPT32.dll",
                               "WLDAP32.dll"]
          }
      })
