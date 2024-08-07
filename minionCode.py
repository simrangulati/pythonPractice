# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

def minion_game(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    strLen= len(string)
    kevinScore = StuartScore = 0;
    for i in range(0, strLen):
        if(string[i] in vowels):
            kevinScore += (strLen - i)
        else:
            StuartScore += (strLen - i)
    if(kevinScore == StuartScore):
        print("Draw")
    elif(kevinScore > StuartScore):
        print("Kevin "+str(kevinScore))
    else:
        print("Stuart "+str(StuartScore))
            
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
