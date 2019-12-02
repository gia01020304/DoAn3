#Implement thuat toan MeanShift duoc mo ta trong document
import matplotlib.pyplot as plt
import numpy as np
colors = 10 * ['r','g','b','c','k','y','m']

class MyMeanShift:
    def __init__(self,bandWidth=30):
        self.bandWidth = bandWidth

    def fit(self,data):
        centroids = {}#khai bao prop centroilds voi data empty

        for i in range(len(data)):
            centroids[i] = data[i]#khoi tao cac diem centroid = data point

        while True:
            newCentroids = []
            for i in centroids:
                inBandWidth = []
                centroid = centroids[i]
                for feature in data:
                    if np.linalg.norm(feature - centroid) < self.bandWidth: #so sanh khoang cach giua centroid va data point, kiem tra xem data point co
                                                                            #nam trong bandwidth hay 0
                        inBandWidth.append(feature)

                newCentroid = np.average(inBandWidth,axis=0)#trung binh khoang cach giua cac data point tiem ra duoc new centroild
                newCentroids.append(tuple(newCentroid))
            
            uniques = sorted(list(set(newCentroids)))#Unique tap du lieu
            tempCentroids = dict(centroids)
            centroids = {}
            for i in range(len(uniques)):
                centroids[i] = np.array(uniques[i])

            optimized = True# Check trong tam khong con thay doi, neu khong con thay doi ket thuc vong lap
            for i in centroids:
                if not np.array_equal(centroids[i],tempCentroids[i]):
                    optimized = False
                if not optimized:
                    break
            if optimized:
                    break
        #Output:
       
        self.centroids = centroids
        self.classifications = {}
        for i in range(len(self.centroids)):
            self.classifications[i] = []

        for featureset in data:
            distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
            classification = distances.index(min(distances))
            self.classifications[classification].append(featureset)

   
    def predict(self,data):
        #so sanh khoang cach voi cac centroid
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification

    def test(self,data):
        self.fit(data)
        centroids = self.centroids

        for classification in self.classifications:
            color = colors[classification]
            for featureset in self.classifications[classification]:
                plt.scatter(featureset[0],featureset[1],color=color,marker='o',s=50)
        
        print("Number of cluster: ",len(centroids))
        #for c in centroids:
        #    plt.scatter(centroids[c][0],centroids[c][1],color=color,marker='*',s=150)
        
        #plt.show()

    def checkCorrect(self,xTest,yTest):
        correct=0
        for i in range(len(xTest)):
            predict_me=np.array(xTest[i].astype(float))
            predict_me=predict_me.reshape(-1,len(predict_me))
            prediction=self.predict(predict_me)
            if prediction==yTest[i]:
                correct+=1
        return correct/len(xTest)