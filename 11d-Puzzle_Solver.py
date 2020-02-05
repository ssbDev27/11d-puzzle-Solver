import timeit
import sys
from heapq import heapify,heappush, heappop

class Setter:
    
    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map


    def __init__(self, state, parent, move, depth, cost, key):

        self.state = state

        self.parent = parent

        self.move = move

        self.depth = depth

        self.cost = cost

        self.key = key

        if self.state:
            self.map = ''.join(str(e) for e in self.state)


goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
goal_node = Setter

global nodes_expanded
nodes_expanded = 0

costs = set()
moves = list()

def ItsTimeforExperiment(time, path):

    global moves
    
    moves = list()

    moves = Traceback_Moves()

    file = open(path, 'w')
    file.write("These are the moves: " + str(moves))
    file.write("\nCost of path: " + str(len(moves)))
    file.write("\nNo of nodes expanded: " + str(nodes_expanded))
    file.write("\nDepth: " + str(goal_node.depth))
    file.write("\nTotal time taken: " + format(time, '.8f'))
    file.close()



def main():
    
    print ('main')
    if len(sys.argv)-1 != 12:
        print( 'Oops! The arguments are not enough to play a 11d Puzzle, Required - 12 and your : '+ str(len(sys.argv)-1))
        exit()
    
    global inputlist
    inputlist=[]

    for i in range(0,12):
        inputlist.append(int(sys.argv[i+1]))

    global alpha_position
    alpha_position={}
    
    alpha_position[0]='a'
    alpha_position[1]='b'
    alpha_position[2]='c'
    alpha_position[3]='d'
    alpha_position[4]='e'
    alpha_position[5]='f'
    alpha_position[6]='g'
    alpha_position[7]='h'
    alpha_position[8]='i'
    alpha_position[9]='j'
    alpha_position[10]='k'
    alpha_position[11]='l'


    print ('calling bst for h1')
    file = open('puzzleBFS-h1.txt', f'w')
    starttime = timeit.default_timer()
    output = bst(inputlist,h1,file,alpha_position)
    stoptime = timeit.default_timer()
    file.close()
    ItsTimeforExperiment(stoptime-starttime,'Experiment-output-BestFirst-h1.txt')

    goal_node = Setter
    moves = list()
    costs = set()
    global nodes_expanded
    nodes_expanded = 0


    print ('calling bst for h2')
    file = open('puzzleBFS-h2.txt', 'w')
    starttime = timeit.default_timer()
    output = bst(inputlist,h2,file,alpha_position)
    stoptime = timeit.default_timer()
    file.close()
    ItsTimeforExperiment(stoptime-starttime,'Experiment-output-BestFirst-h2.txt')
    
    goal_node = Setter
    moves = list()
    costs = set()
    nodes_expanded = 0

    #print (algo.lower())  
    print ('calling ast for h1')  
    file = open('puzzleAs-h1.txt', 'w')
    starttime = timeit.default_timer()
    output = ast(inputlist,h1,file,alpha_position)
    stoptime = timeit.default_timer()
    file.close()
    ItsTimeforExperiment(stoptime-starttime,'Experiment-output-Astar-h1.txt')
    
    goal_node = Setter
    moves = list()
    costs = set()
    nodes_expanded = 0

    #print (algo.lower())  
    print ('calling ast for h2')  
    file = open('puzzleAs-h2.txt', 'w')
    starttime = timeit.default_timer()
    output = ast(inputlist,h2,file,alpha_position)
    stoptime = timeit.default_timer()
    file.close()
    ItsTimeforExperiment(stoptime-starttime,'Experiment-output-Astar-h2.txt')

    print ('calling dfs')
    file = open('puzzleDFS.txt', 'w')
    starttime = timeit.default_timer()
    output = dfs(inputlist,file,alpha_position)
    stoptime = timeit.default_timer()
    file.close()
    ItsTimeforExperiment(stoptime-starttime,'Experiment-output-dfs.txt')


def dfs(inputlist,file,alpha_position):

    closedlist= set()
    stack = list([Setter(inputlist, None, None, 0, 0, 0)])
    
    first_time=True
    while stack:

        node = stack.pop() #stack open list

        closedlist.add(node.map) 
        #print(node.state)
        if first_time:
           file.write("0 " + str(node.state)+'\n') 
           print("0 " + str(node.state)+'\n')
           first_time=False
        else:
           file.write(str(alpha_position[node.state.index(0)])+ " " + str(node.state)+'\n')
           print(str(alpha_position[node.state.index(0)])+ " " + str(node.state)+'\n')
           #exit()


        if node.state == goal_state:
            goal_node = node
            return stack

        children = reversed(getChildNodes(node))

        for child in children:
            #print("child")
            #print (str(child.state))
            if child.map not in closedlist and child not in stack:
                    stack.append(child)
                    
def move(state, pos):

    new_position = state[:] #empty state
 
    zero_index = new_position.index(0) #getting index of blank space
   
    if pos == 1:  # Up

        if zero_index not in range(0, 4): 
            
            new_position[zero_index - 4], new_position[zero_index]= new_position[zero_index] , new_position[zero_index - 4]

            return new_position
        else:
            return None

    if pos == 2:  # Up-Right

        if (zero_index not in range(0, 4)) and (zero_index not in range(3, 12, 4)): 
            
            new_position[(zero_index - 4)+1], new_position[zero_index] = new_position[zero_index] , new_position[(zero_index - 4)+1]

            return new_position
        else:
            return None

    if pos == 3:  # Right
                              
        if zero_index not in range(3, 12, 4): 

            new_position[zero_index + 1] , new_position[zero_index] = new_position[zero_index] , new_position[zero_index + 1]
            
            return new_position
        else:
            return None

    if pos == 4:  # Down-Right 
                          
        if (zero_index not in range(8, 12)) and zero_index not in range(3, 12, 4) : 
            
            new_position[(zero_index + 4)+1], new_position[zero_index] = new_position[zero_index] , new_position[(zero_index + 4)+1]
            
            return new_position
        else:
            return None

    if pos == 5:  # Down   
                      
        if zero_index not in range(8, 12): 
           
            new_position[zero_index + 4] , new_position[zero_index] = new_position[zero_index] , new_position[zero_index + 4]
            
            return new_position
        else:
            return None

    if pos == 6:  # Down-Left   
                           
        if zero_index not in range(8, 12) and zero_index not in range(0, 12, 4): 

            new_position[(zero_index + 4)-1] , new_position[zero_index] = new_position[zero_index] , new_position[(zero_index + 4)-1]
            
            return new_position
        else:
            return None


    if pos == 7:  # Left       
                                   
        if zero_index not in range(0, 12, 4): 

            new_position[zero_index - 1] , new_position[zero_index] = new_position[zero_index] , new_position[zero_index - 1]

            return new_position
        else:
            return None

    if pos == 8:  # Up-Right

        if (zero_index not in range(0, 4)) and zero_index not in range(3, 12, 4) : 

            new_position[(zero_index - 4)-1] , new_position[zero_index] = new_position[zero_index] , new_position[(zero_index - 4)-1]

            return new_position
        
        else:
            return None

                   
               
def getChildNodes(node):

    global nodes_expanded
    
    nodes_expanded += 1

    Children = list()
    
    Children.append(Setter(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    Children.append(Setter(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    Children.append(Setter(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    Children.append(Setter(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    Children.append(Setter(move(node.state, 5), node, 5, node.depth + 1, node.cost + 1, 0))
    Children.append(Setter(move(node.state, 6), node, 6, node.depth + 1, node.cost + 1, 0))
    Children.append(Setter(move(node.state, 7), node, 7, node.depth + 1, node.cost + 1, 0))
    Children.append(Setter(move(node.state, 8), node, 8, node.depth + 1, node.cost + 1, 0))

    returnedchildNodes=[]
    
    for child in Children:
        if child.state:
            #print(child.state)
            returnedchildNodes.append(child)

    return returnedchildNodes


def h2(state):
    
    grand_sum=0
    #print(state)
    for i in range(0,12):
        sum=0
        index_of_i=state.index(i)
        if i!=0:
            for j in range (index_of_i+1,12):
                if state[j]<i and state[j]!=0:
                    sum=sum+1
         
            #print("sum for "+str(i)+" = "+str(sum))        
        
            grand_sum=grand_sum+sum
    #print("grandsum= "+str(grand_sum))
    return grand_sum


def h1(state):
    
    a=0
    
    for i in range(1, 12):
        b=state.index(i)
        g=goal_state.index(i)
        a=a+abs(b % 4 - g % 4) + abs(b//4 - g//4)
        
        
    return a    

def bst(inputlist,h,file,alpha_position):
    
    #import pudb; pu.db
    global goal_node

    closedlist=set()
    openlist = list()
    hashmap = {} #dictionary
    
    key = h(inputlist)
    

    root = Setter(inputlist, None, None, 0, 0, key)

    hn = (key, root) #(h(n),cost,state{start,child1.....etc})

    heappush(openlist, hn) 
    
    first_time=True
    while openlist:

        node = heappop(openlist) #(node = h(n),cost,state{start,child1.....etc}))
        closedlist.add(node[1].map) # closed list - node[2] = state{start,child1.....etc}
        #exit()
        
        if first_time:
           file.write("0 " + str(node[1].state)+'\n')
           print("0 " + str(node[1].state)+'\n') 
           first_time=False
        else:
           file.write(str(alpha_position[node[1].state.index(0)])+ " " + str(node[1].state)+'\n')
           print(str(alpha_position[node[1].state.index(0)])+ " " + str(node[1].state)+'\n') 
           
        if node[1].state == goal_state:
            goal_node = node[1]
            return openlist          #open list

        children = getChildNodes(node[1])

        for child in children:
            child.key= h(child.state)
            
            hn = (child.key, child) 

            if child.map not in closedlist:

                heappush(openlist, hn)  #added into closed list

                closedlist.add(child.map)

                heapify(openlist)


def ast(inputlist,h,file,alpha_position):
    
    #import pudb; pu.db
    closedlist= set()
    openlist= list()

    key = h(inputlist)

    root = Setter(inputlist, None, None, 0, 0, key)

    fn = (key, 0, root) #(h(n),cost,state{start,child1.....etc})

    heappush(openlist, fn) 
    
    first_time=True
    
    while openlist:

        node = heappop(openlist) #(node = h(n),cost,state{start,child1.....etc}))
        closedlist.add(node[2].map) # closed list - node[2] = state{start,child1.....etc}
        #exit()
        
        if first_time:
           file.write("0 " + str(node[2].state)+'\n') 
           print("0 " + str(node[2].state)+'\n') 
           first_time=False
        else:
           file.write(str(alpha_position[node[2].state.index(0)])+ " " + str(node[2].state)+'\n')
           print(str(alpha_position[node[2].state.index(0)])+ " " + str(node[2].state)+'\n')
        
        if node[2].state == goal_state:
            goal_node = node[2]
            return openlist          #open list

        children = getChildNodes(node[2])

        for child in children:
            
            child.key = child.cost + h(child.state) # f(n) = g(n) + h(n)

            fn = (child.key, child.move, child) 

            if child.map not in closedlist:

                heappush(openlist, fn)  #added into closed list

                closedlist.add(child.map)



def Traceback_Moves():

    current_node = goal_node

    while inputlist != current_node.state:

        if current_node.move == 1:
            movement = 'UP'
        elif current_node.move == 2:
            movement = 'UP-RIGHT'
        elif current_node.move == 3:
            movement = 'RIGHT'
        elif current_node.move == 4:
            movement = 'DOWN-RIGHT'
        elif current_node.move == 5:
            movement = 'DOWN'
        elif current_node.move == 6:
            movement = 'DOWN-LEFT'     
        elif current_node.move == 7:
            movement = 'LEFT'            
        elif current_node.move == 8:
            movement = 'UP-LEFT'            

        moves.insert(0, movement) #inserting the movement at first postiion
        current_node = current_node.parent 

    return moves


if __name__ == '__main__':
    main()