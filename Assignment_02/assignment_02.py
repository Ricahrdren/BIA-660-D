# coding: utf-8

# #### Q1 ####

# In[1]:


import requests
import bs4

# In[2]:


from selenium import webdriver
from selenium.webdriver.support.select import Select

# In[3]:


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# In[4]:


import pandas as pd

# In[5]:


import random
import time

# In[6]:


driver = webdriver.Firefox(executable_path=r'/Users/richard/Downloads/geckodriver 2')

# In[7]:


# driver.close()


# In[7]:


driver.get('http://www.mlb.com')

# In[9]:


time.sleep(5)
stats_header_bar = driver.find_element_by_class_name('megamenu-navbar-overflow__menu-item--stats')

# In[10]:


stats_header_bar.click()

# In[11]:


time.sleep(5)
stats_line_items = stats_header_bar.find_elements_by_tag_name('li')

# In[12]:


stats_line_items[0].click()

# In[13]:


time.sleep(5)
hitting_season_element = driver.find_element_by_id('sp_hitting_season')
season_select = Select(hitting_season_element)

# In[14]:


season_select.select_by_index(3)

# In[15]:


time.sleep(5)
team_2015 = driver.find_element_by_css_selector("#st_parent")

# In[16]:


team_2015.click()

# In[17]:


time.sleep(5)
regular_season_element = driver.find_element_by_id('st_hitting_game_type')
regular_season_select = Select(regular_season_element)

# In[18]:


regular_season_select.select_by_visible_text('Regular Season')

# In[19]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')

# In[20]:


soup = bs4.BeautifulSoup(data_html, "html5lib")

# In[21]:


head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[22]:


len(head)

# In[23]:


df1 = pd.DataFrame(columns=head)

# In[24]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

    # In[25]:

context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[26]:


for i in range(30):
    df1.loc[i] = context_b[i]

# In[27]:


df1 = df1.drop("", axis=1)

# In[28]:


df1

# #### Q2 ####

# In[29]:


time.sleep(5)
AL_bar = driver.find_element_by_css_selector("#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(4)")

# In[30]:


AL_bar.click()

# In[31]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')

# In[32]:


soup = bs4.BeautifulSoup(data_html, "html5lib")

# In[33]:


head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[34]:


df2 = pd.DataFrame(columns=head)

# In[35]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

# In[36]:


context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[37]:


for i in range(15):
    df2.loc[i] = context_b[i]
df2

# In[38]:


df2 = df2.drop("", axis=1)

# In[39]:


df2

# In[40]:


time.sleep(5)
NL_bar = driver.find_element_by_css_selector("#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(6)")

# In[41]:


NL_bar.click()

# In[42]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')

# In[43]:


soup = bs4.BeautifulSoup(data_html, "html5lib")

# In[44]:


head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[45]:


df3 = pd.DataFrame(columns=head)

# In[46]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

# In[47]:


context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[48]:


for i in range(15):
    df3.loc[i] = context_b[i]

# In[49]:


df3.drop("", axis=1)

# In[50]:


time.sleep(5)
hitting_hitting_splits_element = driver.find_element_by_id('st_hitting_hitting_splits')
splits_select = Select(hitting_hitting_splits_element)

# In[51]:


splits_select.select_by_visible_text('First Inning')

# In[52]:

time.sleep(5)
AL_bar.click()

# In[53]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')

# In[54]:


soup = bs4.BeautifulSoup(data_html, "html5lib")

# In[55]:


head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[56]:


df4 = pd.DataFrame(columns=head)

# In[57]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

# In[58]:


context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[59]:


for i in range(15):
    df4.loc[i] = context_b[i]

# In[60]:


df4.drop("", axis=1)

# In[61]:

time.sleep(5)
NL_bar.click()

# In[62]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')

# In[63]:


soup = bs4.BeautifulSoup(data_html, "html5lib")

# In[64]:


head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[65]:


df5 = pd.DataFrame(columns=head)

# In[66]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

# In[67]:


context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[68]:


for i in range(15):
    df5.loc[i] = context_b[i]

# In[69]:


df5.drop("", axis=1)

# #### Q3 ####

# In[70]:


time.sleep(5)
Player_bar = driver.find_element_by_css_selector("#sp_parent")

# In[71]:


Player_bar.click()

# In[72]:


time.sleep(5)
MLB_bar = driver.find_element_by_css_selector("#sp_hitting-1 > fieldset:nth-child(1) > label:nth-child(2)")

# In[73]:


MLB_bar.click()

# In[74]:


time.sleep(5)
hitting_hitting_splits_element1 = driver.find_element_by_id('sp_hitting_hitting_splits')
splits_select1 = Select(hitting_hitting_splits_element1)

# In[75]:


splits_select1.select_by_index(0)

# In[76]:


season_select.select_by_index(1)

# In[77]:


time.sleep(5)
Team_element = driver.find_element_by_id('sp_hitting_team_id')
team_select = Select(Team_element)

# In[78]:


team_select.select_by_visible_text('New York Yankees')

# In[79]:


time.sleep(5)
AB_button = driver.find_element_by_css_selector("th.dg-ab > abbr:nth-child(1)")

# In[80]:


AB_button.click()

# In[81]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[82]:


df6 = pd.DataFrame(columns=head)

# In[83]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[84]:


for i in range(17):
    df6.loc[i] = context_b[i]

# In[85]:


df6.drop("", axis=1)

# In[86]:


time.sleep(5)
All_position_element = driver.find_element_by_id('sp_hitting_position')
position_select = Select(All_position_element)

# In[87]:


position_select.select_by_visible_text('RF')

# In[88]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[89]:


RF = pd.DataFrame(columns=head)

# In[90]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[91]:


for i in range(2):
    RF.loc[i] = context_b[i]

RF.drop("", axis=1)

# In[92]:

time.sleep(5)
position_select.select_by_visible_text('CF')

# In[93]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[94]:


CF = pd.DataFrame(columns=head)

# In[95]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[96]:


for i in range(3):
    CF.loc[i] = context_b[i]

CF.drop("", axis=1)

# In[97]:

time.sleep(5)
position_select.select_by_visible_text('LF')

# In[98]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[99]:


LF = pd.DataFrame(columns=head)

# In[100]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[101]:


for i in range(2):
    LF.loc[i] = context_b[i]

# In[102]:


LF.drop("", axis=1)

# #### Q4 ####

# In[103]:


time.sleep(5)
season_select.select_by_index(3)

# In[104]:


time.sleep(5)
AL_bar_2017_player = driver.find_element_by_css_selector("#sp_hitting-1 > fieldset:nth-child(1) > label:nth-child(4)")
AL_bar_2017_player.click()

# In[105]:


time.sleep(5)
team_element1 = driver.find_element_by_id('sp_hitting_team_id')
team_select1 = Select(team_element1)
team_select1.select_by_visible_text('All Teams')

# In[106]:


time.sleep(5)
position_element1 = driver.find_element_by_id('sp_hitting_position')
position_select1 = Select(position_element1)
position_select1.select_by_visible_text('All Positions')

# In[107]:


time.sleep(5)
AB_AL_2015_bar = driver.find_element_by_css_selector("th.dg-ab > abbr:nth-child(1)")
AB_AL_2015_bar.click()

# In[108]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[109]:


df7 = pd.DataFrame(columns=head)

# In[110]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[112]:


for i in range(50):
    df7.loc[i] = context_b[i]

df7.drop("", axis=1).head()

# #### Q5 ####

# In[113]:


time.sleep(5)
season_select.select_by_index(4)

# In[114]:


time.sleep(5)
MLB_2014_Allstar_bar = driver.find_element_by_css_selector("#sp_hitting-1 > fieldset:nth-child(1) > label:nth-child(2)")
MLB_2014_Allstar_bar.click()

# In[115]:


time.sleep(5)
game_element1 = driver.find_element_by_id('sp_hitting_game_type')
game_select1 = Select(game_element1)
game_select1.select_by_visible_text('All-Star Game')

# In[116]:


time.sleep(5)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[117]:


df8 = pd.DataFrame(columns=head)

# In[118]:


context = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context.append(a.text)

context_b = []
for i in range(int(len(context) / len(head))):
    s = context[i * len(head):(i + 1) * len(head)]
    context_b.append(s)

# In[121]:


for i in range(40):
    df8.loc[i] = context_b[i]

df8.drop("", axis=1)

# ### Q1 Answer ###

# In[124]:


df1.sort_values(by=['HR'], ascending=False)
max_hr_team_name = df1.iloc[1, 1]
max_hr_team_name

# ### Q2 Answer ###

# #### a) ####

# In[134]:


df2.to_csv('2015_AL_data.csv')

# In[135]:


df3.to_csv('2015_NL_data.csv')

# In[136]:


AL_data_2015 = pd.read_csv('2015_AL_data.csv')
HR_mean_AL = AL_data_2015['HR'].mean()
HR_mean_AL

# In[137]:


NL_data_2015 = pd.read_csv('2015_NL_data.csv')
HR_mean_NL = NL_data_2015['HR'].mean()
HR_mean_NL

# In[139]:


if HR_mean_AL > HR_mean_NL:
    print('AL')
else:
    print('NL')

# #### b) ####

# In[140]:


df4.to_csv("2015_AL_data_firstinning.csv")

# In[141]:


df5.to_csv('2015_NL_data_firstinning.csv')

# In[142]:


AL_data_2015_first_inning = pd.read_csv('2015_AL_data_firstinning.csv')
HR_mean_AL_first_inning = AL_data_2015_first_inning['HR'].mean()
HR_mean_AL_first_inning

# In[143]:


NL_data_2015_first_inning = pd.read_csv('2015_NL_data_firstinning.csv')
HR_mean_NL_first_inning = NL_data_2015_first_inning['HR'].mean()
HR_mean_NL_first_inning

# In[144]:


if HR_mean_AL_first_inning > HR_mean_NL_first_inning:
    print('AL')
else:
    print('NL')

# ### Q3 Answer ###

# #### a) ####

# In[152]:


new = df6.sort_values(by=['AVG'], ascending=False)
new

# In[28]:


new = pd.read_csv('over30_maxavg_player.csv')

# In[29]:


max_AVG_Player_name = new.iloc[0, 1]
# max_AVG_Player_name
position = new.iloc[0, 5]
print('max_AVG_Player_name:', 'Garrett N. Cooper')
print('position:', position)

# In[154]:


new.to_csv('over30_maxavg_player.csv')

# #### b) ####

# In[157]:


RFnew = RF.sort_values(by=['AVG'], ascending=False)
RFnew

# In[161]:


RF_max_AVG_Player_name = RFnew.iloc[0, 1]
# max_AVG_Player_name
RF_position = RFnew.iloc[0, 5]
print('RF_max_AVG_Player_name:', RF_max_AVG_Player_name)
print('RF_position:', RF_position)

# In[162]:


CFnew = CF.sort_values(by=['AVG'], ascending=False)
CFnew

# In[163]:


CF_max_AVG_Player_name = CFnew.iloc[0, 1]
# max_AVG_Player_name
CF_position = CFnew.iloc[0, 5]
print('CF_max_AVG_Player_name:', CF_max_AVG_Player_name)
print('CF_position:', CF_position)

# In[166]:


LFnew = LF.sort_values(by=['AVG'], ascending=False)
LFnew

# In[167]:


LF_max_AVG_Player_name = LFnew.iloc[0, 1]
# max_AVG_Player_name
LF_position = LFnew.iloc[0, 5]
print('LF_max_AVG_Player_name:', LF_max_AVG_Player_name)
print('LF_position:', LF_position)


RF= RFnew['Player'][0]
RF_AVG=RFnew['AVG'][0]
CF=CFnew['Player'][0]
CF_AVG=CFnew['AVG'][0]
LF=LFnew['Player'][0]
LF_AVG=LFnew['AVG'][0]

if RF_AVG > CF_AVG:
    print('player:', RF)
else:
    print('player:', CF)


if RF_AVG > LF_AVG:
    print('player:', RF)
else:
    print('player:', LF)

RF= RFnew['Player'][0]
RF
# In[168]:


RFnew.to_csv('RF.csv')
CFnew.to_csv('CF.csv')
LFnew.to_csv('LF.csv')

# ### Question 4  Answer ###

# In[170]:


AL_regular_2015 = df7.sort_values(by=['AB'], ascending=False)
AL_regular_2015.head()

# In[173]:


AL_regualr_2015_Player_name = AL_regular_2015.iloc[0, 1]
# max_AVG_Player_name
AL_regualr_2015_position = AL_regular_2015.iloc[0, 5]
AL_regualr_2015_team = AL_regular_2015.iloc[0, 2]
print('AL_regualr_2015_Player_name:', AL_regualr_2015_Player_name)
print('AL_regualr_2015_position:', AL_regualr_2015_position)
print('AL_regualr_2015_team:', AL_regualr_2015_team)

# In[174]:


AL_regular_2015.to_csv('AL_regular_2015.csv')

# ### Question 5 Answer ###

# In[8]:


latin_coun = '''Argentina;Bolivia;Brazil;Chile;Colombia;Costa Rica;Cuba;Dominican Republic;Ecuador;El Salvador;French Guiana;Guadeloupe;Guatemala;Haiti;Honduras;Martinique;Mexico;Nicaragua;Panama;Paraguay;Peru;Puerto Rico;Saint Barthélemy;Saint Martin;Uruguay;Venezuela'''

# In[9]:


latin_coun_list = latin_coun.split(';')

# In[10]:


latin_coun_list

# In[11]:


player_list = []
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
for t in soup.tbody.find_all("tr"):
    player_list.append(t.find_all('td')[1].text.strip())
    # for a in t.find_all("td")[1]:
    #   player_list.append(a.text)

player_list

# In[14]:


data = []
for a in player_list:
    player_name_bar = driver.find_elements_by_link_text(a)
    for k in range(len(player_name_bar)):
        player_name_bar_temp = driver.find_elements_by_link_text(a)

        # player_name = driver.find_element_by_css_selector('#_715571520275262687 > tbody:nth-child(36) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
        player_name_bar_temp[k].click()
        wait = WebDriverWait(driver, 10)
        player_bio = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'player-bio')))
        # p_born = driver.find_element_by_css_selector('div.player-bio:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > span:nth-child(1)').text
        for b in latin_coun_list:
            if b in player_bio.text:
                # born = a.find_element_by_class_name('player-bio').text
                # if country in born:
                player_name = driver.find_element_by_class_name('full-name').text
                normal_delay = random.normalvariate(20, 0.5)
                time.sleep(normal_delay)
                # player_team=driver.find_element_by_class_name('dropdown.team')
                datahtml = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dropdown.team'))).text
                # datahtml=driver.find_element_by_class_name('dropdown.team').text
                team_name = datahtml.split('\n')[0].strip()
                # soup = bs4.BeautifulSoup(datahtml,"html5lib")
                # player_team_update=soup.find('span', attrs={'data-bind': 'text: selectedTeamLabel'}).text
                print('player_name:', player_name)
                data.append(player_name)
                print('team_name:', team_name)
                data.append(team_name)

        driver.back()
        normal_delay = random.normalvariate(20, 0.5)
        time.sleep(normal_delay)

head = ['Players','Team']
context_5 =[]
for i in range(int(len(data)/len(head))):
    s= data[i*len(head):(i+1)*len(head)]
    context_5.append(s)
context_5

head = ['Players','Team']
df_q5=pd.DataFrame(columns= head)
for i in range(16):
    df_q5.loc[i]= context_5[i]
df_q5.to_csv('q5.csv')

# ### Question 6 ###

# In[15]:


import http.client, urllib.request, urllib.parse, urllib.error, base64
import json


# In[16]:


def api(html):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'eb565a0b452d454fb465d9f11e50ac0a',
    }

    conn = http.client.HTTPSConnection('api.fantasydata.net')
    conn.request("GET", html, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    return data


# In[17]:


data2 = api("/v3/mlb/stats/json/Stadiums")

# In[18]:


data2 = json.loads(data2)
data2

# In[19]:


context_2 = []
for i in data2:
    context_2.append([i["StadiumID"], i["Name"], i["City"], i["State"]])
context_2

# In[20]:


data3 = api("/v3/mlb/stats/json/Games/2016")

# In[22]:


data4 = json.loads(data3)

# In[23]:


context = []
for i in data4:
    context.append([i["HomeTeam"], i["AwayTeam"], i["DateTime"][0:10], i["StadiumID"]])
context

# In[24]:


ss = []
for i in context:
    for j in context_2:
        if i[3] == j[0]:
            a = i[:-1] + j[1:]
            ss.append(a)
ss

# In[25]:


final = []
for a in ss:
    if 'HOU' in a:
        # print(a)
        final.append(a)
    else:
        pass

# In[26]:


final

df_q6=pd.DataFrame(columns=['Home Team','Away team','Day', 'Stadium','City','State'])
for i in range(164):
    df_q6.loc[i]= final[i]

df_q6.to_csv('q6.csv')

