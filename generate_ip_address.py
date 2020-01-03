

def isvalid(res):
    if res[0] == '0' or int(res) <= 0 or int(res) > 255:
        return False
    return True
def form(ip):
    if len(ip) > 12:
        return []
    dic = {}
    def util(ip,idx,res):
        if idx == 4:
            if not len(ip):
                newval = ip_arr[:]
                key = '.'.join(newval)
                if not dic.get(key,0):
                   results.append(newval)
                   dic[key] = 1
            return
        
        for dot in range(1,4):
           res = ip[:dot]
           if isvalid(res):
               ip_arr.append(res)
               util(ip[dot:],idx+1,res)
               ip_arr.pop()
           else:
               continue

    res = ""
    results = []
    ip_arr= []
    util(ip,0,res)
    print results



ip = "25525511135"
form(ip)
