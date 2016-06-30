import sys

strFromFile = sys.argv[1]
strToFile = sys.argv[2]

print ("Read from " + strFromFile)
print ("Save to " + strToFile)

fp = open(strFromFile, "r")
lines = fp.readlines()
fp.close()

lines.sort()

fp = open(strToFile, "w")
fp.writelines(lines)
fp.close()
