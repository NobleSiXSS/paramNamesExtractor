import sys
import re

url = sys.argv[1]
params = re.findall("[?&](.*?)=", url)
if(len(sys.argv) > 2):
    file = open(sys.argv[2], "w")
    for param in params:
        file.write(param + "\n")
    file.close()
else:
    for param in params:
        print(param)
