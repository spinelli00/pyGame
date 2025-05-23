from functions import niveleasy, nivelhard, clear_display

def main() :
    while True :
        try :
            nivel = int(input("Select the nivel (1. Easy | 2. Hard) >> "))
            if nivel == 1 :
                niveleasy()
            elif nivel == 2 :
                nivelhard()
            else : 
                print("Invalid option, Try Again !")
                clear_display()

        except ValueError :
            print("Invalid option, Try Again !")
            clear_display()

if __name__ == '__main__' :
    main()
        


