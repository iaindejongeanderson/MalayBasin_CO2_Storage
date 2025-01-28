from CoolProp.CoolProp import PropsSI
from CoolProp.CoolProp import PhaseSI
import numpy as np
import rasterio

def degC_to_kel(x):
    return x + 273.15


groups = [ "D","E","F","H"]
#groups = ["J"]

temp = rasterio.open('filepath\geothermal_gradient.bil')
temp = temp.read()
temp = np.array(temp)[0,:,:]

t_sb = 24

for g in groups:
    print(g)
       
    dep = rasterio.open('filepath\Group '+g+'\Group_'+g+'_Depth.bil')
    out_meta = dep.meta.copy()
    dep = dep.read()
    dep = np.array(dep)[0,:,:]
    
    pres = rasterio.open('filepath\Group '+g+'\Group_'+g+'_Pressure.bil')
    pres = pres.read()
    pres = np.array(pres)[0,:,:]
    
    m = dep.max()
    
    density = np.zeros(dep.shape)
    phase_out = np.zeros(dep.shape)
        
    for i,k in enumerate(dep):
        for j,l in enumerate(k):
            if (int(l) == m) or (dep[i,j]<=0) or (pres[i,j]<=0):
                density[i,j] = m
                phase_out[i,j] = m
            else:
                z = dep[i,j]
                t = temp[i,j]
                p = pres[i,j] * 1000000
                
                t = (float(z)/1000 * float(t)) + t_sb
                density[i,j] = PropsSI('D', 'T', degC_to_kel(t), 'P', p, 'CO2')
                phase = PhaseSI('T', degC_to_kel(t), 'P', p, 'CO2')
                
                
                if (phase == 'supercritical') or (phase == 'supercritical_liquid'):
                    phase_out[i,j]=0
                if (phase == 'supercritical_gas') or (phase == 'gas'):
                    phase_out[i,j]=1       
                            
        
    with rasterio.open(fp=r'filepath\Group '+g+'\Group_'+g+'_CO2_Phase.bil',
                       mode='w',**out_meta) as dst:
        dst.write(phase_out,1)  
        
    with rasterio.open(fp=r'filepath\Group '+g+'\Group_'+g+'_CO2_Density.bil',
                       mode='w',**out_meta) as dst:
        dst.write(density,1) 
        
   


    
