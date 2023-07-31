def outer():
    x = "local"
    def inner():
        nonlocal x #nonlocal is reffering to the parent variable which is x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()