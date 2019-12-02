import MyMeanShift as myMS
from sklearn import datasets

iris = datasets.load_iris()
start = 1
while start != 4:
    instance = myMS.MyMeanShift(start)
    instance.test(iris.data)
    c = instance.checkCorrect(iris.data,iris.target)
    print('Band Width: %5.2f, Performance Evalution: %5.2f' % (start,c))
    start=round(start+0.2,1)