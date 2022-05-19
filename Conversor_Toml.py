

import toml

data = toml.load("pyproject.toml.txt")

f = open("pyproject.toml", "w")
toml.dump(data, f)
f.close()
