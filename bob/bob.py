def hey(string):
    if len(string.split()) == 0:
        return "Fine. Be that way!"
    elif all_caps(string):
        return "Whoa, chill out!"
    elif string.split()[-1][-1] == "?":
        return "Sure."
    else:
        return "Whatever."

def all_caps(string):
    have_alpha = False
    for letter in string:
        if letter.isalpha() and letter != letter.upper():
            return False
        elif letter.isalpha():
            have_alpha = True
    return have_alpha
