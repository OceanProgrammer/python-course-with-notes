
while True:
    try:
        n = input()
        n = int(n)
        print(1/n)
        # print(f"->{n}")
        # print("This is good")
    # except ValueError as e:
    #     # print("Enter a valid number")
    #     print(e)
    # except ZeroDivisionError as f:
    #     print("please don't enter 0")
    #     break
    # except KeyboardInterrupt as k:
    #     print("please don't try to give keyboard interrupt :)")
    except Exception as e:
        # print("There is some other error")
        # quit()
        raise ModuleNotFoundError("BOOM!! your code crashed.. :)")
    # else:
    #     print("code executed successfully!!")
    # finally:
    #     print("Let's go!!")
print("This is ok")
