import pandas as pd
import numpy as np
import math
import seaborn as sns
from matplotlib import pyplot as plt
import plotly.express as px  
import plotly.io as pio
import numpy as np
import plotly.graph_objects as go
import os

import warnings
warnings.filterwarnings("ignore")

import os
from sys import path
path.append(os.path.join(os.getcwd(), '')) 
from function import * 


from sklearn.metrics import accuracy_score, confusion_matrix, RocCurveDisplay
from sklearn.metrics import classification_report, auc, roc_curve
from sklearn.metrics import  f1_score, precision_score,recall_score, roc_auc_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression , RidgeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.naive_bayes import GaussianNB

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

import pickle
import joblib