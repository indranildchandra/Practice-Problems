"""
  Instructions:

  Given a list of student test scores, find the best average grade.
  Each student may have more than one test score in the list.

  Complete the bestAverageGrade function in the editor below.
  It has one parameter, scores, which is an array of student test scores.
  Each element in the array is a two-element array of the form [student name, test score]
  e.g. [ "Bobby", "87" ].
  Test scores may be positive or negative integers.

  If you end up with an average grade that is not an integer, you should
  use a floor function to return the largest integer less than or equal to the average.
  Return 0 for an empty input.

  Example:

  Input:
  [ [ "Bobby", "87" ],
    [ "Charles", "100" ],
    [ "Eric", "64" ],
    [ "Charles", "22" ] ].

  Expected output: 87
  Explanation: The average scores are 87, 61, and 64 for Bobby, Charles, and Eric,
  respectively. 87 is the highest.
"""

import sys
import math

def bestAverageGrade(scores):
    """ Returns the best average grade. """
    avg_score_dict = dict[str,float]()
    avg_score_count_dict = dict[str,int]()
    for _score in scores:
        _stu_name = _score[0]
        avg_score_dict[_stu_name] = avg_score_dict.get(_stu_name, 0) + float(_score[1])
        avg_score_count_dict[_stu_name] = avg_score_count_dict.get(_stu_name, 0) + 1
    # print(avg_score_dict)
    # print(avg_score_count_dict)
    
    highest_val = -sys.maxsize
    for stu_name in avg_score_dict.keys():
        current_avg = avg_score_dict.get(stu_name, 0) / avg_score_count_dict.get(stu_name, 1)
        floored_avg = math.floor(current_avg)
		# print(stu_name, " : average : ", floored_avg)
        if floored_avg > highest_val:
            highest_val = floored_avg

    highest_val = 0 if len(scores) == 0 else highest_val

    return highest_val


def doTestsPass():
    testCases = [       
        ([ [ "Bobby", "87" ],
            [ "Charles", "100" ],
            [ "Eric", "64" ],
            [ "Charles", "22" ] ],
         87),
        ([],
         0),
        ([ [ "Sarah", "91" ],
           [ "Goldie", "92" ],
           [ "Elaine", "93" ],
           [ "Elaine", "95" ],
           [ "Goldie", "94" ],
           [ "Sarah", "93" ] ],
         94),
        ([ [ "Alpha", "99" ],
           [ "Bravo", "99" ],
           [ "Charlie", "99" ],
           [ "Delta", "99" ],
           [ "Echo", "99" ],
           [ "Foxtrot", "99" ],
           [ "Foxtrot", "99" ] ],
         99),
        ([ [ "Gerald", "91" ],
           [ "Gerald", "92" ] ],
         91),
        ([ [ "Bobby", "82" ],
            [ "Charles", "100" ],
            [ "Charles", "100" ],
            [ "Eric", "64" ],
            [ "Charles", "50" ] ],
        83),
        ([ [ "Janie", "-66" ],
           [ "Janie", "0" ],
           [ "Gina", "-88" ],
           [ "Bobby", "0" ],
           [ "Gina", "44" ],
           [ "Bobby", "0" ],
           [ "Bobby", "-6" ] ],
         -2),
        ([ [ "Barry", "-66" ],
           [ "Barry", "-65" ],
           [ "Alfred", "-122"] ],
         -66),
    ]

    passed = True
    for tc, expected in testCases:
        print("-" * 60)
        print("Running test case: ", tc)
        actual = bestAverageGrade(tc)
        if actual != expected:
            passed = False
            print("  >  Failed : expected ", expected, ", actual ", actual, "\n")
        else:
            print("  > Passed\n")
        print("*" * 60)

    return passed



if __name__ == "__main__":
    result = doTestsPass()

    if result:
        print("All tests pass\n")
    else:
        print("Tests fail\n")

