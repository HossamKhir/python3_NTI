#! /usr/bin/python3

f = open("test.txt")
print(f.readline())
print(f.readlines())
printf(f.read())
#	f.readlines(<index>)

#	PERMISSIONS
# input_file = open("in.txt")
# output_file = open("out.txt","w")
#	r:read,	w:write,	a:append

# in C, it is of most important to close the file after finishing working on it
f.close()