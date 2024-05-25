def isLongPressedName(name, typed):
    i = 0
    for j in range(len(typed)):
        if i < len(name) and name[i] == typed[j]:
            i += 1
        elif i > 0 and name[i-1] == typed[j]:
            continue
        else:
            return False
    return i == len(name)
