current_users = ["Brian", "Nancy", "Pauline", "Okumu", "Piper", "Zack"]
new_users = ["Yvone", "Jacky", "Beatrice", "Brian","Okumu", "pauline"]

for used_name in new_users:
    if used_name in current_users:
        print("{} is already in use, try another name".format(used_name))

