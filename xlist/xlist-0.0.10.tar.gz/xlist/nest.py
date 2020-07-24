import copy
from types import MethodType
from .getset import get_via_pl,get_via_pl2,pl_to_bracket_str
from .sort import bat_sort
from .map import mapv as array_map
from .map import for_eachv
from .crud import append

###
def array_map2(*referls,**kwargs):
    '''
        obseleted just for compatible
        from elist.elist import *
        ol = [1,2,3,4]
        refl1 = ['+','+','+','+']
        refl2 = [7,7,7,7]
        refl3 = ['=','=','=','=']
        def map_func(ele,ref_ele1,ref_ele2,ref_ele3,prefix,suffix):
            s = prefix+': ' + str(ele) + str(ref_ele1) + str(ref_ele2) + str(ref_ele3) + suffix
            return(s)
        ####
        rslt = array_map2(ol,refl1,refl2,refl3,map_func=map_func,map_func_args=['Q','?'])
        pobj(rslt)
    '''
    map_func = kwargs['map_func']
    if('map_func_args' in kwargs):
        map_func_args = kwargs['map_func_args']
    else:
        map_func_args = []
    length = referls.__len__()
    rslt = []
    anum = list(referls)[0].__len__()
    for j in range(0,anum):
        args = []
        for i in range(0,length):
            refl = referls[i]
            args.append(refl[j])
        args.extend(map_func_args)
        v = map_func(*args)
        rslt.append(v)
    return(rslt)



#the below is for nested analysis

def is_leaf(obj):
    '''
        the below is for nested-list
        any type is not list will be treated as a leaf
        empty list will be treated as a leaf
        from elist.elist import *
        is_leaf(1)
        is_leaf([1,2,3])
        is_leaf([])
    '''
    if(isinstance(obj,list)):
        length = obj.__len__()
        if(length == 0):
            return(True)
        else:
            return(False)
    else:
        return(True)

class LevelCache():
    '''
        current level unhandled_data stored in .data
        current level unhandled_desc stored in .desc
        next level unhandled_data stored in .ndata
        next level unhandled_desc stored in .ndesc
    '''
    def help(self):
        print(self.__doc__)
    def __init__(self,**kwargs):
        if('datas' in kwargs):
            datas = kwargs['datas']
        else:
            datas = []
        if('descs' in kwargs):
            descs = kwargs['descs']
        else:
            descs = []
        self.data = [datas]
        self.desc = [descs]
        self.ndata = []
        self.ndesc = []
    def update(self):
        self.data = self.ndata
        self.desc = self.ndesc
        self.ndata = []
        self.ndesc = []
    def __repr__(self):
        print("data: {0}".format(self.data))
        print("desc: {0}".format(self.desc))
        print("ndata: {0}".format(self.ndata))
        print("ndesc: {0}".format(self.ndesc),end='')
        return("")
    def clear(self):
        self.data = []
        self.desc = []
        self.ndata = []
        self.ndesc = []

class StateCache():
    '''
        parent level handled_desc stored in .pdesc_level
        current level handled_desc stored in .desc_level
        过早优化乃万恶之源，之所以有LevelCache 和 StateCache 两个Cache 是为了利用我之前的旧代码，弃之可惜，尾大不掉
    '''
    def help(self):
        print(self.__doc__)
    def __init__(self,root_matrix):
        #there is only one level in root_matrix: level 0
        #there is only one element in root_matrix level 0 :element 0 
        self.matrix = root_matrix
        self.depth = 0
        self.pdesc_level = []
        self.desc_level = self.matrix[0]
    def update(self):
        self.pdesc_level = self.desc_level
        self.matrix.append([])
        self.depth = self.depth + 1
        self.desc_level = self.matrix[self.depth]
    def __repr__(self):
        print("depth: {0}".format(self.depth))
        print("pdesc_level: {0}".format(self.pdesc_level))
        print("desc_level: {0}".format(self.desc_level),end='')
        return("")

def pcache_bind_dynamic_method(pcache,**kwargs):
    '''
    '''
    mn = kwargs['method_name']
    func = kwargs['func']
    method_names = ['get_children_handler','parent_handler','child_begin_handler','leaf_handler','non_leaf_handler','child_end_handler']
    cond = (mn in method_names)
    if(cond):
        pcache.__setattr__(mn, MethodType(func,pcache))
    else:
        pass
    return(pcache)

def init_pcache_handler_inline(kwargs):
    pcache = PointerCache()
    for mn in kwargs:
        cond = (mn in ['get_children_handler','parent_handler','child_begin_handler','leaf_handler','non_leaf_handler','child_end_handler'])
        if(cond):
            func = kwargs[mn]
            pcache.__setattr__(mn, MethodType(func,pcache))
        else:
            pass
    return(pcache)

def pcache_reset_methods(pcache,**kwargs):
    '''
    '''
    def get_children_handler(self,*args):
        '''
            list's children list is self
        '''
        return(self.pdata)
    def parent_handler(self,lcache,i,*args):
        '''
            _update_pdesc_sons_info
        '''
        pdesc = lcache.desc[i]
        pdesc['sons_count'] = self.sibs_len
        pdesc['leaf_son_paths'] = []
        pdesc['non_leaf_son_paths'] = []
        return(pdesc)
    def child_begin_handler(self,scache,*args):
        '''
            _creat_child_desc
            update depth,parent_breadth_path,parent_path,sib_seq,path,lsib_path,rsib_path,lcin_path,rcin_path
        '''
        pdesc = self.pdesc
        depth = scache.depth
        sib_seq = self.sib_seq
        sibs_len = self.sibs_len
        pdesc_level = scache.pdesc_level
        desc = copy.deepcopy(pdesc)
        desc = reset_parent_desc_template(desc)
        desc['depth'] = depth
        desc['parent_breadth_path'] = copy.deepcopy(desc['breadth_path'])
        desc['sib_seq'] = sib_seq
        desc['parent_path'] = copy.deepcopy(desc['path'])
        desc['path'].append(sib_seq)
        update_desc_lsib_path(desc)
        update_desc_rsib_path(desc,sibs_len)
        if(depth == 1):
            pass
        else:
            update_desc_lcin_path(desc,pdesc_level)
            update_desc_rcin_path(desc,sibs_len,pdesc_level)
        return(desc)
    def leaf_handler(self,*args):
        '''#leaf child handler'''
        desc = self.desc
        pdesc = self.pdesc
        desc['leaf'] = True
        desc['sons_count'] = 0
        pdesc['leaf_son_paths'].append(copy.deepcopy(desc['path']))
    def non_leaf_handler(self,lcache):
        '''#nonleaf child handler'''
        desc = self.leaf
        pdesc = self.pdesc
        desc['leaf'] = False
        pdesc['non_leaf_son_paths'].append(copy.deepcopy(desc['path']))
        lcache.ndata.append(self.data)
        lcache.ndesc.append(desc)
    def child_end_handler(self,scache):
        '''
            _upgrade_breadth_info
            update breadth, breadth_path, and add desc to desc_level
        '''
        desc = self.desc
        desc_level = scache.desc_level
        breadth = desc_level.__len__()
        desc['breadth'] = breadth
        desc['breadth_path'].append(breadth)
        desc_level.append(desc)
    funcs = [get_children_handler,parent_handler,child_begin_handler,leaf_handler,non_leaf_handler,child_end_handler]
    method_names = ['get_children_handler','parent_handler','child_begin_handler','leaf_handler','non_leaf_handler','child_end_handler']
    for i in range(0,funcs.__len__()):
        mn = method_names[i]
        func = funcs[i]
        pcache.__setattr__(mn, MethodType(func,pcache))
    return(pcache)

class PointerCache():
    '''
    '''
    def get_children_handler(self,*args):
        '''
            list's children list is self
        '''
        return(self.pdata)
    def parent_handler(self,lcache,i,*args):
        '''
            _update_pdesc_sons_info
        '''
        pdesc = lcache.desc[i]
        pdesc['sons_count'] = self.sibs_len
        pdesc['leaf_son_paths'] = []
        pdesc['non_leaf_son_paths'] = []
        pdesc['leaf_descendant_paths'] = []
        pdesc['non_leaf_descendant_paths'] = []
        return(pdesc)
    def child_begin_handler(self,scache,*args):
        '''
            _creat_child_desc
            update depth,parent_breadth_path,parent_path,sib_seq,path,lsib_path,rsib_path,lcin_path,rcin_path
        '''
        pdesc = self.pdesc
        depth = scache.depth
        sib_seq = self.sib_seq
        sibs_len = self.sibs_len
        pdesc_level = scache.pdesc_level
        desc = copy.deepcopy(pdesc)
        desc = reset_parent_desc_template(desc)
        desc['depth'] = depth
        desc['parent_breadth_path'] = copy.deepcopy(desc['breadth_path'])
        desc['sib_seq'] = sib_seq
        desc['parent_path'] = copy.deepcopy(desc['path'])
        desc['path'].append(sib_seq)
        update_desc_lsib_path(desc)
        update_desc_rsib_path(desc,sibs_len)
        if(depth == 1):
            pass
        else:
            update_desc_lcin_path(desc,pdesc_level)
            update_desc_rcin_path(desc,sibs_len,pdesc_level)
        return(desc)
    def leaf_handler(self,*args):
        '''#leaf child handler'''
        desc = self.desc
        pdesc = self.pdesc
        desc['leaf'] = True
        desc['sons_count'] = 0
        pdesc['leaf_son_paths'].append(copy.deepcopy(desc['path']))
        pdesc['leaf_descendant_paths'].append(copy.deepcopy(desc['path']))
    def non_leaf_handler(self,lcache):
        '''#nonleaf child handler'''
        desc = self.desc
        pdesc = self.pdesc
        desc['leaf'] = False
        pdesc['non_leaf_son_paths'].append(copy.deepcopy(desc['path']))
        pdesc['non_leaf_descendant_paths'].append(copy.deepcopy(desc['path']))
        lcache.ndata.append(self.data)
        lcache.ndesc.append(desc)
    def child_end_handler(self,scache):
        '''
            _upgrade_breadth_info
            update breadth, breadth_path, and add desc to desc_level
        '''
        desc = self.desc
        desc_level = scache.desc_level
        breadth = desc_level.__len__()
        desc['breadth'] = breadth
        desc['breadth_path'].append(breadth)
        desc_level.append(desc)
    def update_pdesc(self,lcache,i):
        self.unhandled_seq = i
        self.pdata = lcache.data[i]
        self.children = self.get_children_handler(*self.get_children_handler_args)
        self.sibs_len = self.children.__len__()
        self.pdesc = self.parent_handler(lcache,i,*self.parent_handler_args)
    def update_desc(self,lcache,scache,sib_seq):
        self.sib_seq = sib_seq
        self.data = self.children[self.sib_seq]
        self.desc = self.child_begin_handler(scache)
        if(is_leaf(self.data)):
            self.leaf_handler()
        else:
            self.non_leaf_handler(lcache)
        self.child_end_handler(scache)
    def help(self):
        print(self.__doc__)
    def __init__(self,**kwargs):
        if('get_children_handler_args' in kwargs):
            self.get_children_handler_args = kwargs['get_children_handler_args']
        else:
            self.get_children_handler_args = []
        if('parent_handler_args' in kwargs):
            self.parent_handler_args = kwargs['parent_handler_args']
        else:
            self.parent_handler_args = []
        if('child_begin_handler_args' in kwargs):
            self.child_begin_handler_args = kwargs['child_begin_handler_args']
        else:
            self.child_begin_handler_args = []
        if('leaf_handler_args' in kwargs):
            self.leaf_handler_args = kwargs['leaf_handler_args']
        else:
            self.leaf_handler_args = []
        if('non_leaf_handler_args' in kwargs):
            self.non_leaf_handler_args = kwargs['non_leaf_handler_args']
        else:
            self.non_leaf_handler_args = []
        if('child_end_handler_args' in kwargs):
            self.child_end_handler_args = kwargs['child_end_handler_args']
        else:
            self.child_end_handler_args = []
        self.unhandled_seq = None
        self.children = None
        self.sibs_len = None
        self.pdesc = None
        self.sib_seq = None
        self.data = None
        self.desc = None

##the below is for each element desc handle
def new_ele_description(**kwargs):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        root_desc = new_ele_description(leaf=False,depth=0,breadth_path=[],path=[],parent_path=[],parent_breadth_path=[])
        pobj(root_desc)
        #None means not handled
    '''
    desc = {
        'leaf':None,
        'depth':None,
        'breadth':None,
        'breadth_path':None,
        'sib_seq':None,
        'path':None,
        'parent_path':None,
        'parent_breadth_path':None,
        'lsib_path':None,
        'rsib_path':None,
        'lcin_path':None,
        'rcin_path':None,
        'sons_count':None,
        'leaf_son_paths':None,
        'non_leaf_son_paths':None,
        'leaf_descendant_paths':None,
        'non_leaf_descendant_paths':None,
        'flat_offset':None,
        'flat_len':None
    }
    for key in kwargs:
        desc[key.lower()] = kwargs[key]
    return(desc)

def root_list(*args):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        root_list([1],2,[1,2,3])
    '''
    return(list(args))

def init_desc_matrix(l):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        l = [1,[4],2,[3,[5,6]]]
        desc_matrix = init_desc_matrix(l)
        pobj(desc_matrix)
    '''
    leaf = is_leaf(l)
    root_desc = new_ele_description(leaf=leaf,depth=0,breadth_path=[],path=[],parent_path=[],parent_breadth_path=[])
    if(leaf):
        root_desc['sons_count'] = 0
    else:
        pass
    desc_matrix = [
        [root_desc]
    ]
    return(desc_matrix)

def reset_parent_desc_template(desc):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        pobj(desc)
        tem = reset_parent_desc_template(desc)
        pobj(tem)
        #only inherit path  and breadth_path
    '''
    tem = new_ele_description()
    tem['path'] = desc['path']
    tem['breadth_path'] = desc['breadth_path']
    return(tem)

def _init_unhandled(l,inited_matrix):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        l = [1,[4],2,[3,[5,6]]]
        desc_matrix = init_desc_matrix(l)
        unhandled = _init_unhandled(l,desc_matrix)
        unhandled_data = unhandled['data']
        unhandled_desc = unhandled['desc']
        unhandled_data[0]
        unhandled_desc[0]
        unhandled_data[1]
        unhandled_desc[1]
    '''
    root_desc = inited_matrix[0][0]
    unhandled = {'data':[],'desc':[]}
    length = l.__len__()
    root_desc['sons_count'] = length
    root_desc['leaf_son_paths'] = []
    root_desc['non_leaf_son_paths'] = []    
    if(length == 0):
        pass
    else:
        inited_matrix.append([])
        level = inited_matrix[1]
        for i in range(0,length):
            child = l[i]
            desc = copy.deepcopy(root_desc)
            desc = reset_parent_desc_template(desc)
            desc['depth'] = 1
            desc['breadth'] = i
            desc['parent_breadth_path'] = copy.deepcopy(desc['breadth_path'])
            desc['breadth_path'].append(i)
            desc['sib_seq'] = i
            desc['parent_path'] = copy.deepcopy(desc['path'])
            desc['path'].append(i)
            if(i==0):
                pass
            else:
                desc['lsib_path'] = [i-1]
            if(i == (length - 1)):
                pass
            else:
                desc['rsib_path'] = [i+1]
            if(is_leaf(child)):
                desc['leaf'] = True
                desc['sons_count'] = 0
                root_desc['leaf_son_paths'].append(copy.deepcopy(desc['path']))
            else:
                desc['leaf'] = False
                root_desc['non_leaf_son_paths'].append(copy.deepcopy(desc['path']))
                unhandled['data'].append(child)
                unhandled['desc'].append(desc)
            level.append(desc)
    return(unhandled)

def update_desc_lsib_path(desc):
    '''
        leftSibling
        previousSibling
        leftSib
        prevSib
        lsib
        psib
        
        have the same parent,and on the left
    '''
    if(desc['sib_seq']>0):
        lsib_path = copy.deepcopy(desc['path'])
        lsib_path[-1] = desc['sib_seq']-1
        desc['lsib_path'] = lsib_path
    else:
        pass
    return(desc)

def update_desc_rsib_path(desc,sibs_len):
    '''
        rightSibling
        nextSibling
        rightSib
        nextSib
        rsib
        nsib
        
        have the same parent,and on the right
    '''
    if(desc['sib_seq']<(sibs_len-1)):
        rsib_path = copy.deepcopy(desc['path'])
        rsib_path[-1] = desc['sib_seq']+1
        desc['rsib_path'] = rsib_path
    else:
        pass
    return(desc)

def update_desc_lcin_path(desc,pdesc_level):
    '''
        leftCousin
        previousCousin
        leftCin
        prevCin
        lcin
        pcin
        
        parents are neighbors,and on the left
    '''
    parent_breadth = desc['parent_breadth_path'][-1]
    if(desc['sib_seq']==0):
        if(parent_breadth==0):
            pass
        else:
            parent_lsib_breadth = parent_breadth - 1
            plsib_desc = pdesc_level[parent_lsib_breadth]
            if(plsib_desc['leaf']):
                pass
            else:
                lcin_path = copy.deepcopy(plsib_desc['path'])
                lcin_path.append(plsib_desc['sons_count'] - 1)
                desc['lcin_path'] = lcin_path
    else:
        pass
    return(desc)

def update_desc_rcin_path(desc,sibs_len,pdesc_level):
    '''
        rightCousin
        nextCousin
        rightCin
        nextCin
        rcin
        ncin
        
        parents are neighbors,and on the right
    '''
    psibs_len = pdesc_level.__len__()
    parent_breadth = desc['parent_breadth_path'][-1]
    if(desc['sib_seq']==(sibs_len - 1)):
        if(parent_breadth==(psibs_len -1)):
            pass
        else:
            parent_rsib_breadth = parent_breadth + 1
            prsib_desc = pdesc_level[parent_rsib_breadth]
            #because from left to right to handle each level
            #sons_count will only be updated in the next-round 
            if(prsib_desc['leaf']):
                pass
            else:
                rcin_path = copy.deepcopy(prsib_desc['path'])
                rcin_path.append(0)
                desc['rcin_path'] = rcin_path
    else:
        pass
    return(desc)

def scan(l,**kwargs):
    '''
        from elist.elist import *
        from elist.jprint import pobj
        l = [1,[4],2,[3,[5,6]]]
        desc = description(l)
        l = [1,2,[4],[3,[5,6]]]
        desc = description(l)
    '''
    if('itermode' in kwargs):
        itermode = True
    else:
        itermode = False
    ####level ==  0
    desc_matrix = init_desc_matrix(l)
    if(desc_matrix[0][0]['leaf'] == True):
        return(desc_matrix)
    else:
        pass
    ####cache
    lcache=LevelCache(datas=l,descs=desc_matrix[0][0])
    scache=StateCache(desc_matrix)
    pcache = init_pcache_handler_inline(kwargs)
    ####level > 0
    while(lcache.data.__len__() > 0):
        #add next desc_level 
        scache.update()
        for unhandled_seq in range(0,lcache.data.__len__()):
            #handle parent
            pcache.update_pdesc(lcache,unhandled_seq)
            for sib_seq in range(0,pcache.sibs_len):
                #handle child
                pcache.update_desc(lcache,scache,sib_seq)
        #update level lcache
        lcache.update()
    return(desc_matrix)

class DescMatrix():
    '''
    '''
    def __init__(self,matrix):
        self.matrix = matrix
    @classmethod
    def loc(cls,desc):
        return([desc['depth'],desc['breadth']])
    @classmethod
    def ploc(cls,desc):
        if(desc['parent_breadth_path'] == []):
            col = 0
        else:
            col = desc['parent_breadth_path'][-1]
        if(desc['depth'] == 0):
            row = 0
        else:
            row = desc['depth']-1
        return([row,col])
    def pdesc(self,desc):
        pd = get_via_pl(self.matrix,self.ploc(desc))
        return(pd)

def fullfill_descendants_info(desc_matrix):
    '''
       flat_offset
    '''
    pathloc_mapping = {}
    locpath_mapping = {}
    #def leaf_handler(desc,pdesc,offset):
    def leaf_handler(desc,pdesc):
        #desc['flat_offset'] = (offset,offset+1)
        desc['non_leaf_son_paths'] = []
        desc['leaf_son_paths'] = []
        desc['non_leaf_descendant_paths'] = []
        desc['leaf_descendant_paths'] = []
        desc['flat_len'] = 1
        if(pdesc['flat_len']):
            pdesc['flat_len'] = pdesc['flat_len'] + 1
        else:
            pdesc['flat_len'] = 1
    #def non_leaf_handler(desc,pdesc,offset):
    def non_leaf_handler(desc,pdesc):
        #desc['flat_offset'] = (offset,offset+desc['flat_len'])
        pdesc['non_leaf_descendant_paths'].extend(copy.deepcopy(desc['non_leaf_descendant_paths']))
        pdesc['leaf_descendant_paths'].extend(copy.deepcopy(desc['leaf_descendant_paths']))
        if(pdesc['flat_len']):
            pdesc['flat_len'] = pdesc['flat_len'] + desc['flat_len']
        else:
            pdesc['flat_len'] = desc['flat_len']
    def fill_path_mapping(desc):
        pmk = tuple(desc['path'])
        pmv = tuple(DescMatrix.loc(desc))
        pathloc_mapping[pmk] = pmv
        locpath_mapping[pmv] = pmk
    dm = DescMatrix(desc_matrix)
    depth = desc_matrix.__len__()
    desc_level = desc_matrix[depth - 1]
    length = desc_level.__len__()
    #the last level
    #offset = 0
    for j in range(length - 1,-1,-1):
        desc = desc_level[j]
        fill_path_mapping(desc)
        pdesc = dm.pdesc(desc)
        leaf_handler(desc,pdesc)
        #leaf_handler(desc,pdesc,offset)
        #offset = offset + 1
    for i in range(depth-2,0,-1):
        #offset = 0
        desc_level = desc_matrix[i]
        length = desc_level.__len__()
        for j in range(length-1,-1,-1):
            desc = desc_level[j]
            fill_path_mapping(desc)
            pdesc = dm.pdesc(desc)
            if(desc['leaf']):
                leaf_handler(desc,pdesc)
                #leaf_handler(desc,pdesc,offset)
                #offset = offset + 1
            else:
                non_leaf_handler(desc,pdesc)
                #non_leaf_handler(desc,pdesc,offset)
                #offset = offset + desc['flat_len']
    desc_matrix[0][0]['flat_offset'] = (0,desc_matrix[0][0]['flat_len'])
    for i in range(0,depth-1):
        pdesc_level = desc_matrix[i]
        length = pdesc_level.__len__()
        for j in range(0,length):
            pdesc = pdesc_level[j]
            si = pdesc['flat_offset'][0]
            for i in range(0,pdesc['sons_count']):
                spl = append(pdesc['path'],i,mode='new')
                pk = tuple(spl)
                locx,locy = pathloc_mapping[pk]
                son = desc_matrix[locx][locy]
                ei = si + son['flat_len']
                son['flat_offset'] = (si,ei)
                si = ei
    return(desc_matrix,pathloc_mapping,locpath_mapping)

####from elist.jprint

def get_block_op_pairs(pairs_str):
    '''
        # >>> get_block_op_pairs("{}[]")  
        # {1: ('{', '}'), 2: ('[', ']')}
        # >>> get_block_op_pairs("{}[]()")
        # {1: ('{', '}'), 2: ('[', ']'), 3: ('(', ')')}
        # >>> get_block_op_pairs("{}[]()<>")
        # {1: ('{', '}'), 2: ('[', ']'), 3: ('(', ')'), 4: ('<', '>')}
    '''
    pairs_str_len = pairs_str.__len__()
    pairs_len = pairs_str_len // 2
    pairs_dict = {}
    for i in range(1,pairs_len +1):
        pairs_dict[i] = pairs_str[i*2-2],pairs_str[i*2-1]
    return(pairs_dict)

def is_lop(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
    # is_lop('{',block_op_pairs_dict)
    # is_lop('[',block_op_pairs_dict)
    # is_lop('}',block_op_pairs_dict)
    # is_lop(']',block_op_pairs_dict)
    # is_lop('a',block_op_pairs_dict)
    '''
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(ch == block_op_pairs_dict[i][0]):
            return(True)
        else:
            pass
    return(False)

def is_rop(ch,block_op_pairs_dict=get_block_op_pairs('{}[]()')):
    '''
        # is_rop('{',block_op_pairs_dict)
        # is_rop('[',block_op_pairs_dict)
        # is_rop('}',block_op_pairs_dict)
        # is_rop(']',block_op_pairs_dict)
        # is_rop('a',block_op_pairs_dict)
    '''
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(ch == block_op_pairs_dict[i][1]):
            return(True)
        else:
            pass
    return(False)

def get_next_char_level_in_j_str(curr_lv,curr_seq,j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()")):
    ''' the first-char is level-1
        when current is  non-op, next-char-level = curr-level
        when current is  lop,  non-paired-rop-next-char-level = lop-level+1;
        when current is  lop,  paired-rop-next-char-level = lop-level
        when current is  rop,  next-char-level = rop-level - 1
        # {"key_4_UF0aJJ6v": "value_1", "key_2_Hd0t": ["value_16", "value_8", "value_8", "value_15", "value_14", "value_19", {......
        # 122222222222222222222222222222222222222222222333333333333333333333333333333333333333333333333333333333333333333333334......
        # {\n"key_4_UF0aJJ6v": "value_1", \n"key_2_Hd0t": [\n"value_16", \n"value_8", \n"value_8", \n"value_15", \n"value_14", \n"value_19",...... 
        # 1 222222222222222222222222222222 2222222222222222 3333333333333 333333333333 333333333333 3333333333333 3333333333333 3333333333333...... 
        '''
    curr_ch = j_str[curr_seq]
    next_ch = j_str[curr_seq + 1]
    cond = 0
    for i in range(1,block_op_pairs_dict.__len__()+1):
        if(curr_ch == block_op_pairs_dict[i][0]):
            if(next_ch == block_op_pairs_dict[i][1]):
                next_lv = curr_lv               
            else:
                next_lv = curr_lv + 1
            cond = 1
            break
        elif(curr_ch == block_op_pairs_dict[i][1]):
            if(is_rop(next_ch,block_op_pairs_dict)):
                next_lv = curr_lv - 1
            else:
                next_lv = curr_lv
            cond = 1
            break
        else:
            pass
    if(cond == 1):
        pass
    elif(is_rop(next_ch,block_op_pairs_dict)):
        next_lv = curr_lv - 1
    else:    
        next_lv = curr_lv
    curr_lv = next_lv
    curr_seq = curr_seq + 1
    return(curr_lv,curr_lv,curr_seq)

def get_j_str_lvs_dict(j_str,block_op_pairs_dict=get_block_op_pairs("{}[]()")):
    j_str_len = j_str.__len__()
    j_str_lvs_dict = {}
    if( j_str_len == 0):
        j_str_lvs_dict = {}
    elif(j_str_len == 1):
        j_str_lvs_dict = {0:1}
    else:
        curr_lv = 1
        j_str_lvs_dict = {0:1}
        seq = 1
        curr_seq = 0
        while(curr_seq < j_str_len - 1):
            level,curr_lv,curr_seq = get_next_char_level_in_j_str(curr_lv,curr_seq,j_str,block_op_pairs_dict)
            j_str_lvs_dict[seq] =level
            seq = seq + 1
    return(j_str_lvs_dict)



####from elist.utils
def str_display_width(s):
    '''
        from elist.utils import *
        str_display_width('a')
        str_display_width('去')
    '''
    s= str(s)
    width = 0
    len = s.__len__()
    for i in range(0,len):
        sublen = s[i].encode().__len__()
        sublen = int(sublen/2 + 1/2)
        width = width + sublen
    return(width)

####from elist.ltdict
def ltdict2list(ltdict):
    l = []
    length = ltdict.__len__()
    for i in range(0,length):
        l.append(ltdict[i])
    return(l)

####beautiful display
def spacize(s,lvnum):
    lvs = get_j_str_lvs_dict(s)
    lvs = ltdict2list(lvs)
    sl=list(s)
    length = sl.__len__()
    rslt =''
    for i in range(0,length):
        if(lvs[i]>=lvnum):
            rslt = rslt + sl[i]
        else:
            rslt = rslt + chr(32)*str_display_width(sl[i])
    return(rslt)

def table(l,depth,**kwargs):
    if('no_return' in kwargs):
        no_return = kwargs['no_return']
    else:
        no_return = True
    s = l.__str__()
    rslt = ''
    for i in range(1,depth+1):
        rslt = rslt + spacize(s,i) + '\n'
    rslt = rslt[:-1]
    if(no_return):
        print(rslt)
    else:
        return(rslt)

####mat func for description matrix

def matrix_map(mat,map_func,map_func_args=[]):
    '''
        mat = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        
        def map_func(value,indexr,indexc,prefix,suffix):
            msg = prefix + str((indexr,indexc)) + " : "+str(value) + suffix
            return(msg)
        
        mmat = matrix_map(mat,map_func,map_func_args=["<",">"])
        
        mmat 
    '''
    mmat = []
    for i in range(0,mat.__len__()):
        level = mat[i]
        mmat.append([])
        for j in range(0,level.__len__()):
            value = level[j]
            indexr = i
            indexc = j
            ele = map_func(value,indexr,indexc,*map_func_args)
            mmat[i].append(ele)
    return(mmat)

def is_matrix(m,**kwargs):
    def cond_func(ele,lngth):
        cond = (ele.__len__() == lngth)
        return(cond)
    cond_1 = every(m,isinstance,list)
    if(cond_1):
        if('mode' in kwargs):
            mode = kwargs['mode']
        else:
            mode = 'strict' 
        if(mode == 'strict'):
            try:
                lngth = m[0].__len__()
                cond_2 = every(m,cond_func,lngth)
            except:
                return(False)
            else:
                pass
        else:
            cond_2 = True
        return(cond_1 & cond_2)
    else:
        return(True)


#

#dfs depth-first-search trace
def get_dfs(l):
    '''
        l = ['v_7', 'v_3', 'v_1', 'v_4', ['v_4', 'v_2'], 'v_5', 'v_6', 'v_1', 'v_6', 'v_7', 'v_5', ['v_4', ['v_1', 'v_8', 'v_3', 'v_4', 'v_2', 'v_7', [['v_3', 'v_2'], 'v_4', 'v_5', 'v_1', 'v_3', 'v_1', 'v_2', 'v_5', 'v_8', 'v_8', 'v_7'], 'v_5', 'v_8', 'v_7', 'v_1', 'v_5'], 'v_6'], 'v_4', 'v_5', 'v_8', 'v_5']
        dfs = get_dfs(l)
    '''
    ltree = ListTree(l)
    dfs = ltree.tree()
    return(dfs)


#wfs  width-first-search trace
#wfsmat width-first-search matrix

def get_wfsmat(l):
    '''
       l = ['v_7', 'v_3', 'v_1', 'v_4', ['v_4', 'v_2'], 'v_5', 'v_6', 'v_1', 'v_6', 'v_7', 'v_5', ['v_4', ['v_1', 'v_8', 'v_3', 'v_4', 'v_2', 'v_7', [['v_3', 'v_2'], 'v_4', 'v_5', 'v_1', 'v_3', 'v_1', 'v_2', 'v_5', 'v_8', 'v_8', 'v_7'], 'v_5', 'v_8', 'v_7', 'v_1', 'v_5'], 'v_6'], 'v_4', 'v_5', 'v_8', 'v_5']
       get_wfs(l)
    '''
    ltree = ListTree(l)
    vdescmat = ltree.desc
    wfsmat = matrix_map(vdescmat,lambda v,ix,iy:v['path'])
    wfsmat.pop(0)
    return(wfsmat)



def mat2wfs(wfsmat):
    trace = []
    for i in range(0,wfsmat.__len__()):
        trace.extend(wfsmat[i])
    return(trace)

def wfs2mat(wfs):
    '''
        wfs = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [4, 0], [4, 1], [11, 0], [11, 1], [11, 2], [11, 1, 0], [11, 1, 1], [11, 1, 2], [11, 1, 3], [11, 1, 4], [11, 1, 5], [11, 1, 6], [11, 1, 7], [11, 1, 8], [11, 1, 9], [11, 1, 10], [11, 1, 11], [11, 1, 6, 0], [11, 1, 6, 1], [11, 1, 6, 2], [11, 1, 6, 3], [11, 1, 6, 4], [11, 1, 6, 5], [11, 1, 6, 6], [11, 1, 6, 7], [11, 1, 6, 8], [11, 1, 6, 9], [11, 1, 6, 10], [11, 1, 6, 0, 0], [11, 1, 6, 0, 1]]
    '''
    wfsmat = []
    depth = 0
    level = filter(wfs,lambda ele:ele.__len__()==1)
    while(level.__len__()>0):
        wfsmat.append([])
        wfsmat[depth] = level
        depth = depth+1
        level = filter(wfs,lambda ele:ele.__len__()==depth+1)
    return(wfsmat)


def get_wfs(l):
    wfsmat = get_wfsmat(l)
    wfs =  mat2wfs(wfsmat)
    return(wfs)


def dfs2wfsmat(dfs):
    '''
        dfs = [[0], [1], [2], [3], [4], [4, 0], [4, 1], [5], [6], [7], [8], [9], [10], [11], [11, 0], [11, 1], [11, 1, 0], [11, 1, 1], [11, 1, 2], [11, 1, 3], [11, 1, 4], [11, 1, 5], [11, 1, 6], [11, 1, 6, 0], [11, 1, 6, 0, 0], [11, 1, 6, 0, 1], [11, 1, 6, 1], [11, 1, 6, 2], [11, 1, 6, 3], [11, 1, 6, 4], [11, 1, 6, 5], [11, 1, 6, 6], [11, 1, 6, 7], [11, 1, 6, 8], [11, 1, 6, 9], [11, 1, 6, 10], [11, 1, 7], [11, 1, 8], [11, 1, 9], [11, 1, 10], [11, 1, 11], [11, 2], [12], [13], [14], [15]]
        
        dfs2wfs(dfs)
    '''
    wfsmat = []
    depth = 0
    level = filter(dfs,lambda ele:ele.__len__()==1)
    while(level.__len__()>0):
        wfsmat.append([])
        wfsmat[depth] = level
        depth = depth+1
        level = filter(dfs,lambda ele:ele.__len__()==depth+1)
    return(wfsmat)


     


def wfsmat2dfs(wfsmat):
    '''
        wfs = [[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]], [[4, 0], [4, 1], [11, 0], [11, 1], [11, 2]], [[11, 1, 0], [11, 1, 1], [11, 1, 2], [11, 1, 3], [11, 1, 4], [11, 1, 5], [11, 1, 6], [11, 1, 7], [11, 1, 8], [11, 1, 9], [11, 1, 10], [11, 1, 11]], [[11, 1, 6, 0], [11, 1, 6, 1], [11, 1, 6, 2], [11, 1, 6, 3], [11, 1, 6, 4], [11, 1, 6, 5], [11, 1, 6, 6], [11, 1, 6, 7], [11, 1, 6, 8], [11, 1, 6, 9], [11, 1, 6, 10]], [[11, 1, 6, 0, 0], [11, 1, 6, 0, 1]]]
        wfs2dfs(wfs)
        
    '''
    dfs = mat2wfs(wfsmat)
    dfs.sort()
    return(dfs)




def dfs2wfs(dfs):
    wfsmat = dfs2wfsmat(dfs)
    wfs = mat2wfs(wfsmat)
    return(wfs)

def wfs2dfs(wfs):
    wfsmat = wfs2mat(wfs)
    dfs = wfsmat2dfs(wfsmat)
    return(dfs)

####


class ListTree():
    '''
        
        
        ltree.parent_path(3,1,0)
        ltree.parent(3,1,0)
        
        ltree.son_paths(3)
        ltree.sons(3)
        ltree.son_paths(3,leaf_only=True)
        ltree.son_paths(3,non_leaf_only=True)
        ltree.sons(3,leaf_only=True)
        ltree.sons(3,non_leaf_only=True)
        
        ltree.descendant_paths(3)
        ltree.descendants(3)
        ltree.descendant_paths(3,from_lv=3)
        ltree.descendants(3,from_lv=3)
        ltree.descendant_paths(3,from_lv=2,to_lv=2)
        ltree.descendants(3,from_lv=2,to_lv=2)
        ltree.descendant_paths(3,leaf_only=True)
        ltree.descendants(3,leaf_only=True)
        ltree.descendant_paths(3,non_leaf_only=True)
        ltree.descendants(3,non_leaf_only=True)
        
        ltree.ancestor_paths(3,1,0)
        ltree.ancestors(3,1,0)
    '''
    def __init__(self,l):
        self.list = l
        self.desc = scan(l)
        self.desc,self.pathloc_mapping,self.locpath_mapping= fullfill_descendants_info(self.desc)
        self.depth = self.desc.__len__()
        self.maxLevelWidth = max(array_map(self.desc,len))
        self.flatWidth = self.desc[0][0]['flat_len']
        self.total = self.desc[0][0]['leaf_descendant_paths'].__len__() + self.desc[0][0]['non_leaf_descendant_paths'].__len__()
        self.trace = self.tree(show=False)
        self.prevSibling = self.lsib
        self.prevSibPath = self.lsib_path
        self.nextSibling = self.rsib
        self.nextSibPath = self.rsib_path
        self.precedingSibPaths = self.preceding_sib_paths
        self.precedingSibs = self.preceding_sibs
        self.followingSibPaths = self.following_sib_paths
        self.followingSibs = self.following_sibs
        self.someSibPaths = self.some_sib_paths
        self.someSibs = self.some_sibs
        self.whichSibPath = self.which_sib_path
        self.whichSib = self.which_sib
        self.showlog = None
    def __repr__(self):
        s = table(self.list,self.depth,no_return=0)
        showl = s.split('\n')
        self.showlog = showl
        return(s)
    def tree(self,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        if('show' in kwargs):
            show = kwargs['show']
        else:
            show = True
        lpls = copy.deepcopy(self.desc[0][0]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[0][0]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            if(cond1 & cond2):
                nrslt.append(pl)
            else:
                pass
        showl = array_map(nrslt,pl_to_bracket_str)
        nrslt,showl = bat_sort(nrslt,nrslt,showl)
        if(show):
            for_eachv(showl,print)
            self.showlog = ['tree -'+prompt+' :']
            self.showlog.extend(showl)
        else:
            pass
        return(nrslt)
    def level(self,lvnum,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        desc_level = self.desc[lvnum]
        lpls = []
        nlpls = []
        for i in range(0,desc_level.__len__()):
            desc = desc_level[i]
            pathlist = copy.deepcopy(desc['path'])
            if(desc['leaf']):
                lpls.append(pathlist)
            else:
                nlpls.append(pathlist)
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        showl = array_map(rslt,pl_to_bracket_str)
        rslt,showl = bat_sort(rslt,rslt,showl)
        for_eachv(showl,print)
        self.showlog = ['level -' +prompt+' ' +str(lvnum)+' :']
        self.showlog.extend(showl)
    def flatten(self):
        lpls = self.tree(leaf_only=True,show=False)
        flat = array_map(lpls,get_via_pl2,self.list)
        return(flat)
    def include(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        try:
            get_via_pl(self.list,pl)
        except:
            return(False)
        else:
            return(True)
    def __getitem__(self,*sibseqs):
        #this is a trick for __getitem__
        sibseqs = sibseqs[0]
        return(get_via_sibseqs(self.list,*sibseqs))
    def loc(self,*sibseqs):
        pl = list(sibseqs)
        pk = tuple(pl)
        loc = self.pathloc_mapping[pk]
        return(list(loc))
    def path(self,locx,locy):
        loc = (locx,locy)
        pl = self.locpath_mapping[loc]
        pl = list(pl)
        return(pl)
    def path2loc(self,pathlist):
        pl = pathlist
        pk = tuple(pl)
        loc = self.pathloc_mapping[pk]
        return(list(loc))
    def loc2path(self,loc):
        loc = tuple(loc)
        pl = self.locpath_mapping[loc]
        pl = list(pl)
        return(pl)
    @classmethod
    def showroute(cls,arr):
        def arrow(ele):
            return(str(ele)+' ->')
        arr = array_map(arr,arrow)
        for_eachv(arr,print)
        return(arr)
    def dig(self,howmanysteps=None):
        if(howmanysteps):
            pass
        else:
            howmanysteps = self.total
        self.showlog = ['dig -steps '+howmanysteps+' :']
        self.showlog.extend(self.showroute(self.trace[:howmanysteps]))
        return(self.trace[:howmanysteps])
    def parent(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        loc = self.path2loc(pl)
        ppl = self.desc[loc[0]][loc[1]]['parent_path']
        value = get_via_pl(self.list,ppl)
        return(value)
    def parent_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        return(ppl)
    def son_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_son_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_son_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        rslt,= bat_sort(rslt,rslt)
        return(rslt)
    def sons(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_son_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_son_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        rslt,= bat_sort(rslt,rslt)
        rslt = array_map(rslt,get_via_pl2,self.list)
        return(rslt)
    def descendant_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            if(cond1 & cond2):
                nrslt.append(pl)
            else:
                pass
        nrslt, = bat_sort(nrslt,nrslt)
        return(nrslt)
    def descendants(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        lpls = copy.deepcopy(self.desc[locx][locy]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[locx][locy]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            if(cond1 & cond2):
                nrslt.append(pl)
            else:
                pass
        nrslt, = bat_sort(nrslt,nrslt)
        nrslt = array_map(nrslt,get_via_pl2,self.list)
        return(nrslt)
    @classmethod
    def ancestlize(cls,l,**kwargs):
        length = l.__len__()
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = length - 2
        nrslt = []
        si = from_lv - 1
        ei = to_lv + 1
        for i in range(si,ei):
            pl = l[:(i+1)]
            nrslt.append(pl)
        return(nrslt)
    def ancestor_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        p = copy.deepcopy(self.desc[locx][locy]['path'])
        anps = self.ancestlize(p,from_lv=from_lv,to_lv=to_lv)
        return(anps)
    def ancestors(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        p = copy.deepcopy(self.desc[locx][locy]['path'])
        anps = self.ancestlize(p,from_lv=from_lv,to_lv=to_lv)
        ans = array_map(anps,get_via_pl2,self.list)
        return(ans)
    def lsib_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lsibp = copy.deepcopy(self.desc[locx][locy]['lsib_path'])
        return(lsibp)
    def lsib(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lsibp = copy.deepcopy(self.desc[locx][locy]['lsib_path'])
        lsibv = get_via_pl(self.list,lsibp) 
        return(lsibv)
    def rsib_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rsibp = copy.deepcopy(self.desc[locx][locy]['rsib_path'])
        return(rsibp)
    def rsib(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rsibp = copy.deepcopy(self.desc[locx][locy]['rsib_path'])
        rsibv = get_via_pl(self.list,rsibp) 
        return(rsibv)
    def lcin_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lcinp = copy.deepcopy(self.desc[locx][locy]['lcin_path'])
        return(lcinp)
    def lcin(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        lcinp = copy.deepcopy(self.desc[locx][locy]['lcin_path'])
        lcinv = get_via_pl(self.list,lcinp) 
        return(lcinv)
    def rcin_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rcinp = copy.deepcopy(self.desc[locx][locy]['rcin_path'])
        return(rcinp)
    def rcin(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = pl.__len__() - 2
        locx,locy = tuple(self.path2loc(pl))
        rcinp = copy.deepcopy(self.desc[locx][locy]['rcin_path'])
        rcinv = get_via_pl(self.list,rcinp) 
        return(rcinv)
    def sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        return(sibps)
    def sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibvs = array_map(sibps,get_via_pl2,self.list)
        return(sibvs)
    def preceding_sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            return(sibps)
        else:
            return(sibps[:seq])
    def preceding_sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            pre = sibps
        else:
            pre = sibps[:seq]
        sibvs = array_map(pre,get_via_pl2,self.list)
        return(sibvs)
    def following_sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            follow = sibps
        else:
            follow = sibps[(seq+1):]
        return(follow)
    def following_sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        try:
            seq = sibps.index(pl)
        except:
            follow = sibps
        else:
            follow = sibps[(seq+1):]
        sibvs = array_map(follow,get_via_pl2,self.list)
        return(sibvs)
    def some_sib_paths(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        #here "some" mean "seqs"
        some = kwargs['some']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        #sibps = select_some(sibps,some)
        sibps = select_seqs(sibps,some)
        return(sibps)
    def some_sibs(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        #here some mean seqs
        some = kwargs['some']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        #sibps = select_some(sibps,some)
        sibps = select_seqs(sibps,some)
        sibvs = array_map(sibps,get_via_pl2,self.list)
        return(sibvs)
    def which_sib_path(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        which = kwargs['which']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibp = sibps[which]
        return(sibp)
    def which_sib(self,*sibseqs,**kwargs):
        if('pathlist' in kwargs):
            pl = kwargs['pathlist']
        else:
            pl = list(sibseqs)
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        which = kwargs['which']
        locx,locy = tuple(self.path2loc(pl))
        ppl = self.desc[locx][locy]['parent_path']
        seq = self.desc[locx][locy]['sib_seq']
        sibps = self.son_paths(pathlist=ppl,leaf_only=leaf_only,non_leaf_only=non_leaf_only)
        sibp = sibps[which]
        sibv = get_via_pl(self.list,sibp)
        return(sibv)
    def search(self,value,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth -1
        lpls = copy.deepcopy(self.desc[0][0]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[0][0]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            v = get_via_pl(self.list,pl)
            cond3 = (v == value)
            if(cond1 & cond2 & cond3):
                nrslt.append(pl)
            else:
                pass
        showl = array_map(nrslt,pl_to_bracket_str)
        nrslt,showl = bat_sort(nrslt,nrslt,showl)
        if(type(value)==type("")):
            vstr = '"' + str(value) + '"'
        else:
            vstr = str(value)
        self.showlog = ['search '+ vstr + ' -'+prompt+' :']
        self.showlog.extend(showl)
        for_eachv(showl,print)
        return(nrslt)
    def cond_search(self,**kwargs):
        ###
        cond_func = kwargs['cond_func']
        if('cond_func_args' in kwargs):
            cond_func_args = kwargs['cond_func_args']
        else:
            cond_func_args = []
        ###
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
            prompt = 'leaf_only'
        else:
            leaf_only = False
            prompt = ''
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
            prompt = 'non_leaf_only'
        else:
            non_leaf_only = False
            prompt = ''
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth -1
        lpls = copy.deepcopy(self.desc[0][0]['leaf_descendant_paths'])
        nlpls = copy.deepcopy(self.desc[0][0]['non_leaf_descendant_paths'])
        if(leaf_only):
            rslt = lpls
        elif(non_leaf_only):
            rslt = nlpls
        else:
            rslt = lpls+nlpls
        nrslt = []
        nvs = []
        for i in range(0,rslt.__len__()):
            pl = rslt[i]
            length = pl.__len__()
            cond1 = (length >= from_lv)
            cond2 = (length <= to_lv)
            v = get_via_pl(self.list,pl)
            cond3 = cond_func(v,pl,*cond_func_args)
            if(cond1 & cond2 & cond3):
                nrslt.append(pl)
                nvs.append(v)
            else:
                pass
        def showlog_append(ele1,ele2,*args):
            return(ele1 + ' : ' + str(ele2))
        showl = array_map(nrslt,pl_to_bracket_str)
        showl2 = array_map2(showl,nvs,map_func=showlog_append)
        nrslt,showl = bat_sort(nrslt,nrslt,showl)
        func_name = cond_func.__name__
        vstr = 'ele_value,ele_pathlist,' +str(cond_func_args)[1:-1]
        vstr = func_name + '(' + vstr + ')'
        self.showlog = ['search '+ vstr + ' -'+prompt+' :']
        self.showlog.extend(showl2)
        for_eachv(showl,print)
        return(nrslt)


