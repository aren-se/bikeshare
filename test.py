import pandas as pd
import numpy as np
import time
import datetime
import calendar as cal
import math

df = pd.read_csv('nyc_short.csv')

gender_count = df['Gender'].count()
female_count = df[df['Gender'] == 'Female'].count()[0]
f_pct = int(female_count / gender_count * 100)
male_count = df[df['Gender'] == 'Male'].count()[0]
m_pct = int(male_count / gender_count * 100)


print('   * {:,} female ({}%)'.format(female_count, f_pct))
print('   * {:,} male ({}%))'.format(male_count, m_pct))
