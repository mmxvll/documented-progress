def minion_game(s):
    # Kevin makes words with vowels
    # Stuart makes words with consonants
    # add points and compare results
    subs = list()
    i = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subs.append(s[i:j])
    
    for sub in subs:
    return subs

def find_permutations(string):
    



s = input()
print(minion_game(s))