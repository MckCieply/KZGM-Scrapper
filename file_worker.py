from scrapper import names_of_proceedings

#Phrase of intrest in proceeding names we are looking for 
phrase = "Remont mieszkań"

def file_check(new_length):
    with open("proceedings.txt", "r+", encoding="utf-8") as f:
        old_proceedings = f.readlines()
        active_proceedings = names_of_proceedings()
        #Checking for diffrence in length
        old_length = len(old_proceedings)

        #if there is diffrent lenght in saved and scrapped state rewrite file
        if(old_length != new_length):
            #truncating file
            f.truncate(0)
            f.seek(0)

            for element in active_proceedings:
                f.write(element)
            return old_proceedings

        #if its the same lenght, its checking for diffrences between saved state and scrapped state
        else:
            #if its same length, but with diffrent proceedings, rewrite file
            if(old_proceedings != active_proceedings):
                #truncating file
                f.truncate(0)
                f.seek(0)

                for element in active_proceedings:
                    f.write(element)
                return old_proceedings

#checking if there were new proceedings of intrest
def contains_objective(old_proceedings):
    with open("proceedings.txt", "r", encoding="utf-8") as f:
        new_proceedings = f.readlines()
        old_intrest = [line for line in old_proceedings if phrase in line]
        new_intrest = [line for line in new_proceedings if phrase in line]
        diffrence = [line for line in new_intrest if line not in old_intrest]
        return diffrence