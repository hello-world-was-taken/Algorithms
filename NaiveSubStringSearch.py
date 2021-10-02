def naiveSubStringSearch(myStr, subStrValue):
    count = 0
    for i in range(len(myStr) - 1):
        innerCount = 0
        if(myStr[i] == subStrValue[0]):
            j = 0
            k = i # to account for the 'i' value at the start of the loop
            while(j < len(subStrValue) and myStr[j + k] == subStrValue[j] ):
                innerCount += 1
                j += 1
                i += 1
            if(innerCount == len(subStrValue)):
                count += 1
    return count

myStr = "I love popsicle. Especially, the popsicles that pop"
sub = "pop"

print(naiveSubStringSearch(myStr, sub))