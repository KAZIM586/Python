# loop side by side program
for i in range(1,6,1):
    for j in range(1,i+1,1):
             print(i,end="")
    for k in range(2*j,20,1):
             print(end=" ")
    for l in range(i,0,-1):
             print(l,end="")
    print("\r")