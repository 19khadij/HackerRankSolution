# import numpy 
# # Get N, M and cast to integer
# n, m = map(int, input().split())

# # Create a N-length array of integers
# arrays = numpy.array([input().split(" ") for _ in range(n)], int)

# # Print stats
# print(numpy.mean(arrays, axis=1))
# print(numpy.var(arrays, axis=0))
# print(round(numpy.std(arrays, axis=None), 11))

# n = int(input())
# a=numpy.array([input().split(" ") for _ in range(n)], int)
# b=numpy.array([input().split(" ") for _ in range(n)], int)
# print(numpy.dot(a,b))

def count_substring(string, sub_string):
    counting = 0
    while sub_string in string:
        a=string.find(sub_string)
        string=string[a+1:]
        counting += 1
    return counting

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)