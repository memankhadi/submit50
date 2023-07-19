def main():
    face1()
    face2()
    goodbye()

def face1():
    f1=input("type hello :) ").replace(":)","🙂")
    print("hello ",f1)

def face2():
    f2=input("Type hello (: ").replace("(:","🙁")
    print("hello ",f2)

def goodbye():
    g=input("Type Hello :) Goodbye (: ").replace(":)","🙂").replace("(:","🙁")
    print(g)
main()