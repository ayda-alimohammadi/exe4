newpostI=int()
newtwiitT=0
getpostI=0
gettwiitT=0
newpost=[]
newtwitt=[]

class socialM:

    def __init__(self , new):
        if newpostI!="0":
            self.newpost = new
            newpost.append(new)
        if newtwiitT!="0":
            self.newtwitt = new
            newtwitt.append(new)

class instagram(socialM):
    pass
class twiiter(socialM):
    pass
def menu():
    newpostI = 0
    socialMedia = input("1.Instagream:"
                        "2.twitter:"
                        "3.exit")
    if socialMedia == "1":
        services = input("1.new post:"
                         "2.get post:")
        if services == "1":
            post = input("new post:")
            if post.__len__() < 10:
                newpostI = +1
                instagram(post)
            else:
                print("errore")
        if services == "2":
            print("post:")
            print(newpost)

    if socialMedia == "2":
        services = input("1.new teitte:"
                         "2.get twittes:")
        if services == "1":
            twitte = input("new twitte:")
            newtwiitT = +1
            twiiter(twitte)
        if services == "2":
            print("twitte:")
            print(newtwitt)
    if socialMedia=="3":
        exit()
print("wellcome")
socialMedia = input("1.Instagream:"
                          "2.twitter:"
                    "3.exit")

while socialMedia!="3":
    countMenu = +1
    menu()