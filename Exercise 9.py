# A string of length 6 consisting of lowercase English letters is said to be coffee-like if and only if its 3-rd and 
# 4-th characters are equal and its 5-th and 6-th characters are also equal.Given a string S, determine whether it is coffee-like.
S=input()
if(S[2]==S[3] and S[4]==S[5]): print("Yes")
else: print("No")
