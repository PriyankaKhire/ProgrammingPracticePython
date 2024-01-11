# reverseInParentheses
# https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6
'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''
def solution(inputString):
    stack = []
    i = 0
    while(i < len(inputString)):
        char = inputString[i]
        if (char != ")"):
            stack.append(char)
            i += 1
            continue
        # char == ) then pop the stack till we reach (
        temp = []
        while(stack[-1] != "("):
            temp.append(stack.pop())
        # pop the remaining (
        stack.pop()
        # put it back in stack
        stack = stack + temp
        i += 1
    return "".join(stack)
