import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import perceptron as ppn

s = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
print('From URL:', s)
df = pd.read_csv(s, header=None, encoding='utf-8')
df.tail()
