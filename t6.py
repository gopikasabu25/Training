
def palindrome(s):
        str=""
        for i in s:
            if i.isalnum():
                  str=str+i
        str=str.lower()
        p=str[::-1]
        return p==str

s=input()
print(palindrome(s))