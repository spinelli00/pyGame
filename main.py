from functions.functions import niveleasy, nivelhard, clear_display

def menu() :
    while True :
        try :
            print('| Welcome to pyGame ! |')
            nivel = int(input("| Select the nivel (1. Easy | 2. Hard) >> "))
            match nivel:
                case 1 :
                    niveleasy()
                case 2 :
                    nivelhard()
                case _ : 
                    print("Invalid option, Try Again !")
                    clear_display()

        except ValueError :
            print("Invalid option, Try Again !")
            clear_display()

if __name__ == '__main__' :
    menu()
        


