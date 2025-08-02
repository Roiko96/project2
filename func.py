scores = []

def add_score():
    name = input("Enter player name: ")
    game = input("Enter game name: ")
    while True:
        try:
            score = float(input("Enter score: "))
            break
        except ValueError:
            print("Please enter a number.")
    scores.append({"name": name, "game": game, "score": score})
    print("Score added.")

def show_scores():
    if not scores:
        print("No scores to show.")
        return
    for player in scores:
        print(f"Name: {player['name']}, Game: {player['game']}, Score: {player['score']}")

def delete_score():
    name = input("Enter player name to delete: ")
    for player in scores:
        if player['name'] == name:
            scores.remove(player)
            print(f"{name} removed.")
            return
    print(f"{name} not found.")

def sort_scores():
    print("Sort by:")
    print("1. Name")
    print("2. Game")
    print("3. Score")

    choice = input("Enter your choice: ")

    if choice == "1":
        sorted_list = sorted(scores, key=lambda x: x['name'])
        for p in sorted_list:
            print(p['name'])
    elif choice == "2":
        sorted_list = sorted(scores, key=lambda x: x['game'])
        for p in sorted_list:
            print(p['game'])
    elif choice == "3":
        sorted_list = sorted(scores, key=lambda x: x['score'], reverse=True)
        for p in sorted_list:
            print(p['score'])
    else:
        print("Invalid choice.")

def average_score():
    if not scores:
        print("No scores.")
        return
    avg = sum(p['score'] for p in scores) / len(scores)
    print(f"Average score: {avg:.2f}")

def edit_score():
    name = input("Enter player name to edit: ")
    game = input("Enter game name to edit: ")
    found = False

    for player in scores:
        if player['name'] == name and player['game'] == game:
            print("What would you like to edit?")
            print("1. Name")
            print("2. Game")
            print("3. Score")

            choice = input("Enter your choice: ")

            if choice == "1":
                new_name = input("Enter new name: ")
                player['name'] = new_name
                print("Name updated.")
            elif choice == "2":
                new_game = input("Enter new game name: ")
                player['game'] = new_game
                print("Game updated.")
            elif choice == "3":
                while True:
                    try:
                        new_score = float(input("Enter new score: "))
                        player['score'] = new_score
                        print("Score updated.")
                        break
                    except ValueError:
                        print("Please enter a number.")
            else:
                print("Invalid choice.")

            found = True
            break

    if not found:
        print(f"No entry found for player {name} and game {game}.")
