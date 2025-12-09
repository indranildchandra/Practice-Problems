"""
  1) The execution entry point is main().
  2) Consider adding some additional tests in doTestsPass().
  3) Implement reverseStr(str) correctly.
  4) If time permits, some possible follow-ups.
"""

"""
Takes str and returns a string such that the characters
are in reversed order.
Example: reverseStr(str) where str is "abcd" returns "dcba".
"""
def reverseStr(str):
    reversed_str = ""
    for c in str[len(str)-1::-1]:
        reversed_str += c
    return reversed_str

"""
Returns true if all tests pass. Otherwise returns false
"""
def doTestsPass():
    if reverseStr("abcd") != "dcba":
        return False

    if reverseStr("odd abcde") != "edcba ddo":
        return False

    if reverseStr("even abcde") != "edcba neve":
        return False

    if reverseStr(reverseStr("no change")) != "no change":
        return False

    if reverseStr("") != "":
        return False

    return True


if __name__ == "__main__":
    result = doTestsPass()

    if result:
            print("All tests pass\n")
    else:
            print("Tests fail\n")