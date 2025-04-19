import hotpo
import sys


printable="[(0,0)"
if len(sys.argv)>1:
    n=int(sys.argv[1])
    steps=0
    while n!=1:
        steps+=1
        printable+=f",({steps},{n})"
        n=hotpo.hotpo(n)
    printable+=f",({steps},{n})]"
    print(printable)
