from tokenize import tokenize, untokenize
import sys

inter = sys.argv[1]

def run_code(file: str):
    keys = {
       "your keyword": "python keyword" # then add a comma for multiple
    }

    with open(file, 'rb') as src:
        tokens = []

        for token in tokenize(src.readline):
            if token.string in keys:
                t = (token.type, keys[token.string])
                
            else:
                t = (token.type, token.string)

            tokens.append(t)

        code = untokenize(tokens).decode('utf-8') 
        exec(code)

# Any file extension works just do python3 parse.py <file>
if __name__ == '__main__':
    run_code(file=inter)     
