with open('aoc_test1.txt') as f:
    lines = [int(line.rstrip()) for line in f]

def sum_():
    total = 0
    m = len(lines) 
    for pos, i in enumerate(lines):
        if pos + 1 < m:
            if i < lines[pos +1]:
                total += 1
        else:
            print(total)
        
# print(lines)
#terrible memory use by calling multiple indexes for each iteration lol
def sum_2():
    total = 0
    m = len(lines)
    for pos, i in enumerate(lines):
        if pos + 3 < m:
            t1 = i + lines[pos+1] + lines[pos+2]
            t2 = lines[pos+1] + lines[pos+2]+ lines[pos+3]
            if t1 < t2:
                total += 1
    print (total)


# sum_()    
# sum_2()
