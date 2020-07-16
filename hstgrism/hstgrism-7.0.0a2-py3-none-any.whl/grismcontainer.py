# Kornpob Bhirombhakdi
# kbhirombhakdi@stsci.edu

import os,glob

class GrismContainer:
    def __init__(self,saveprefix,savefolder,plotformat,overwrite):
        self.data = {'saveprefix':saveprefix,
                     'savefolder':savefolder,
                     'plotformat':plotformat,
                     'overwrite':overwrite
                    }
        self._prep_container()
    def _prep_container(self):
        tmp = glob.glob('*')
        if self.data['savefolder'] in tmp:
            sentinel = True
        else:
            sentinel = False
        if not sentinel:
            os.mkdir(self.data['savefolder'])
        else:
            if not self.data['overwrite']:
                string = 'Folder {0} already exists. Remove the folder or set overwrite = True'.format(self.data['savefolder'])
                raise ValueError(string)
            else:
                os.system('rm -r ./{0}'.format(self.data['savefolder']))
                os.mkdir(self.data['savefolder'])
    