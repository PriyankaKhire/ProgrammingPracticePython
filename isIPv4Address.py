# isIPv4Address
# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso
'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

An identification number for devices connected to the internet. An IPv4 addresses written in dotted quad notation consists of four 8-bit integers separated by periods.
In other words, it's a string of four numbers each between 0 and 255 inclusive, with a "." character in between each number. All numbers should be present without leading zeros.

Given a string, find out if it satisfies the IPv4 address naming rules.
'''
def solution(inputString):
    # split the string with the help of .
    ipNumberList = inputString.split(".")
    # go through the numbers and see if they fall between 0 to 255
    if len(ipNumberList) != 4:
        return False
    for ipNum in ipNumberList:
        # if the current number is empty string ex: .1.0.196
        if not ipNum:
            return False
        # if the number is not a digit ex: 1a.1.0.196
        if not ipNum.isdigit():
            return False
        # check for leading 0
        if (len(ipNum) > 1 and ipNum.startswith("0")):
            return False
        # if the number doesn't fall between 0 and 255
        if not(0 <= int(ipNum) and int(ipNum) <= 255):
            return False
    return True
