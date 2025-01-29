import numpy as np
import rasterio
from scipy.stats import truncnorm


def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


groups = [ "D","E","F","H","I"]


for g in groups:
    
    dep = rasterio.open('filepath\Group '+g+'\Group_'+g+'_Depth.bil')
    out_meta = dep.meta.copy()
    dep = dep.read()
    dep = np.array(dep)[0,:,:]
    
    m = dep.max()
    
        
    por_dep_out = np.zeros(dep.shape)

    for i,k in enumerate(dep):
        for j,l in enumerate(k):
            
            z = dep[i,j]
            
            
            if int(l) == m:
                por_dep_out[i,j] = m
            else:
                por_dep_out[i,j] = 45*np.exp(-0.00052826*z)
                
            
    with rasterio.open(fp=r'filepath\Group '+g+'\Group_'+g+'_Porosity.bil',
                        mode='w',**out_meta) as dst:
        dst.write(por_dep_out,1)
        
