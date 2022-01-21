import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip() # Stripping \n on the line
    # encode() -> function convets string to bytes
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # decode() -> fucntion converts bytes to string
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<==>", cooked_string)

languages = open("Data/ex23_languages.txt", encoding="utf-8")

main(languages, encoding, error)
