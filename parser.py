

count = 1

def parse(line,res,d):
    index = 0
    global count
    temp = ""
    while index < len(line):
        if line[index].isalpha():
            while index < len(line) and line[index].isalpha():
                temp += line[index]
                index += 1
            if temp in d:
                res.append(d[temp])
            else:
                next_num = count
                res.append(next_num)
                count += 1
                d[temp] = next_num
            temp = ""
        if index < len(line) and line[index] == '.':
            if line[index] in d:
                res.append(d[line[index]])
            else:
                next_num = count
                res.append(next_num)
                count += 1
                d[line[index]] = next_num
        if index < len(line) and line[index] == '/':
            if line[index] in d:
                res.append(d[line[index]])
            else:
                next_num = count
                res.append(next_num)
                count += 1
                d[line[index]] = next_num
        index += 1

    print res


def encode(s):
    d = dict()
    final = []
    for line in s:
        res = []
        parse(line,res,d)




s = ["www.slack.com/jab/chat/mosh"]
encode(s)
