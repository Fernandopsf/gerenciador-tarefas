<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 22:41:21 2022

@author: prumo
"""

import toml

data = toml.load("pyproject.toml.txt")

f = open("pyproject.toml", "w")
toml.dump(data, f)
f.close()
=======
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 22:41:21 2022

@author: prumo
"""

import toml

data = toml.load("pyproject.toml.txt")

f = open("pyproject.toml", "w")
toml.dump(data, f)
f.close()
>>>>>>> 9eade0cc3adcbe53f013dc223292e6100cb81cc3
