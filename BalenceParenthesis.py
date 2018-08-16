#Given expression containing parenthesis output an expression that contains balenced parenthesis
#example:
#")(" -> ""
#"((())" -> "(())"
#"()())()" -> "()()()" or  "(())()"
class Approch1(object):
    def __init__(self, string):
        self.string = string

    def replace(self, string, index):
        return string[:index]+"0"+string[index+1:]

    def check(self):
        stack = []
        for i in range(len(self.string)):
            if(self.string[i] == "("):
                stack.append(i)
            else:
                if(stack and self.string[stack[-1]] == "("):
                    stack.pop()
                else:
                    stack.append(i)
        for i in stack:
            self.string = self.replace(self.string, i)
        output = ""
        for letter in self.string:
            if letter == "(" or letter == ")":
                output = output+letter
        print output

#Main
o = Approch1(")(")
o.check()
o = Approch1("(()))")
o.check()
