from functions import *

while True:
    print("menu:")
    print("1. add score")
    print("2. show scores")
    print("3. delete score")
    print("4. sort scores")
    print("5. average score") 
    print("6. exit")

    choice = input("choose an option: ")

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
        print("goodbye, thanks for using!")
        break
    else:
        print("iinvalid option.\n")
