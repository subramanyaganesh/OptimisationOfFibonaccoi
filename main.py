from math import sqrt, pow
import pandas
import matplotlib.pyplot as plt


def Fib_closeform(n):
    sqrt5 = sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return (pow(phi, n) - pow(psi, n)) / sqrt5


def fibAndCloseForm(fn, n):
    x = list(range(0, n + 1))
    y1 = list(map(fn, x))
    y2 = list(map(Fib_closeform, x))
    y3 = list(map(emperical_Fib_count, x))
    y4 = list(map(theoritical_Fib_count, x))
    return (x, y1, y2, y3, y4)


def plotVsCloseform(x, y1, y2, label1, label2):
    plt.figure(figsize=(6, 6))
    plt.plot(x, y1, c='red')
    plt.plot(x, y2, c='blue', ls='dashed')
    plt.xlabel('n', fontsize=16)
    plt.ylabel('Fib', fontsize=16)
    plt.legend([label1, label2])
    plt.title(label1 + " vs " + label2)
    plt.grid(True)
    plt.show()


def tabularize(x, y1, y2, label1, label2):
    d = {'n': x}
    d[label1] = y1
    d[label2] = y2
    df = pandas.DataFrame(data=d)
    print(df.to_string())


count = 0


# Part(a)
def Fib(n):
    global count
    count += 1
    if n <= 1:
        return n
    return Fib(n - 1) + Fib(n - 2)


def Best_Fib_Code(n):
    a = 0
    b = 1
    for i in range(n, 0, -1):
        c = a + b
        a = b
        b = c
    return a


def emperical_Fib_count(n):
    global count
    count = 0
    Fib(n)
    return count


def theoritical_Fib_count(n):
    return 2 * Best_Fib_Code(n + 1) - 1


(x, y1, y2, y3, y4) = fibAndCloseForm(Fib, 35)
plotVsCloseform(x, y1, y2, "Fib", "Closed form")
tabularize(x, y1, y2, "Fib", "Closed form")
tabularize(x, y3, y4, "Empirical", "Theoretical")
print(y3)
print(y4)


# Part(f)
def Better_Fib(n):
    r = [0] * (n + 1)  # memo array to store the results
    if n <= 1:  # Handling corner case
        return n
    r[0] = 0  # base condition 1
    r[1] = 1  # base condition 2
    for j in range(2, n + 1):  # going bottom-up
        r[j] = r[j - 1] + r[j - 2]  # finding fibonacci of nth number and store in memo array
    return r[n]


(x, y1, y2, y3, y4) = fibAndCloseForm(Better_Fib, 50)
plotVsCloseform(x, y1, y2, "Fib better", "Closed form")
tabularize(x, y1, y2, "Fib better", "Closed form")
