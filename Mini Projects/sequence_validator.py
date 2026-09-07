import os

import Bio
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


path = input('Please enter the file exact path: ')

while True:
    if path.lower() == 'esc':
        print('Exiting program...')
        break
    
    elif not os.path.isfile(path):
        print('INVALID REQUEST! File does not exist.')

    elif not path.lower().endswith(('.fasta', '.fa')):
        print('INVALID REQUEST! The file must be a FASTA file.')

    else:
        print('Valid FASTA file!')
        break

    path = input('Please enter a valid FASTA file location (or type "esc" to exit): ')

number_of_recs = 0
number_of_invalids = 0
invalid_ids = []

for rec in SeqIO.parse(path, format='fasta'):
    number_of_recs += 1
    
    if not rec.seq.startswith('M'):
        number_of_invalids += 1
        invalid_ids.append(rec.id)
        
print(f'Total Records:{number_of_recs}\nNumber of Invalid Sequences:{number_of_invalids}\nInvalid Sequences IDs:{invalid_ids}')
