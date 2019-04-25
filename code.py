# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
#Code starts here
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)



# --------------
#Code starts here




data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here





top_countries = data.loc[:,['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)
def top_ten(top_countries,column) :
    country_list = []
    top10 = top_countries.nlargest(10,column)
    country_list = list(top10['Country_Name'])
    return country_list;
top_10_summer = list(top_ten(top_countries,'Total_Summer'))
top_10_winter =list(top_ten(top_countries,'Total_Winter'))
top_10 = list(top_ten(top_countries,'Total_Medals'))
common_array = np.intersect1d(top_10_summer,top_10_winter)
common = list(np.intersect1d(common_array,top_10))
print(top_10_summer,top_10_winter,top_10)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
#summer_df.plot('Country_Name','Total_Summer',kind='bar')
#winter_df.plot('Country_Name','Total_Winter',kind='bar')
#top_df.plot('Country_Name','Total_Medals',kind='bar')
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xlabel('Country Name')
plt.ylabel('Medals Won')
plt.xticks(rotation=90)
plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
plt.xlabel('Country Name')
plt.ylabel('Medals Won')
plt.xticks(rotation=90)
plt.title('Winter')
plt.bar(top_df['Country_Name'],top_df['Total_Medals'])
plt.xlabel('Country Name')
plt.ylabel('Medals Won')
plt.xticks(rotation=90)
plt.title('Top')
#plt.legend()
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio  = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'] == summer_max_ratio, 'Country_Name'].iloc[0]
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'] ==winter_max_ratio, 'Country_Name'].iloc[0]
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'] == top_max_ratio, 'Country_Name'].iloc[0] 


# --------------
#Code starts here
data_1 = data.iloc[:-1,:]
data_1['Total_Points'] = (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total'])
most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'] == most_points, 'Country_Name'].iloc[0]
print('Best country :',best_country)


# --------------
#Code starts here
best = data.loc[data['Country_Name'] == best_country]
best = best.loc[:,['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=1)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


