from sklearn import tree

X = [[182,345,22], [24,56,44], [99,46,89], [180,40,30], [200,45,70], [199,70,20], [210,30,41], [166,99,29], [177,87,60], [150,50,50]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'female', 'male', 'male', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[199,70,20]])
print(prediction)

#prediction = clf.prediction(['male'])
#print(prediction)
