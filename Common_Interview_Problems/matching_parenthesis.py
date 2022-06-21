# The valid parentheses problem involves checking that:

# all the parentheses are matched, i.e., every opening parenthesis has a corresponding closing parenthesis.
# the matched parentheses are in the correct order​, i.e., an opening parenthesis should come before the closing parenthesis.

the_string = "(((()((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()(())()()))(())))))))))))))))"

def check_parenthesis(test_string):
    my_stack = []
    for i in test_string:
        if i == "(":
            my_stack.append(i)
        elif i == ")":
            if len(my_stack) == 0:
                return False
            my_stack.pop()
        else:
            return False
    if len(my_stack) == 0:
        return True
    return False


print(check_parenthesis(the_string))