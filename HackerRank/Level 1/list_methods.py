'''
Initialize your list and read in the value of followed by lines of 
commands where each command will be of the types listed above. 

Iterate through each command in order and perform the corresponding 
operation on your list. 

'''

def menu():
    
    print("\n--MENU--\n")
    print("insert i e   - Insert integer 'e' at position i")
    print("print        - Print list")
    print("remove e     - Delete the first occurrence of intefer 'e'")
    print("append e     - Insert integer 'e' at the end of the list")
    print("sort         - Sort the list")
    print("pop          - Pop the las element from the list")
    print("revese       - Reverse the list")

## MAIN
if __name__ == '__main__':
    print("Introduce numero de operaciones: ")
    N = int(input())

    menu()

    # Repetir N veces pedir accion y guardarlo en una lista
    actions_list = []
    for action in range(N):

        print("\nIntroduce opcion: ")
        option = input().split()    # separar entreada 
        actions_list.append(option) # guardar en lista de acciones a realizar

    print("\n\n---Aciones a realizar---\n")
    print(actions_list)


    # Realizar acciones
    my_list = []
    for action in range(N):

        # Insert i e
        if actions_list[action][0] == 'insert':
            pos = int(actions_list[action][1])
            val = int(actions_list[action][2])
            
            my_list.insert(pos,val) # my_list[pos] = val

        # print    
        if actions_list[action][0] == 'print':
            print("\nMy lista: ")
            print(my_list)

        # remove e
        if actions_list[action][0] == "remove":
            val = int(actions_list[action][1])
            my_list.remove(val)
        
        # append e
        if actions_list[action][0] == "append":
            val = int(actions_list[action][1])
            my_list.append(val)
        
        # sort
        if actions_list[action][0] == "sort":
            my_list.sort()
        
        # pop
        if actions_list[action][0] == "pop":
            my_list.pop(-1)

        # reverse
        if actions_list[action][0] == "reverse":
            my_list.reverse()
        

    
  