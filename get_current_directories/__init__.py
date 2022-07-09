import os
from fnmatch import fnmatch
import pandas as pd

root = os.getcwd()
pattern = "*"

data = {
	"files": []
}

df = pd.DataFrame(data)

for path, subdirs, files in os.walk(root):
	for name in files:
		if fnmatch(name, pattern):
			print(os.path.join(path, name))
			df = df.append({"files": os.path.join(path, name)}, ignore_index=True)

df.to_csv('list_of_dirs.csv', sep=',', encoding='utf-8')
