import sys
from hotpo import hotpo

memory={1:0}


def checklife(num):
    if num in memory:
        return memory[num]
    else:
        memory[num]=checklife(hotpo(num))+1
        return memory[num]
    
ending=1000
if len(sys.argv)>1:
    ending=int(sys.argv[1])

output="["

for i in range(1,ending):
    output+=f"({i},{checklife(i)}),"
output+="(0,0)]"
print(output)