
# coding: utf-8

# In[6]:

#4.2 (A)
# Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
# Hint:​ ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
#Here 2,3 and 4 are the lengths of the words in the list.
def long_words(str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        word_len.append(len(x))
    return word_len	
print(long_words("The quick brown fox jumps over the lazy dog helloworld"))


# In[11]:

#4.2 (B)
# Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
def long_words(str):
    isVowel = "False"
    txt = str.split(" ")
    for x in txt:
        if len(x)>1:
            print ("invalid character")
        else:
            if x  in 'aeiou' or x  in 'AEIOU':
                isVowel = "True"
            else:
                isVowel = "False"
        #word_len.append(len(x))
    return isVowel	
    
print(long_words("U"))
print(long_words("X"))
print(long_words("A"))
print(long_words("u"))
print(long_words("i"))


# In[ ]:




# In[ ]:



