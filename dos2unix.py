#! /usr/bin/env python
'''
dos2unix.py dos to unix or unix to dos file converter
'''
def dos2unix(name):
	data = open(name, 'r').read()
	open(name, 'w').write(data.replace('\r\n', '\n' ))

def unix2dos(name):
	data = open(name, 'r').read()
	open(name, 'w').write(data.replace('\n', '\r\n'))

def help():
	print 'dos2unix.py'
	print 'Arguments: dos2unix.py fileName [option]'
	print 'Options:'
	print '-d 	Default, dos to unix file conversion'
	print '-u 	unix to dos conversion'


if __name__ == '__main__':
	'''
	Arguments: dos2unix.py fileName [option]
	Options:
		-d 		Default, convert dos file to unix
		-u 		Convert unix file to dos
	'''
	import sys
	if len(sys.argv) in [2, 3]:
		if len(sys.argv) == 2:
			pass
		elif sys.argv[2] == '-d':
			dos2unix(sys.argv[1])
		elif sys.argv[2] == '-u':
			unix2dos(sys.argv[1])
		else:
			help()
	else:
		help()
		