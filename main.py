from scrapper import count_of_proceedings
from file_worker import file_check, contains_objective

new_length = count_of_proceedings()
old_proceedings = file_check(new_length)
if old_proceedings != None:
    contains_objective(old_proceedings)
else:
    print("No changes")