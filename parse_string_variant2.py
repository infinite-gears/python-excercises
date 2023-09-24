#!/usr/bin/env python3

class BadStringError(Exception):
    pass

def parse_string(S):
    try:
        integer_value = int(S)
        return integer_value
    except ValueError:
        raise BadStringError("Bad String")

def main():
    S = input()
    try:
        result = parse_string(S)
        print(result)
    except BadStringError as e:
        print(e)

if __name__ == "__main__":
    main()
