
# Data structures
# 1. List

papers = ["Time series", "EcoStat Vital", "CDA", "LST"]

print(papers[0])
print(papers[-1])

papers[0] = "Time series & Stochastic Process"
print(papers)

# Don't try to memorize every function, all you need to remember is the operations you can do, Google is always there for you to know how to do. MAKE NOTES IN YOUR BRAIN.

programming = ["Python","R","SAS","SQL"]
stats = ["Probability","Inferential stat","Regression & Linear Models- Non-Linear Models","Descriptive stats"]
maths = ["Calculus","Linear Algebra","Real Analysis"]

DS_ML = [stats, programming, maths] # Nested List
print(programming)
print(stats)
print(maths)
print(DS_ML)
print(DS_ML[1][1]) # This will clear how nested list works
print(DS_ML[1])

# This question combines several of the Python List concepts that we’ve seen in the previous lessons in isolation. If the code above is at all confusing, I recommend breaking down what’s going on using several print statements using repl.it. First, try printing out:

# print(dirty_dozen)
# Then print out:

# print(dirty_dozen[0])
# print(dirty_dozen[1])
# To see what happens at the next stage print out:

# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])
# I hope this helps clarify how nested lists work. 🙂
print("❤️")