def check_string(s1,s2):
    hashed = {}
    str2 = s2.split(" ")
    flag = (len(s1) == len(str2))
    if flag:
        for i in range(len(s1)):
            if s1[i] not in hashed:
                hashed[s1[i]] = str2[i]
            elif hashed[s1[i]] != str2[i]:
                flag = False
                break
    return(flag)

if __name__ == '__main__':
    s1 = str(input())
    s2 = str(input())
    print("Output = ",check_string(s1,s2))