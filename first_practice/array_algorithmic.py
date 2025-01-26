import random

def generate_random_list(size):
    random_list = []
    for _ in range(size):
        # randomly choose to add either an integer or a string
        if random.choice([True, False]):
            random_list.append(random.randint(1, 100))
        else:
            random_list.append(random.choice(['golang', 'cpp', 'rust', 'python', 'java', 'kotlin', 'javascript', 'php']))
    return random_list

def filter_numbers(data):
    return [item for item in data if isinstance(item, int)]

def filter_strings(data):
    return [item for item in data if isinstance(item, str)]

def find_maximum(data):
    numbers = filter_numbers(data)
    return max(numbers) if numbers else None

def find_minimum(data):
    numbers = filter_numbers(data)
    return min(numbers) if numbers else None

def find_average(data):
    numbers = filter_numbers(data)
    return sum(numbers) / len(numbers) if numbers else None

def find_longest_word(data):
    strings = filter_strings(data)
    return max(strings, key=len) if strings else None

def find_shortest_word(data):
    strings = filter_strings(data)
    return min(strings, key=len) if strings else None

def search_word(data, word):
    return word in filter_strings(data)

def main():
    # gen rand list of size 20
    random_list = generate_random_list(20)
    print("gen List:", random_list)

    # filt nums & strs
    numbers = filter_numbers(random_list)
    strings = filter_strings(random_list)
    print("filt nums:", numbers)
    print("filt strs:", strings)

    # find max & min
    max_number = find_maximum(random_list)
    min_number = find_minimum(random_list)
    print("max num:", max_number)
    print("min num:", min_number)

    # find average
    average = find_average(random_list)
    print("average of nums:", average)

    # find longest & shortest words
    longest_word = find_longest_word(random_list)
    shortest_word = find_shortest_word(random_list)
    print("longest word:", longest_word)
    print("shortest word:", shortest_word)

    # search a word
    word_to_search = input("enter a word to search: ")
    found = search_word(random_list, word_to_search)
    print(f"the word '{word_to_search}' in the list? {'y' if found else 'n'}")

if __name__ == "__main__":
    main()