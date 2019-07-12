#str1, str2 = input().upper(), input().upper()
str1 = "FRANCE".upper()
str2 = "french".upper()

division1 = [str1[i:i+2] for i in range(0, len(str1)-1) if 'A' <= str1[i] <= 'Z' and 'A' <= str1[i+1] <= 'Z']
division2 = [str2[i:i+2] for i in range(0, len(str2)-1) if 'A' <= str2[i] <= 'Z' and 'A' <= str2[i+1] <= 'Z']

div_set1, div_set2 = set(division1), set(division2)

div_inter = list(div_set1 & div_set2)
div_sym_diff = list(div_set1 ^ div_set2)

div_set1, div_set2 = list(div_set1), list(div_set2)

div_dict1 = {div_set1[i]: division1.count(div_set1[i]) for i in range(0, len(div_set1))}
div_dict2 = {div_set2[i]: division2.count(div_set2[i]) for i in range(0, len(div_set2))}

sum_inter, sum_union = 0, 0

for i in range(0, len(div_inter)):
    if div_dict1[div_inter[i]] > div_dict2[div_inter[i]]:
        sum_inter += div_dict2[div_inter[i]]
        sum_union += div_dict1[div_inter[i]]
    else:
        sum_inter += div_dict1[div_inter[i]]
        sum_union += div_dict2[div_inter[i]]
    div_dict1.pop(div_inter[i])

for i in range(0, len(div_sym_diff)):
    try:
        tmp1 = div_dict1[div_sym_diff[i]]
    except Exception as e:
        tmp1 = 0
    try:
        tmp2 = div_dict2[div_sym_diff[i]]
    except Exception as e:
        tmp2 = 0
    sum_union += max(tmp1, tmp2)

if sum_union == 0:
    print(65536)
else:
    print(int(sum_inter/sum_union*65536))