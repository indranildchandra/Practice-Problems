#!/usr/bin/env python
# coding: utf-8

# # Given dataset - Commentary.txt, calculate following:
# 1. List balls(delivery) when “Four” runs were scored and extract batsman and bowler for the same
# 2. List balls(delivery) when “Yorker” was bowled and extract batsman and bowler for the same
# 
# ## Output Format:
# ![image.png](attachment:image.png)

# In[1]:


import pandas as pd
import numpy as np
import re


# In[2]:


file = open('Commentary.txt', 'r') 
lines = [x.strip() for x in file.readlines()]


# In[3]:


lines


# In[4]:


regex_pattern = re.compile("^[0-9]*[.][0-9]$")


# In[5]:


match_details_list = list()

for line_num, line in enumerate(lines):
    if regex_pattern.match(line):
        delivery = str(line).strip()
        print("Delivery: {}".format(delivery))
        runs_scored = str(lines[line_num-1]).strip()
        print("Runs Scored: {}".format(runs_scored))
        batsman = str(lines[line_num+1]).split('to')[1].strip()
        print("Batsman: {}".format(batsman))
        bowler = str(lines[line_num+1]).split('to')[0].strip()
        print("Bowler: {}".format(bowler))
        commentary = str(lines[line_num+2]).strip()
        print("Commentary: {}".format(commentary))
        is_yorker = "yes" if "yorker" in commentary.lower() else "no"
        print("Is Yorker?: {}".format(is_yorker))
        delivery_details_dict = {"delivery": delivery, "runs_scored": runs_scored, "batsman": batsman, "bowler": bowler, "commentary": commentary, "is_yorker": is_yorker}
        match_details_list.append(delivery_details_dict)


# In[6]:


match_details_df = pd.DataFrame(match_details_list)  


# In[7]:


match_details_df.head(10)


# In[8]:


match_details_df.to_excel('match_details.xlsx', index=False)


# In[9]:


match_details_df.dtypes


# # Answer to Problem #1
# ## Assumption: Extras added to the total due to WIDE balls (marked as WD) have not been considered in the runs scored in any particular delivery. 
# ## Example: for Delivery 2.4 where an extra run was provided due to WIDE ball and boundary (i.e. 4 runs) was scored of the next ball, only 4 runs were associated with Delivery 2.4.

# In[10]:


match_details_df.loc[match_details_df.runs_scored == '4', ['delivery', 'batsman', 'bowler']]


# In[11]:


match_details_df.loc[match_details_df.runs_scored == '4', ['delivery', 'batsman', 'bowler']].to_csv('answer1.csv', index=False)


# # Answer to Problem #2
# ## Assumption: Deliveries where the keyword "yorker" was found in the commentary were tagged as a yorker delivery.

# In[12]:


match_details_df.loc[match_details_df.is_yorker == 'yes', ['delivery', 'batsman', 'bowler']]


# In[13]:


match_details_df.loc[match_details_df.is_yorker == 'yes', ['delivery', 'batsman', 'bowler']].to_csv('answer2.csv', index=False)


# In[ ]:




