DNA = []
genes = ["A","C","G","T"]
n = 1
mutations = []
StrDNA = []

def mutate(nMutation,index,StrDNA):
    global DNA
    global strDNA
    global n
    global genes
    if(nMutation > n):
        return
    if(index == len(DNA)):
        mutations.append(''.join(str(e) for e in StrDNA))
        return
    

    for i in genes:
        StrDNA[index] = i       
        if(StrDNA[index] == DNA[index]):
            mutate(nMutation,index+1,StrDNA)
        else:
            mutate(nMutation+1,index+1,StrDNA)

def main():
    global DNA
    global StrDNA
    global n
    global mutations
    
    nTimes = int(input())
    for i in range(nTimes):
        _,n = map(int,input().split(" "))
        DNA = list(input())
        StrDNA = list(DNA)
        mutate(0,0,list(DNA))
        print(len(mutations))
        for j in mutations:
            print(j)
            pass   
        mutations = []
main()
