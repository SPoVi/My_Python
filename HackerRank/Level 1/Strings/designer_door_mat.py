'''
Mr. Vincent works in a door mat manufacturing company. 
One day, he designed a new door mat with the following specifications:

- Mat size must be NxM.(N is an odd natural number, and M is 3 times N.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use |, . and - characters.

'''

'''
txt = 12345

txt.center(15) -> Coje 15 casillas y centra el texto:     _ _ _ _ _ 1 2 3 4 5 _ _ _ _ _

txt.rjust(10)  -> Coje 10 casillas y lo justifica a la derecha:     _ _ _ _ _ 1 2 3 4 5

rxr.ljust(10)  -> Coje 10 casillas y lo justifica a la izquierda:   1 2 3 4 5 _ _ _ _ _

'''



def doorDesign(lines, columns):

    design = '.|.'
    len_design = len(design)
    text = 'WELCOME'
    len_text = len(text)

    for i in range(lines):
        if i <= (lines//2 - 1): # 7 // 2 = 3 - 1 = 2 -> 0, 1, 2
            #print("Linea: {}".format(i+1))
            print(('-').ljust(0)*(lines-(i*len_design)+(lines-len_design)//2)+('.|.').center(0)*(2*i+1)+('-').rjust(0)*(lines-(i*len_design)+(lines-len_design)//2))
            #print(('-').ljust(0)*(lines-(i*3)+2)+('.|.').center(i)*(2*i+1)+('-').rjust(0)*(lines-(i*3)+2))
        
        if i == (lines // 2 ): # 7 // 2 = 3 -> 3
            #print("Linea {}".format(i+1))
            #print(('-').ljust(0)*(lines-(i*3))+('WELCOME').center(0)+('-').rjust(0)*(lines-(i*3)))
            print(('-').ljust(0)*((columns-len_text)//2)+text+('-').rjust(0)*((columns-len_text)//2))
        
        if  i > (lines // 2): # 7 // 2 = 3 -> 4, 5, 6
            #print("Linea: {}".format(i+1))
            result = 2*(lines - i) - 1
            laterales = (columns - len_design*result)//2
            #print("Linea: {}\t i: {}\t result: {}\t laterales: {}".format(lines, i, result, laterales))
            print(('-').ljust(0)*(laterales)+('.|.').center(0)*(result)+('-').rjust(0)*(laterales))
            
def otherSolution(n,m):
    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))             
            
    
   



if __name__ == '__main__':
    print("\nIntroduce N (5 - 101):")
    N = int(input())
    M = N * 3

    doorDesign(N,M)
    
    #print("\n\nSOLUCION 2: ")
    #otherSolution(N,M)

