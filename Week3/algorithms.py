def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1
    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1
    return True

print(isPalindrome('rtbtr'))

# this algorithm does the work but it will do it twice as it has to iterate through out the list.