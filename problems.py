import re


def problem1(searchstring):
    """
    Match emails.

    :param searchstring: string
    :return: 'valid' or invalid
    """
    check_email = r"^[1-7]\d{2}\.[a-zA-Z]{1,10}\d*@(?:sheild\.gov|avengers\.com)$" 
    # ^ start of string
    # [1-7]\d{2} mathcehs number between 100 - 799 since checks start of number only
    # \. checks for a period
    # [a-zA-Z]{1,10} matches a name of upper or lower case letters at least 1 but no more than 10 letters
    # \d* matches any amount of numbers following the letters of the name
    # (?:sheild\.gov|avengers\.com) matches either "sheild.gov OR avengers.com"
    # $ end of the string
    
    if re.match(check_email, searchstring):
        return "valid"
    else:
        return "invalid"
    




def problem2(searchstring):
    """
    Extract Hero Name and vehicle.

    :param searchstring: string
    :return: tuple
    """
    check_transcript =  r"([A-Z][a-z]*( [A-Z][a-z]*)?) (rides|flies) a ([A-Z][a-z]*(( [A-Z][a-z]*)?)|([A-Z][a-zA-Z]*|[a-z]+))"
    #r"([A-Z][a-z]*( [A-Z][a-z]*)?) (rides|flies) a ([A-Z][a-zA-Z]*|[a-z]+)"
    #(?:a )?
    # ^ matches the start of the string
    # ([A-Z][a-z]* ?[A-Z]?[a-z]*) The name can be one word or two words,each word starts with a capital letter.
    #(?:a )? matches "a " if it is present
    # ([A-Z][a-zA-Z]*|[a-z]+) matches the spaceship.
    
    match = re.search(check_transcript, searchstring) # check for a match so you know what to return
    if match:
        person = match.group(1)
        vehicle = match.group(4)
        person = " ".join(person.split()) #removes extra spaces
        vehicle = " ".join(vehicle.split()) #removes extra spaces
    #.split creates substirngs the sperator is a white space character
        return person, vehicle
    else:
        return "nohero", "noname"
    




def problem3(searchstring):
    """
    Boy/Girl or boy/gir with Man/Woman.

    :param searchstring: string
    :return: string
    """
    
    check_audio = r'([A-Z][a-z]*)\s+(Boy|Girl|boy|girl)\b'
    # [A-Z][a-z]*): matches a name that starts with a capital letter
    # \s+(Boy|Girl|boy|girl)\b: matches the gender word. 
    match = re.search(check_audio, searchstring)
    if match:
        name, gender = match.groups()
        if name:
            return searchstring.replace(match.group(0), f"{name} {'Man' if gender in ('Boy', 'boy') else 'Woman'}")
    return "nomatch"
    


if __name__ == '__main__':
    #Added nomatch test cases for Problem 2 and 3
    print("\nProblem 1:")
    testcase11 = '123.iamironman@avengers.com'
    print("Student answer: ",problem1(testcase11),"\tAnswer correct?", problem1(testcase11) == 'valid')

    testcase12 = '250.Srogers1776@avengers.com'
    print("Student answer: ",problem1(testcase12),"\tAnswer correct?", problem1(testcase12) == 'valid')

    testcase13 = '100.nickfury@sheild.gov'
    print("Student answer: ",problem1(testcase13),"\tAnswer correct?", problem1(testcase13) == 'valid')

    testcase14 = '144.venom@avengers.comasdf'
    print("Student answer: ",problem1(testcase14),"\tAnswer correct?", problem1(testcase14) == 'invalid')

    testcase15 = '942.hyperion@avengers.com'
    print("Student answer: ",problem1(testcase15),"\tAnswer correct?", problem1(testcase15) == 'invalid')

    testcase16 = '567.greengoblin@sheild.gov'
    print("Student answer: ",problem1(testcase16),"\tAnswer correct?", problem1(testcase16) == 'invalid')

    testcase17 = '324drdoom324@avengers.com'
    print("Student answer: ",problem1(testcase17),"\tAnswer correct?", problem1(testcase17) == 'invalid')

    testcase18 = '765.Hosborn*876@sheild.gov'
    print("Student answer: ",problem1(testcase18),"\tAnswer correct?", problem1(testcase18) == 'invalid')

    testcase19 = '234.vulture@sheild.com'
    print("Student answer: ",problem1(testcase19),"\tAnswer correct?", problem1(testcase19) == 'invalid')

    print("\nProblem 2:")
    testcase21 = "Captain America rides a Harley"
    print("Student answer: ",problem2(testcase21),"\tAnswer correct?", problem2(testcase21) == ("Captain America","Harley"))

    testcase22 = "No one rides a Harley like Ghost Rider, athough Spider Man rides a Harley with some similar expertise"
    print("Student answer: ",problem2(testcase22),"\tAnswer correct?", problem2(testcase22) == ("Spider Man", "Harley"))

    testcase23 = "Groot rides a spaceship"
    print("Student answer: ", problem2(testcase23), "\tAnswer correct?", problem2(testcase23) == ("Groot", "spaceship"))

    testcase24 = "Starlord flies a Milano"
    print("Student answer: ",problem2(testcase24),"\tAnswer correct?", problem2(testcase24) == ("Starlord", "Milano"))

    testcase25 = "The Starlord flies many ships, but Rocket flies a Warbird Special much faster"
    print("Student answer: ",problem2(testcase25),"\tAnswer correct?", problem2(testcase25) == ("Rocket", "Warbird Special"))

    testcase26 = "Spider Man flies through the city"
    print("Student answer: ",problem2(testcase26),"\tAnswer correct?", problem2(testcase26) == ("nohero", "noname"))


    print("\nProblem 3:")
    testcase31 = 'Spider Boy, I need help!'
    print("Student answer: ",problem3(testcase31),"\tAnswer correct?", problem3(testcase31) == "Spider Man, I need help!")

    testcase32 = 'There is a boy trapped in a burning building Iron Boy'
    print("Student answer: ",problem3(testcase32),"\tAnswer correct?", problem3(testcase32) == "There is a boy trapped in a burning building Iron Man")

    testcase31 = 'Spider Girl, I need help!'
    print("Student answer: ",problem3(testcase31),"\tAnswer correct?", problem3(testcase31) == "Spider Woman, I need help!")

    testcase34 = 'The Invisible girl is a member of the Fantastic Four'
    print("Student answer: ",problem3(testcase34),"\tAnswer correct?", problem3(testcase34) == "The Invisible Woman is a member of the Fantastic Four")

    testcase35 = 'There is a boy that needs to be saved from the alien!'
    print("Student answer: ",problem3(testcase35),"\tAnswer correct?", problem3(testcase35) == "nomatch")