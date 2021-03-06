'''
Asher Forman
Pseudocode to Python Conversion
3/6/21
'''

# Sequential Search
N = [2, 9, 5, 6, 7, 8]
X = 7
Found = False
Counter = 0

for Counter in range(0, 5):
    if N[Counter] == X:
        Found = True
        print(N[Counter], "found at position", Counter)
if Found == False:
    print(X, "not found")


# Binary Search
VALUES = [11, 12, 15, 16, 112, 118, 123, 145]
TARGET = 15
MIN = 0
HIGH = 7
FOUND = False
ANSWER = 0
MID = 0

while FOUND == False and MIN <= HIGH:
    MID = ((MIN + HIGH) / 2)
    MID_Int = int(MID) #Can't do a float
    if VALUES[MID_Int] == TARGET:
        FOUND = True
        ANSWER = MID_Int
    elif TARGET > VALUES[MID_Int]:
        MIN = MID_Int + 1
    else:
        HIGH = MID_Int - 1
if FOUND == True:
    print(TARGET, "FOUND AT ARRAY INDEX", ANSWER)
else:
    print(TARGET, " was not found")