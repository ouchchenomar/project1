#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install researchpy


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

import statistics as stat


# In[3]:


data = pd.read_excel("demographics_MENA.xlsx")
data


# In[4]:


data.head()


# In[5]:


data.describe()


# In[7]:


data.rename(columns={
                         "Age dependency ratio (% of working-age population) [SP.POP.DPND]":"ADR"
                         ,"Age dependency ratio, old [SP.POP.DPND.OL]":"ADR_old"
                         ,"Age dependency ratio, young [SP.POP.DPND.YG]":"ADR_young"
                         ,"Birth rate, crude (per 1,000 people) [SP.DYN.CBRT.IN]":"BRC"
                         ,"Death rate, crude (per 1,000 people) [SP.DYN.CDRT.IN]":"DRC"
                         ,"Fertility rate, total (births per woman) [SP.DYN.TFRT.IN]":"FRT"
                         ,"Life expectancy at birth, female (years) [SP.DYN.LE00.FE.IN]":"LEB_F"
                         ,"Life expectancy at birth, male (years) [SP.DYN.LE00.MA.IN]":"LEB_M"
                         ,"Life expectancy at birth, total (years) [SP.DYN.LE00.IN]":"LEB"
                         ,"Mortality rate, adult, female (per 1,000 female adults) [SP.DYN.AMRT.FE]":"MR_A_F"
                         ,"Mortality rate, adult, male (per 1,000 male adults) [SP.DYN.AMRT.MA]":"MR_A_M"
                         ,"Mortality rate, infant (per 1,000 live births) [SP.DYN.IMRT.IN]":"MR_I"
                         ,"Mortality rate, infant, female (per 1,000 live births) [SP.DYN.IMRT.FE.IN]":"MR_I_F"
                         ,"Mortality rate, infant, male (per 1,000 live births) [SP.DYN.IMRT.MA.IN]":"MR_I_M"
                         ,"Mortality rate, neonatal (per 1,000 live births) [SH.DYN.NMRT]":"MR_n"
                         ,"Net migration [SM.POP.NETM]":"NM"
                         ,"Number of infant deaths [SH.DTH.IMRT]":"NID"
                         ,"Number of infant deaths, female [SH.DTH.IMRT.FE]":"NID_F"
                         ,"Number of infant deaths, male [SH.DTH.IMRT.MA]":"NID_M"
                         ,"Population growth (annual %) [SP.POP.GROW]":"PG_a"
                         ,"Population, female [SP.POP.TOTL.FE.IN]":"PF"
                         ,"Population, male [SP.POP.TOTL.MA.IN]":"PM"
                         ,"Population, total [SP.POP.TOTL]":"PT"
                         ,"Rural population [SP.RUR.TOTL]":"RP"
                         ,"Rural population growth (annual %) [SP.RUR.TOTL.ZG]":"RPG_a"
                         ,"Urban population [SP.URB.TOTL]":"UP"
                         ,"Urban population growth (annual %) [SP.URB.GROW]":"UPG_a"
                         ,"Population ages 65 and above, total [SP.POP.65UP.TO]":"PA>=65"
                         ,"Population ages 15-64, total [SP.POP.1564.TO]":"15<PA<64"
                         ,"Population ages 0-14, total [SP.POP.0014.TO]":"0<PA<14"
                        }, inplace=True)
data
data.info()


# In[9]:


data.nunique() #"identify the continuous and categorical columns in the data"
#remarque len(dataframe)=nombre de lignes !!!!!!!!!!!!!!!!!!!!
missing_data=data.isna().sum()
perc_missingdata=(missing_data/(len(data)))*100
missing_data
perc_missingdata


# In[10]:


data = data.drop(['Country Name','Time Code'],axis=1)
data


# In[11]:


data.rename(columns={'Country Code': 'Region'}, inplace=True)
data


# In[12]:


data.describe().T


# In[13]:


data.dtypes


# In[14]:


data_MAR=data.iloc[:36:4, :]
data_DZA=data.iloc[1:36:4, :]
data_LBY=data.iloc[2:36:4, :]
data_MEA=data.iloc[3:36:4, :]
data_MAR
data_DZA
data_LBY
data_MEA


# In[15]:


data_MAR.describe().T
data_DZA.describe().T
data_LBY.describe().T
data_MEA.describe().T


# In[16]:


data_MAR_POP=data_MAR[['Time', 'Region','ADR', 'ADR_old', 'ADR_young','NM',  'PG_a', 'PF', 'PM', 'PT', 'RP','RPG_a', 'UP', 'UPG_a', 'PA>=65', '15<PA<64', '0<PA<14']]
data_DZA_POP=data_DZA[['Time', 'Region','ADR', 'ADR_old', 'ADR_young','NM',  'PG_a', 'PF', 'PM', 'PT', 'RP','RPG_a', 'UP', 'UPG_a', 'PA>=65', '15<PA<64', '0<PA<14']]
data_LBY_POP=data_LBY[['Time', 'Region','ADR', 'ADR_old', 'ADR_young','NM',  'PG_a', 'PF', 'PM', 'PT', 'RP','RPG_a', 'UP', 'UPG_a', 'PA>=65', '15<PA<64', '0<PA<14']]
data_MEA_POP=data_MEA[['Time', 'Region','ADR', 'ADR_old', 'ADR_young','NM',  'PG_a', 'PF', 'PM', 'PT', 'RP','RPG_a', 'UP', 'UPG_a', 'PA>=65', '15<PA<64', '0<PA<14']]


data_MAR_MOR=data_MAR[['Time', 'Region', 'DRC', 'MR_A_F', 'MR_A_M', 'MR_I', 'MR_I_F', 'MR_I_M','MR_n',  'NID', 'NID_F', 'NID_M']]
data_DZA_MOR=data_DZA[['Time', 'Region', 'DRC', 'MR_A_F', 'MR_A_M', 'MR_I', 'MR_I_F', 'MR_I_M','MR_n',  'NID', 'NID_F', 'NID_M']]
data_LBY_MOR=data_LBY[['Time', 'Region', 'DRC', 'MR_A_F', 'MR_A_M', 'MR_I', 'MR_I_F', 'MR_I_M','MR_n',  'NID', 'NID_F', 'NID_M']]
data_MEA_MOR=data_MEA[['Time', 'Region', 'DRC', 'MR_A_F', 'MR_A_M', 'MR_I', 'MR_I_F', 'MR_I_M','MR_n',  'NID', 'NID_F', 'NID_M']]


data_MAR_BIR=data_MAR[['Time', 'Region', 'BRC', 'FRT','LEB_F', 'LEB_M', 'LEB']]
data_DZA_BIR=data_DZA[['Time', 'Region', 'BRC', 'FRT','LEB_F', 'LEB_M', 'LEB']]
data_LBY_BIR=data_LBY[['Time', 'Region', 'BRC', 'FRT','LEB_F', 'LEB_M', 'LEB']]
data_MEA_BIR=data_MEA[['Time', 'Region', 'BRC', 'FRT','LEB_F', 'LEB_M', 'LEB']]


# In[17]:


print("Médiane : ",stat.median(data_MAR['FRT']))

print("Mean : ",stat.mean(data_MAR['FRT']))

print("Mode : ",stat.mode(data_MAR['FRT']))

print("Quantiles : ",stat.quantiles(data_MAR['FRT']))

print("Variance : ",stat.pvariance(data_MAR_BIR['FRT']))

print("Standar_Deviation: ",stat.stdev(data_MAR_BIR['FRT']))

print("Variation_Coefficient: ",stats.variation(data_MAR_BIR['FRT']))

print("interquartile range : ",stats.iqr(data_MAR_BIR['FRT']))

print("Etendue : ",max(data_MAR_BIR['FRT'])-min(data_MAR_BIR['FRT']))


# In[18]:


region_order = data['Region'].unique()
region_order


# In[19]:


plt.figure(figsize=(8,4))
sns.barplot(x='Region', y='ADR', data=data, order=region_order)
plt.xlabel('Region')
plt.ylabel('Age Dependency Ratio')
plt.title('Age Dependency Ratio Across Different Regions')
plt.show()


# In[20]:


##interpretation:
>Examining the Age Dependency Ratio among regions reveals that DZA bears the most substantial demographic burden, trailed by MEA, LBY, and MAR. This points to potential divergences in the age compositions of populations, signaling diverse economic ramifications.


# In[21]:


plt.figure(figsize=(12, 6))
sns.lineplot(x='Time', y='BRC', data=data, label='Crude Birth Rate')
sns.lineplot(x='Time', y='DRC', data=data, label='Crude Death Rate')

plt.xlabel('Time')
plt.ylabel('Rate per 1,000 people')
plt.title('Trend in Crude Birth Rate and Crude Death Rate Over Time')
plt.legend()
plt.show()


# In[ ]:


##interpretation:
>The Crude Birth Rate line indicates a slow decline in the number of births per 1,000 people, hinting at possible shifts in fertility habits or the adoption of family planning measures.

On the other hand, the consistently low values of the Crude Death Rate line suggest a stable and low mortality rate per 1,000 people. This implies a sustained overall health and longevity in the population.

It's noteworthy that the depicted trends are from the year 2020, likely influenced by the impact of COVID-19 during that period.


# In[26]:


from scipy.stats import pearsonr
plt.figure(figsize=(10, 8))

sns.regplot(x='FRT', y='LEB', data=data, scatter_kws={'s': 50}, line_kws={'color': 'blue'})


plt.xlabel('Fertility Rate (births per woman)')
plt.ylabel('Life Expectancy at Birth (years)')
plt.title('Correlation between Fertility Rate and Life Expectancy')

plt.show()
correlation_coefficient, _ = pearsonr(data_EDA['FRT'].dropna(), data_EDA['LEB'].dropna())
print(correlation_coefficient)


# In[ ]:


#interpretation:
>The correlation coefficient of 0.2692 indicates a mild positive link between Fertility Rate and Life Expectancy. In simple terms, when the number of births per woman goes up, there's a slight tendency for life expectancy to also increase, though the connection isn't very strong.


# In[27]:


data.columns


# In[28]:


data_melted = data.melt(id_vars=['Time'], value_vars=['MR_I', 'MR_I_F', 'MR_I_M'],
                            var_name='Mortality Type', value_name='Mortality Rate')
plt.figure(figsize=(12, 8))
sns.boxplot(x='Mortality Type', y='Mortality Rate', data=data_melted, palette='viridis')

plt.xlabel('Mortality Type')
plt.ylabel('Mortality Rate (per 1,000 live births)')
plt.title('Mortality Rate Variation Between Male and Female Infants')

plt.show()


# In[ ]:


#interpretation:
The boxplots offer insights into Mortality Rates across various age and gender groups. Notably, there's a divergence in median rates; female infants exhibit a slightly lower median rate (17.5) in contrast to the overall infant median (19), whereas male infants show a slightly higher median rate (21). Furthermore, the absence of outliers indicates a consistent distribution of Mortality Rates within the specified age and gender categories.

