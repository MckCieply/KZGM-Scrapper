from scrapper import count_of_proceedings
from file_worker import file_check

new_length = count_of_proceedings()
file_check(new_length)