# -*- coding: utf-8 -*-
"""
@author: rerwin21
"""

# In[import]
import os, pandas as pd
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
products = pd.read_csv(file_name, nrows=5)


# In[remove_string] 
'''
replace the "remove after loading" string ...
the string below, rm_str is in place just to be extra cautious about ...
leading zeros in the product id. So, to preserve the string format across ...
platforms, I include a string to remove upon loading
'''
rm_str = "remove after loading"
products['product_id'] = products['product_id'].replace(rm_str, "", regex=True)


# In[api_call]
# define api
from lxml import etree
api = amazonproduct.API(locale="us")

# submit a request
results = api.item_lookup("B012A8DUVK", ResponseGroup="ItemAttributes,SalesRank")
print etree.tostring(results, pretty_print=True) # just a string 

