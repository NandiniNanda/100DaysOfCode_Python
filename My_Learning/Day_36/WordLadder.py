from collections import deque

def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    
    queue = deque([(beginWord, 1)])
    visited = set([beginWord])

    while queue:
        current_word, level = queue.popleft()
        if current_word == endWord:
            return level
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + char + current_word[i+1:]
                if next_word in word_set and next_word not in visited:
                    queue.append((next_word, level + 1))
                    visited.add(next_word)
    
    return 0

# Take user input for beginWord, endWord, and wordList
beginWord = input("Enter the beginWord: ")
endWord = input("Enter the endWord: ")
wordList = input("Enter the wordList separated by space: ").split()

# Find the number of words in the shortest transformation sequence
result = ladderLength(beginWord, endWord, wordList)
print("Output:", result)