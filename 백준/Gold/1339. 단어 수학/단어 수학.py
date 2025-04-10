import sys
input = sys.stdin.readline


def calculate_weights(words):
    weights = {}
    for word in words:
        length = len(word)
        for i in range(length):
            char = word[i]
            power = length - i - 1
            weights[char] = weights.get(char, 0) + 10 ** power
    return weights

def assign_numbers(weights):
    sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)
    alpha_to_num = {}
    num = 9
    for char, _ in sorted_weights:
        alpha_to_num[char] = num
        num -= 1
    return alpha_to_num

def calculate_total(words, alpha_to_num):
    total = 0
    for word in words:
        value = 0
        for char in word:
            value = value * 10 + alpha_to_num[char]
        total += value
    return total


n = int(input())
words = [input().rstrip() for _ in range(n)]

weights = calculate_weights(words)
alpha_to_num = assign_numbers(weights)
print(calculate_total(words, alpha_to_num))