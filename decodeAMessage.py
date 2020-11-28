#!/usr/bin/env python
# coding: utf-8

# In[5]:


#! - python3
# - Decoding a Message originally written in figures

scrambledText = input('Enter Scrambled Message: ')
scrambledList = scrambledText.split(',') # - creates a list of the scrambled numbers

decodedMessage = ''

# - lists of modes
uppercase = ['-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
punctuation = ['-', '!', '?', ',', '.', ' ', ';', '"', '\'']

UPPERCASE_MOD = 27 # - modular number for uppercase
LOWERCASE_MOD = 27 # - modular number for lowercase
PUNCTUATION_MOD = 9 # - modular number for punctuation

modes = ['uppercase', 'lowercase', 'punctuation'] # - 3 modes that exists in order
switchCount = 0

# - Iterating over the scrambledList[list]
for number in scrambledList:
    modeIndex = switchCount % 3 # - defines the index of the current mode in the modes[list]
    currentMode = modes[modeIndex]
    
    # - In UPPERCASE mode----------------------------------
    if currentMode == 'uppercase':
        letterIndex = int(number) % UPPERCASE_MOD
        if letterIndex == 0:
            switchCount += 1
            continue
        else:
            letter = uppercase[letterIndex]
            decodedMessage += letter
            continue
    
    # - In LOWERCASE mode ---------------------------------
    elif currentMode == 'lowercase':
        letterIndex = int(number) % LOWERCASE_MOD
        if letterIndex == 0:
            switchCount += 1
            continue
        else:
            letter = lowercase[letterIndex]
            decodedMessage += letter
            continue
    
    # - In PUNCTUATION mode ------------------------------
    elif currentMode == 'punctuation':
        punctuationIndex = int(number) % PUNCTUATION_MOD
        if punctuationIndex == 0:
            switchCount += 1
            continue
        else:
            punct = punctuation[punctuationIndex]
            decodedMessage += punct
            continue
# - End of for loop

print('\n-Decoded Message = [' + decodedMessage + ']')


# In[ ]:




