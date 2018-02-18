"""
When you program, you will often find that similar ideas 
come up again and again, and, you may want to use the same 
variable in order to make the code readable easily.
E.g in counting, iterating.
You may think you need to come up with the new/different variables each time
Fortunately, you don't need to do this.
Reusing names for objects is OK as long as you keepthem in seperate scope
"Scope" refers to which parts of the prog a vari can be referanced from.

If the variable is created inside the fun., it can be used within that.ab

Consider these two funcs- "word_count" and "nearest_square".
Both func include "answer" variable, but they are distinct variables
that only exist within their respective functions.

Good practice: It's best to define variable in the smaller scope 
                the will be needed in, rather than larger scope.

"""
def word_count(document,search_term):
    """
    This function counts how many times "search_term" appears in document
    """
    words = document.split()
    answer = 0
    for word in words:
        if word == search_term:
            answer += 1
    return answer

def nearest_square(limit):
    """ Find the largest square number smaller than limit."""
    answer = 0
    while (answer+1)**2 < limit:
        answer  += 1
    return answer**2

            
