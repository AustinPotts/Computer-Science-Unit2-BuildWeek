
# Lecture Coding Challenges 


# Return Yes if  at least one letter in both value are the same
def twoStrings(s1,s2):

    for char in s1:
        if char in s2:
            print("YES")

    return "No"


twoStrings("hello", "hi")    