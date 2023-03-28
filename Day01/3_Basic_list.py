squares = [1,4,9,16,25]
squares[2:-1]
squares[2:]
squares[1:-1]

cubes = [1,8,27,65,125]
allval = squares+cubes
allval
allval[-2] = 64
allval

allinonelist = [1,4,9,10,11] # 5 items
allinonelist[3] = "Num" # 4th item to string
allinonelist[4] = [2,4,6] # last item to list

allinonelist[3]
allinonelist[4]
allinonelist[4][0] # first item in list

cubes.append(6**3)
cubes
cubes.append(7**3)
cubes
cubes.remove(343) # by item
cubes[3] = 65
cubes


