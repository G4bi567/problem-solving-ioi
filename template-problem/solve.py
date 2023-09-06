'''

Template for France-IOI programming tasks with debugger in gitpod

The Python version on gitpod is 3.11, whereas the python version on france-ioi
is sadly stuck at 3.4.2 ... This means no type hints, no dataclasses, ... The
code should therefore remain pretty basic to run flawlessly on france-ioi

'''

######################## Tests ###############################
try:
    from soiutils import load_test
    load_test('test1')
except:
    pass
######################## Tests ###############################
    
from collections import namedtuple

Problem = namedtuple('Problem', [])

    


def parse_input():
    '''
    
    Parses the input data and returns a dictionary with everything
    well structured.
    
    '''
    lignes = [int(x) for x in input().split(" ")]
    plan = []
    for _ in range(lignes[0]):  
        plan.append([int(x) for x in input().split(" ")])
    biggestside=0
    return 

def solve(problem):
    def gothrough(lignes, plan, biggestside):
        for y in range(lignes[0]):
            for x in range(lignes[1]):
                if plan[y][x]==0:
                    side = findside(y,x,lignes,plan)
                    if biggestside < side:
                    square = searchforsquare(x,y,side,plan,lignes)
                    if square == True:
                        biggestside = side
        return biggestside 
    
    def findside(y,x,lignes,plan):   
        counter = 1
        x1=1
        while x + x1 < lignes[1] and plan[y][x + x1] == 0:
            counter += 1
            x1 += 1
        return counter 

    def searchforsquare(x,y,counter,plan,lignes):
        for y1 in range(counter):
            for x1 in range(counter):
                if y+y1 == lignes[0]:
                    return False
                elif plan[y+y1][x+x1]==1:
                    return False
   return True
    
    return result
        
    
    
def output(result):
    for r in result:
        print(r)
    
            


if __name__ == '__main__':
    problem = parse_input()
    result = solve(problem)
    output(result)