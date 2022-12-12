import sys
from lexer import Lexer
from os.path import exists


def main():
    assert len(sys.argv) - 1, "You need to pass in a file as an argument"
    main_file_path = sys.argv[1]
    assert main_file_path[-6:] == ".pasta", "You need to execute a .pasta file"
    assert exists(sys.argv[1]), "This file does not exist or is being edited"

    with open(sys.argv[1]) as main_file:
        lexer = Lexer(main_file)
        tokens = lexer.do()

    print(tokens)


if __name__ == '__main__':
    main()
