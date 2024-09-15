import pandas as pd
import streamlit as st

results = [{'Model name': 'SVM',
  'Accuracy': 0.7535211267605634,
  'Precision': 0.7288135593220338,
  'Recall': 0.6935483870967742,
  'F1 score': 0.7107438016528926},
 {'Model name': 'Random Forest',
  'Accuracy': 0.7112676056338029,
  'Precision': 0.6615384615384615,
  'Recall': 0.6935483870967742,
  'F1 score': 0.6771653543307087},
 {'Model name': 'Logistic Regression',
  'Accuracy': 0.7605633802816901,
  'Precision': 0.7,
  'Recall': 0.7903225806451613,
  'F1 score': 0.7424242424242423},
 {'Model name': 'Naive Bayes Gaussian',
  'Accuracy': 0.5211267605633803,
  'Precision': 0.4634146341463415,
  'Recall': 0.6129032258064516,
  'F1 score': 0.5277777777777778},
 {'Model name': 'Naive Bayes Multinomial',
  'Accuracy': 0.676056338028169,
  'Precision': 0.6333333333333333,
  'Recall': 0.6129032258064516,
  'F1 score': 0.6229508196721313},
 {'Model name': 'Decision Tree',
  'Accuracy': 0.6056338028169014,
  'Precision': 0.5441176470588235,
  'Recall': 0.5967741935483871,
  'F1 score': 0.5692307692307692},
 {'Model name': 'Adaboost with DecisionTree',
  'Accuracy': 0.5845070422535211,
  'Precision': 0.5254237288135594,
  'Recall': 0.5,
  'F1 score': 0.5123966942148761},
 {'Model name': 'Adaboost with LogisticRegrission',
  'Accuracy': 0.7746478873239436,
  'Precision': 0.7205882352941176,
  'Recall': 0.7903225806451613,
  'F1 score': 0.7538461538461538},
 {'Model name': 'Gradient Boost',
  'Accuracy': 0.5704225352112676,
  'Precision': 0.5079365079365079,
  'Recall': 0.5161290322580645,
  'F1 score': 0.512},
  {'Model name': 'CNN',
   'Accuracy': 0.92842149,
   'Precision': 0.913793,
   'Recall': 0.854839, 
   'F1 score': 0.883333}]

data=pd.DataFrame(results)

def getdata():
    st.write(data)
    return data