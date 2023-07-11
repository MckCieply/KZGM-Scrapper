from scrapper import names_of_proceedings

def file_check(new_length):
    with open("proceedings.txt", "r+", encoding="utf-8") as f:
        old_proceedings = f.readlines()
        active_proceedings = names_of_proceedings()
        #Checking for diffrence in length
        old_length = len(old_proceedings)
        if(old_length != new_length):
            for element in active_proceedings:
                f.write(element)

        #if its the same lenght, its checking for diffrences between saved state and scrapped state
        else:
            if(old_proceedings != active_proceedings):
                for element in active_proceedings:
                    f.write(element)
