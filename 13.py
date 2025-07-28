def romanToInt(self, s):
    """
    :type s: str
    :returnType: int

    """
    sum = 0
    romanCharDict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    for i in range(len(s)):
        if i+1 < len(s) and romanCharDict[s[i]] < romanCharDict[s[i+1]]:
            sum = sum - romanCharDict[s[i]]
        else:
            sum = sum + romanCharDict[s[i]]
    
    return sum