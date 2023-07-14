from scrapper import count_of_proceedings
from file_worker import file_check, contains_objective
from mail_sender import produce_email

new_length = count_of_proceedings()
old_proceedings = file_check(new_length)

#None is if there is no updates
if old_proceedings != None:
    result = contains_objective(old_proceedings)

    #if there is any fitting proceeding proceed to send email
    if result != []:
        #Recovering links for all fitting proceedings
        links = [link.split('|')[1].split('\n')[0] for link in result]
        produce_email(links)
        
