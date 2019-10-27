'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    return [the_list[0], the_list[-1]]


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):

    end += 1 #includes the end value
   
    if int(end) > int(beginning) and beginning >= 0 and end <= len(the_list):
        reverselist = the_list[beginning:end]
        reverselist.reverse()   
        return reverselist # hint this is incomplete
    else:
        raise ValueError


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    i = 0
    while i < 3:
        the_list.insert(index, the_list[index])
        i += 1
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    revword = ''
    for i in word:
        revword = i + revword  # appending chars in reverse order
    reversetest = word == revword
    return reversetest

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    s = sentence
    s = s.replace(' ', '')
    s = s.lower()
    revsen = ''
    for i in s:
        revsen = i + revsen
    reversetest = s == revsen
    return reversetest

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):

    s1 = sentence1.strip() # remove whitespace
    s2 = sentence2.strip()
    first_letter1 = s1[0]
    first_letter2 = s2[0]
    last_letter1 = s1[-1]
    last_letter2 = s2[-1]

    punct = ['.','?','!']

    is_up_1 = first_letter1.isupper()
    punct_ok_1 = last_letter1 in punct
    is_up_2 = first_letter2.isupper()
    punct_ok_2 = last_letter2 in punct

    # test = first_letter1.isupper() == True and (last_letter1 == '.' or last_letter1 == '?' or last_letter1 == '!') and (first_letter2.isupper() == True and (last_letter2 == '.' or last_letter2 == '?' or last_letter2 == '!')
    # test = (first_letter1.isupper() == True) and (last_letter1 in ['.','?','!']) and (first_letter2.isupper() == True) and (last_letter2 in ['.','?','!'])

    if is_up_1 + punct_ok_1 + is_up_2 + punct_ok_2 == 4:
        combsen = s1 + ' ' + s2
        print(combsen)
        pass #????
    else:
        print('you did it wrong')
        pass #adding pass here and above fixed issue but I don't know why...
    return combsen


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False
    return

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    dictionary1.update(dictionary2)
    return dictionary1
