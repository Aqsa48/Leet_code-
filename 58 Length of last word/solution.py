class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splited=s.strip()  # Removes leading and trailing whitespace.
        splited= splited.split()   #method splits a string into a list using whitespace 
        # print(splited)
        return len(splited[-1])  // Returns the length of last word


