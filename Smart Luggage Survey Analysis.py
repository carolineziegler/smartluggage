#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


inpPath = "C:/CarolineZiegler/Studium_DCU/8. Semester/Business Analytics Portfolio/Portfolio/02_Uni Projects/"
NED_Df = pd.read_csv(inpPath + "Blank Quiz.csv", delimiter = ",")
NED_Df


# In[3]:


NED_Df.drop("Timestamp", inplace = True, axis =1)
NED_Df


# In[4]:


NED_Df.columns


# In[5]:


NED_Df.rename(columns = {"How old are you?": "Age", 
                         "What is your nationality (nationalities)?":"Nationality", 
                         "Where do you currently reside (city and country)?": "Current Residence",
                         "What is your occupation?": "Occupation",
                         "How often do you travel per year (by airline, train, bus, etc.)?":"Travel per year", 
                         "What type of luggage do you use when travelling? (multiple answers possible)":"Travel Luggage", 
                         "Do you use bulky luggage and if so, for what items?":"Bulky Luggage", 
                         "Do you plan to buy a new piece of luggage in the next year?":"Luggage Buying Plans (next year)", 
                         "If yes, what type of luggage and why?":"Plan-to-buy Luggage", 
                         "Have you ever had to repack your luggage because you exceeded the weight limit?":"Repacking Luggage", 
                         "Have you ever left behind your luggage somewhere when travelling?": "Forgotten luggage", 
                         "Has your luggage ever been misplaced by an airline?":"Misplaced Luggage by Airlines", 
                         "Do you own any smart luggage?":"Smart Luggage Owner", 
                         "If yes, which smart luggage do you own and why did you buy it? ":"Kind of Smart Luggage", 
                         "If no, what currently prevents you from purchasing a smart luggage?":"Prevention from Buying Smart Luggage", 
                         "Do you own and use an AirTag or similar tracking device when travelling?":"AirTag Users", 
                         "What would enhance your travel experience when travelling with luggage (e.g. tracking device, integrated scale)?":"Travel Enhancements", 
                         "What are your biggest concern(s)/fear(s) when travelling with luggage?":"Biggest travel Concerns & Fears", 
                         "How much would you be willing to pay for such a solution?":"Price Sensitivity for a Add-on Digital Solution"}, inplace = True)
NED_Df


# In[6]:


NED_Df = NED_Df[NED_Df['Age'] >= 18]
NED_Df


# In[7]:


NED_Df["Nationality"].unique()


# In[8]:


NED_Df["Nationality"] = NED_Df["Nationality"].str.capitalize()
NED_Df


# In[9]:


NED_Df["Nationality"].unique()


# In[10]:


NED_Df["Nationality"].replace("Germany", "German", inplace = True)
NED_Df["Nationality"].replace("Deutsch", "German", inplace = True)
NED_Df["Nationality"].replace("France", "French", inplace = True)
NED_Df["Nationality"].replace("Germqn", "German", inplace = True)
NED_Df["Nationality"].replace("Germany ", "German", inplace = True)
NED_Df["Nationality"].replace("Deutsch ", "German", inplace = True)
NED_Df["Nationality"].replace('Gemany', "German", inplace = True)
NED_Df["Nationality"].replace("Ferman", "German", inplace = True)
NED_Df["Nationality"].replace("Austria ", "Austria", inplace = True)
NED_Df["Nationality"].replace("Swiss ", "Swiss", inplace = True)
NED_Df["Nationality"].replace("Usa (former austria) ", "American", inplace = True)
NED_Df["Nationality"].replace('Usa (former austria)', "American", inplace = True)
NED_Df["Nationality"].replace('Belgian ', "Belgian", inplace = True)
NED_Df["Nationality"].replace('German ', "German", inplace = True)
NED_Df["Nationality"].replace('French ', "French", inplace = True)
NED_Df["Nationality"].replace("German, swiss", "Dual citizenship", inplace = True)
NED_Df["Nationality"].replace("Swiss italian", "Dual citizenship", inplace = True)
NED_Df["Nationality"].replace("German and new zealand ", "Dual citizenship", inplace = True)
NED_Df["Nationality"].replace("German and irish", "Dual citizenship", inplace = True)
NED_Df["Nationality"].replace("German and british", "Dual citizenship", inplace = True)
NED_Df["Nationality"].replace("German, bulgarian", "Dual citizenship", inplace = True)
NED_Df["Nationality"].replace("German, french", "Dual citizenship", inplace = True)
NED_Df["Nationality"].replace("Italian ", "Italian", inplace = True)
NED_Df["Nationality"].replace("Austria", "Austrian", inplace = True)
NED_Df["Nationality"].replace("Various", "Dual citizenship", inplace = True)
NED_Df["Nationality"].replace('German, american ', "Dual citizenship", inplace = True)

NED_Df["Nationality"].unique()


# In[11]:


values_to_replace = ["German / irish", "Germany / uk / malta ", "German-brazilian", "German / italian", "German+ usa", "German and french", "German, british", "Belgian french", "German and swiss", "German, american", "German, australian", "Austria, germany"]  
NED_Df["Nationality"].replace(values_to_replace, "Dual citizenship", inplace=True)
NED_Df["Nationality"].unique()


# In[12]:


nationality_counts = NED_Df["Nationality"].value_counts()

plt.pie(nationality_counts, labels=nationality_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Nationalities')
plt.show()


# In[13]:


nationality_counts


# In[14]:


conditions = [
    (NED_Df["Age"] <= 24),
    (NED_Df["Age"] >= 25) & (NED_Df["Age"] <= 33),
    (NED_Df["Age"] >= 34) & (NED_Df["Age"] <= 42),
    (NED_Df["Age"] >= 43) & (NED_Df["Age"] <= 51),
    (NED_Df["Age"] >= 52)
]

values = ["16-24", "25-33", "34-42", "43-51", ">52"]

NED_Df["Age Range"] = np.select(conditions, values, default="Unknown")
NED_Df


# In[15]:


age_range_counts = NED_Df["Age Range"].value_counts()

plt.pie(age_range_counts, labels=age_range_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Age')
plt.show()


# In[16]:


age_range_counts 


# In[17]:


NED_Df["Current Residence"].unique()


# In[18]:


values_to_replace_IRE = ["Dublin, Ireland ", "Dublin, Ireland", "dublin ireland", "Galway, Ireland ", "Ireland ", "Dublin Ireland ", "Dublin", "Dublin "]  
NED_Df["Current Residence"].replace(values_to_replace_IRE, "Ireland", inplace=True)
NED_Df["Current Residence"].unique()


# In[19]:


values_to_replace_DE = ["Kirchentellinsfurt", 'Tübingen Germany ', "Weinstadt, Germany ", "Tübingen, Germany", "Kirchentellinsfurt, Germany", "BERLIN/GERMANY", "Laaber - Germany", "Esslingen, germany", "Germany ", "Frankfurt Germany ", "Kaarst germany", "Mainz", "hamburg/germany", "Hamburg Germany ", "Hannover, Germany", "Stuttgart/Germany", "Günstadt Germany ", "Stuttgart, Germany ", "Stuttgart Germany", "Karlsruhe, Germany", "Frankfurt Germany", "Stuttgart, Germany", "Trier, Germany", "Berlin / Germany", "Germany, Bonn", "Augsburg, Germany", "Marburg, Germany ", "Mannheim, Germany", 'Frankfurt, Germany', 'Freiburg, Germany', 'Kassel, Germany',
       '02799 Waltersdorf, Germany', 'Reutlingen, Germany', "Esslingen, germany ",
       'Jena, Germany ', 'Konstanz, Germany', "Munich, Germany ", "Fladungen, Germany", "Mainz, Germany", "Berlin, Germany","Kirchentellinsfurt, Germany ", "Darmstadt, Germany", "Munich Germany ", "stuttgart ,germany ", "Bielefeld, Germany", "Leipzig, Germany", "Munich, Germany", "Heidelberg, Germany ", "Heidelberg, germany ", "Deutschland, Hessen, Königstein im Taunus ", "Munich", "Dresden, Germany ", "Cologne, Germany ", "Pfaffenhofen an der Ilm, Germany", "weinstadt, Germany", "Germany, Schleswig-Holstein, 25436 Tornesch", "Frankfurt am Main, Germany", "Cologne", "Erlangen, Germany", "Regensburg, Germany ", "Elsterheide, Germany", "Frankfurt", "Berlin, GERMANY ", "Dresden in Deutschland ", "Munich "]  
NED_Df["Current Residence"].replace(values_to_replace_DE, "Germany", inplace=True)
NED_Df["Current Residence"].unique()


# In[20]:


values_to_replace_UK = ["Lancaster, UK", "Leeds, UK ", "London, UK", "Cambridge, UK", "London (GB)", "Loughborough, UK", "United Kingdom, Cambridgeshire", "England ", "Glasgow, UK", "Guildford, UK", "uk"]  
NED_Df["Current Residence"].replace(values_to_replace_UK, "UK", inplace=True)
NED_Df["Current Residence"].unique()


# In[21]:


values_to_replace_Belgium = ["bruxelles belgium", "waterloo belgium ", "Liège, Belgium"]  
NED_Df["Current Residence"].replace(values_to_replace_Belgium, "Belgium", inplace=True)
NED_Df["Current Residence"].unique()


# In[22]:


values_to_replace_Netherlands = ["Maastricht, The Netherlands", "Haarlem/ Netherlands ", "Utrecht, Netherlands", "Breda, Netherlands ", "Groningen ", "Maastricht, Netherlands"]  
NED_Df["Current Residence"].replace(values_to_replace_Netherlands, "Netherlands", inplace=True)
NED_Df["Current Residence"].unique()


# In[23]:


values_to_replace_France = ["Marseille france", "Lyon", "Toulouse ", "Toulouse, France", "Huningue France"]  
NED_Df["Current Residence"].replace(values_to_replace_France, "France", inplace=True)
NED_Df["Current Residence"].unique()


# In[24]:


values_to_replace_Spain = ["Madrid, Spain", "Valencia, Spain"]  
NED_Df["Current Residence"].replace(values_to_replace_Spain, "Spain", inplace=True)
NED_Df["Current Residence"].unique()


# In[25]:


values_to_replace_USA = ["Houston, Texas (USA)", "Fargo, ND, USA", "Granger USA", "Elon, US", "Raleigh, United States", "Houston, United States", "Beach Lake, USA", "Usa", "Utah, USA ", "Monroe, NY, USA", "Washington D.C., USA"]  
NED_Df["Current Residence"].replace(values_to_replace_USA, "USA", inplace=True)
NED_Df["Current Residence"].unique()


# In[26]:


values_to_replace_Canada = ["Vancouver, Canada", "Montreal, Canada", "Toronto, Canada"]  
NED_Df["Current Residence"].replace(values_to_replace_Canada, "Canada", inplace=True)
NED_Df["Current Residence"].unique()


# In[27]:


values_to_replace_Switzerland = ["Switzerland ", "Zürich, Switzerland ", 'Olten Switzerland', 'Basel, Switzerland', "St. Gallen, Switzerland", "Basel, Switzerland ", "Uznach Switzerland "]  
NED_Df["Current Residence"].replace(values_to_replace_Switzerland, "Switzerland", inplace=True)
NED_Df["Current Residence"].unique()


# In[28]:


values_to_replace_UAE = ["Dubai / UAE", "Dubai, UAE", "Dubai, United Arab Emirates", "Dubai", "Dubai VAE"]  
NED_Df["Current Residence"].replace(values_to_replace_UAE, "United Arab Emirates", inplace=True)
NED_Df["Current Residence"].unique()


# In[29]:


values_to_replace_China = ["Hong Kong, P. R. China", "Suzhou, China", "Hong Kong,  China ", "Beijing, China"]  
NED_Df["Current Residence"].replace(values_to_replace_China, "China", inplace=True)
NED_Df["Current Residence"].unique()


# In[30]:


values_to_replace_Japan = ["Kusatsu, Japan", "Tokyo, Japan"]  
NED_Df["Current Residence"].replace(values_to_replace_Japan, "Japan", inplace=True)
NED_Df["Current Residence"].unique()


# In[31]:


values_to_replace_Jordan = ["Amman / Jordan", "Amman, jordan"]  
NED_Df["Current Residence"].replace(values_to_replace_Jordan, "Jordan", inplace=True)
NED_Df["Current Residence"].unique()


# In[32]:


values_to_replace_Australia = ["Sydney"]  
NED_Df["Current Residence"].replace(values_to_replace_Australia, "Australia", inplace=True)
NED_Df["Current Residence"].unique()


# In[33]:


values_to_replace_Austria = ["Dornbirn austria"]  
NED_Df["Current Residence"].replace(values_to_replace_Austria, "Austria", inplace=True)
NED_Df["Current Residence"].unique()


# In[34]:


values_to_replace_Portugal = ["Santarém portugal ", "Lisbon, Portugal"]  
NED_Df["Current Residence"].replace(values_to_replace_Portugal, "Portugal", inplace=True)
NED_Df["Current Residence"].unique()


# In[35]:


values_to_replace_Rwanda = ["Kigali rwanda"]  
NED_Df["Current Residence"].replace(values_to_replace_Rwanda, "Rwanda", inplace=True)
NED_Df["Current Residence"].unique()


# In[36]:


values_to_replace_Finland = ["Helsinki, Finland"]  
NED_Df["Current Residence"].replace(values_to_replace_Finland, "Finland", inplace=True)
NED_Df["Current Residence"].unique()


# In[37]:


values_to_replace_Poland = ["Cracow Poland "]  
NED_Df["Current Residence"].replace(values_to_replace_Poland, "Poland", inplace=True)
NED_Df["Current Residence"].unique()


# In[38]:


values_to_replace_Pakhistan = ["Lahore "]  
NED_Df["Current Residence"].replace(values_to_replace_Pakhistan, "Pakhistan", inplace=True)
NED_Df["Current Residence"].unique()


# In[39]:


values_to_replace_Namibia = ["Omaruru Namibia"]  
NED_Df["Current Residence"].replace(values_to_replace_Namibia, "Namibia", inplace=True)
NED_Df["Current Residence"].unique()


# In[40]:


values_to_replace_Indonesia = ["Jakarta, Indonesia"]  
NED_Df["Current Residence"].replace(values_to_replace_Indonesia, "Indonesia", inplace=True)
NED_Df["Current Residence"].unique()


# In[41]:


values_to_replace = ["Country", "city"]  
NED_Df["Current Residence"].replace(values_to_replace, "NaN", inplace=True)
NED_Df["Current Residence"].unique()


# In[42]:


values_to_replace_Qatar = ["Doha, Qatar"]  
NED_Df["Current Residence"].replace(values_to_replace_Qatar, "Qatar", inplace=True)
NED_Df["Current Residence"].unique()


# In[43]:


values_to_replace_Vietnam = ["Hanoi, Vietnam "]  
NED_Df["Current Residence"].replace(values_to_replace_Vietnam, "Vietnam", inplace=True)
NED_Df["Current Residence"].unique()


# In[44]:


values_to_replace_Romania = ["Bucharest"]  
NED_Df["Current Residence"].replace(values_to_replace_Romania, "Romania", inplace=True)
NED_Df["Current Residence"].unique()


# In[45]:


residence_counts = NED_Df["Current Residence"].value_counts()

plt.pie(residence_counts, labels=residence_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Residence')
plt.show()


# In[46]:


residence_counts


# In[47]:


NED_Df["Occupation"].unique()


# In[48]:


students = ['Music student ',"Students",'Student','student ','Stduent','gap year','Student at a University','university student ','Student, but also working at DZ BANK','working student','Student / Working Student','Student / Private Equity Working Student','dual student','Architektur Student','Consultant in a Student Consultancy & Student','Student & part-time flight attendant','School']
retired =['Retired', 'retired']
unknown = ['-', 'None', 'Not working', 'None ']
homemakers = ['Housewife','Homemaker','Home maker','Housewife ','Midwife','Direct Sales and Stay at home mom']
healthcare_professions = ['EMS-Personaltrainer and Human Ressource Manager','psycholoog','Nutritionist','Medical sciences','Nurse','Physiotherapeutin','Pharmacist','Physiotherapist','Pharmacist at the UN','Nutritionist','Medical sciences']
education_professions = ['Teacher','Professor at University','Student Assistent','Education Consultant']
creative_professions = ['Architect','Interior designer','Publishing service provider','Photographer','Graphic designer','Web designer','Real Estate Business','Goldsmith','Journalist','Music student','Web designer','Translator']
management_professionals = ['Sales director','Assistent Productionmanager','Sales','Office Assistant','Self occupied','school secretary','Self occupied ','Business Development for Training Company','Personal assistant','Office Manager','Business Development for Training Company','Assistant','Management Assistant ','Executive Assistant','EMS-Personaltrainer and Human Resource Manager ','Executive','CEO','Business manager','Manager','Self employed','Self employed','Self-employed','Interim manager- self employed','Backoffice Manager','Business owner (Coach)','Senior Vice President','Head of Marketing & Communication','Management Assistant','Test Manager','Managing Director','Customer support']
advisory = ['Social and psychological counselor','Self-employed consultant','Advisor','Consultant','Labour lawyer','Market research consultant','Software Consultant']
finance = ['Banker','Credit risk analyst']
research = ['Senior Researcher','PostDoc']
engineering_professionals = ['Civilengineer','Civil Engineering','Software-Engineer/Computer Scientist']
marketing_professions = ['Sales director ','Trainee PR','Customer Success']
social_professions = ['Social worker','Social and psychological counselor ']
hospitality_professions = ['Driver/Cook/Cleaner/Entertainer/Therapist','Self ocvupied in tourism','Tour operator','Travel agent','Shipping Operator','Travel agent ','Travelagent']
government_professions = ['Diplomat (Angestellte geh. Dienst)']
architecture_professions = ['Architect ','Apartment ','Property Manager']
miscellaneous = ['Intern','Basket ball','Intern, Founder‘s Associate'] 

conditions = [
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, students)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, retired)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, unknown)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, homemakers)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, healthcare_professions)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, education_professions)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, creative_professions)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, management_professionals)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, advisory)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, finance)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, research)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, engineering_professionals)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, marketing_professions)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, social_professions)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, hospitality_professions)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, government_professions)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, architecture_professions)),
    NED_Df["Occupation"].str.strip().str.lower().isin(map(str.lower, miscellaneous))
]


choices = ["Students", 
           "Retired", 
           "Unknown", 
           "Homemakers",
           "Healthcare Professions",
           "Education Professions",
           "Creative and Design Professions",
           "Management Professions", 
           "Advisory and Consulting Professions", 
           "Finance and Banking", 
           "Researcher", 
           "Engineering Professions", 
           "Marketing Professions", 
           "Social Professions", 
           "Hospitality Professions",
           "Governmental Professions",
           "Architecture Professions",
           "Miscellaneous"]

NED_Df["Occupation Group"] = np.select(conditions, choices, default="Other")
NED_Df


# In[49]:


NED_Df["Occupation Group"].unique()


# In[50]:


occupation_counts = NED_Df["Occupation Group"].value_counts()

plt.pie(occupation_counts, labels=occupation_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Occupation')
plt.show()


# In[51]:


occupation_counts


# In[52]:


occupation_counts.sum()


# In[53]:


travel_frequency_counts = NED_Df["Travel per year"].value_counts()

plt.pie(travel_frequency_counts, labels=travel_frequency_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Travel Frequency')
plt.show()


# In[54]:


travel_frequency_counts


# In[55]:


NED_Df["Bulky Luggage"].unique()


# In[56]:


values_to_replace = ["nan",'No, I don’t use bulky luggage when traveling ','No','No ','no, i hate too much luggage',"No, I don't.",'All of my luggage', 'Suitcase ','Not necessarily unless its for a long stay, it is usually clothes','normally not ','Mostly not ','Not really ','Apart from a checked suitcase, no.','No not really','Not really','No, I only travel with small luggage','Usually not','no']  
NED_Df["Bulky Luggage"].replace(values_to_replace, "No", inplace=True)

values_to_replace_clothes = ['Clothes','Clothes, Books, Electronical devices, usual travel objects','Clothes ','Clothes and Personal Belonging','Shoes, coats, heavier clothing, sports equipment ','Clothes and personal belongings ','clothing','Clothing, expansive things ', 'Clothes an co. ','Suitcase for clothes','Clothing shoes toilettery','Cloths','normally not ','Mainly clothes and vanity bag(s)','clothing, camera equipment, shoes, liquids, climbing gear']  
NED_Df["Bulky Luggage"].replace(values_to_replace_clothes, "Clothes and Personal Belonging", inplace=True)

values_to_replace_sport = ['Snowboard ','Racing Bike','Bike','Hiking sticks','Scuba Equipment ','Yes, for Sports equipment','Sirfboard','Golf','Sometimes Golf Equipment ', 'Surfboards ', 'Ski']  
NED_Df["Bulky Luggage"].replace(values_to_replace_sport, "Sport Equipment", inplace=True)

values_to_replace_moving = ['Kartons when bringing items from home country','I do when I go back to Germany. Mostly for bringing back German products (food, cosmetics, etc)','Suitcase if I have to take large amounts of clothing, gifts, etc.','When moving to a new place, otherwise I try to avoid it.','when I move countries']  
NED_Df["Bulky Luggage"].replace(values_to_replace_moving, "Moving Purpose", inplace=True)

values_to_replace_vacation = ['Yes, for longer travel periods. Mostly for clothes and liquid (skin) care products >100ml when traveling by plane.','For long vacation, I usually use a middle seize suitcase. For less than 2 weeks I like to use a backpack. ','Only for very long trips','Rarely, only if travelling for a month or more.','Only for a festival but not regularly ','only for longer travels (eg big suitcase) by plane, happens once in a couple of years','for longer holidays (~10+ days), I use a big suitcase','For longer vacations and when I moved from Germany to Spain, so mostly clothes ','If you travel for a longer period of stuff, you simply need more space','Longer trips, clothes and gifts']  
NED_Df["Bulky Luggage"].replace(values_to_replace_vacation, "Longer Vacation", inplace=True)

values_to_replace_instruments = ['Yes, instruments']  
NED_Df["Bulky Luggage"].replace(values_to_replace_instruments, "Instruments", inplace=True)

values_to_replace_big_things = ['Child Seat','For fragile items']  
NED_Df["Bulky Luggage"].replace(values_to_replace_big_things, "Bulky and Fragile Things", inplace=True)

values_to_replace_animals = ['Dog']  
NED_Df["Bulky Luggage"].replace(values_to_replace_animals, "Animals", inplace=True)

values_to_replace_other = ['Only if  necessary ','Various']  
NED_Df["Bulky Luggage"].replace(values_to_replace_other, "Other", inplace=True)

NED_Df["Bulky Luggage"].unique()


# In[57]:


bulky_luggage_counts = NED_Df["Bulky Luggage"].value_counts()

plt.pie(bulky_luggage_counts, labels=bulky_luggage_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Bulky Luggage Usage')
plt.show()


# In[58]:


bulky_luggage_counts


# In[59]:


NED_Df["Plan-to-buy Luggage"].unique()


# In[60]:


values_to_replace_small_suitcase = ['Carry on suitcase ','Suitcase (carry on)','Small carry on because the handle on the old one is faulty','Carry on suitcase, travel frequency will increase due to new job','suitcase for flights''Carry on suitcase ', 'carry on suitcase ','Soft case ', 'Carry-on suitcase','suitcase (carry on)','New carry on suitcase because my current one is damaged ','Carey on suitcase','A lighter suitcase for maximising the benefits of carry-on luggage ','Suitcase in very light fabric','A small hand luggage suitcase (to be taken in the plane), because it costs less than a regular big suitcase (and is even free with some airlines)','Carry On suite case, don’t have one in Dublin','Suitcase and carry on trolkey','Carry on suitcase']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_small_suitcase, "Carry-on Suitcase", inplace=True)

values_to_replace_suitcase = ['Suitcase (check-in)','suitcase (checked-in luggage) as my old one is quite old and starts to fall apart in places','check in luggage','Suitcase ','New suitcase because my old one broke', 'meidum-size suitcase','Hard shell suitcase for a longer trip','a suitcase because my current ones are old','suitcase because mine is too small','Suitcase, mid-size; old one worn off','Suitcase (checkin luggage))','Lightweight suitcase', 'Big suitcase, current one broke']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_suitcase, "Check-in Suitcase", inplace=True)

values_to_replace_backpack = ['Backpack','A backpack for hand luggage']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_backpack, "Backpack (small)", inplace=True)

values_to_replace_suitcase_set = ['suitcase set (I need a business set)']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_suitcase_set, "Suitcase Set", inplace=True)

values_to_replace_big_backpack = ['Bigger Backback for a backpacking trip ','Bigger backpack... My current backpack ist to small and not comfortable ','Backpack (about 50 litre)']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_big_backpack, "Backpack(big)", inplace=True)

values_to_replace_dufflebag = ['Duffel bag because old one is damaged']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_dufflebag, "Dufflebag", inplace=True)

values_to_replace_bag_wheels = ['Bag with Wheely','Suitcase with wheels for both check in and hand carry. The current suitcase is falling apart.','Bag with wheels, light weight, easy to carry ']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_bag_wheels, "Bag with Wheels", inplace=True)

values_to_replace_old = ['Handluggage because mine is broken ','Bigger suitcase as my old one needs to be renewed ','New suitcase as my old one is not the best anymore (old)','Suitcase, because I want to get a better one with more quality ','Replacing an old suitcase','suitcase, wear an tear']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_old, "Replacing Old Luggage", inplace=True)

values_to_replace_no = ['/']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_no, "No", inplace=True)

values_to_replace_other = ["I love buying bags so I guess I'll buy something at some point ",'suitcase for flights','Rimowa - because of the good quality (light and long lasting)','suitcase, wear an tear','Rimowa suitcase ','Case for bicycle','Suitcase with 4 wheels','Current one broke','Bag for carry on','A new laptop backpack']  
NED_Df["Plan-to-buy Luggage"].replace(values_to_replace_other, "Other", inplace=True)

NED_Df["Plan-to-buy Luggage"].unique()


# In[61]:


buying_luggage_counts = NED_Df["Plan-to-buy Luggage"].value_counts()

plt.bar(buying_luggage_counts.index, buying_luggage_counts, color='turquoise', width=0.3)
plt.title('Buying Luggage Plans')
plt.xticks(fontsize=5)
plt.show()


# In[62]:


buying_luggage_counts


# In[63]:


buy_luggage_counts = NED_Df["Plan-to-buy Luggage"].value_counts()

plt.pie(buy_luggage_counts, labels=buy_luggage_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Buying Plans')
plt.show()


# In[64]:


repacking_luggage_counts = NED_Df["Repacking Luggage"].value_counts()

plt.pie(repacking_luggage_counts, labels=repacking_luggage_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Repacking Luggage')
plt.show()


# In[65]:


repacking_luggage_counts


# In[66]:


forgotten_luggage_counts = NED_Df["Forgotten luggage"].value_counts()

plt.pie(forgotten_luggage_counts, labels=forgotten_luggage_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Forgotten Luggage')
plt.show()


# In[67]:


forgotten_luggage_counts


# In[68]:


misplaced_luggage_counts = NED_Df["Misplaced Luggage by Airlines"].value_counts()

plt.pie(misplaced_luggage_counts, labels=misplaced_luggage_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Misplaced Luggage by Airlines')
plt.show()


# In[69]:


misplaced_luggage_counts


# In[70]:


smart_luggage_owner_counts = NED_Df["Smart Luggage Owner"].value_counts()

plt.pie(smart_luggage_owner_counts, labels=smart_luggage_owner_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Smart Luggage Owner')
plt.show()


# In[71]:


smart_luggage_owner_counts


# In[72]:


airTag_counts = NED_Df["AirTag Users"].value_counts()

plt.pie(airTag_counts, labels=airTag_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of AirTag Users')
plt.show()


# In[73]:


airTag_counts


# In[74]:


NED_Df["Price Sensitivity for a Add-on Digital Solution"].unique()


# In[75]:


values_to_replace_1 = ['1-15']  
NED_Df["Price Sensitivity for a Add-on Digital Solution"].replace(values_to_replace_1, '1-15 €', inplace=True)

values_to_replace_2 = ['16-30','16-30 euros']  
NED_Df["Price Sensitivity for a Add-on Digital Solution"].replace(values_to_replace_2, '16-30 €', inplace=True)

values_to_replace_3 = ['31-45']  
NED_Df["Price Sensitivity for a Add-on Digital Solution"].replace(values_to_replace_3, '31-45 €', inplace=True)

values_to_replace_4 = ['46-60']  
NED_Df["Price Sensitivity for a Add-on Digital Solution"].replace(values_to_replace_4, '46-60 €', inplace=True)

values_to_replace_5 = ['61-75']  
NED_Df["Price Sensitivity for a Add-on Digital Solution"].replace(values_to_replace_5, '61-75 €', inplace=True)

values_to_replace_6 = ['76-100']  
NED_Df["Price Sensitivity for a Add-on Digital Solution"].replace(values_to_replace_6, '76-100 €', inplace=True)

values_to_replace_7 = ['Above 100 euros']  
NED_Df["Price Sensitivity for a Add-on Digital Solution"].replace(values_to_replace_7, 'Above 100 €', inplace=True)


NED_Df["Price Sensitivity for a Add-on Digital Solution"].unique()


# In[76]:


price_sensitivity_counts = NED_Df["Price Sensitivity for a Add-on Digital Solution"].value_counts()

plt.pie(price_sensitivity_counts, labels=price_sensitivity_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Price Sensitivity')
plt.show()


# In[77]:


price_sensitivity_counts


# In[78]:


NED_Df["Kind of Smart Luggage"].unique()


# In[79]:


TSA_lock = ['Away hardshell carry-o','Away bag at the Away store','TSA approved lock - for traveling to the US','TSA-approved lock','carry-on suitcase with tsa lock','Suitcase(es) with TSA lock','TSA lock on carry on','TSA approved locks','TSA lock, for security while traveling USB charging port','My Cabin Luggage is smart. Bought it because of the TSA Lock (could be opened from customs without assistance from my side) and made it smart on my own with an AirTag ','A TSA-approved lock to make travelling more accessible in case my luggage has to be accessed without me being around.','TSA locks, for convenience & safety','TSA approved and use an AirTag for my bag']
usb_charging =['usb charging port, was included lol','Usb charging (gift)']
tracking = ['Suitcase with integrated location tracking']
more_than_one_smart_feature = ['Backpack. Good looks.','Samsung, because I needed a new carry on suitcase','Suitcases, mandatory on flights','Tumi bag','A smal suitcase for a 4 day trip','Samsonite ecodriver for a vacation and for the weekend/short vacation']


conditions = [
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, TSA_lock)),
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, usb_charging)),
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, tracking)),
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, more_than_one_smart_feature)),
]


choices = ["TSA Lock", "USB Charging Port", "Tracking Feature", "More than one Feature"]

NED_Df["Bought Smart Luggage Type"] = np.select(conditions, choices, default="No")
NED_Df


# In[80]:


NED_Df["Bought Smart Luggage Type"].unique()


# In[81]:


bought_smart_luggage_counts = NED_Df["Bought Smart Luggage Type"].value_counts()

plt.bar(bought_smart_luggage_counts.index, bought_smart_luggage_counts, color='purple', width=0.3)
plt.title("Bought Smart Luggage Type")
plt.xticks(fontsize=7)
plt.show()


# In[82]:


bought_smart_luggage_counts


# In[83]:


filtered_df = NED_Df[NED_Df["Bought Smart Luggage Type"] != 'No']

bought_smart_luggage_counts = filtered_df["Bought Smart Luggage Type"].value_counts()

plt.bar(bought_smart_luggage_counts.index, bought_smart_luggage_counts, color='purple', width=0.3)
plt.title("Bought Smart Luggage Type")
plt.xticks(fontsize=7)
plt.show()


# In[84]:


plt.pie(bought_smart_luggage_counts, labels=bought_smart_luggage_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Bought Smart Luggage Type')
plt.show()


# In[85]:


replacing_old_luggage = ['Because it was time to replace the old\nSuitcase','Samsung, because I needed a new carry on suitcase']
light_weight =['Because it’s  light']
security = ['TSA lock, for security while traveling USB charging port',"TSA locks, for convenience & safety"]
no_excplicit_reason = ['usb charging port, was included lol','It happened to have smart features, but I did not buy it because of its smart features.']
looking = ['Backpack. Good looks.']
damage_prevention_airport_security = ['My Cabin Luggage is smart. Bought it because of the TSA Lock (could be opened from customs without assistance from my side) and made it smart on my own with an AirTag','A TSA-approved lock to make travelling more accessible in case my luggage has to be accessed without me being around.']


conditions = [
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, replacing_old_luggage)),
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, light_weight)),
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, security)),
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, no_excplicit_reason)),
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, looking)),
    NED_Df["Kind of Smart Luggage"].str.strip().str.lower().isin(map(str.lower, damage_prevention_airport_security))
]


choices = ["Replacing Old Luggage", "Light Weight", "Security Reasons", "No Explicit Reason", "Design", "Damage Prevention from Airport Security"]

NED_Df["Reasons for Buying Smart Luggage Type"] = np.select(conditions, choices, default="No")
NED_Df


# In[86]:


NED_Df["Reasons for Buying Smart Luggage Type"].unique()


# In[87]:


reasons_bought_smart_luggage_counts = NED_Df["Reasons for Buying Smart Luggage Type"].value_counts()

plt.bar(reasons_bought_smart_luggage_counts.index, reasons_bought_smart_luggage_counts, color='blue', width=0.3)
plt.title("Reasons for Smart Luggage Purchase")
plt.xticks(fontsize=5)
plt.show()


# In[88]:


reasons_bought_smart_luggage_counts


# In[89]:


filtered_df2 = NED_Df[NED_Df["Reasons for Buying Smart Luggage Type"] != 'No']

reasons_for_bought_smart_luggage_counts = filtered_df2["Reasons for Buying Smart Luggage Type"].value_counts()

plt.bar(reasons_for_bought_smart_luggage_counts.index, reasons_for_bought_smart_luggage_counts, color='blue', width=0.3)
plt.title("Reasons for Smart Luggage Purchase")
plt.xticks(fontsize=7)
plt.show()


# In[90]:


plt.pie(reasons_for_bought_smart_luggage_counts, labels=reasons_for_bought_smart_luggage_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Distribution of Reasons for Smart Luggage Purchase')
plt.show()


# In[91]:


NED_Df["Prevention from Buying Smart Luggage"].unique()


# In[92]:


good_existing_luggage = ['I do not see the benefit and like to stick to more classy looking luggage (Rimowa aluminum)','My current luggage is still fine, higher cost or low quality','Old suitcase is not broken','I still have perfectly good luggage and bought a small handheld scale. Works great','My old one still works','i have enough of the old ones and no need yet to buy immediately an additional new one','Don’t need new suitcase',"I have had my luggage for a long time. It still works so I don't plan on buying anything new.",'I am content with the luggage I already own','Most likely the price','I already have other luggage','I own well-working existing luggage and therefore don´t have a strong need for replacing them just to add smart elements that I could at least partially replace otherwise.','All available without smart luggage','So far I am fine with my suitcase/backpack. I travel with stuff that wouldn’t be an issue if lost.','Have not bought a new suitcase','That I already own a normal suitcase/bag',"I like my dufffle bag and I don't have the need for USB ports and stuff like that on my bag or backpack",'no need to buy a new piece of luggage since mine are fully functional. If buying a new one in a couple of years, I might consider buying smart luggage depending on the price','No need for new equipment. Might consider when I need new one','I have my suitcases and don’t need new ones','The price and the fact that I already own good quality suitcases.','I don’t need a new piece of luggage right now - my used pieces of luggage are still in a good condition','No need for a new piece of luggage','I already have the luggage I need, and buying a new one ist too expensive','I already have enough suitcases etc hence it would be an unnecessary expense',"I don't need one/ am content with the luggage I currently have","I have enough pieces, don't need anything else.",'my suitcase is fine for years, so i don‘t need a new one','My old luggage is perfectly intact','Still got my good suitcases','My luggage is to new to replace','Do not need extra luggage at the moment','Never thought about it. I am happy with the stuff I own right now (1 medium, 1 large suitcase, 1 30l backpack, 1 55l backpack)','The pieces of luggage I own still have a lot of life in them and I therefore don’t want to spend the money on a new piece of smart luggage']
too_expensive = ['To expensive','Not enough money as a student','Cost and Weight','Cost','Price/Design','Prices and already owning a lot of luggage','The price and that I dont think I need it','The fire and safety risk it still poses on board as well as the price','Money',"Didn't think about it but probably also the price","No need for it and higher cost",'Too expensive','Pricing - battery is too heavy','No need / expensive','Too expensive','Expensive and I don’t need it','Price','The need and price','High Price','Money',"Too expensive and also I don't see the point to be honest ",'Price?','Price, Design, weight of luggage']
no_full_solution = ['Only one feature per solution and too expensive for only one feature']
not_considered_yet = ['Never thought about it',"I didn't know about that type of luggage.","Haven't considered it yet, too expensive",'Never thought about',"haven't considered it, no recent purchases of new luggage",'Never thought about it, never felt like I needed something other than regular luggage','I so far have not felt like I needed it but it also has not been on my radar','I don‘t think I need it, but I haven’t given it much thought before','Don’t know if I need it','Haven‘ t think about it','Didn’t think about it yet','I just haven’t looked into those yet','Never thought of it']
no_need = ["Don't think I need it",'Not necessary','I do not need a new piece of luggage','No need for now','didn’t need anything new the last years','No need',"I didn't needed it untill now","I don't really need it",'No needed','I don‘t think it is super necessary','Don’t need that shit','No necessary','I dont See the Benefit','Don’t see the need','I never felt like I need it','I don’t need it',"Don't need yet",'No benefit',"no need to spend money on luggage because I currently own suitcases; do not use a large suitcase frequently enough to warrant spending more money on smart features; never misplaced my backpack/carry-on and always bring it with me so no real need for a tracking function; own a suitcase scale",'No need for it','For me it’s fancy but not necessary','no need so far','Don’t need it','No desperate need for it','No need for a new luggage',"Frankly, no need. I do not travel by air frequently and I normally don't lose my luggage otherwise. And I can charge my phone at home...",'Currently no need for smart luggage','Haven’t had the news for it so far','Does not feel necessary to me.',"I don't feel like it's necessary for my needs. Right now, I travel mostly with carry-on luggage, hence no need of a tracking device, and I don't fly often, so no need of a built-in scale.",'Not necessary (travelling by train)',"I don't need it for my travelling.","I have never felt the need to own it, I have other ways of covering for these needs, e.g. power banks, locks etc. I'm not opposed to it though.",'No need because of infrequent air travel','No need for new luggage.','No need for new luggage at the moment','No need','I don’t need it','Didnt see the need until now','Right now not necessary. I would purchase a smart luggage as soon as needed.']
did_not_know_existence = ['Never heard of it before','I did not know about it',"Didn't know that existed","Didn't know about it beforehand",'Hadn’t heard about it','Didnt know it exists','Never heard of it','No need so far/ didn’t know the categorie',"i didn't know something like that exists and i never felt ne need of one","Didn't know about it",'I did not know it exists','Never heard of it before','did not know it existed','I have never heard of smart luggage before','I never heard about it. I try to pack as light as possible.','I didn’t know it existed.','I did not know that they exist',"Didn't know it existed",'No need for it, did not know about it']
having_AirTags = ['I use an Air Tag to track my luggage.','Use of AirTag sufficient for my need','AirTag can do same','I have Apple AirTags']
no_existing_solution_backpack = ['Currently no smart hiking backpacks']
no_time = ['Yet no time and no offer','No time']
would_like_but_have_not_bought = ['nothing, just have not done it yet','In fact: my next piece of luggage will be smart. I just need to buy it eventually…','It’s on my list','Did not buy it yet','I would like to have one']
missing_information = ['Haven’t even really heard about it until now. So what’s preventing me: Lack of knowledge; probably price since I expect them to be rather expensive','information, what’s the benefit , price?','No trust','I rarely check in luggage.','I dont know wäre to buy','Availability and information']
bad_quality_no_trust = ['Did not see the value yet and also possibly the charging battery being fault.','Life span of the device','Restrictions from airlines',"don't trust smart devices","I don't need it, often the quality is bad"]
other = ["What's the point?",'I am not having problems with the luggage, even though we have unusual countries traveling too. we usually  book the slightly more reliable (and expensive) airlines. Maybe this is the reason why we do not have problems','No idea','Nothing','To avoid problems with airline','Upgrade after sale, e.g. Apple Location Chip','No interest','I never had any issues with my luggages.','What is a smart luggage?', 'Nothing ','no idea','Only few problems','Self-worth']

conditions = [
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, good_existing_luggage)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, too_expensive)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, no_full_solution)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, not_considered_yet)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, no_need)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, did_not_know_existence)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, having_AirTags)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, no_existing_solution_backpack)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, no_time)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, would_like_but_have_not_bought)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, missing_information)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, bad_quality_no_trust)),
    NED_Df["Prevention from Buying Smart Luggage"].str.strip().str.lower().isin(map(str.lower, other))
]


choices = ["Good Existing Luggage", "Too Expensive", "No full-feature Solution", "Not Considered Yet", "No Need", "Did Not Know Existence", "AirTags", "No Existing Suitable Solution", "No Time to Consider", "Would like to have One", "Missing Information", "Bad Quality & No Trust", "Other"]

NED_Df["Reasons for No Smart Luggage"] = np.select(conditions, choices, default="No")
NED_Df


# In[93]:


NED_Df["Reasons for No Smart Luggage"].unique()


# In[94]:


filtered_df3 = NED_Df[NED_Df["Reasons for No Smart Luggage"] != 'No']

reasons_no_smart_luggage_counts = filtered_df3["Reasons for No Smart Luggage"].value_counts()

plt.pie(reasons_no_smart_luggage_counts, labels=reasons_no_smart_luggage_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Reasons for No Smart Luggage')
plt.show()


# In[95]:


reasons_no_smart_luggage_counts


# In[96]:


NED_Df["Travel Enhancements"].unique()


# In[97]:


tracking_devices = ['Integrated tracking possibilities','Tracking devices ','tracking device would be good, but would be better to be used across my multiple suitcases (I have different sizes for different lengths of trips and depending on which season I travel)','vibration meter / detector','Location tracking','possibly a tracking device','Air Tag ','Tracking Device','Maybe tracking','Air Tag','tracking, smart lock','maybe a tracking device','AirTag for sure','Tracking','Tracking (hence the AirTag)','Tracking device maybe','Probably an AirTag','tracking','maybe am tracking device in case of an loss of luggage','AirTag',"I'm thinking of a tracking device but more for other stuff like keys or my wallet",'Tracking device would be nice','A tracking device','Tracking my luggage is most important for me.','Tracking Devices','A tracking device would be helpful especially when traveling by plane, since it occurs very often  lately that luggage gets lost','Tracking device, measuring device to determine whether the luggage has been subjected to violent shocks','Knowing where my luggage is','Maybe less stress to loose my luggage.','Tracking device','Probably a tracking device','tracking device\n', 'A good lock. Tracking device.','a tracking device','Using an airtag is a game changer','A built in tracking device would be great','track the suitcase','Tracking device, phone charger','tracking device','Tracking','Tracking mostly','tracking device, scale','Tracking device','A tracking device sounds useful.','Maybe a tracking device... I used to put a spare old phone in my backpack to locate it in case of emergency.','Tracking device, scale on the luggage, name tag','Tracking device, smart lock, …']
integrated_scale = ['scale','Integrated scale would be super. 👍 ','Integrated Scale','Scale!','Integrated scale and a better and safer closing system','Integrated scale would be useful','Integrated Scale','An integrated scale would probably be very helpful','Integrated scale sure thing but not 100% needed ; tracking device is useless from my point of view because if its lost somewhere its lost like I wont fly back just to pick up my suitcase and then fly back again','Not having to worry about weight limit when packing a reasonable amount.','The packing process would be easier with a scale','Integrated Scale, but only for bigger luggage','Integrated scale',"Definitely a integrated scale so that I don't have to take a scale while traveling to avoid overweight",'Scale maybe','Scale','A good lock and an integrated scale','Integrated scales','Scale','Weight','Integrated scale','integrated scale','Integrales scale','An integrated scale']
tracking_and_scale = ['Tracking device, scale, lock','great! tracking device and integrated scale','All of the above and very good wheels','Scale, tracking','Tacking device, integrated scale all in one','Integrated weight measurement, probably also an integrated GPS tracking device','Tracking device, integrated scale','tracking device, integrated power bank/usb port','Tracking device & scale','Scale, tracking, charger, lock','tracking device, integrated scale, charging port','Yes, tracking and integrated scale','Integrated scale would be cool but if it increases the weight considerably, then not. Tracking: def interested','both of these would. Airtags are an easy solution if people are afraid of luggage misplacement. An integrated scale is probably convenient, but most frequent travellers will already have a way to determine their luggage‘s weight.','Tracking device and integrated scale and measurement of luggage in terms of size','Tracking device, scale, USB charging port','Integrated scale, tracking device','integrated scale, tracking device, lock, possibility to show flight information',"For bigger journeys a tracking device might be helpfull as well as an integrated scale, if there isn't one available.",'Tracking Device, Scale, sustainable materials','integrated scale und tracking','Tracking, Scale, Lock','Tracking device and luggage scale which I carry with me.','Integrated scale and tracking','tracking device, integrated scale','Tracking device,integrated scale, much safety']
charging_port_power_bank = ['Tracking device, integrated (phone) charging station','Scale, USB port for charging','Integrated power box','USB charging ports','USB charger','Tracking device, integrated power bank','Integrated usb charging port, integrated scale','Maybe charging supply']
comfort_convenience = ['No more luggage delays','More reliable services from the airlines.','The coziness.','Less worries','Free carriage of luggage','Lighter luggage','luggage which carries itself','Less waiting time for check in luggage (check-in, waiting for check in luggage)','More security about the whereabouts','Feeling more save','Having to worry less about my luggage','More comfort, easy to use suitcases, digital solutions, up-to-Date information, news, all in one travel solution,']
quality_features = ['Luggage service at home (like baggage service in Dubai offered by Emirates)','In general high quality of the luggage (robust materials, smooth wheels)']
airline_compability_tracking = ["I would like to have tracking devices in all my luggage. Ideally, airlines would take these into consideration when they lose your luggage. An integrated scale sounds nice as well. But i don't want these additions to increase the weight of the luggage.",'I have a suitcase with an AirTag but none of the airlines I have flown with so far actually support the technology!']
other_not_clear = ['a transparent 1 liter clip-on bag for liquids','Both suggestions.','Adjustable size','More locks, integrated foldable backpack, easy to access water bottle','Both namens examples','selbstfahrender koffer (koffer mit Motorwelchen man mit dem Handy steuern kann) mit eingebautem Ortungsgrät','I did not think about this topic before','Restricting myself to take less','Both','smart storage solutions to pack more efficiently','Insurance for the luggage','Amazing','It an opportunity','Don’t know',"A luggage that is easy to transport even when it's heavy",'No Airline fees for luggage','No different airline rules for hand luggage size, especially on backpacks','Both might be helpful','I am honestly quite satisfied without any add-on devices as you mostly find a way to eg. borrow a scale or something so that purchasing something new seems unnecessary','Easy to lift (e.g up to luggage spaces in trains)',"Sturdy wheels that don't jam",'Unlimited weight restriction, better wheels on trolleys','Yes','Needs to be Light, easily movable (wheels), still waiting for a suitcase that does not take up space when stored or not in use.','Better involvement of the travel company I pay']
no_enhancements_needed = ["Can't think of any","I don't know",'Not needed','I do not need further technological advancements ','No idea ','None','Not required','No idea','I don‘t need much…. My suitcase should hold my stuff and be distiguishable from other suitcases',"I haven't needed it before and don't think I will in the future",'None of the above. To me, it sounds like gizmos that might be good in specific situations but are mainly useless in everyday life.','-','nothing, stay classic','Not necessary','integrated scale is cool but not necessary', 'Nothing.','?','Na','No','Nothing','Nothing ','N/a','Np idee','I am perfectly happy with a bag that does not require firmware updates']

conditions = [
    NED_Df["Travel Enhancements"].str.strip().str.lower().isin(map(str.lower, tracking_devices)),
    NED_Df["Travel Enhancements"].str.strip().str.lower().isin(map(str.lower, integrated_scale)),
    NED_Df["Travel Enhancements"].str.strip().str.lower().isin(map(str.lower, tracking_and_scale)),
    NED_Df["Travel Enhancements"].str.strip().str.lower().isin(map(str.lower, charging_port_power_bank)),
    NED_Df["Travel Enhancements"].str.strip().str.lower().isin(map(str.lower, comfort_convenience)),
    NED_Df["Travel Enhancements"].str.strip().str.lower().isin(map(str.lower, quality_features)),
    NED_Df["Travel Enhancements"].str.strip().str.lower().isin(map(str.lower, airline_compability_tracking)),
    NED_Df["Travel Enhancements"].str.strip().str.lower().isin(map(str.lower, other_not_clear)),
    NED_Df["Travel Enhancements"].str.strip().str.lower().isin(map(str.lower, no_enhancements_needed))
]


choices = ["Tracking", "Integrated Scale", "Tracking and Integrated Scale","Charging Port", "Comfort & Convenience", "Quality Features", "Airline Support by Tracking", "No enhancements Needed","Other"]

NED_Df["Travel Enhancement Groups"] = np.select(conditions, choices, default="NaN")
NED_Df


# In[98]:


travel_enhancements_counts = NED_Df["Travel Enhancement Groups"].value_counts()

plt.pie(travel_enhancements_counts, labels=travel_enhancements_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Travel Enhancements')
plt.show()


# In[99]:


travel_enhancements_counts


# In[100]:


NED_Df


# In[101]:


plt.scatter(NED_Df["Age"], NED_Df["Price Sensitivity for a Add-on Digital Solution"])
plt.title('Correlation between Age and Price Sensitivity')
plt.show()


# In[102]:


NED_Df.to_csv('C:/CarolineZiegler/Studium_DCU/8. Semester/Business Analytics Portfolio/Portfolio/02_Uni Projects/outFile.csv', index=False)

