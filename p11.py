# p1) Create a new file

import os
filename = input("enter filename to be created ")
if os.path.exists(filename):
	print(filename, "already exists ")
else:
	f = None
	try:
		f = open(filename, "a")
		print(filename, " created ")
	except Exception as e:
		print("issue ", e)
	finally:
		if f is not None:
			f.close()