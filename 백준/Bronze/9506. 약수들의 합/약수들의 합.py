while True:
    n = int(input())
    if n == -1: 
        break
    factors = [i for i in range(1, n) if n % i == 0]
    sum_val = sum(factors)
    if n == sum_val:
        print(n, " = ", " + ".join(str(i) for i in factors), sep="")
    else:
        print(f"{n} is NOT perfect.")