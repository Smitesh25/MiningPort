import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import sys
import time




from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier

from yellowbrick.classifier import ClassificationReport

from classifier.detector_classifier import DetectorClassifier
from concept_drift.adwin import AdWin
from concept_drift.page_hinkley import PageHinkley
from concept_drift.DDM import DDM
from concept_drift.ewma import EWMA
from evaluation.prequential import prequential
from sklearn.linear_model import LogisticRegression


def read_data(filename):
    df = pd.read_csv(filename)
    data = df.values
    return data[:, :-1], data[:, -1]

def select_data(x):
    df = pd.read_csv(x)
    scaler = MinMaxScaler()
    df.iloc[:,0:df.shape[1]-1] = scaler.fit_transform(df.iloc[:,0:df.shape[1]-1])
    return df


if __name__ == '__main__':
    
    X, y = read_data(sys.argv[1])

    w =int(sys.argv[2])
    n_train = int(w/10)
    
    clfs = [
        DetectorClassifier(GaussianNB(), PageHinkley(), np.unique(y)),
        DetectorClassifier(GaussianNB(), AdWin(), np.unique(y)),
        DetectorClassifier(GaussianNB(), DDM(), np.unique(y)),
        DetectorClassifier(GaussianNB(), EWMA(), np.unique(y))]
    clfs_label = ["Page-Hinkley", "AdWin", "DDM", "EWMA"]
    
    df=select_data(sys.argv[1])
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    start = time.time()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    classifier=RandomForestClassifier(n_estimators=350, criterion='entropy', random_state=0)
    classifier.fit(X_train, y_train)

    y_pred=classifier.predict(X_test)
    elapsed = (time.time() - start)
    
    classes=["0", "1"]
    model=RandomForestClassifier()
    visualizer = ClassificationReport(model, classes=classes, support=True)
    visualizer.fit(X_train, y_train)        
    visualizer.score(X_test, y_test)        
    visualizer.show(outpath="class.png") 
    
    f = plt.figure()
    

    for i in range(len(clfs)):
        print("\n{}:".format(clfs_label[i]))
        with np.errstate(divide='ignore', invalid='ignore'):
            y_pre, time1 = prequential(X, y, clfs[i], n_train)
        if clfs[i].__class__.__name__ == "DetectorClassifier":
            print("Drift detection: {}".format(clfs[i].change_detected))
        estimator = (y[n_train:] == y_pre) * 1
        print("Time taken: {0:.4f}".format(time1[i]))

        acc_run = np.convolve(estimator, np.ones((w,)) / w, 'same')
        print("Average accuracy : {0:.2f}".format(100*(np.mean(acc_run))))
        plt.plot(acc_run,"-", label=clfs_label[i])
    

        

    
    
    
    
    print("\n" + "Accuracy of classifying the dataset is " , end="")
    print(100*(round(accuracy_score(y_test, y_pred), 4)))
    print("Time taken to classify the dataset is ", end="")
    print(round(elapsed, 4))

    
    
    plt.title("Accuracy")
    plt.xlabel("Instances")
    plt.ylabel("Accuracy")
    plt.legend(loc='lower right')
    plt.ylim([0, 1])
    f.savefig("plot.png", bbox_inches='tight')
    
    
    