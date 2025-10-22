def fizzbuzz_range(start, end):
    result = ""

    if start > end:
        return result
    
    for num in range(start, end + 1):
        if num % 15 == 0:
            result += "FizzBuzz" 
        elif num % 5 == 0:
            result += "Buzz"
        elif num % 3 == 0:
            result += "Fizz"
        else:
            result += f"{num}"
        if num != end:
            result += " "
    
    return result