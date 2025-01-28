import numpy as np
import rasterio
import os


groups = ["B","D","E","F","H","I","J","K"]


for g in groups:
    
    
    # Load .bil raster files
    por = rasterio.open('filepath\Group '+g+'\Group_'+g+'_Porosity.bil')
    den = rasterio.open('filepath\Group '+g+'\Group_'+g+'_CO2_Density.bil')
    fau = rasterio.open('filepath\Group '+g+'\Group_'+g+'_Faults.bil')
    pha = rasterio.open('filepath\Group '+g+'\Group_'+g+'_CO2_Phase.bil')
    dep = rasterio.open('filepath\Group '+g+'\Group_'+g+'_Depth.bil')
    
    # only loads if overpressure raster is present
    if os.path.isfile('filepath\Group '+g+'\Group_'+g+'_Overpressure_Zone.bil'):
        pre = rasterio.open('filepath\Group '+g+'\Group_'+g+'_Overpressure_Zone.bil')
    
    
    
    
    out_meta = por.meta.copy()
    out_meta['nodata']=0
    out_meta['dtype']=rasterio.uint8

    # Convert to numpy array
    por = np.array(por.read())[0,:,:]
    den = np.array(den.read())[0,:,:]
    fau = np.array(fau.read())[0,:,:]
    pha = np.array(pha.read())[0,:,:]
    dep = np.array(dep.read())[0,:,:]

    # convert to numpy array only if overpressure raster is present
    # otherwise, create dummy overpressure raster set to zero (no overpressure)
        if 'pre' in globals():
            pre = np.array(pre[0,:,:])
        else:
            pre = np.full(por.shape,0)
       
    # Create output array and fill with null values
    
    optim_out = np.full(por.shape,0)
    
    # Set any negative depths to zero (artefacts around edges)
    
    dep[dep<0]=0
    
    # Get null value
    
    m = dep.max()

    for i,k in enumerate(por):
            for j,l in enumerate(k):
                if dep[i,j] != m:
                    if (por[i,j] >= 10) and \ 
                       (pre[i,j] == 0) and \ 
                       (den[i,j] >= 300) and \ 
                       (pha[i,j] == 0) and \ 
                       (fau[i,j] >= 2): # 
                           
                           optim_out[i,j] = 3
                           
                    elif (por[i,j] >= 6) and \
                         (den[i,j] >= 100) and \
                         (pha[i,j] == 0) and \
                         (fau[i,j] > 0):
                             
                             optim_out[i,j] = 2
                    else:
                        optim_out[i,j] = 1
                
        # Export
                    
        with rasterio.open(fp=r'filepath\Group '+g+'\Group_'+g+'_Optimal_Zone.bil',
                          mode='w',**out_meta) as dst:
            dst.write(optim_out.astype(rasterio.uint8),1) 
                
            
    
    
    
    
    
    
    
