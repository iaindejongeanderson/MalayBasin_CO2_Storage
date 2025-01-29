import numpy as np
import rasterio
from sklearn.cluster import DBSCAN
import pandas as pd


#%% Load optimal zone grid

groups = "D"

opt = rasterio.open('filepath\Group '+groups+'\Group_'+groups+'_Optimal_Zone.bil')
out_meta = opt.meta.copy()

#%% Create matrices of x, y and flag
band1 = opt.read()
height = band1.shape[1]
width = band1.shape[2]
cols, rows = np.meshgrid(np.arange(width), np.arange(height))
xs, ys = rasterio.transform.xy(opt.transform, rows, cols)
xs = np.array(xs)
ys = np.array(ys)
zs = np.array(opt.read())[0,:,:]

#%% reshape matrices
xs = np.reshape(xs,-1)
ys = np.reshape(ys,-1)
zs = np.reshape(zs,-1)
df = pd.DataFrame({'x':xs,'y':ys,'z':zs})              
                  
#%% create dbscan input

df_splice = df[df['z']==3]
df_nosplice = df[df['z']!=3]
df_nosplice['z']=0
df_splice=df_splice.drop('z',axis=1)
df_nosplice=df_nosplice.drop('z',axis=1)
#%% fit cluster model
model = DBSCAN(eps=100,min_samples=5)
fitted_model = model.fit(df_splice.values)
labels = fitted_model.labels_+1
df_splice['z'] = labels
df_out=pd.concat([df_nosplice,df_splice])
df_out=df_out.sort_index()

#%% calculate area of each cluster type
unique_vals = df_out['z'].unique()
for i in unique_vals:
    c = df_out[df_out['z']==i]
    count = len(c)
    area_km2 = 100 * 100 * count * 1e-6
    print(i,area_km2)
    if area_km2 < 100:
        df_out[df_out['z']==i]=0
    

#%% reshape back to matrix
z_out=np.reshape(df_out['z'].values,rows.shape)
z_out[np.isnan(z_out)]=0


#%%
with rasterio.open(fp=r'filepath\Group '+groups+'\Group_'+groups+'_conected_optimal_zone.bil', mode='w',**out_meta) as dst:
    dst.write(z_out.astype(rasterio.uint8),1) 

