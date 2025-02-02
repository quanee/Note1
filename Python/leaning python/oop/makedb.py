from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve


db = shelve.open('persondb')

for obj in (bob, sue, tom):
    db[obj.name] = obj

db.close()

import glob

print(glob.glob('person*'))

print(open('persondb.dir').read())

print(open('persondb.dir', 'rb').read())

db = shelve.open('persondb')

print(len(db))

print(list(db.keys()))

bob = db['Bob Smith']

print(bob)
print(bob.lastName())
