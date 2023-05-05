from tokenize import tokenize, untokenize
import shutil
import config
import sys


infile = sys.argv[1]
outfile = sys.argv[2]

def parse(file: str):
    keys = config.tokens

    with open(file, 'rb') as src:
        tokens = []

        for token in tokenize(src.readline):
            if token.string in keys:
                t = (token.type, keys[token.string])
                
            else:
                t = (token.type, token.string)

            tokens.append(t)
            
        parsed = untokenize(tokens).decode('utf-8') 

    out = open(outfile, 'w')
    out.write(parsed)
    out.close()


parse(file=infile)
shutil.rmtree("/__pycache__")
