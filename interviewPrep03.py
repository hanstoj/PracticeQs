#  Given a phrase return a dictionary that has length as a key and a list of words that have that length 

#  Hello Hannah 
#  5:[Hello] 6:[Hannah]

#  it is happy
#  2: [it, is] 
#  5: [happy]
 
#  ""
#  {}

# function takes phrase
# make a dict
# loop that splits
#     check length
#     check if len in dict 
#     if it is add it to the list
#     else add to dict


def create_length_dict(phrase):
    length_dict = {}

    for word in phrase.split():
        length_dict[len(word)] = length_dict.get(len(word), []).append(word)
        
        # length_dict.get(len(word),[word]) = length_dict[len(word)].append(word)
        """
        length_dict = {3:["one"], 4:["five"] }
        "two"
        ["one"] = ["one"].append("two")
        
        """
        # [hello]
        # if len(word) in length_dict:
        #     length_dict[len(word)].append(word)
        # else:
        #     length_dict[len(word)] = [word]
    return length_dict
    
    
print(create_length_dict(""))
        

