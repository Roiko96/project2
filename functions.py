scores = []

def add_score():
  name = input("enter player name:")
  game = input("enter game name:")
  while True:
    try:
      score = float(input("enter score:"))
      break
    except ValueError:
      print("enter only num")
  scores.append({"name": name, "game": game, "score": score})

def show_scores():
  if not scores:
    print("no scores")
    return
  for player in scores:
    print(f"name: {player['name']}, game: {player['game']}, score: {player['score']}")

def delete_score():
  name = input("enter player name to delete:")
  if player["name"] == name:
    scores.remove(player)
    print(f" {name} removed")
    return
    print (f" {name} not founhd")

def sort_scores():
  print("sort by:")
  print("1. name")
  print("2. game")
  print("3. score")
  choice = input("enter your chiice please: ")

  if choice == "1": 
    sorted_list = sorted(scores, key=lambda x: x["name"])
    print("sorted names:")
    for p in sorted_list:
      print(p["name")
  elif choice == "2":
    sorted_list = sorted(scores, key=lambda x: x["game"])
    print("sorteg games:")
    for p in sorted_list:
      print(p["game"])
  elif choice == "3":
    sorted_list = sorted(scores, key=lambda x: x["score"])
    print("sorted scores:")
    for p in sorted_list:
      print(p["score"])
def average_score():
  if not scores:
    print("no scores")
    return
  avg = sum(p["score"]) for p in scores) / len(scores)
  print(f" {avg:.2f}")
def edit_score():
  name = input("enter name to edit:")
  game = input("enter game to edit his name:")
  found = False

  for player in scores:
    if player["name"] == name and player["game"] == game:
      print("what to edit?")
      print("1. name")
      print("2. game")
      print("3. score")
      choice = input("enter choice:")

      if choice == "1":
        new_name = input("new name:")
        player["name"] = new_name
        print("name updated")
      elif choice == "2":
        new_game = input("new game:")
        player["game"] = new_game
        print("game name updated")
      elif choice == "3":
        while True:
          try:
            new_score = float(input("enter new score:"))
            player["score"] = new_score
            print("score updated")
      else:
        print("invalid choice")

        found = True
        break
  if not found:
    print(f"player {name} not found")
    
                    
