import numpy as np

def is_consistence(answer, constraints):
    if ((answer[0] == 0) or (answer[4] == 0)):
        return False
    for i in range(8):
        for j in range(i):
            if (answer[i] == answer[j]) and (answer[i] >= 0):
                return False
    for i in range(len(constraints)):
        for j in range(len(constraints[i])):
            if answer[j] < 0:
                constraints[i] = np.array([0] * 11)
                break
    answer = [i if i >= 0 else 0 for i in answer]
    tmp = np.dot(constraints, answer)
    for i in tmp:
        if i != 0:
            return False
    return True

def backtrack(answer, pointer):
    while (1):
        if (is_consistence(answer, constraints)):
            for i in range(10):
                if (pointer < 11):
                    answer[pointer] = i
                    pointer += 1
                    answer, pointer = backtrack(answer, pointer)
                else:
                    return (answer, pointer)
        else:
            pointer -= 1
            answer[pointer] = -1
            return (answer, pointer)

if __name__ == '__main__':
    constraints = np.array([
        [0, 1, 0, 1, 0, 0, 0, -1, -10, 0 , 0],
        [0,-1, 1, 0, 0, 0, 1,  0,  1 ,-10, 0],
        [0, 1,-1, 0, 0, 1, 0,  0,  0 , 1 ,-10],
        [1, 0, 0, 0,-9,-1, 0,  0,  0 , 0 , 1],
    ], dtype=int)
    answer = np.array([-1]*11, dtype=int)
    pointer = 0
    answer, pointer = backtrack(answer, pointer)
    print(answer)
