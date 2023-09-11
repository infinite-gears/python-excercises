# Read input
N = int(input().strip())

if N % 2 == 1:
    # N is odd, so it's Weird
    print("Weird")
elif N % 2 == 0 and 2 <= N <= 5:
    # N is even and in the range [2, 5], so it's Not Weird
    print("Not Weird")
elif N % 2 == 0 and 6 <= N <= 20:
    # N is even and in the range [6, 20], so it's Weird
    print("Weird")
elif N % 2 == 0 and N > 20:
    # N is even and greater than 20, so it's Not Weird
    print("Not Weird")
