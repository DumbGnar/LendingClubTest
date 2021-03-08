import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import settings as st

warnings.filterwarnings('ignore') #忽略警告
loanDF = pd.read_csv(st.DATA_ACEPETED_PATH)
loanDF.info()

