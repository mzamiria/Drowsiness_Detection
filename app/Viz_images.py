#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ipywidgets as widgets
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import voila
sns.set()


# In[2]:


df_eyes=pd.read_csv('eyes_stat.csv')


# In[6]:


##### categorical DropDown widgets

dd1_cat=widgets.Dropdown(options= df_eyes.columns, value=df_eyes.columns[0], description='Category')

dd2_cat=widgets.Dropdown(options= df_eyes.columns, value=df_eyes.columns[3], description='Hue')

ui=widgets.HBox([dd1_cat,dd2_cat])


# In[13]:


def draw_countplot(column,hue):
    plt.figure(figsize=(16, 8))
    
    if df_eyes[column].dtype=='O' and len(df_eyes[column].unique()) > 4:
        p=sns.countplot(data=df_eyes , x=column , hue=hue, hue_order = df_eyes[hue].value_counts().index , order = df_eyes[column].value_counts().index, palette=["C1", "C0"])
        p.set_xticklabels(p.get_xticklabels(), rotation=-45, horizontalalignment='left')
    elif df_eyes[column].dtype=='O' and len(df_eyes[column].unique()) < 5:
        p=sns.countplot(data=df_eyes , x=column , hue=hue,  hue_order = df_eyes[hue].value_counts().index, order = df_eyes[column].value_counts().index, palette=["C1", "C0"])
    elif df_eyes[column].dtype!='O':
        p=sns.countplot(data=df_eyes , x=column , hue=hue, hue_order=df_eyes[hue].value_counts().index, palette=["C1", "C0"])

        
    plt.legend(title=hue, loc='upper right')    
        
out = widgets.interactive_output(draw_countplot, {'column':dd1_cat, 'hue':dd2_cat})
display(ui , out)


# In[ ]:




