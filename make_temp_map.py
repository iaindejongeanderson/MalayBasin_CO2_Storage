import numpy as np
import rasterio

group = 'E'
fp = 'filepath\Group '+group+'\Group_'+group+'_Depth.bil'

dep = rasterio.open(fp)


out_meta = dep.meta.copy()
dep = dep.read()
dep = np.array(dep)[0,:,:]

gg_map ='filepath\geothermal_gradient.bil'
temp = rasterio.open(gg_map)
temp = temp.read()
temp = np.array(temp)[0,:,:]

m = dep.max()

t_sb = 24

temp_out = np.zeros(dep.shape)

for i,k in enumerate(dep):
    for j,l in enumerate(k):
        if int(l) == m:
            temp_out[i,j]=m
        else:
            t_grad = temp[i,j]
            z = dep[i,j]
            temp_out[i,j] = t_grad*(z/1000)+t_sb
                     
with rasterio.open(fp=r'filepath\Group '+group+'\Group_'+group+'_Temp.bil',
                   mode='w',**out_meta) as dst:
    dst.write(temp_out,1)  