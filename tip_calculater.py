def main():
    dollars_to_float()


def dollars_to_float():
    
    d=input("$ meal amount ").strip("$")
    dollars=float(d)
    p=input("$ tip percentage ").strip("$").strip("%")
    pp=(int(p))/100
    percent=pp
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")



main()