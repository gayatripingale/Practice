"""
- A common use of tuple is to return multiple values from a funtion:
"""
def first_and_last(sequence):
    return sequence[0],sequence[-1],sequence[-2]
# This fun returns the first and the last values of the sequence
print(first_and_last(["Spam","egg","sausage","spam"]))



