def rebase(input_base,digits, output_base):
    if input_base <= 1:
        raise ValueError("input base must be >= 2")
    elif output_base <= 1:
        raise ValueError("output base must be >= 2")
    number = 0
    for d in digits:
        if d < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        number = number * input_base + d
    result = []
    while number > 0:
        result.insert(0,number % output_base)
        number //= output_base
    if not result:
        return [0]
    else:    
        return result

print(rebase(10,[4,2],2))