from collections import Counter

def check():

    dictionary ={
        'CH':'B',
        'HH':'N',
        'CB':'H',
        'NH':'C',
        'HB':'C',
        'HC':'B',
        'HN':'C',
        'NN':'C',
        'BH':'H',
        'NC':'B',
        'NB':'B',
        'BN':'B',
        'BB':'N',
        'BC':'B',
        'CC':'N',
        'CN':'C'
    }
    text = 'NNCB'

    for x in range(10):
        last_string = ''
        for i in range(len(text)-1):
            last_string += text[i]
            last_string += dictionary[text[i] + text[i+1]]
        text = last_string + text[-1]
        #print(text)
    #print(len(text))
    letters = Counter(text)
    #print(letters)
    #b_counts = letters['B']

    max_values_of_letters = max(letters.values())
    min_values_of_letters = min(letters.values())
    result = max_values_of_letters - min_values_of_letters
    print(result)

check()
