scores = []

def add_score():
    name = input("Enter player name: ")
    game = input("Enter game name: ")
    while True:
        try:
            score = float(input("Enter score: "))
            break
        except ValueError:
            print("Invalid score. Please enter a number.")
    scores.append({"name": name, "game": game, "score": score})
    print("Score added successfully.")

def show_scores():
    if not scores:
        print("No scores to show.")
        return
    for player in scores:
        print(f"Name: {player['name']}, Game: {player['game']}, Score: {player['score']}")

def delete_score():
    name = input("Enter player name to delete: ")
    for player in scores:
        if player["name"] == name:
            scores.remove(player)
            print(f"{name} removed successfully.")
            return
    print(f"{name} not found.")

def sort_scores():
    print("Sort by:")
    print("1. Name")
    print("2. Game")
    print("3. Score")
    choice = input("Enter your choice: ")

    if choice == "1":
        sorted_list = sorted(scores, key=lambda x: x["name"])
        for p in sorted_list:
            print(p["name"])
    elif choice == "2":
        sorted_list = sorted(scores, key=lambda x: x["game"])
        for p in sorted_list:
            print(p["game"])
    elif choice == "3":
        sorted_list = sorted(scores, key=lambda x: x["score"], reverse=True)
        for p in sorted_list:
            print(f"{p['name']} - {p['score']}")
    else:
        print("Invalid sort option.")

def average_score():
    if not scores:
        print("No scores available.")
        return
    avg = sum(p["score"] for p in scores) / len(scores)
    print(f"Average score: {avg:.2f}")

def edit_score():
    name = input("Enter player name to edit: ")
    for player in scores:
        if player["name"] == name:
            new_game = input("Enter new game name: ")
            while True:
                try:
                    new_score = float(input("Enter new score: "))
                    break
                except ValueError:
                    print("Invalid score. Please enter a number.")
            player["game"] = new_game
            player["score"] = new_score
            print(f"{name}'s score updated.")
            return
    print(f"{name} not found.")
