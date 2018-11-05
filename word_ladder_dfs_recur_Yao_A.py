# Adam Yao
import time
import sys
sys.setrecursionlimit(3000)

'''helper methods'''

from collections import deque

explored = {}
lista = []

initial_word = input("Initial word: ")
final_word = input("Final word: ")

if len(initial_word) != 6 or len(final_word) != 6:
    print("Sorry, invalid length. ")

dictionary = []
filename = open("words.txt")
for e in filename.readlines():
    dictionary.append(e)
dictionary = [x.strip() for x in dictionary]


def generate_path(list):
    print(len(list))
    print(list[::-1])


def dfs_recur(state, final, explored, lista):
    if goalTest(state, final):
        lista.append(final)
        state_checker = final
        while state_checker != initial_word:
            state_checker = explored[state_checker]
            lista.append(state_checker)
        return lista
    else:
        for neighbor in neighbors(state, dictionary):
            if neighbor not in explored.keys():
                explored[neighbor] = state
                result = dfs_recur(neighbor, final, explored, lista)
                if result != "No solution":
                    return result
        return "No solution"


def neighbors(string1, dictionary):
    list = []
    counter = 0
    for x in dictionary:
        for i in range(0, len(string1)):
            if string1[i] != x[i]:
                counter += 1
        if counter < 2 and string1 != x:
            list.append(x)
        counter = 0

    return list


def goalTest(word1, word2):
    if word1 == word2:
        return True
    return False



start = time.time()


dfs_len = dfs_recur(initial_word, final_word, explored, lista)
print("DFS Recur: ", dfs_len[::-1])
print(time.time() - start)
