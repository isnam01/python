#!usr/bin/python
from subprocess import check_output

output = check_output('compgen -u', shell=True, executable='/bin/bash')
commands = output.splitlines()
for i in commands:
	print(i)

