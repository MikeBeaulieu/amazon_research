# -*- coding: utf-8 -*-
"""
@author: rerwin21
"""

# In[import]
import re, os, pandas as pd
import amazonproduct


# In[chg_wd]
# what directory is the file in?
data_path = "/home/rerwin21/amazon_proj/"

# now us the os module to change the working directory
os.chdir(data_path)

# In[load_data]
# file name, located in the working directory
file_name = "products_reviewed.csv"

# use pandas to read in the data
products = pd.read_csv(file_name)


# In[remove_string] 