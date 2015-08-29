# Open files
fo = open("foo.txt", "w+")
f1 = open("n0.txt", "w+")
f2 = open("n1.txt", "w+")
f3 = open("n2.txt", "w+")
f4 = open("n3.txt", "w+")


pm = [200,0,0,0]
lm = [  [0,2,1,1],
        [0.5,0,0,0],
        [0,0.4,0,0],
        [0,0,0.5,0]  ]
for k in range(200):
    rm = [0,0,0,0]
    for j in range(4):
        for i in range(4):
            rm[j] = rm[j] + lm[j][i]*pm[i]
    pm = rm
    
    fo.write(str(sum(pm)));
    fo.write('\n')
    
    f1.write(str(pm[0]));
    f1.write('\n')
    
    f2.write(str(pm[1]));
    f2.write('\n')
    
    f3.write(str(pm[2]));
    f3.write('\n')
    
    f4.write(str(pm[3]));
    f4.write('\n')
    

# Close opened file
fo.close()
f1.close()
f2.close()
f3.close()
f4.close()