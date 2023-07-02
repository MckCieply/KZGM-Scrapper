
def file_update(new_length):
    with open("proceedings.txt", "r+") as f:
        lines = f.readlines()
        old_length = len(lines)
        if(old_length != new_length):
            print("Gotta Update")