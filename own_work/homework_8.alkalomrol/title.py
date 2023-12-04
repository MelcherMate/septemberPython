import re

def search_title(txt):
    lines = txt.split('\n')
    for line in lines:
        if "Title:" in line:
            title = line.replace("Title:", "").strip()
            if ", Complete" in title:
                title = title.replace(", Complete", "").strip()
            return title
    return None