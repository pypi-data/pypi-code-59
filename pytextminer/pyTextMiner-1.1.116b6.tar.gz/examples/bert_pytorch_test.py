
import pytorch_pretrained_bert as ppb
import torch

#bert multi-lingual model
#https://github.com/google-research/bert/blob/master/multilingual.md

device = torch.device("cpu")
model = ppb.BertModel.from_pretrained('bert-base-multilingual-cased')
model.to(device)