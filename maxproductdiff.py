def max_product_diffrence(k: list) -> int :
    smallest1,smallest2 = None,None
    largest1,largest2 = None, None

    for num in k:
        if largest1 is None or num > largest1:
            largest2 = largest1
            largest1 = num
        elif largest2 is None or num > largest2:
            largest2 = num

        if smallest1 is None or num < smallest1:
            smallest2 = smallest1
            smallest1 = num
        elif smallest2 is None or num < smallest2:
            smallest2=num

    return (largest1*largest2) - (smallest1*smallest2)

print(max_product_diffrence([1,2,3,4,5,6]))