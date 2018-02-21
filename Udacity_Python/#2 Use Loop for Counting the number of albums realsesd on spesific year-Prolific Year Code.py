# Quiz/code on dictionaynamed "Prolific year"(from Udamy)

def most_prolific(album_dict):
    years_count = {}
    for album in album_dict:
        if album_dict[album] in years_count:
           years_count[album_dict[album]] += 1
        else:
            years_count[album_dict[album]] = 1
    
    max_count = years_count[max(years_count)]
    prolific_years = []
    for year in years_count:
        if years_count[year] == max_count:
            prolific_years.append(year)
    return(prolific_years)

my_album = {"a":1952,"b":1965, "c":1965,"d":1965,"e":1964,"f":1964,"g":1964}
print("My album: ", my_album)
print("Most prolific years are: ", most_prolific(my_album))