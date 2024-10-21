#defining the function
    
def mine_function(two_d_list):
    # #=mine and -=no mine
    # square 2d list
    return_list = []
    test = [[0,0,0],[1,1,1],[2,2,2]]
    for i in range(len(two_d_list)): #iterate through the lists contained in two_d_list
        return_sublist = []
        for j in range(len(two_d_list)): #iterate through each sub-list
            
            mine_count = 0
            #print(i,j)
            #the corner cases would be exceptions as they have only 3 positions next to them
            if j == 0 and i == 0: #top left
                #check right, check lower right, check below
                if two_d_list[i+1][j] == '#':
                    mine_count = mine_count + 1
                if two_d_list[i][j+1] == '#':
                    mine_count = mine_count + 1
                if two_d_list[i+1][j+1] == '#':
                    mine_count = mine_count + 1
            elif j == 0 and i == len(two_d_list)-1: #bottom left
                #check right, check above, check upper right
                if two_d_list[i-1][j] == '#':
                    mine_count = mine_count + 1
                if two_d_list[i][j+1] == '#':
                    mine_count = mine_count + 1
                if two_d_list[i-1][j+1] == '#':
                    mine_count = mine_count + 1
            elif j == len(two_d_list)-1 and i == 0: #top right
                #check left, check below, check lower left
                if two_d_list[i+1][j] == '#':
                    mine_count = mine_count + 1
                if two_d_list[i][j-1] == '#':
                    mine_count = mine_count + 1
                if two_d_list[i+1][j-1] == '#':
                    mine_count = mine_count + 1  
            elif j == len(two_d_list)-1 and i == len(two_d_list)-1: #bottom right
                #check above, upper left, left
                if two_d_list[i-1][j] == '#':
                    mine_count = mine_count + 1
                if two_d_list[i][j-1] == '#':
                    mine_count = mine_count + 1
                if two_d_list[i-1][j-1] == '#':
                    mine_count = mine_count + 1 
             #now consider non-corner cases:
            else:
                #edge positions are also exceptions as they have only 5 positions next to them
                if i == 0:
                    #check right, left, check lower right, lower left, check below
                    if two_d_list[i+1][j] == '#':
                        mine_count = mine_count + 1
                    if two_d_list[i][j+1] == '#':
                        mine_count = mine_count + 1
                    if two_d_list[i+1][j+1] == '#':
                        mine_count = mine_count + 1
                    if two_d_list[i][j-1] == '#':
                        mine_count = mine_count + 1
                    if two_d_list[i+1][j-1] == '#':
                        mine_count = mine_count + 1
                elif j == 0: 
                    #check right, upper right, lower right, above, below
                    if two_d_list[i+1][j] == '#': #below
                        mine_count = mine_count + 1
                    if two_d_list[i][j+1] == '#': #right
                        mine_count = mine_count + 1
                    if two_d_list[i+1][j+1] == '#': #lower right
                        mine_count = mine_count + 1
                        mine_count = mine_count + 1
                    if two_d_list[i-1][j] == '#': #above
                        mine_count = mine_count + 1
                    if two_d_list[i-1][j+1] == '#': #upper right
                        mine_count = mine_count + 1
                elif i == len(two_d_list)-1:
                    #check right, left, check upper right, upper left, check above
                    if two_d_list[i-1][j] == '#': #above
                        mine_count = mine_count + 1
                    if two_d_list[i-1][j+1] == '#': #upper right
                        mine_count = mine_count + 1
                    if two_d_list[i-1][j-1] == '#': #upper left
                        mine_count = mine_count + 1
                    if two_d_list[i][j+1] == '#': #right
                        mine_count = mine_count + 1
                    if two_d_list[i][j-1] == '#': #left
                        mine_count = mine_count + 1
                elif j == len(two_d_list)-1:
                    #check left, upper left, lower left, above, below
                    if two_d_list[i][j-1] == '#': #left
                        mine_count = mine_count + 1
                    if two_d_list[i+1][j-1] == '#': #lower left
                        mine_count = mine_count + 1
                    if two_d_list[i-1][j] == '#': #above
                        mine_count = mine_count + 1
                    if two_d_list[i-1][j-1] == '#': #upper left
                        mine_count = mine_count + 1
                    if two_d_list[i+1][j] == '#': #below
                        mine_count = mine_count + 1
                else:
                    #check all
                    if two_d_list[i+1][j] == '#': #below
                        mine_count = mine_count + 1
                    if two_d_list[i][j+1] == '#': #right
                        mine_count = mine_count + 1
                    if two_d_list[i+1][j+1] == '#': #lower right
                        mine_count = mine_count + 1
                    if two_d_list[i][j-1] == '#': #left
                        mine_count = mine_count + 1
                    if two_d_list[i+1][j-1] == '#': #lower left
                        mine_count = mine_count + 1
                    if two_d_list[i-1][j] == '#': #above
                        mine_count = mine_count + 1
                    if two_d_list[i-1][j+1] == '#': #upper right
                        mine_count = mine_count + 1
                    if two_d_list[i-1][j-1] == '#': #upper left
                        mine_count = mine_count + 1
            if two_d_list[i][j] == '-':
                return_sublist.append(mine_count) #append mine count to the sublist for eaxh value of j
            elif two_d_list[i][j] == '#':
               return_sublist.append('#') #if there is a mine in the space, add '#' to the sublist
            print(f' return sublist = {return_sublist}')
        return_list.append(return_sublist) #append the sublist to the main list for each value of i
        print(f'return list = {return_list}')
    print(return_list)
    return return_list
            
   
            
test_list = [['#','-','-', '-'],['#','#','#', '-'],['-','#','-','#'], ['#', '#', '-','-']]
mine_function(test_list)
                    
            
                  
                
                
