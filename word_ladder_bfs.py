import time

'''helper methods'''

from collections import deque



def word_ladder(initial, final):
    dictionary = []
    filename = open("words.txt")
    for e in filename.readlines():
        dictionary.append(e)
    dictionary = [x.strip() for x in dictionary]

    frontier = deque()
    explored = {}
    frontier.append(initial)
    while len(frontier) > 0:
        n = frontier.popleft()
        if goalTest(n, final):
            counter = 0
            temp = n
            list = []
            list.append(final)  # solved case
            while temp != initial_word:
                temp = explored[temp]
                counter += 1  # shortest_path counter
                list.append(temp)
            counter += 1
            print(list[::-1])
            return counter
        else:
            for a in dictionary:
                    if neighbors(a, n):
                        if a not in explored.keys():
                            explored[a] = n
                            frontier.append(a)
    return "No solution"



def neighbors(string1, string2):
    counter = 0
    for i in range(0, len(string1)):
        if string1[i] != string2[i]:
                counter += 1
    if counter > 1 and string1 != string2:
            return False
    return True


def goalTest(word1, word2):
    if word1 == word2:
        return True
    return False


# display(initial_word)

start = time.time()
initial_word = input("Initial word: ")
final_word = input("Final word: ")

if len(initial_word) != 6 or len(final_word) != 6:
    print("Sorry, invalid length. ")
else:
    bfs_len = word_ladder(initial_word, final_word)

    print("Shortest Length BFS: ", bfs_len)
    print(time.time() - start)
