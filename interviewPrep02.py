# given a phrase print wordcount for each how many times each word appears in alpha order. 

# All Cats are Bad

# All, 1  
# are, 1 
# Bad, 1 
# Cats, 1

# Cats are Cats

# Are, 1
# Cats, 2



# function to take in phrase as an argument
#     create a dict. 

#     loop through the phrase
#         if word has not been scene add to dict add 1
#         if it has add 1 

#     sort dictionary 
#     loop through dict 
#         to print word, value:


def word_count(phrase):
    word_dict= {}
    alpha_words = []
    # don't need this
    # for word in phrase.split():
    #     alpha_words.append(word)


    alpha_words = sorted(alpha_words)
    print(f'alphawords - {alpha_words}')


    for word in phrase.split():
        # print(word)
        # if word in word_dict:
        #     word_dict[word] = word_dict[word] + 1
        # else:
        #     word_dict[word] = 1

        word_dict[word.lower()] = word_dict.get(word, 0) + 1
    sorted_keys = sorted(word_dict)    

    for word in sorted_keys:
        print(f'{word}, {word_dict[word]}')

word_count("Cats are Cats")
    
    
        

    