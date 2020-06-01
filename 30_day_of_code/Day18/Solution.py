# python3
class Solution:

    def __init__(self):
        self.stack = []
        self.queue = []

    # code here
    def pushChar(self,s):
        self.stack.append(s)

    def enqueueChar(self,s):
        self.queue.append(s)

    def popChar(self):
        return self.stack.pop()

    def dequeueChar(self):
        c = self.queue[0]
        self.queue.remove(c)
        return c

# read the string

s = input()

# create the solution class obj
obj = Solution()

l = len(s)

# push/enqueue all the characters of the string s to stack

for i in range(l):
    obj.pushChar(s[i])
    obj.enqueueChar(s[i])

isPalindrome = True
''' pop the top character from the stack
dequeue the first char from the queue
compare both the char
'''

for i in range(l // 2):
    if obj.popChar() != obj.dequeueChar():
        isPalindrome = False
        break

#print whether string is palindrome or not


if isPalindrome:
    print('The word, ' + s + ', is palindrome.')

else:
    print('The word, ' + s + ', is not a palindrome.')    
