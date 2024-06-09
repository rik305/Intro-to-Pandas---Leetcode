#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A1.
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns = ('student_id','age'))
    return df


# In[ ]:


#A2.
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players),players.shape[1]]


# In[ ]:


#A3: 2879. Display the First Three Rows
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


# In[ ]:


#A4: 2880. Select Data
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101][['name','age']]


# In[ ]:


#A5: 2881. Create a New Column
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 2*employees['salary'] 
    return employees


# In[ ]:


#A6: 2882. Drop Duplicate Rows
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', inplace=True)
    return customers


# In[ ]:


#A7: 2883. Drop Missing Data
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset=['name'])
    return students


# In[ ]:


#A8: 2884. Modify Columns
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary']*2
    return employees


# In[ ]:


#A9: 2885. Rename Columns
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students[['student_id','first_name','last_name','age_in_years']]= students[['id','first','last','age']]
    students.drop(columns=['id','first','last','age'], inplace = True)
    return students


# In[ ]:


#A10: 2886. Change Data Type
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students


# In[ ]:


#A11: 2887. Fill Missing Data
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0,inplace = True)
    return products


# In[ ]:


#A12: 2888. Reshape Data: Concatenate
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1,df2])


# In[ ]:


#A13: 2889. Reshape Data: Pivot
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month',columns='city',values='temperature')


# In[ ]:


#A14: 2890. Reshape Data: Melt
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars = 'product',var_name = 'quarter', value_name = 'sales')


# In[ ]:


#A15: 2891. Method Chaining
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"]>100].sort_values(by=['weight'],ascending = False)[['name']]

