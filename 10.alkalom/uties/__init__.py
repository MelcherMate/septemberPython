"""
The __init__.py file's tasks:

    - lower the depth of imports
    - controll the visibility -> namespace use
    - the code can offer the instantly avialabe moduls, variables, functions ...

"""

from .file_handler import get_data_from_txt, write_json
from .statistics import (get_book_title,
                         get_page_number,
                         get_release_date,
                         count_line, 
                         count_words)