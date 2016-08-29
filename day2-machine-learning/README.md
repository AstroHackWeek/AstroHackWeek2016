<h1>Machine Learning</h1>

<h2><font color="grey">Day 2 (AstroData Hack Week 2016)</font></h2>
<hr>

<i>Lecturer</i>: <a href="mailto:profjsb@gmail.com">Josh Bloom</a> (@profjsb; UC Berkeley)


Outline
----

1. What is machine learning?

   - Flavors and facets of machine learning
      - supervised, semi-supervised, clustering, ...
      - classification / regression
   - When to use it, when not to
   - scikit-learn
   - testing/validation sets, cross-validation
   - metrics: ROC, AUC, confusion matrix
   
2. Regression

   - Logistic regression
   - kNN
   - random forest
   
   [breakout: predict quasar redshifts from photometric data]
      
3. Classification

   - SVM
   - random forest
   - deep learning
   
   [breakout: predict Star/Galaxy/QSO from photometric data]
   
4. Improving your models

   - hyperparameter optimization      
        ```GridSearchCV```
   - dealing with missing data
   - Feature selection / feature importance
   - feature engineering

   [breakout: redo Star/Galaxy/QSO from photometric data]

5. Considerations in getting into production

   - multicore / multimachine / Dask
   - scikit-learn pipelines
   - Bigdata machine learning: dato/turi, MLlib (Spark)


Notes/Setup
---

1. Make sure you have the latest version (0.17) of scikit-learn

    - ``conda update scikit-learn matplotlib seaborn dask distributed``

2. Download some datasets locally
   
    - TBD 
    

Links
---

* [Scikit-learn](http://scikit-learn.org/stable/): Machine Learning in Python
     

* Josh's lectures on scikit-learn from his graduate seminar class:

    *  [Notebooks](https://github.com/profjsb/python-seminar/tree/master/DataFiles_and_Notebooks/05_Scikits_Learn). Take a look at [newsgroups.ipynb](http://nbviewer.ipython.org/github/profjsb/python-seminar/blob/master/DataFiles_and_Notebooks/05_Scikits_Learn/newsgroups.ipynb) to see some natural language processsing.