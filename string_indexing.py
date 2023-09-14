# Read the number of test cases
t = int(input().strip())

# Iterate through each test case
for _ in range(t):
    # Read the input string
    s = input().strip()
    
    # Initialize even and odd strings
    even_chars = ""
    odd_chars = ""

    # Iterate through the characters in the string
    for i in range(len(s)):
        if i % 2 == 0:
            even_chars += s[i]
        else:
            odd_chars += s[i]

    # Print even and odd characters separated by a space
    print(even_chars, odd_chars)
