import re


def solution(dart_result):
    pass


dart_result = "1S2D*3T"


p = re.compile("(\d+)([SDT])([*#]?)")
dart = p.findall(dart_result)


print(dart)
