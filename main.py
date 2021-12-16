def getOccurrences(input: str) -> str:
    input_map = dict()

    for letter in input:
        if letter in input_map:
            input_map[letter] += 1
        else:
            input_map[letter] = 1
    
    new_filt = dict(filter(lambda val: val[1] > 1, input_map.items()))
    return list(new_filt.keys())[0] if new_filt else 'NULL'

def main():
    test_list = ['tesst', 'ABCA', 'BCABA', 'ABC', 'DBCABA']
    for string in test_list:
        print(f'First occurence in string {string}: ' + getOccurrences(string))    

if __name__ == '__main__':
    main()
    print('Finished main function')