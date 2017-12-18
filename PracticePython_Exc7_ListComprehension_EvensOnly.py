a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

evensonly = []
oddsonly = []
for num in a:
    if num % 2 == 0:
        evensonly.append(num)

print "List with only even numbers are: %s" % evensonly


#printing list of even numbers only
