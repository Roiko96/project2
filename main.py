# main.py
from functions import scores, add_score_data, delete_score_by_name, sort_scores_by_key, calculate_average, edit_score_data

def main():
    while True:
        print("\nMenu:")
        print("1. Add Score")
        print("2. Show Scores")
        print("3. Delete Score")
        print("4. Sort Scores")
        print("5. Average Score")
        print("6. Edit Score")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            game = input("Enter game: ")
            try:
                score = float(input("Enter score: "))
                add_score_data(name, game, score)
            except ValueError:
                print("Invalid score")

        elif choice == "2":
            for s in scores:
                print(f"Name: {s['name']}, Game: {s['game']}, Score: {s['score']}")

        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_score_by_name(name)

        elif choice == "4":
            key = input("Sort by (name/game/score): ")
            sort_scores_by_key(key)

        elif choice == "5":
            avg = calculate_average()
            print(f"Average score: {avg:.2f}")

        elif choice == "6":
            current_name = input("Current name: ")
            current_game = input("Current game: ")
            new_name = input("New name: ")
            new_game = input("New game: ")
            try:
                new_score = float(input("New score: "))
                edit_score_data(current_name, current_game, new_name, new_game, new_score)
            except ValueError:
                print("Invalid score")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
