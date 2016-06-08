d = {1:1,2:1,3:1,4:3,5:8,6:21}

def SOP(n,case):
    if(n < 7):
        print("Case #%d: %d" %(case,d[n]))
    else:
        if(n % 2 == 0):
            print("Case #%d: %d" %(case,((n**3 - (16*n) + 27)/6)+1))
        else:
            print("Case #%d: %d" % (case,(n**3 - (16*n) + 30)/6))
    
def main():
    case = 1
    while(True):
        n = int(input())
        if(n == 0):
            break
        SOP(n,case)
        case += 1
main()
