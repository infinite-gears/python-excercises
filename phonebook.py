# Read the number of entries in the phone book
n = int(input())

# Initialize an empty phone book (dictionary)
phone_book = {}

# Read and store the phone book entries
for _ in range(n):
    entry = input().split()
    name, phone_number = entry[0], entry[1]
    phone_book[name] = phone_number

# Read and process the queries
while True:
    try:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
