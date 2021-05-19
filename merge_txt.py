from pathlib import Path

filenames = [str(x) for x in Path('./results/').glob('**/*.txt')]

abstract_list = []
for fname in filenames:
    with open(fname, encoding='utf-8') as infile:
        for line in infile:
            abstract_list.append(line)

with open('results_file.txt','w', encoding='utf-8') as f:
    for row in abstract_list:
        f.write(repr(row)+'\n')
