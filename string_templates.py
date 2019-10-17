import string
template = string.Template("$artist sang $song in $year")
print(template.substitute(artist = "Jaymo", song = "mama mia", year = "1999"))
# take care not to encompass the variable names in quotes

#substituting the variables with new values, simply initiate a new substitute () function
print(template.substitute(artist = "Charlo", song = "keyboard warrior", year ="2019"))

#creating dictionaries in place of the substitute function
d = dict(artist = 'Billy Idol', song = 'Mama Mia', year = '2000')
print(template.substitute(d))
