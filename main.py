"""coding:utf-8"""

import numpy as np
import pandas as pd


if __name__ == '__main__':
    d_mat = pd.read_csv('student/student-mat.csv', ';')
    d_por = pd.read_csv('student/student-por.csv', ';')

    d_pm = pd.concat([d_mat, d_por], keys=['mat', 'por'])

    result = pd.merge(d_mat, d_por, on=["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu", "Mjob",
                                        "Fjob", "reason", "nursery", "internet"])
