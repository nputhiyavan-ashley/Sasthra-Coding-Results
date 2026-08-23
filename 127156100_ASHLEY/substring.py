def unique_substring(s):
    last={}
    l=0
    maxi=0
    s_i=0
    for r,ch in enumerate(s):
            if ch in last and last[ch]>=l:
                l=last[ch] + 1
            last[ch.lower()]=r
            current_len=r-l+1
            if current_len>maxi:
                maxi=current_len
                s_i=l
    return maxi,s_i

s=input()
l,i=unique_substring(s)
print(l,i)