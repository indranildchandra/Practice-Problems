#!/usr/bin/env python
# coding: utf-8

# # Given dataset - Employee.xlsx, calculate the following:
# 1.	Total no of employee (organization size) at each year end
# 2.	Average employee Tenure at each year end
# 3.	Attrition rate for each year (total no employee left in year / Total employee at year end)
# 4.	For each employee match email with first name and last name to get score for match to authenticate email belongs to person
# 
# 
# ## Output format:
#  
# ![image.png](attachment:image.png)

# In[1]:


import pandas as pd
import datetime as dt
import numpy as np


# In[2]:


employee_df = pd.read_excel('Employee.xlsx')


# In[3]:


employee_df.head(5)


# In[4]:


employee_df.dtypes


# In[ ]:





# In[5]:


temp_employee_df = employee_df.copy(deep=True)


# In[6]:


temp_employee_df.DOJ.isnull().sum()


# In[7]:


temp_employee_df.DOL.isnull().sum()


# In[8]:


temp_employee_df['DOJ'] = pd.to_datetime(temp_employee_df['DOJ'], errors='coerce')


# In[9]:


temp_employee_df['YOJ'] = temp_employee_df.DOJ.apply(lambda x: dt.datetime.strftime(x, '%Y'))


# In[10]:


temp_employee_df[['YOJ', 'DOJ']].head(5)


# In[11]:


def extract_year(dol_list):
    try:
        x = dt.datetime.strftime(dol_list, '%Y')
        return x
    except:
        None


# In[12]:


temp_employee_df['YOL'] = temp_employee_df.DOL.apply(extract_year)


# In[13]:


temp_employee_df[['YOL', 'DOL']].head(5)


# In[14]:


temp_employee_df.YOJ.value_counts().sort_index().cumsum(axis = 0)


# In[15]:


temp_employee_df.YOL.value_counts().sort_index().cumsum(axis = 0)


# In[16]:


temp_employee_df.YOJ.value_counts().sort_index().cumsum(axis = 0).subtract(temp_employee_df.YOL.value_counts().sort_index().cumsum(axis = 0))


# In[17]:


answer_df = pd.DataFrame(temp_employee_df.YOJ.value_counts().sort_index().cumsum(axis = 0).subtract(temp_employee_df.YOL.value_counts().sort_index().cumsum(axis = 0)))


# In[18]:


answer_df.rename(columns = {0: 'No_of_employees'}, inplace=True)


# # Answer to Problem #1
# ## Formula: No. of employees at end of year x = Cumulative sum of all employees who have joined between the year 2010 and year x (inclusive) - Cumulative sum of all employees who have left between the year 2010 and year x (inclusive)

# In[19]:


answer_df.head(10)


# In[ ]:





# In[ ]:





# In[20]:


temp_employee_df.dtypes


# In[21]:


pd.datetime.date(dt.datetime.strptime('21-07-2020', '%d-%m-%Y'))


# In[22]:


current_year = '2010'
pd.datetime.date(dt.datetime.strptime('31-12-{}'.format(current_year), '%d-%m-%Y'))


# In[23]:


print(temp_employee_df.loc[1, 'DOL'].date())
print(type(temp_employee_df.loc[1, 'DOL'].date()))


# In[24]:


print(pd.NaT)
print(type(pd.NaT))


# In[25]:


print(np.datetime64('NaT'))
print(type(np.datetime64('NaT')))


# In[26]:


temp_employee_df.loc[1, 'DOL'].date() == pd.NaT


# In[27]:


pd.isnull(temp_employee_df.loc[1, 'DOL'].date())


# In[28]:


def get_tenure(row, current_year):
    print("----------------------------")
    print("Email ID: {}".format(row['email']))
    doj = row['DOJ'].date()
    dol = row['DOL'].date()
    yoj = row['YOJ']
    yol = row['YOL']
    print("DOJ: {}".format(doj))
    print("DOL: {}".format(dol))
    print("YOJ: {}".format(yoj))
    print("YOL: {}".format(yol))
    print("Current Year: {}".format(current_year))
    if yoj > current_year:
        print("YOJ > Current Year, output: {}".format(None))
        return None
    elif yol is not None and yol < current_year:
        print("YOL < Current Year, output: {}".format(None))
        return None
    else:
        if pd.isnull(dol):
            print("DOL is None")
            print("Last date of Current Year: {}".format(pd.datetime.date(dt.datetime.strptime('31-12-{}'.format(current_year), '%d-%m-%Y'))))
            print("Difference between Last Date of Current Year and DOJ: {}".format((pd.datetime.date(dt.datetime.strptime('31-12-{}'.format(current_year), '%d-%m-%Y')) - doj).days))
            return (pd.datetime.date(dt.datetime.strptime('31-12-{}'.format(current_year), '%d-%m-%Y')) - doj).days
        else:
            print("DOL is not None")
            print("Last date of Current Year: {}".format(pd.datetime.date(dt.datetime.strptime('31-12-{}'.format(current_year), '%d-%m-%Y'))))
            print("Minimum of Last date of Current Year and DOL (Last Active Date of Current Year): {}".format(min([dol, pd.datetime.date(dt.datetime.strptime('31-12-{}'.format(current_year), '%d-%m-%Y'))])))
            print("Difference between Last Active Date of Current year and DOJ: {}".format(( min([dol, pd.datetime.date(dt.datetime.strptime('31-12-{}'.format(current_year), '%d-%m-%Y'))]) - doj).days))
            return ( min([dol, pd.datetime.date(dt.datetime.strptime('31-12-{}'.format(current_year), '%d-%m-%Y'))]) - doj).days #/ np.timedelta64(1, 'D')


# In[29]:


# temp_employee_df = temp_employee_df.loc[0:5, :]
# temp_employee_df.head()


# In[30]:


for current_year in ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']:
    temp_employee_df['tenure_sum_in_{}'.format(current_year)] = temp_employee_df.apply(lambda row: get_tenure(row, current_year), axis=1)


# In[31]:


temp_employee_df.head(10)


# In[32]:


print("Number of active employees: ", "\tSum of Tenure of employees: ")
no_active_employees_list, sum_tenure_employees_list = list(), list()
for current_year in ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']:
    no_active_employees_list.append(temp_employee_df['tenure_sum_in_{}'.format(current_year)].notnull().sum())
    sum_tenure_employees_list.append(temp_employee_df['tenure_sum_in_{}'.format(current_year)].sum())
    print(temp_employee_df['tenure_sum_in_{}'.format(current_year)].notnull().sum(), "\t\t\t\t", temp_employee_df['tenure_sum_in_{}'.format(current_year)].sum())


# In[33]:


print(no_active_employees_list)
print(sum_tenure_employees_list)


# In[34]:


tenure_sum_df = pd.DataFrame()
tenure_sum_df['year'] = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
tenure_sum_df['no_active_employees'] = no_active_employees_list
tenure_sum_df['sum_tenure_employees'] = sum_tenure_employees_list


# In[35]:


tenure_sum_df.head(10)


# In[36]:


answer_df['Average_tenure_in_days'] = tenure_sum_df['sum_tenure_employees'].values / tenure_sum_df['no_active_employees'].values


# # Answer to Problem #2
# ## Formula: Average tenure of employees in year x (in days) = Sum of tenure of all employees who were active in the year x / Number of active employees in year x 
# ### where active employees in year x are the ones who have joined on or before year x and left on or after year x

# In[37]:


answer_df.head(10)


# In[ ]:





# In[ ]:





# In[38]:


temp_employee_df.YOL.value_counts().sort_index()


# In[39]:


temp_employee_df.YOL.value_counts().sort_index().values


# In[40]:


answer_df['Attrition_rate'] = temp_employee_df.YOL.value_counts().sort_index().values / answer_df['No_of_employees']


# In[41]:


answer_df.rename_axis('Year', inplace=True)


# # Answer to Problem #3
# ## Formula: Attrition Rate in year x = Number of employees who left in year x / Number of employees at the end of year x

# In[42]:


answer_df.head(10)


# In[43]:


answer_df.to_csv('answer_1_2_3.csv')


# In[ ]:





# In[ ]:





# # Answer to Problem #4
# ## Levenshtein Distance Algorithm was used for fuzzy matching of strings
# ## Formula: email_match_score = max(fuzzy_match_score(first_name, email_name), fuzzy_match_score(last_name, email_name)),
# ### Both first name and last name are matched against the email id of any record since most of the records showed trend that one of either first name or last name is generally mentioned in the email id of the record.
# ### Only the part of the email id before "@" was considered for fuzzy matching.

# In[44]:


# Reference: https://www.datacamp.com/community/tutorials/fuzzy-string-python
def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions, insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        # print("The strings are {} edits away".format(distance[row][col]))
        return distance[row][col]


# In[45]:


levenshtein_ratio_and_distance(s="abc".lower(), t="abd".lower(), ratio_calc = True)


# In[46]:


temp_employee_df.head(5)


# In[47]:


def get_email_match_score(row):
    first_name = row['first_name'].lower()
    last_name = row['last_name'].lower()
    email_name = str(row['email']).split("@")[0].lower()
    
    first_name_match_score = levenshtein_ratio_and_distance(s=first_name, t=email_name, ratio_calc=True)
    last_name_match_score = levenshtein_ratio_and_distance(s=last_name, t=email_name, ratio_calc=True)
    match_score = max(first_name_match_score, last_name_match_score)
    
    return match_score


# In[48]:


employee_df['email_match_score'] = temp_employee_df.apply(lambda row: get_email_match_score(row), axis=1)


# In[49]:


employee_df.head(10)


# In[50]:


employee_df.loc[:, ['id', 'email_match_score']].to_csv('answer_4.csv', index = False)


# In[ ]:





# In[ ]:





# # Answer - #1, #2, #3

# In[51]:


answer_df


# # Answer - #4

# In[52]:


employee_df.loc[:, ['id', 'email_match_score']].head(20)


# In[ ]:





# In[ ]:




