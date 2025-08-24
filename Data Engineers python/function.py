def my_func(p_x):
    print("Hello world")
    try:
        if(p_x % 2 == 0):
            return 1
    except Exception as e:
        return e
    
    finally:
        print("Hello world")

my_func(4)