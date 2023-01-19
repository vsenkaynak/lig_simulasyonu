from random import shuffle

def get_score_list():
    score_list = []
    for x in range(110):
        score_list.append([1,1])
    for x in range(105):
        score_list.append([1,0])
    for x in range(85):
        score_list.append([2,1])
    for x in range(77):
        score_list.append([0,0])
    for x in range(74):
        score_list.append([0,1])
    for x in range(73):
        score_list.append([2,0])
    for x in range(63):
        score_list.append([1,2])
    for x in range(47):
        score_list.append([2,2])
    for x in range(44):
        score_list.append([0,2])
    for x in range(43):
        score_list.append([3,0])
    for x in range(42):
        score_list.append([3,1])
    for x in range(27):
        score_list.append([1,3])
    for x in range(25):
        score_list.append([3,2])
    for x in range(23):
        score_list.append([0,3])
    for x in range(20):
        score_list.append([4,0])
    for x in range(19):
        score_list.append([2,3])
    for x in range(18):
        score_list.append([4,1])
    for x in range(10):
        score_list.append([1,4])
    for x in range(10):
        score_list.append([4,2])
    for x in range(10):
        score_list.append([3,3])
    for x in range(9):
        score_list.append([0,4])
    for x in range(8):
        score_list.append([5,0])
    for x in range(7):
        score_list.append([5,1])
    for x in range(7):
        score_list.append([2,4])
    for x in range(4):
        score_list.append([4,3])
    for x in range(4):
        score_list.append([0,5])
    for x in range(4):
        score_list.append([5,2])
    for x in range(4):
        score_list.append([1,5])
    for x in range(3):
        score_list.append([6,0])
    for x in range(3):
        score_list.append([3,4])
    for x in range(3):
        score_list.append([6,1])
    for x in range(2):
        score_list.append([2,5])
    for x in range(2):
        score_list.append([7,0])
    for x in range(2):
        score_list.append([0,6])
    score_list.append([1,6])
    score_list.append([4,4])
    score_list.append([6,2])
    score_list.append([5,3])
    score_list.append([7,1])
    score_list.append([3,5])
    score_list.append([8,0])
    score_list.append([0,7])
    score_list.append([2,6])
    score_list.append([1,7])
    score_list.append([6,3])
    score_list.append([7,2])
    score_list.append([5,4])
    shuffle(score_list)
    #print(score_list)
    return score_list
