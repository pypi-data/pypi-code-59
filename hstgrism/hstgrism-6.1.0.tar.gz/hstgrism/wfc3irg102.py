# Kornpob Bhirombhakdi
# kbhirombhakdi@stsci.edu

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import copy
from .confreader import ConfReader
from .computesip import ComputeSIP
from .computetracenwavelength import ComputeTraceNWavelength

class Wfc3IrG102:
    def __init__(self,objname='None',dfile=None,gfile=None,extnum=4,
                 conffile=None,beam=None,
                 xyd=None
                ):
        self.data = {'objname':objname,
                     'dfile':dfile,
                     'gfile':gfile,
                     'extnum':extnum,
                     'conffile':conffile,
                     'beam':beam,
                     'xyd':xyd,
                     'ROOTNAME':None,
                     'NAXIS1':None,
                     'NAXIS2':None,
                     'xgbound':(-65.,250.)
                    }
        self.conf = None
        self.trace = {'XYREF':(None,None),
                      'XG':None,
                      'YG':None,
                      'WW':None
                     }
        self.tracefile = None
        self._get_root()
        self._get_nax()
        self._get_conf()
    def _get_root(self):
        try:
            tmp = fits.open(self.data['gfile'])[0].header['ROOTNAME']
            self.data['ROOTNAME'] = tmp
        except:
            print('Cannot find ROOTNAME for {0}.\n'.format(self.data['gfile']))
    def _get_nax(self):
        try:
            tmp = fits.open(self.data['gfile'])[self.data['extnum']].header
            self.data['NAXIS1'] = tmp['NAXIS1']
            self.data['NAXIS2'] = tmp['NAXIS2']
        except:
            print('Cannot find NAXIS1,NAXIS2 for {0}.\n'.format(self.data['gfile']))
    def _get_conf(self): 
        try:
            conffile = self.data['conffile']
            conf = ConfReader(conffile)
            conf.getbeam(beam=self.data['beam'])
            conf.make_coef2d()
            self.conf = copy.deepcopy(conf)
        except:
            print('Cannot get conf for {0}.\n'.format(self.data['gfile']))
    ##########
    ##########
    ##########
    def compute(self):
        xyd = self.data['xyd']
        xydiff = self._compute_xydiff()
        xyoff = self._get_xyoff()
        xyref = np.array(xyd) + np.array(xydiff) + np.array(xyoff)
        obj = ComputeSIP(self.conf.coef2d,xyref[0],xyref[1])
        obj.compress()
        newobj = ComputeTraceNWavelength(obj.coef1d,obj.x1,obj.x2,self.data['NAXIS1'],self.data['NAXIS2'])
        newobj.compute()
        tmpx,tmpy,tmpw = newobj.trace['XG'],newobj.trace['YG'],newobj.wavelength['WW']
        xref = xyref[0]
        xgbound = self.data['xgbound']
        m = np.where((tmpx >= xref-xgbound[0])&(tmpx <= xref+xgbound[1]))
        tmpx,tmpy,tmpw = tmpx[m],tmpy[m],tmpw[m]
        self.trace['XYREF'] = xyref
        self.trace['XG'] = tmpx
        self.trace['YG'] = tmpy
        self.trace['WW'] = tmpw
        self.trace['COEF1D'] = newobj.data['COEF1D']
    def _compute_xydiff(self):
        EXTNUM = self.data['extnum']
        tmpd = fits.open(self.data['dfile'])
        tmpd_p1,tmpd_p2,tmpd_s = tmpd[0].header['POSTARG1'],tmpd[0].header['POSTARG2'],tmpd[EXTNUM].header['IDCSCALE']
        tmpg = fits.open(self.data['gfile'])
        tmpg_p1,tmpg_p2,tmpg_s = tmpg[0].header['POSTARG1'],tmpg[0].header['POSTARG2'],tmpg[EXTNUM].header['IDCSCALE']
        dx = tmpg_p1/tmpg_s - tmpd_p1/tmpd_s
        dy = tmpg_p2/tmpg_s - tmpd_p2/tmpd_s
        return (dx,dy)
    def _get_xyoff(self):
        beam = self.data['beam']
        confbeam = self.conf.beam
        return (confbeam['XOFF_'+beam].astype(float)[0],confbeam['YOFF_'+beam].astype(float)[0])
    ##########
    ##########
    ##########
    def save(self,savename_prefix=None):
        rootname = self.data['ROOTNAME']
        ##### xyref
        xyref = self.trace['XYREF']
        xref = np.full_like(self.trace['XG'],None,dtype=float)
        yref = np.full_like(self.trace['XG'],None,dtype=float)
        xref[0],yref[0] = xyref[0],xyref[1]
        ##### dydx, dldp
        dydx = np.full_like(self.trace['XG'],None,dtype=float)
        dldp = np.full_like(self.trace['XG'],None,dtype=float)
        for i in self.trace['COEF1D']:
            if i.split('_')[0] == 'DYDX':
                j = int(i.split('_')[-1])
                dydx[j] = self.trace['COEF1D'][i]
            elif i.split('_')[0] == 'DLDP':
                j = int(i.split('_')[-1])
                dldp[j] = self.trace['COEF1D'][i]
            else:
                pass
        tmp = {'XREF':xref,'YREF':yref,'XG':self.trace['XG'],'YG':self.trace['YG'],'WW':self.trace['WW'],
               'DYDX':dydx,'DLDP':dldp
              }
        if savename_prefix is None:
            savename_prefix = rootname
        string = '{0}_trace.csv'.format(savename_prefix)
        pd.DataFrame(tmp).to_csv(string,index=False)
        self.tracefile = string
        print('Save {0}'.format(string))
    ##########
    ##########
    ##########
    def show(self,save=False,savename_prefix=None,saveformat='pdf',
             dminmax=(5.,99.),gminmax=(5.,80.),alpha=0.6,lw=4,xpertick=50,
             dxy=(50,50),rotation=30,
             figsize=(10,10),fontsize=12
            ):
        EXTNUM = self.data['extnum']
        pixx,pixy = self.data['xyd'][0],self.data['xyd'][1]
        OBJNAME = self.data['objname']
        root = self.data['ROOTNAME']
        xg,yg,ww = self.trace['XG'],self.trace['YG'],self.trace['WW']
        xyref = self.trace['XYREF']
        dx,dy = dxy[0],dxy[1]        
        plt.figure(figsize=figsize)
        
        ax1 = plt.subplot(2,2,1)
        tmp = fits.open(self.data['dfile'])
        tmpheader = tmp[0].header
        tmpp = tmp[EXTNUM]
        tmppheader = tmpp.header
        tmppdata = tmpp.data
        m = np.isfinite(tmppdata)
        vmin,vmax = np.percentile(tmppdata[m],dminmax[0]),np.percentile(tmppdata[m],dminmax[1])
        ax1.imshow(tmppdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
        ax1.scatter(pixx,pixy,s=30,facecolor='None',edgecolor='red')
        fname = self.data['dfile'].split('/')[-1]
        string = '{0} {1} {2} SUBARRAY={3}\n'.format(fname,tmpheader['DATE-OBS'],tmpheader['FILTER'],tmpheader['SUBARRAY'])
        string += 'EXPSTART={0:.3f} EXPTIME={1:.3f}\n'.format(tmpheader['EXPSTART'],tmpheader['EXPTIME'])
        string += 'EXTNUM={0} BUNIT={1}'.format(EXTNUM,tmppheader['BUNIT'])
        ax1.set_title(string,fontsize=fontsize)

        ax2 = plt.subplot(2,2,2)
        ax2.imshow(tmppdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
        ax2.scatter(pixx,pixy,s=30,facecolor='None',edgecolor='red')
        ax2.set_xlim(pixx-dx,pixx+dx)
        ax2.set_ylim(pixy-dy,pixy+dy)
        string = '{0}\n'.format(OBJNAME)
        string += 'xy={0:.3f},{1:.3f}'.format(pixx,pixy)
        ax2.set_title(string,fontsize=fontsize)
        
        ax3 = plt.subplot(2,2,3)
        tmp = fits.open(self.data['gfile'])
        tmpheader = tmp[0].header
        tmpp = tmp[EXTNUM]
        tmppheader = tmpp.header
        tmppdata = tmpp.data
        m = np.isfinite(tmppdata)
        vmin,vmax = np.percentile(tmppdata[m],gminmax[0]),np.percentile(tmppdata[m],gminmax[1])
        ax3.imshow(tmppdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
        ax3.plot(xg,yg,'r-',alpha=alpha,lw=lw)
        fname = self.data['gfile'].split('/')[-1]
        string = '{0} {1} {2} SUBARRAY={3}\n'.format(fname,tmpheader['DATE-OBS'],tmpheader['FILTER'],tmpheader['SUBARRAY'])
        string += 'EXPSTART={0:.3f} EXPTIME={1:.3f}\n'.format(tmpheader['EXPSTART'],tmpheader['EXPTIME'])
        string += 'EXTNUM={0} BUNIT={1}'.format(EXTNUM,tmppheader['BUNIT'])
        ax3.set_title(string,fontsize=fontsize)
        
        ax4 = plt.subplot(2,2,4)
        ax4.imshow(tmppdata,origin='lower',cmap='viridis',vmin=vmin,vmax=vmax)
        ax4.plot(xg,yg,'r:',alpha=alpha,lw=lw)
        for i,ii in enumerate(xg):
            if (i in {0,len(xg)-1}) or (np.mod(i,xpertick)==0):
                label = '{0}A'.format(int(ww[i]))
                ax4.plot(xg[i],yg[i],'ro')
                ax4.annotate(label,(xg[i],yg[i]),
                             textcoords='offset points',
                             xytext=(0,10),
                             ha='center',
                             fontsize=fontsize,
                             rotation=rotation
                            )
        ax4.set_xlim(xg.min()-dx,xg.max()+dx)
        ax4.set_ylim(yg.min()-dy,yg.max()+dy)  
        string = 'xyref={0:.3f},{1:.3f}'.format(xyref[0],xyref[1])
        ax4.set_title(string,fontsize=fontsize)
        
        plt.tight_layout()
        if save:
            if savename_prefix is None:
                savename_prefix = root
            string = '{0}_overview.{1}'.format(savename_prefix,saveformat)
            plt.savefig(string,format=saveformat,bbox_inches='tight')
            print('Save {0}\n'.format(string))
        