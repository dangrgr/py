# https://www.hackerrank.com/challenges/counting-valleys/
# representation of valley count
"""
_/\        _
   \    /\/
    \/\/
"""
n = 8
s = "UDDDUDUUDU"

def countingValleys(n, s):
    alt = 0
    valleys = 0
    for step in s:
        # step down, decrement altitude (alt)
        if step == "D":
            alt -= 1
        # step up, increment altitude (alt); check if step up is from -1 (brings us to "sea level")
        elif step == "U" and alt == -1:
            alt += 1
            valleys +=1
        # step up, increment altitude guage (alt)
        else:
            alt += 1
        ## debug #print("Altitude is: {} and Valley count is: {}".format(alt, valleys))
    return valleys

result = countingValleys(n, s)
print(result)
