def search_release_date(txt):
    lines = txt.split('\n')
    for line in lines:
        if "Release Date:" in line:
            release_date = line.replace("Release Date:", "").strip()
            if "[" in release_date:
                release_date = release_date[:release_date.index("[")].strip()
            return release_date
    return None

