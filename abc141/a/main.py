S = str(input())
L = ('Sunny', 'Cloudy', 'Rainy')
print(L[(L.index(S)+1)%3])
