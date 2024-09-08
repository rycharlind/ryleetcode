words = ['hello', 'world', 'python', 'map']

lambda_upper = lambda x: x.upper()
uppercase_words = map(lambda_upper, words)

print(type(uppercase_words))
print(list(uppercase_words))