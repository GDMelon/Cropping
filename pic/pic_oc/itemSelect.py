import os

itemlst = []
def itemSelect(lst):
    for i in lst:
        # print(i)
        if _extension(i) == ".JPG":
            itemlst.append(i)
        return itemlst


def _extension(filepath):
    lst = os.path.splitext(filepath)
    # print(lst[-1])
    return lst[-1]