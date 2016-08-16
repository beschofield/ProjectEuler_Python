'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

# optimized a bit

def algorithm(min, max):
    nums = []

    for x in range(min, max):
        if (x % 3 == 0 or x % 5 == 0):
            nums.append(x)

    return nums

def main():
    # verifying with the example
    print ("sum of (1, 10): " + str(sum(algorithm(1, 10))))

    # finding the solution
    print ("sum of (1, 1000): " + str(sum(algorithm(1, 1000))))

if __name__ == '__main__':
    main()
