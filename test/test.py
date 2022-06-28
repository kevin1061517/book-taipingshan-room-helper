def fun_test(fun):
    print(fun(5, 2))

if __name__ == '__main__':
    fun_test(lambda x, y: x * y)

    # multiply = lambda x, y: x * y
    # print(multiply(4, 2))
    #
    # #Lambda函式支持IIFE(immediately invoked function expression)
    # name = 'kevin'
    # (lambda name: print('hello', name))(name)
    #
    # numbers = [50, 10, 23, 6, 55, 79]
    # print(list(filter(lambda x: x > 30, numbers)))
    #
    # print(list(map(lambda x: x*2, numbers)))
    #
    # cars = [
    #     ('mazda', 2000),
    #     ('toyota', 1000),
    #     ('benz', 5000)
    # ]
    # print(sorted(cars, key=lambda car: car[1]))