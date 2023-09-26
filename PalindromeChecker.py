class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop(0)

# Read the string s
s = input()

# Create the Solution class object
obj = Solution()

l = len(s)

# Push/enqueue all the characters of string s to stack and queue
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

# Pop the top character from stack and dequeue the first character from queue, then compare both characters
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

# Finally, print whether string s is a palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
