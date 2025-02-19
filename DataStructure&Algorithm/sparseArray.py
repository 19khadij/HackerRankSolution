

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    frequency={}
    for s in stringList:
        frequency[s]=frequency.get(s,0)+1
        
    result= [frequency.get(q,0) for q in queries]
    return result
if __name__ == '__main__':

    stringList = ['abbb','baba','rrabc','abuuc','abuuc','a','ab']
    queries=['ab','a','abc','abuuc','abuuc']

    res = matchingStrings(stringList, queries)

    print(res)