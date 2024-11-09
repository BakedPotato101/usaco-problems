tests = 10
passed = 0

for t in range(tests):

    file = open(f"testing/{t+1}.in", "r") 

    N = int(file.readline())
    A = []
    shuffled = []
    original = [0]*N

    for integer in file.readline().split():
        A.append(int(integer))
    for i in file.readline().split():
        shuffled.append(int(i))



    for i in range(3):
        for j in range(N):
            original[j] = shuffled[A[j]-1]
        shuffled = original.copy()




    output = open(f"testing/{t+1}.out", "r")
    correctOriginal = [0]*N
    for i in range(N):
        correctOriginal[i] = int(output.readline())
    if original == correctOriginal:
        print("Test case", t+1, "passed")
        passed += 1
    else:
        print("Test case", t+1, "failed")
        print("Expected:", correctOriginal)
        print("Got:", original)

print(f"Passed: {passed} / {tests}" )






