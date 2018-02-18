"""
print_list is a function that takes a list as its input and prints it line by line as a numbered or bulleted list. It takes three arguments:

l: The list to print
numbered: set to True to print a numbered list.
bullet_character: The symbol placed before each list element. This is ignored if numbered is True.
This function is pretty cumbersome to call. It requires a bullet_character even if the user wants a numbered list!

Make the function easier to use by adding default arguments. By default the function should produce a bulleted list, and the default bullet character should be "-".

After your changes, the function should behave like this:

>>> print_list(["cats", "in", "space"])
- cats
- in
- space
>>> print_list(["cats", "in", "space"], True)
1: cats
2: in
3: space
"""
def print_list(l, numbered,bullet_character = "-"):
    """Prints a list on multiple lines, with numbers or bullets
    
    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print ("{}: {}".format(index+1, element))
        else:
            print ("{} {}".format(bullet_character, element))
            
#print(print_list(["cats", "in", "space"],False,"*"))
#print(print_list(["cats","in","space"],True))
print(print_list(["cats","in","space"],False))
