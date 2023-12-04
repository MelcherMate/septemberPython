"""
solution
"""

from importation import data

# 1. How many pages does the book have?

from pages import get_page_number
page_num = get_page_number(data)
print(f"The book contains {page_num} pages.")

# 2. When was the book released?

from release import search_release_date
release_date = search_release_date(data)
print(f'The book was released in {release_date}.')

# 3. What's the title of the book?

from title import search_title
title = search_title(data)
print(f'The title of the book is "{title}".')

# 4. How many words does the book contain?

from words import word_cnt
nb_words = word_cnt(data)
print(f'The "{title}" contains {nb_words} words.')