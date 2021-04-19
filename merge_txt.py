from pathlib import Path

filenames = [str(x) for x in Path("./results/").glob("**/*.txt")]

with open('results_file.txt', 'w', encoding="utf-8") as outfile:
    for fname in filenames:
        with open(fname, encoding="utf-8") as infile:
            for line in infile:
                outfile.write(line)
