def fibonacci(n,lookup):

    if n ==0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fibonacci(n-1,lookup) +  fibonacci(n-2,lookup)

    return lookup[n]


if __name__ == "__main__":
    n = 3
    lookup = [None]*60
    print (fibonacci(n,lookup))