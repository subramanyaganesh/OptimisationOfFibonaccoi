# OptimisationOfFibonaccoi

In this code we have comparison between different ways in which Fibonacci Series is computed

1. Recurssion: This is the most obvious way to compute recussion. However, for huge values the commputation takes a lot of time and also might run out of stack memory. The time complexity is O(nlogn)
2. Memorisation: In this approach we will be reducing the time complexity by inceasing the space complexity. In order to do this we initialise an array and store all the sup-problems computed results. This improves the time complexity to O(n). However space complexity is S(n)
3. Variable Creation: This is the best approach as it improves the space complexity as well as time complexity. In this case there are 3 variables the keeps getting updated in each iteration. Hence the time complexity is O(n) and the space complexity is S(1)
