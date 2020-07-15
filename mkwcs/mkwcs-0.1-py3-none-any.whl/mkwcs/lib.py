import numpy as np
from astroquery.vizier import Vizier
import astropy.units as u
import astropy.coordinates as coord

########################################## Calling USNO B1 ############################################
# USNO B1: my preferred catalog choice
catalog_list = Vizier.find_catalogs('USNOB1')
Vizier.ROW_LIMIT=10000


def get_cat(pos_ra,pos_dec,box_width,mag_limit,nmax=100):
    '''Using Astroquery.Vizier to get a USNO-B1 catalog of stars around the position.'''
    result = Vizier.query_region(coord.SkyCoord(ra=pos_ra, dec=pos_dec, unit=(u.deg, u.deg), frame='fk5'), width=f"{box_width}m",height=f"{box_width}m", catalog=["USNOB1"], column_filters={"R2mag":f"<{mag_limit}","Ndet":">3"})
    coo_ra  =result[0]['RAJ2000']
    coo_dec =result[0]['DEJ2000']
    coo_mag =result[0]['R2mag']
    mag =coo_mag[coo_mag>0]
    ra1 =coo_ra[coo_mag>0]
    dec1=coo_dec[coo_mag>0]
    zipped= zip(mag,ra1,dec1)
    sorted_zipped = sorted(zipped)
    newm   =[a for a,_,_ in sorted_zipped]
    newra  =[a for _,a,_ in sorted_zipped]
    newdec =[a for _,_,a in sorted_zipped]
    return(newm[0:nmax],newra[0:nmax],newdec[0:nmax])


##########################################  Detecting stars in the image  ##################################

from astropy.io import fits
from astropy.stats import sigma_clipped_stats,SigmaClip
from photutils import Background2D, MedianBackground,DAOStarFinder


def get_stars_xy(image_file,nmax=100,extension=0):
    '''Detection of stars in an image, using astropy and photutils tools.'''
    image_data = fits.getdata(image_file, ext=extension)
    mean, median, std = sigma_clipped_stats(image_data, sigma=3.0)  
    sigma_clip = SigmaClip(sigma=3.)
    bkg_estimator = MedianBackground()
    bkg = Background2D(image_data, (50, 50), filter_size=(3, 3),sigma_clip=sigma_clip, bkg_estimator=bkg_estimator)
    newdata=image_data - bkg.background
    daofind = DAOStarFinder(fwhm=3.0, threshold=5.*std)  
    sources = daofind(newdata)  
    for col in sources.colnames:  
        sources[col].info.format = '%.8g'  # for consistent table output
    #print(sources) 
    xc=sources['xcentroid']
    yc=sources['ycentroid']
    mc=sources['mag']
    zipped= zip(mc,xc,yc)
    sorted_zipped = sorted(zipped)
    nmc =[a for a,_,_ in sorted_zipped]
    nxc =[a for _,a,_ in sorted_zipped]
    nyc =[a for _,_,a in sorted_zipped]
    return(nmc[0:nmax],nxc[0:nmax],nyc[0:nmax])



################# My own algorithm to match horizontally-vertically shifted catalogs ##############################

def get_hvshift(cat1,cat2,pixtol=2,binsize=1.0,plot=False,verbose=True):
    '''This function computes a simple horizontal and vertical shift (dx,dy) 
    between 2 x,y catalogs (when there is no rotation or scaling expected between them).'''
    dx=[]
    dy=[]
    mt=[]
    for i in range(len(cat1)):
        for k in range(len(cat2)):
            dx.append(cat2[k][0]-cat1[i][0])
            dy.append(cat2[k][1]-cat1[i][1])
            mt.append([i,k])
    dx=np.array(dx)
    dy=np.array(dy)
    xr=np.arange(min(dx),max(dx)+5*binsize,binsize)
    yr=np.arange(min(dy),max(dy)+5*binsize,binsize)
    hx,_=np.histogram(dx,bins=xr)
    hy,_=np.histogram(dy,bins=yr)
    distx=binsize*np.argmax(hx)+np.min(dx)+binsize/2.0
    disty=binsize*np.argmax(hy)+np.min(dy)+binsize/2.0
    if(verbose):
        print (f"Match Results:  dx={distx:.2f}  dy={disty:.2f}  accum_in_x= {np.max(hx):03d}  accum_in_y= {np.max(hy):03d}")
    c=0
    match=[]
    for i in range(len(dx)):
        if(abs(dx[i]-distx)<pixtol and abs(dy[i]-disty)<pixtol):
            #line="Match: %03d  (cat1,cat2)   %.1f %.1f "%(c+1,distx,disty)
            line = f"Match: {c+1:03d}  (c1,c2)= ({mt[i][0]:03d},{mt[i][1]:03d})  s1= {cat1[mt[i][0]][0]:6.1f} {cat1[mt[i][0]][1]:6.1f}    s2= {cat2[mt[i][1]][0]:6.1f} {cat2[mt[i][1]][1]:6.1f} dx = {cat2[mt[i][1]][0]-cat1[mt[i][0]][0]:4.1f}  dy = {cat2[mt[i][1]][1]-cat1[mt[i][0]][1]:6.1f}"
            if(verbose):
                print (line)
            c=c+1
            match.append(mt[i])
    return(distx,disty,[match[i][0] for i in range(c)],[match[i][1] for i in range(c)],match)




############# Writing a WCS solution into the header  ###############################
from astropy import wcs

def wcs2header(newwcs,image_file):
    # Editar Header
    h2=newwcs.to_header()
    hs=newwcs.to_header_string()
    # Obtener las Keywords
    n=80
    hnames=[hs[i:i+n] for i in range(0, 80*int(len(hs)/80), n)]
    kw=[]
    for i in range(len(hnames)):
        if(hnames[i][0:4]!="END " and hnames[i][0]!=' '):
            kw.append(hnames[i][0:8])
    # Agregar las Keywords con la nueva WCS
    for i in range(len(kw)):
        try:
           fits.delval(image_file,kw[i],ext=0)
        except:
            pass
        fits.setval(image_file,kw[i], value=h2[kw[i]],ext=0)
        print(f"Key: {kw[i]:10s}   Val:{h2[kw[i]]:20}")
    #borrar keywords de dudosa utilidad
    fits.delval(image_file,'DATEREF')
    fits.delval(image_file,'MJDREFI')
    fits.delval(image_file,'MJDREFF')


######### Final tasks, and putting all together ################################

from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord
import astropy.coordinates as coord
import astropy.wcs.utils as wu
from astropy.wcs import WCS
import astropy.units as u
import matplotlib.pyplot as pl
import os,sys





def makewcs(image_file,pixsize,ra_c,dec_c,mag_limit=19,nmax=100,rot_angle_deg=0,plot=False):
    '''Match 2 x-y catalogs assuming there is no scaling or rotation between them.'''
    hdul = fits.open(image_file) 
    hdr = hdul[0].header
    nx1= int(hdr['NAXIS1'])
    nx2= int(hdr['NAXIS2'])
    box_width=((nx1+nx2)*pixsize/(2*60.))
    # se conecta a USNO-B1 y obtiene un catalogo centrado en las coordenadas (y ordenadas por brillo)
    newm,newra,newdec=get_cat(ra_c,dec_c,box_width,mag_limit,nmax)
    # crea primera aproximacion a la solucion    
    wcs = WCS(naxis=2)
    wcs.wcs.crpix = [ nx1/2., nx2/2.]
    wcs.wcs.cdelt = [-pixsize*1./3600., pixsize*1./3600.]
    wcs.wcs.crval = [ra_c, dec_c]
    wcs.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    wcs.wcs.crota = [rot_angle_deg,rot_angle_deg]
    # crea catalogo xy  partir de las coordenadas 
    xp, yp = wcs.wcs_world2pix(newra,newdec, 1)
    # se imprime en pantalla 
    for i in range(len(newm)):
        print ("RA-Dec cat  %02d %10.6f  %10.6f %8.3f  %8.3f  %8.3f"%(i+1,newra[i],newdec[i],newm[i],xp[i],yp[i]))
    # se busca estrellas en la imagen (ordenadas por brillo)
    nmc,nxc,nyc=get_stars_xy(image_file,nmax=100,extension=0)
    # se imprime en pantalla
    for i in range(len(nmc)):
        print ("X-Y cat  %02d %8.3f  %8.3f"%(i+1,nxc[i],nyc[i]))
    # Catalogos para hacer match, ordenados por brillo.
    scat=list(zip(xp,yp))
    tcat=list(zip(nxc,nyc))
    # Se hace el Match de Catalogs x-y
    dx,dy,idx_s,idx_t,match=get_hvshift(scat,tcat,binsize=1,plot=False)
    if(len(match)>5):
        print("######### %d stars matched #######"%(len(match)))
        # Figure (optional)
        if(plot==True):
            pl.figure(figsize=(8,8))
            pl.plot(xp,yp,'s',color='blue',label='USNO-B1',alpha=0.5)
            pl.plot(nxc,nyc,'o',color='red',label='DaoFind',alpha=0.5)
            for i in range(len(match)):
                pl.plot([scat[match[i][0]][0],tcat[match[i][1]][0]],[scat[match[i][0]][1],tcat[match[i][1]][1]],'--',color='black',alpha=0.5,lw=2)
            pl.legend()
            pl.savefig('MKWCS.png')
            pl.close()
        # se transforma en un arreglo numpy para que pueda transponerse
        tcat=np.array(tcat)
        # crear sistema de coordenadas
        scat_sky = SkyCoord(ra=[newra[i] for i in idx_s]*u.degree, dec=[newdec[i] for i in idx_s]*u.degree, frame='fk5')
        # crear solucion a aprtir del match de estrellas de catalog y estrellas en la imagen
        nwcs=wu.fit_wcs_from_points(tcat[idx_t].T, scat_sky, proj_point='center', projection='TAN')#, sip_degree=3)
        # Editar Header
        wcs2header(nwcs,image_file)
        print("################ Done! #################")
    else:
        print ("#############################\nERROR: Less than 5 matches! Try increasing the number of stars by extending limit magnitude.\n#############################################")



def search_angle(image_file,pixsize,ra_c,dec_c,angle0,angle1,delta_angle,mag_limit=19,nmax=100):
    '''Look for the best angle to match 2 x-y catalogs.'''
    hdul = fits.open(image_file)
    hdr = hdul[0].header
    nx1= int(hdr['NAXIS1'])
    nx2= int(hdr['NAXIS2'])
    box_width=((nx1+nx2)*pixsize/(2*60.))
    # se busca estrellas en la imagen (ordenadas por brillo)
    nmc,nxc,nyc=get_stars_xy(image_file,nmax=100,extension=0)
    # se imprime en pantalla
    for i in range(len(nmc)):
        print ("X-Y cat  %02d %8.3f  %8.3f"%(i+1,nxc[i],nyc[i]))
    # Catalogos para hacer match, ordenados por brillo.
    # se conecta a USNO-B1 y obtiene un catalogo centrado en las coordenadas (y ordenadas por brillo)
    newm,newra,newdec=get_cat(ra_c,dec_c,box_width,mag_limit,nmax)
    # crea primera aproximacion a la solucion    
    angle=np.arange(angle0,angle1,delta_angle)
    best_angle=9999
    best_score=-1
    for i in range(len(angle)):
        wcs = WCS(naxis=2)
        wcs.wcs.crpix = [ nx1/2., nx2/2.]
        wcs.wcs.cdelt = [-pixsize*1./3600., pixsize*1./3600.]
        wcs.wcs.crval = [ra_c, dec_c]
        wcs.wcs.ctype = ["RA---TAN", "DEC--TAN"]
        wcs.wcs.crota = [angle[i],angle[i]]
        # crea catalogo xy  partir de las coordenadas 
        xp, yp = wcs.wcs_world2pix(newra,newdec, 1)
        # se imprime en pantalla 
        #for i in range(len(newm)):
        #    print ("RA-Dec cat  %02d %10.6f  %10.6f %8.3f  %8.3f  %8.3f"%(i+1,newra[i],newdec[i],newm[i],xp[i],yp[i]))
        scat=list(zip(xp,yp))
        tcat=list(zip(nxc,nyc))
        # Se hace el Match de Catalogs x-y
        dx,dy,idx_s,idx_t,match=get_hvshift(scat,tcat,binsize=1,plot=False,verbose=False)
        print ("Angle: %6.2f  Matches= %03d"%(angle[i],len(match)))
        if(len(match)>best_score):
            best_score=len(match)
            best_angle=angle[i]
    return(best_angle,best_score)




