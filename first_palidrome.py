




def next_pali(N):
    N = list(str(N))
	i = j = len(N)/2
    if len(N) %2 == 0:
        i -= 1
	
	while i >= 0:
		if (str[i] == '9') {
			str[i] = str[j] = '0';
		} else {
			str[i]++;
			str[j] = str[i];
			break;
		}
		i--;
		j++;
	}
	
	if (i < 0) {
		str += '1';
		str[0] = '1';
	}
	return atoi(str.c_str());
}


def first_pali(N):
    s = str(N)
    s = list(s)
    i = j = len(s) - 1
    while i >= 0:
        if s[i] == '9':
            s[j] = s[i] = '0'
            j+=1
            i-=1
            continue
        else:
            s[i] = str(int(s[i]) + 1)
            break
    while i >= 0:
        s[j] = s[i]
        i-=1
        j+=1

    return int(''.join(s))

print next_pali(first_pali(8))
