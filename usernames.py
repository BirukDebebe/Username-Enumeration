from itertools import product

def variants(word):
    return [word, word.capitalize(), word.upper()]

names = ['john']
roles = ['administratior', 'admin','ad']
separators = ['', '.', '_']

with open('username.txt', 'w') as f:
    for n, r, sep in product(names, roles, separators):
        for nv, rv in product(variants(n), variants(r)):
            print(f"{n}{sep}{rv}\n")
            f.write(f"{n}{sep}{rv}\n") 