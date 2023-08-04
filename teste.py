'''string = 'SheikSkullKidGanondorfImpa'
nome = 'Ganodorf'
letra = nome [0]
x = string.split(letra)
print(x)'''

def find_word_in_string(s, word):
    if s == "":
        return False

    x = s[:len(word)]
    if s[:len(word)] == word:
        return True, s

    return find_word_in_string(s[1:], word)

print(find_word_in_string('dGanondorfImpa', 'Ganondorf'))