import pandas as pd
import numpy as np

## Load raw stratigraphic tops

file = 'file.xlsx'
df=pd.read_excel(file)

## Create blank column for standardised tops

df['Pick_IdJA']=np.nan

## lists of different top nomenclature

a_tops = ['Seafloor/Group A','Seabed/Group A','Group A','Group A (Recent-Pliocene)','Top Group A']

b_tops = ['Group B','Group B (Mio-Pliocene)','B Group','Top B','B','Top Group B']

d_tops = ['D','Top D','Group D','Top Group D', 'Top Group D (Unconformity)','Unconformity/Group D','D Group','Mid Plioc. Uncon./Group D','Mid Plio Unconf. (Group D)','Plio-Miocene Unconf./Group D','Group D (Unc)','Mid-Plio Unc/Group D','Group D Top',
'Mid Pliocene Unconformity (Group D)','Top Group D Top (Unconformity)','Group D Mid Plio Unconformity']

e_tops = ['E','Top E','Group E','Top Group E','Group E Top','Top Group E (Plio-Mio Unc.)','Group E Seismic Marker','E Group']

f_tops = ['F','Top F','Group F','Top Group F','Group F Top','Top Group F/Plio-Mio Unc','Plio-Mio Unc/Top Group F','F Group']

h_tops = ['H','Top H','Top H Group','Group H','Top Group H','Group H (Mio-Pliocene','Plio-Mio Unc./Group H','Group H Top','Unc/Top of Group H','Miocene-Pliocene Unc/Group H','Mio-Pliocene Unc/Group H']

i_tops = ['I','Group I','Top Group I','Group I (Mio-Pliocene','Group I Top','Top Group I Seismic Horizon','Group I/Unconformity','Estimated Group I','I Group','Top I Group','Top I','Top I Group']

j_tops = ['J','Group J','Top Group J','Group J (Miocene)','Group J Top','Group J (Seismic)','J Group','Top J Group','Top J']

k_tops =['K','Group K','Top Group K','Group K (Miocene)','Group K Top','K Group','Top K Group','Top K','Top K Group',
         'K Shale','Trengganu Shale','Top K-Shale','MTSB (K Shale)','Terengganu Shale','23.0Ma Pink (K Shale/Terengganu Fm)',
         'Group K Shale','Top K Shale','Terengganu Shale Equivalent','K-Shale','Group K (Terengganu Shale)','Top K (K-SHALE)']

l_tops = ['L','Group L','Top Group L','L Group','Top L','L Shale','Top L Shale']

m_tops = ['M','Group M','Top Group M','M Group','Top M','M Shale','Top of M shale']

unc_tops = ['Basal B Unconformity','Base Group B','Base Pliocene','B-unconformity','Group D','Group D (eroded)','Group D (Unc)',
'Group D Mid Plio Unconformity',
'Group D Top',
'Group D&E',
'Group I/Unconformity',
'Late Mio Unc.',
'Mid PIio Unconf.',
'Mid Plio Unconf. (Group D)',
'Mid Plio Unconformity',
'Mid Plioc. Uncon./Group D',
'Mid Plioc. Uncon./Group D (eroded)',
'Mid Pliocene Unc. (Group D)',
'Mid Pliocene Unconf. (Group F)',
'Mid Pliocene Unconformity',
'Mid Pliocene Unconformity (Group D)',
'Mid-Plio  Unconformity',
'Mid-Plio Unc/Group D',
'Mid-Plio Unconformity',
'Mid-Pliocene Unconformity',
'Miocene-Pliocene Unc/Group H',
'Miocene-Pliocene Unconform.',
'Miocene-Pliocene Unconformity',
'Miocene-Pliocene Unconformity/Group F',
'Mio-Plio Unconformity',
'Mio-Plio Unconformity/Top F',
'Mio-Pliocene Unc. /Group H',
'Near MMU',
'PIio-Mio Unc./Group H',
'PLIO.-MIO.UNCONF.',
'Pliocene-Miocene Unc.',
'Pliocene-Miocene Unconformity',
'Pliocene-Miocene Unconformity/Group E',
'Pliocene-Miocene Unconformity/Group F',
'Pliocene-Miocene Unconformity/Group G',
'Pliocene-Miocene Unconformity/Top E',
'Pliocene-Miocene Unconformity/Top F',
'Pliocene-Miocene Unconformity/Top H',
'Plio-Mid/Unconformity',
'Plio-Mio Unc/Top Group F',
'Plio-Mio Unconformity',
'Plio-Miocene Unconf./Group D',
'Red unconformity',
'Red Unconformity/Group J'
'Top D Unconformity',
'Top Group D (Unconformity)',
'Top Group D Top (Unconformity)',
'Top Group E (Plio-Mio Unc.)',
'Top Group F/Plio-Mio Unc'
'UNC',
'Unc/Top of Group H',
'Unconf. Group F',
'Unconf/Top K',
'Unconformity',
'Unconformity (Group D)',
'Unconformity Sand',
'Unconformity/Group D',
'Unconformity/Top Group F'
]

## Define empty dataframe which to populate

df_out=pd.DataFrame()

## Loop through wells, then tops, checking if top is in list, and assigning standardised top 

for i in df['Wellbore Name'].unique():
    df_s=df[df['Wellbore Name']==i]
    for j in df_s.index:
        if df_s['Pick Name'][j] in a_tops:
            df_s['Pick_IdJA'][j]='Top Group A (IdJA)'
        if df_s['Pick Name'][j] in b_tops:
            df_s['Pick_IdJA'][j]='Top Group B (IdJA)'
        if df_s['Pick Name'][j] in d_tops:
            df_s['Pick_IdJA'][j]='Top Group D (IdJA)'
        if df_s['Pick Name'][j] in e_tops:
            df_s['Pick_IdJA'][j]='Top Group E (IdJA)'
        if df_s['Pick Name'][j] in f_tops:
            df_s['Pick_IdJA'][j]='Top Group F (IdJA)'
        if df_s['Pick Name'][j] in h_tops:
            df_s['Pick_IdJA'][j]='Top Group H (IdJA)'
        if df_s['Pick Name'][j] in i_tops:
            df_s['Pick_IdJA'][j]='Top Group I (IdJA)'
        if df_s['Pick Name'][j] in j_tops:
            df_s['Pick_IdJA'][j]='Top Group J (IdJA)'
        if df_s['Pick Name'][j] in k_tops:
            df_s['Pick_IdJA'][j]='Top Group K (IdJA)'
        if df_s['Pick Name'][j] in l_tops:
            df_s['Pick_IdJA'][j]='Top Group L (IdJA)'
        if df_s['Pick Name'][j] in m_tops:
            df_s['Pick_IdJA'][j]='Top Group M (IdJA)'
        if df_s['Pick Name'][j] in unc_tops:
            df_s['Pick_IdJA'][j]='Mio-Plio Unc (IdJA)'    
            
    df_out=df_out.append(df_s)

## Remove any nan values     
df_out=df_out.dropna(subset=['Pick_IdJA'])

## Remove columns except well, new tops and depths
df_out=df_out[['Wellbore Name','Pick_IdJA','MD','TVDSS']]

## Export to .txt file
df_out.to_csv('new_picks_IdJA.txt',sep='\t',index=False)
    
            
