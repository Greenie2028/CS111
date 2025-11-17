graph = [
    ['C','A','T'],
    ['R','R','E'],
    ['D','O','G']
]

# Generate all possible strings starting at 0,0
list_of_words = []

def generate_words(row, col, letters):
    if row < 0 or row == len(graph) or col < 0 or col == len(graph[0]) or graph[row][col] == 0:
        return
    letter = graph[row][col]
    letters.append(letter)
    graph[row][col] = 0
    #print(letter, end = "")

    #print("".join(letters))
    print(letters)
    generate_words(row+1, col, letters)
    generate_words(row, col+1, letters)
    generate_words(row-1, col, letters)
    generate_words(row, col-1, letters)

    graph[row][col] = letter
    letters.pop()

generate_words(0,0,[])