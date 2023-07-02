from scrapper import active_proceedings
from file_worker import file_update

new_length = active_proceedings()
file_update(new_length)