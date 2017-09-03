import shelve


db = shelve.open('persondb')

for key in sorted(db):
    print(key, '\t=>', db[key])