import operator
def cal(list, prev = 0, maxi = 0,shit_list=[]):
    list = sorted(list)

    for num in list:
        picked = num
        new_list = [n for n in list]
        numplus = [n for n in new_list if n==picked+1]
        numminus = [n for n in new_list if n==picked-1]
        new_list.pop(new_list.index(picked))
        new_list = [n for n in new_list if n not in numplus]
        new_list = [n for n in new_list if n not in numminus]
        cal(new_list, prev+picked,  max(maxi,prev+picked))
        maxi = max(maxi, prev + picked)
        shit_list.append(maxi)
    return shit_list

print(cal([1,6,3,3,8,4,8,10,1,3]))