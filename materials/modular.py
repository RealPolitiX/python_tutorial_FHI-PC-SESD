#! /usr/bin/env python

import pkgutil

def findmodule(package):
    try:
        for _, modname, _ in pkgutil.iter_modules(package.__path__):
            if not modname.startswith('_'):
                print("scipy.{}".format(modname))
    except:
        raise Exception('Input needs to be a module with a __path__ attribute !')
    
    return