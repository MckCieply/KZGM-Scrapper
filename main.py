from scrapper import count_of_proceedings
from file_worker import file_check, contains_objective
from mail_sender import produce_email

new_length = count_of_proceedings()
old_proceedings = file_check(new_length)
if old_proceedings != None:
    result = contains_objective(old_proceedings)
    if result == True:
        produce_email()
        
