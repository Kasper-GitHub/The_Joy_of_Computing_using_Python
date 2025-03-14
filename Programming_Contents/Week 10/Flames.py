import copy

name_1 = list(input("Enter the first name: ").upper())
name_2 = list(input("Enter the second name: ").upper())

p1 = copy.deepcopy(name_1)
p2 = copy.deepcopy(name_2)

for letter in name_1:
    try:
        p2.remove(letter)
        p1.remove(letter)
    except ValueError: pass

print(p1,p2)
count = len(p1)+len(p2)
flames = list("FLAMES")
index = 0

def steps(count,flames):
    index_new = count
    if index_new > len(flames) - 1:
        return ( index_new % len(flames) )
    else:   return index_new - 1

def rearrange(index,flames):
    flames_new = list(flames)
    for i in range(len(flames)):
        flames_new[0-i] = flames[index-i]
        print(i, "0-i = ", 0-i,"index-i = ", index-i, flames_new)
    return flames_new


while len(flames) > 1:
    print("Before",index,count,flames)
    index = steps(count,flames)
    print("After",index, count, flames)
    print(flames[index])
    flames.pop(index)
    print("check",flames)
    flames = rearrange(index,flames)


print("Result of FLAMES between ", ''.join(name_1), " & ", ''.join(name_2), " is : ",end=" ")
if flames[0] == "F": print("Friends")
elif flames[0] == "L": print("Love")
elif flames[0] == "A": print("Affection")
elif flames[0] == "M": print("Marriage")
elif flames[0] == "E": print("Enemy")
elif flames[0] == "S": print("Siblings")






















'''
def steps(index,count,flames):
    if index + count > len(flames):
        index_new = ((index + count) % len(flames))
        if index_new > len(flames) - 1 - index:
            return index_new - (len(flames) - 1 - index) - 1
        else:   return index_new + index
    else: return index + count - 1

while len(flames) > 1:
    print(index,count,flames)
    index = steps(index,count,flames)
    print(flames[index])
    flames.pop(index)
    if index > len(flames) - 1:
        index = index - len(flames)

print("Result of FLAMES between ", ''.join(name_1), " & ", ''.join(name_2), " is : ",end=" ")
if flames[0] == "F": print("Friends")
elif flames[0] == "L": print("Love")
elif flames[0] == "A": print("Affection")
elif flames[0] == "M": print("Marriage")
elif flames[0] == "E": print("Enemy")
elif flames[0] == "S": print("Siblings")
'''





