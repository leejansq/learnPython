import string

alphas = string.ascii_letters + '_'
nums = string.digits
alphabet_nums = alphas + nums

inText = input("enter identifier to check legality")

if len(inText) > 1:
    if inText[0] not in alphas:
        print("invalid variable name " + inText + "symbol should start with " + str(alphas))
    else:
        for restChar in inText[1:]:
            if restChar not in alphabet_nums:
                print("symbols should be alphanumeric")
                break
        else:  # for 循环的 else 语句是一个可选项，它只在 for 循环完整的结束,没有遇到 break 时执行
            print("for-else 语句展示")
    print("okay Congrats")
else:
    print("identifier can not be None")

