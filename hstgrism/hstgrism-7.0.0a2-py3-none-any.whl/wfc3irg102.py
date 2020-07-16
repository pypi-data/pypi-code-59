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
    def __init__(self,container,gfile,dfile,conffile,
                 objname=None,xyd=None,beam=None,
                 xgbound=(-25.,250.)
                ):
        self.container = container
        self.data = {'objname':objname,
                     'dfile':dfile,
                     'gfile':gfile,
                     'conffile':conffile,
                     'beam':beam,
                     'xyd':xyd,
                     'xgbound':xgbound,
                     'NAXIS1':None,
                     'NAXIS2':None,
                    }
        self.conf = None
        self.trace = {'XYREF':(None,None),
                      'XG':None,
                      'YG':None,
                      'WW':None
                     }
        self.tracefile = None
        self._get_nax()
        self._get_conf()
    def _get_nax(self):
        try:
            gfile = self.data['gfile']
            tmp = fits.open(gfile[0])[gfile[1]].header
            self.data['NAXIS1'] = tmp['NAXIS1']
            self.data['NAXIS2'] = tmp['NAXIS2']
        except:
            print('Cannot find NAXIS1,NAXIS2 for {0}.\n'.format(gfile[0]))
    def _get_conf(self): 
        try:
            conffile = self.data['conffile']
            conf = ConfReader(conffile)
            conf.getbeam(beam=self.data['beam'])
            conf.make_coef2d()
            self.conf = copy.deepcopy(conf)
        except:
            print('Cannot get conf for {0}.\n'.format(gfile[0]))
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
        gfile = self.data['gfile']
        dfile = self.data['dfile']
        tmpd = fits.open(dfile[0])
        tmpd_p1,tmpd_p2,tmpd_s = tmpd[0].header['POSTARG1'],tmpd[0].header['POSTARG2'],tmpd[dfile[1]].header['IDCSCALE']
        tmpg = fits.open(gfile[0])
        tmpg_p1,tmpg_p2,tmpg_s = tmpg[0].header['POSTARG1'],tmpg[0].header['POSTARG2'],tmpg[gfile[1]].header['IDCSCALE']
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
    def save(self):
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
        saveprefix = self.container.data['saveprefix']
        savefolder = self.container.data['savefolder']
        string = './{0}/{1}_trace.csv'.format(savefolder,saveprefix)
        pd.DataFrame(tmp).to_csv(string,index=False)
        self.tracefile = string
        print('Save {0}'.format(string))
    ##########
    ##########
    ##########
    def show(self,save=False,
             params={'figsize':(10,10),
                     '221':{'minmax':(5.,99.),'cmap':'viridis','s':30,'facecolor':'None','edgecolor':'red','fontsize':12},
                     '222':{'minmax':(5.,99.),'cmap':'viridis','s':30,'facecolor':'None','edgecolor':'red','dxy':(50,50),'fontsize':12},
                     '223':{'minmax':(5.,99.),'cmap':'viridis','s':30,'facecolor':'None','edgecolor':'red','color':'red','ls':'-','lw':4,'alpha':0.6,'fontsize':12},
                     '224':{'minmax':(5.,99.),'cmap':'viridis','s':30,'facecolor':'None','edgecolor':'red','color':'red','ls':'-','lw':4,'alpha':0.6,'dxy':(50,50),'xpertick':50,'rotation':30.,'fontsize':12},
                    }
            ):
        gfile = self.data['gfile']
        dfile = self.data['dfile']
        pixx,pixy = self.data['xyd'][0],self.data['xyd'][1]
        OBJNAME = self.data['objname']
        xg,yg,ww = self.trace['XG'],self.trace['YG'],self.trace['WW']
        xyref = self.trace['XYREF']
        plt.figure(figsize=params['figsize'])
        
        ax1 = plt.subplot(2,2,1)
        fontsize = params['221']['fontsize']
        tmp = fits.open(dfile[0])
        tmpheader = tmp[0].header
        tmpp = tmp[dfile[1]]
        tmppheader = tmpp.header
        tmppdata = tmpp.data
        m = np.isfinite(tmppdata)
        vmin,vmax = np.percentile(tmppdata[m],params['221']['minmax'][0]),np.percentile(tmppdata[m],params['221']['minmax'][1])
        ax1.imshow(tmppdata,origin='lower',cmap=params['221']['cmap'],vmin=vmin,vmax=vmax)
        ax1.scatter(pixx,pixy,s=params['221']['s'],facecolor=params['221']['facecolor'],edgecolor=params['221']['edgecolor'])
        fname = dfile[0].split('/')[-1]
        string = '{0} {1} {2} SUBARRAY={3}\n'.format(fname,tmpheader['DATE-OBS'],tmpheader['FILTER'],tmpheader['SUBARRAY'])
        string += 'EXPSTART={0:.3f} EXPTIME={1:.3f}\n'.format(tmpheader['EXPSTART'],tmpheader['EXPTIME'])
        string += 'EXTNUM={0} BUNIT={1}'.format(dfile[1],tmppheader['BUNIT'])
        ax1.set_title(string,fontsize=fontsize)

        ax2 = plt.subplot(2,2,2)
        fontsize = params['222']['fontsize']
        dx,dy = params['222']['dxy']
        vmin,vmax = np.percentile(tmppdata[m],params['222']['minmax'][0]),np.percentile(tmppdata[m],params['222']['minmax'][1])
        ax2.imshow(tmppdata,origin='lower',cmap=params['222']['cmap'],vmin=vmin,vmax=vmax)
        ax2.scatter(pixx,pixy,s=30,facecolor=params['222']['facecolor'],edgecolor=params['222']['edgecolor'])
        ax2.set_xlim(pixx-dx,pixx+dx)
        ax2.set_ylim(pixy-dy,pixy+dy)
        string = '{0}\n'.format(OBJNAME)
        string += 'xy={0:.1f},{1:.1f}'.format(pixx,pixy)
        ax2.set_title(string,fontsize=fontsize)
        
        ax3 = plt.subplot(2,2,3)
        fontsize = params['223']['fontsize']
        tmp = fits.open(gfile[0])
        tmpheader = tmp[0].header
        tmpp = tmp[gfile[1]]
        tmppheader = tmpp.header
        tmppdata = tmpp.data
        m = np.isfinite(tmppdata)
        vmin,vmax = np.percentile(tmppdata[m],params['223']['minmax'][0]),np.percentile(tmppdata[m],params['223']['minmax'][1])
        ax3.imshow(tmppdata,origin='lower',cmap=params['223']['cmap'],vmin=vmin,vmax=vmax)
        ax3.plot(xg,yg,color=params['223']['color'],ls=params['223']['ls'],lw=params['223']['lw'],alpha=params['223']['alpha'])
        fname = gfile[0].split('/')[-1]
        string = '{0} {1} {2} SUBARRAY={3}\n'.format(fname,tmpheader['DATE-OBS'],tmpheader['FILTER'],tmpheader['SUBARRAY'])
        string += 'EXPSTART={0:.3f} EXPTIME={1:.3f}\n'.format(tmpheader['EXPSTART'],tmpheader['EXPTIME'])
        string += 'EXTNUM={0} BUNIT={1}'.format(gfile[1],tmppheader['BUNIT'])
        ax3.set_title(string,fontsize=fontsize)
        
        ax4 = plt.subplot(2,2,4)
        fontsize = params['224']['fontsize']
        xpertick = params['224']['xpertick']
        rotation = params['224']['rotation']
        dx,dy = params['224']['dxy']
        vmin,vmax = np.percentile(tmppdata[m],params['224']['minmax'][0]),np.percentile(tmppdata[m],params['224']['minmax'][1])
        ax4.imshow(tmppdata,origin='lower',cmap=params['224']['cmap'],vmin=vmin,vmax=vmax)
        ax4.plot(xg,yg,color=params['224']['color'],ls=params['224']['ls'],lw=params['224']['lw'],alpha=params['224']['alpha'])
        for i,ii in enumerate(xg):
            if (i in {0,len(xg)-1}) or (np.mod(i,xpertick)==0):
                label = '{0}A'.format(int(ww[i]))
                ax4.plot(xg[i],yg[i],'ro')
                ax4.annotate(label,(xg[i],yg[i]),
                             textcoords='offset points',
                             xytext=(0,10),
                             ha='center',
                             fontsize=fontsize,
                             rotation=rotation,
                             color=params['224']['color']
                            )
        ax4.set_xlim(xg.min()-dx,xg.max()+dx)
        ax4.set_ylim(yg.min()-dy,yg.max()+dy)  
        string = '{0}\n'.format(OBJNAME)
        string += 'xyref={0:.1f},{1:.1f}'.format(xyref[0],xyref[1])
        ax4.set_title(string,fontsize=fontsize)
        
        plt.tight_layout()
        if save:
            saveprefix = self.container.data['saveprefix']
            savefolder = self.container.data['savefolder']
            saveformat = self.container.data['plotformat']
            string = './{2}/{0}_overview.{1}'.format(saveprefix,saveformat,savefolder)
            plt.savefig(string,format=saveformat,bbox_inches='tight')
            print('Save {0}\n'.format(string))
        