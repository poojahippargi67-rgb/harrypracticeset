p1= "get job"
p2= "dream big"
p3= "fous on goals"
p4= "make a lot of money"
message=input("enter your comment:")

if((p1 in message) or (p2 in meassage) or (p3 in meassage) or (p4 in meassage)):
    print("this comment is a spam")
else:
    print("this comment is not spam")