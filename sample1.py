def mostcommonfirstletters(s):
    d=s.split(" ")
    count=0
    s1=""
    for i in range(0,len(d),1):
        s1=s1+d[i][0]
    count=s1.count(s1[0])
    for i in range(1,len(s1),1):
        ch=s1[i]
        if(s1.count(ch)>count):
            count=s1.count(ch)
            print(ch)
mostcommonfirstletters("do you have a voting plan for the election happening next month?")

# d = { "apples" : 5, "beets" : 2, "lemons" : 1 }
# total=0
# for k in d:
#      total=total+d[k]
# print(total)
# def mostcommonfirstletters(s):
#     large=0
#     a=list(s)
#     for i in range(0,len(a),1):
#         print(a[i][0])
    # a=""
    # for i in range(0,len(s),1):
    #     ch=s[i]
    #     if " " in s:
    #         if(s.count(ch)>=large):
    #             large=s.count(ch)
    #             a=ch
    # return a
# s="do you have a voting plan for the election happening next month?"
# print(mostcommonfirstletters(s))