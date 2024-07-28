inp_str = "qwertysadgssdfgfsfdgasdfqwertysadgssdfgfsg"
unq_str = list(set(inp_str))
for i in unq_str:
    print(i,inp_str.count(i))
