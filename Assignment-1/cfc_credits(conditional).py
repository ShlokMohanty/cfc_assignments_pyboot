def position(credits):
    if credits >= 7500 :
        print("Tera Leader")
    elif credits >= 6000 and credits < 7500 :
        print("Gega Leader")
    elif credits >= 4500 and credits < 6000 :
        print("Mega Leader")
    elif credits < 4500 :
        print("Rising Star")
position(5000)
