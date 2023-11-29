from itertools import product

def generate_words(characters, n):
    # Use itertools.product to generate all combinations of characters of length n
    combinations = product(characters, repeat=n)
    
    # Join each combination to form a string and add it to the result list
    result = [''.join(combination) for combination in combinations]
    
    return result

