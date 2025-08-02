from func import *

def main():
    while True:
        print("Gamescore board menu:")
        print("1. add sccore")
        print("2. show scores")
        print("3. delete score")
        print("4. sort scores")
        print("5. average score")
        print("6. edit score")
        print("7. exit")

        choice = input("enter choice:")
       
        if choice == "1":
            add_score()
        elif choice == "2":
            show_scores()
        elif choice == "3":
            delete_score()
        elif choice == "4": 
            sort_scores()
        elif choice == "5":
            average_score()
        elif choice == "6":
            edit_score()
        elif choice == "7": 
            print ("bye bye")
            break
        else:
            print("invalid choice try again")
if __name__ == "__main__":
    main()