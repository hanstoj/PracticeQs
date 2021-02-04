# 1/21/2021

# takes in a string returns if it can be made into a palendrome.

# needs to take in a string as an argument
# needs to count each letter 
#check if all letter counts are even
#account for cap and whitespace

# define pal_checker(str)  Hannah 
    # str = str.replace(' ', '' )
    #  letter_dict = {}
    #  for letter in string: 
        # if letter lower  not already in dictionary 
        #  add letter to dict as key value set to one 
    # if keys are all even
        #  return true
    # else
        # return false 

# str = "Hannah"
def pal_checker(str):
    str = str.replace(' ', '')
    str = str.lower()
    letter_dict = {}

    for letter in str:
        if letter not in letter_dict:
            letter_dict[letter] = 1 
        else:
            letter_dict[letter] += 1 
    print(letter_dict)
    for letter in letter_dict:
        print(letter_dict[letter])
        if letter_dict[letter] % 2 != 0:
            return False
    return True
    

print(pal_checker("Hannah") == True)

print(pal_checker("Taco Cat") == True)