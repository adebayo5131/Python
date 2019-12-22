import sys


def solution(T):
    time = T.split(":")
    t1 = time[0]
    t2 = time[1]

    if t1.isdigit() and t2.isdigit():
        return T
    elif t1 == "??" and t2 == "??":
        return "23:59"
    else:
        if t1 == "??":
            s = "23"
            t1 = "".join(s)
        else:
            s = list(t1)
            if t1[0] == "?":
                if int(t1[1]) > 3:
                    s[0] = "1"
                    t1 = "".join(s)
                else:
                    s[0] = "2"
                    t1 = "".join(s)

            # list one after split
            if t1[1] == "?":
                if int(t1[0]) == 1:
                    s[1] = "9"
                    t1 = "".join(s)
                else:
                    s[1] = "3"
                    t1 = "".join(s)
    if t2 == "":
        s = "59"
        t2 = "".join(s)
    else:
        s = list(t2)
        if t2[0] == "?":
            s = list(t2)
            s[0] = "5"
            t2 = "".join(s)
        elif t2[1] == "?":
            s = list(t2)
            s[1] = "9"
            t2 = "".join(s)

    return t1 + ":" + t2


print(solution("12:11"))
