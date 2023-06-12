import csv
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
class Barchart:
    def view(self,list):
        plt.rcdefaults()
        objects = ('NaiveBayes','DecisionTree','RandomForest','SupportVectorMachine')
        y_pos = np.arange(len(objects))
        plt.bar(y_pos,list, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Accuracy')
        plt.title('Batters Classification Analysis')
        plt.show()

    def viewblrs(self,list):
        plt1.rcdefaults()
        objects = ('NaiveBayes','DecisionTree','RandomForest','SupportVectorMachine')
        y_pos = np.arange(len(objects))
        plt1.bar(y_pos,list, align='center', alpha=0.5)
        plt1.xticks(y_pos, objects)
        plt1.ylabel('Accuracy')
        plt1.title('Bowlers Classification Analysis')
        plt1.show()
