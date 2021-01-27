#  count lowercase and uppercase

def islower_or_upper(simple_string):
    lower = 0
    upper = 0
    for i in simple_string:
        if(str(i).islower()) : lower += 1
        if(str(i).isupper()) : upper += 1
    return lower, upper

print(f"lower case character : {islower_or_upper('The quick Brow Fox')[0]}\nupper case character : {islower_or_upper('The quick Brow Fox')[1]}")
