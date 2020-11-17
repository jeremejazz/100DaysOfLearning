import re
with open("regex_sum_1074733.txt") as f:
    haystack = f.read()
    numbers = map(lambda item : int(item) ,re.findall(r'[0-9]+', haystack))
    print(sum(numbers))
    