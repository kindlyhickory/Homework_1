different_types = ['str', 123, 12.3, False, None, {"key_1": 'abc', "key_2": True}, b'abc', (1, 2, False, 'c'),
                   [None, 1.154]]

for element in different_types:
    print(type(element))
