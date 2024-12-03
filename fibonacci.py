# f(n) = f(n-1) + f(n-2)
# f0 = 0
# f1 = 1
def fibonacci_recursive(n):
    if n <= 1:
        return n  #
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print("*******************Fibonacci with Recursive*******************************")
for i in range(10):  # print the first 10 numbers
    print(fibonacci_recursive(i))


# Another way which consider more qualify
# by Using loop instead of using directly recursive
def fibonacci_iterative(n):
    fib_series = [0, 1]

    for ie in range(2, n):
        next_value = fib_series[ie - 1] + fib_series[ie - 2]
        fib_series.append(next_value)

    return fib_series


print("******fibonacci with Loop is better than recursive********")
# طباعة أول 10 أرقام في السلسلة
print(fibonacci_iterative(10))

##########################
print("***********Now print with dynamic which is the best*************")


def fibonacci_dynamic(n):
    # إنشاء قائمة لتخزين القيم المحسوبة مسبقاً
    fib = [0] * (n + 1)  # list of zeros rang depends on value of n

    # initial values in fibonacci series
    fib[0] = 0
    if n > 0:
        fib[1] = 1  # already known
    # حساب باقي الأرقام باستخدام القيم السابقة المخزنة
    for i in range(2, n + 1):  # start from 2 coz already knows fib[0] nad fib[1]
        # n+1 to include n also
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# طباعة أول 10 أرقام في السلسلة
for i in range(10):
    print(fibonacci_dynamic(i))
