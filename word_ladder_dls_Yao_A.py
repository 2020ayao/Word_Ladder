# Adam Yao
dict = {}
def readFile(filename):
    file = open("words.txt")
    list = []
    for e in file.readlines():
        if e != "":
            list.append(e[:len(e)-1])
    return list

def createGraph(wordList):
    for word in wordList:
        s = set()
        dict[word] = s
        for others in wordList:
            count = 0
            for i in range(len(word)):
                if others[i] != word[i]:
                    count+=1
            if count == 1:
                dict[word].add(others)


def DLS(current_state, goal_state, lim, explored):
    if current_state == goal_state:
        generate_path(current_state, explored)
        return "Solved!"
    elif lim == 0:
        return "cutoff"
    else:
        bool = False
        for e in dict[current_state]:
            if e not in curPath(current_state, explored):
                explored[e] = current_state
                result = DLS(e, goal_state, lim - 1, explored)
                if result == "cutoff":
                    bool = True
                elif result != "Fail":
                    return result
        if bool:
            return "cutoff"
        else:
            return "Fail"

def curPath(n, explored):
    path = set(n)
    while(explored[n] != "s"):
        path.add(explored[n])
        n = explored[n]
    return path

def generate_path(n, explored):
   l = []
   while explored[n] != "s":
      l.append(n)
      n = explored[n]
   l.append(n)
   print(l[::-1])
   print ("The number of steps:", len(l))
   return ""

def main():
   starting = input("Starting 6-letter word: ")
   goal = input("Goal word: ")
   list = readFile("words.txt")
   if len(starting) != 6 or len(goal) != 6:
       print("Words are not 6 letters long. ")
   elif starting not in list or goal not in list:
       print("Words not in file. ")
   lim = input("What depth for limit of search? ")
   createGraph(list)
   DLS(starting, goal, int(lim), {starting:"s"})

if __name__ == '__main__':
    main()