#!/usr/bin/env python3

def main():
    S = input()
    try:
        integer_value = int(S)
        print(integer_value)
    except ValueError:
        print("Bad String")

if __name__ == "__main__":
    main()
