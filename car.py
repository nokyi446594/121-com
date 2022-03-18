'''
Created on 14 mar 2022

@author: hui nok yi
'''
def main ():
    instructions = """\nEnter one of the following:
       1 to print all the car praking area in hong kong
       2 to print all valid input data
         3 enter adjustment marks
       4 to print all students overall mark 
       5 to print all students whose mark less than 40
       6 to plot distribution of grade
       Q to end \n"""
    
    while True:
        sys.stderr.flush()    
        sys.stdout.write (instructions)        
        choice = input( "Enter 1 to 6 " ) 
        sys.stdout.flush()
        readData(sys.argv[1])
        
        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":
            printlist(sys.argv[1])
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "Q":
            break  