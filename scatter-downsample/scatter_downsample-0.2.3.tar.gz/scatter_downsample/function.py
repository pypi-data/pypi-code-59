import numpy as np 
import matplotlib.pyplot as plt
from .helpers import reshape_array,pca,make_filters,apply_filters
import warnings
import string
warnings.simplefilter(action='ignore',category=FutureWarning)


# method 1: downsample by mean and standard deviation
def down2withSD(I,L,filter=2):

  #initialize labels
    if not L:
        L = ["r","g","b"]

  #copy the original image
    n = np.array(I.shape)
    nd = np.copy(n)
    nd[:2] = nd[:2]//2
    J = np.zeros(nd)
    K = np.zeros(nd)
  #apply averaging
    for i in range(2):
        for j in range(2):
            J += I[i:nd[0]*2:2, j:nd[1]*2:2,:] / 4.0

  #filtering out the channels with 2 1's
    rmv = [L.index(x) for x in L if x.count("1")>(filter-1)]
    Im = np.delete(I, rmv, axis=2)

  #calculate standard deviations
    Im = reshape_array(Im)
    K = np.std(Im,axis=3)

  #concatenate mean and standard deviation arrays
    ret = np.concatenate((J,K), axis=2)

  #each iteration, append to labels
    label = [x+"0" for x in L] + [x+"1" for x in L if x.count("1")<filter]

    return ret, label

# method 2: downsample with 3 direction
def down2withDirection(I,L,F=2):
  #initialize labels
    if type(L) is not list:
        L=L.tolist()
    if not L:
        L = ["r","g","b"]

  #copy the original image
    n = np.array(I.shape)
    nd = np.copy(n)
    nd[:2] = nd[:2]//2
    I_1 = np.zeros(nd)
    I_2= np.zeros(nd)
    I_3 = np.zeros(nd)
    I_4= np.zeros(nd)
    a=nd[0]*2
    b=nd[1]*2

  #apply averaging (mean)
    for i in range(2):
        for j in range(2):
            I_1 += I[i:a:2, j:b:2,:] / 4.0 
    rmv = [L.index(x) for x in L if (x.count("1") + x.count("2") + x.count("3") + x.count("4"))>(F-1)]
    Im = np.delete(I, rmv, axis=2)

  #adding directions
  #derivative in the (1,0) direction (x direction), label: 2
    I_2 = abs(Im[0:a:2,0:b:2,:]*0.25 - Im[1:a:2,0:b:2,:]*0.25 + Im[0:a:2,1:b:2,:]*0.25 - Im[1:a:2,1:b:2,:]*0.25)
  #derivative in the (1,1) direction, label: 3
    I_3 = abs(Im[0:a:2,0:b:2,:]*0.25 + Im[1:a:2,0:b:2,:]*0.25 - Im[0:a:2,1:b:2,:]*0.25 - Im[1:a:2,1:b:2,:]*0.25)
  #derivative in the (0,1) direction (y direction), label: 4
    I_4 = abs(Im[0:a:2,0:b:2,:]*0.25 - Im[1:a:2,0:b:2,:]*0.25 - Im[0:a:2,1:b:2,:]*0.25 + Im[1:a:2,1:b:2,:]*0.25)

  #concatenate channels
    ret = np.concatenate((I_1, I_2, I_3, I_4), axis=2)
  #update labels
    label = [x+"0" for x in L] +[x+"2" for x in L if (x.count("1") + x.count("2") + x.count("3") + x.count("4"))<F]+[x+"3" for x in L if (x.count("1") + x.count("2") + x.count("3") + x.count("4"))<F]+[x+"4" for x in L if (x.count("1") + x.count("2") + x.count("3") + x.count("4"))<F]

  #if a label includes a 2 or 4, translate every 2 to 4 and vice versa
  #compare with original labels, if they are the same, store the indices of this pair in a list
    label_list =[]
    label_copy = label.copy()
    for i in label_copy:
        label_cut = label[int(label.index(i)+1)::]
        if '2' in i or '4' in i:
            translated = i.translate(str.maketrans("24", "42"))
            if translated in label_cut:
                label_list.append([label_copy.index(i), (label_cut.index(translated)+label_copy.index(i)+1)])
  
  #take two channels and find average
  #insert average into one and delete the other (delete labels as well)
    del_label = []
    for c1, c2 in label_list:
        ret[:,:,c1] = (ret[:,:,c1] + ret[:,:,c2])/2
        del_label.append(c2)
    label = np.delete(label,del_label)
    ret = np.delete(ret,del_label,axis=2)

    return ret, label

# method 3 and 4: gaussian filter downsampling
def gaussianDownsampling(I,L,F=2,directions=4,option=1):
  '''
  Downsampling with Gaussian filters
  option 1 = high pass filters, take absolute value, low pass filter, take absolute value
  option 2 = low pass filter, take absolute value
  '''

  #convert labels to list
  if type(L) is not list:
    L=L.tolist()
  label = L
  I_cp = I.copy()

  #remove labels with F characters that are not 0
  rmv = [L.index(x) for x in L if (len(x)-x.count("0"))>F]
  I_cp = np.delete(I_cp, rmv, axis=2)

  # make filters
  lp,hp = make_filters(n_directions=directions)    

  #option 1 - apply high pass filters, then low pass filter
  if option == 1:
    #apply high pass filters, take absolute value
    Ifiltered = np.abs(apply_filters(I_cp,hp))
    Ifiltered = Ifiltered.reshape(Ifiltered.shape[0],Ifiltered.shape[1],Ifiltered.shape[2]*directions)
    #concatenate with original
    Ifiltered = np.concatenate((I, Ifiltered), axis=-1)
    #apply low pass filter, take absolute value
    Ifiltered = np.abs(apply_filters(Ifiltered,lp))
    Ifiltered = Ifiltered.reshape(Ifiltered.shape[0],Ifiltered.shape[1],Ifiltered.shape[2])
    #downsample with slicing
    Ifiltered = Ifiltered[::2,::2,:]
    #update labels
    for i in range(int(hp.shape[2])+1):
      if i == 0:
        label =[x+"0" for x in L]
      else: 
        label += [x + str(i) for x in L if (len(x)-x.count("0"))<(F+1)]

  #option 2 - only apply low pass filter
  else:
    Ifiltered = np.abs(apply_filters(Ifiltered,lp))
    label = [x+"0" for x in L]
  return Ifiltered, label

def ScatterDown(I,ndown2,filtered_std=2,method=1,dirt=2):
    I = plt.imread(I)
    I = I.astype(float)
    I /= 255.0
    Id = np.copy(I)
    L = ["r","g","b"]

    if method == 1:
        for n in range(ndown2):
            Id,L = down2withSD(Id,L,filtered_std)
    elif method == 2:
        for n in range(ndown2):
            Id,L = down2withDirection(Id,L,filtered_std)
    elif method == 3:
        for n in range(ndown2):
            Id,L = gaussianDownsampling(Id,L,filtered_std,dirt,option=1)
    elif method == 4:
        for n in range(ndown2):
            Id,L = gaussianDownsampling(Id,L,filtered_std,dirt,option=2)
    
    Ip = pca(Id)
    f,ax = plt.subplots()
    ax.imshow(Ip[...,0:3])
    ax.set_title('First three channels')
    f.savefig('output.jpg')

  # f,ax = plt.subplots() 
  # ax.imshow(Ip[...,3:6])
  # ax.set_title('Second three channels')

  # f,ax = plt.subplots()
  # ax.imshow(Ip[...,6:9])
  # ax.set_title('Third three channels')

  # f,ax = plt.subplots()
  # ax.imshow(Ip[...,9:12])
  # ax.set_title('Last three channels')

    return Id,L,f

def Rotations(I,L):
  #if a label includes a 2 or 4, translate every 2 to 4 and vice versa
  #compare with original labels, if they are the same, store the indices of this pair in a list
  label_list =[]
  ret = I.copy()
  label_copy = L.copy()
  label = L.copy()
  for i in label_copy:
    label_cut = label[int(label.index(i)+1)::]
    if '2' in i or '4' in i:
      translated = i.translate(str.maketrans("24", "42"))
      if translated in label_cut:
        label_list.append([label_copy.index(i), (label_cut.index(translated)+label_copy.index(i)+1)])
  
  #take two channels and find average
  #insert average into one and delete the other (delete labels as well)
  del_label = []
  for c1, c2 in label_list:
    ret[:,:,c1] = (ret[:,:,c1] + ret[:,:,c2])/2
    del_label.append(c2)
  label = np.delete(label,del_label)
  ret = np.delete(ret,del_label,axis=2)
  # if type(label) is not list:
  #   label=label.tolist()
  
  #print(label)
  # print(len(label))
  # print(ret.shape)
  return ret, label

def gaussianRotations(I,L,n_directions=4):
    '''
    Identify channels that are rotations of each other and average these channels into one
    Generate all possible rotations for each label and compare with the original labels to find rotations
    '''
    #initialize lists and make copies 
    label_list =[]
    del_labels=[]
    return_label = L.copy()
    return_arr = I.copy()

    #generate all possible rotations for each label
    for label in L:
        temp_list = []
        val = label
        for n in range(n_directions):
            s = str()
            for char in val:
                if char != val[0] and char != '0':
                    char = str(int(char)+1%n_directions)
                    if int(char) > n_directions:
                        char = 1
                s += str(char)
            temp_list.append(s)
            val = s
        #if they are not all the same (all zeros)
        if (temp_list.count(temp_list[0]) != len(temp_list)):
            del_labels.append(list(sorted(temp_list)))
    del_labels = [tuple(i) for i in np.unique(del_labels, axis=0)]

    #get list of generated rotations that are in the actual labels
    rotate_labels = []
    b_set = set(L) 
    for i in del_labels:
        a_set = set(i) 
        if len(a_set.intersection(b_set)) > 0: 
            rotate_labels.append(sorted((a_set.intersection(b_set))))

    #find the index of the labels of the channels
    for i in rotate_labels:
        l = []
        if len(i)>1:
            for j in i:
                l.append(L.index(j))
            if l not in label_list:
                label_list.append(l)

    #take channels in the same equivalence class and find average
    #insert average into one and delete the others
    del_label = [] 
    for k in label_list:
        for i in k:
            return_arr[:,:,k[0]]= return_arr[:,:,k[0]]+return_arr[:,:,i]
            if i != k[0] and i not in del_label:
                del_label.append(i)
        return_arr[:,:,k[0]] = (return_arr[:,:,k[0]])/n_directions

    #remove excess channels and labels
    return_label = np.delete(return_label,del_label)
    return_arr = np.delete(return_arr,del_label,axis=2)

    return return_arr, return_label

def gaussianFlipped(Id,L,n_directions=4):
    '''
    Identify channels that are flipped versions of each other, average each pair into one channel
    '''

    label_list =[]
    return_arr = Id.copy()
    return_label = L.copy()
    increments = []
    #Convert labels to increments
    for label in L:
        #get index of all non-zero characters in label
        n_zeros = [idx for idx, val in enumerate(label) if val != '0' and val.isdigit()]
        #get index of all zeros in label 
        zeros = [idx for idx, val in enumerate(label) if val == '0']
        #put place holders for zeros
        shift = list(label)
        for i in zeros:
            shift[i] = 'z'
        #for each nonzero character except the first, replace that position with an increment
        for i in n_zeros:
            if i != n_zeros[0]:
                #ensure each increment is less than directions/2
                if (int(label[i])-int(prev)) > int(n_directions/2):
                    shift[i] = str((int(label[i])-int(prev))-n_directions)
                elif (int(label[i])-int(prev)) < int(-(n_directions/2)):
                    shift[i] = str((int(label[i])-int(prev))+n_directions)
                else:
                    shift[i] = str(int(label[i])-int(prev))
            prev = label[i]
        #add the increment version of all labels to a list
        if shift not in increments:
            increments.append(shift)

    #for each increment label, flip each digit starting at the second
    #search the rest of the increment labels to find an identical one, or a flipped rotation of one
    #get the index of these two labels and store them in a list
    for idx, label in enumerate(increments):
        if (len(increments)-idx)>1:
            #get the increment labels after label
            label_cut = increments[(idx+1)::]
            #get the position of the first digit
            j = [i for i in range(len(label)) if label[i].isdigit()==True]
            if len(j)>0:
                j = j[0]
            #flip every digit after the first
            flipped_label = label.copy()
            for idx, val in enumerate(label):
                if idx != j and val.isalpha()==False:
                    flipped_label[idx] = str((int(flipped_label[idx]))*(-1))
            
            temp_label = flipped_label.copy()
            next = flipped_label.copy()
            #get the rotations of the flipped label
            for i in range(n_directions-1):
                for idx,val in enumerate(flipped_label):
                    if idx == j:
                        temp_label[j] = str((int(next[j])+1)%n_directions)
                        #special case - roll over 0 -> n_directions
                        if temp_label[j] == '0':
                            temp_label[j] = str(n_directions)
                        #if the rotated label is in the list of labels, store the indexes
                        if temp_label in label_cut:
                            label_list.append([increments.index(label), increments.index(temp_label)])
                next = temp_label
            #if the flipped label is in the list of labels, store the indexes
            if flipped_label in label_cut:
                label_list.append([increments.index(label), increments.index(flipped_label)])

    #take two channels and find average
    #insert average into the first and delete the other (both channel and label)
    del_labels = []
    for c1, c2 in label_list:
        return_arr[:,:,c1] = (return_arr[:,:,c1] + return_arr[:,:,c2])/2
        del_labels.append(c2)
    return_label = np.delete(return_label,del_labels)
    return_arr = np.delete(return_arr,del_labels,axis=2)
    
    return return_arr, return_label

