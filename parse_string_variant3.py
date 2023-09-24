#!/usr/bin/env python3

def main():
    S = input()
    if S.isnumeric():
        print(int(S))
    else:
        print("Bad String")

if __name__ == "__main__":
    main()
