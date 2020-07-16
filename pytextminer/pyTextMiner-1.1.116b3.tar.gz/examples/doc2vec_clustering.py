from collections import namedtuple

from sklearn.cluster import KMeans

from py_doc2vec.doc2vecModel import Doc2VecTrainer
import logging
import pyTextMiner as ptm
import csv
import sys
from py_document_clustering.documentclustering import DocumentClustering
import matplotlib.pyplot as plt

corpus = []
filename = '../data/news_articles_201701_201812.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            title = row[3]
            content = row[4]
            print(title + " : " + content)
            corpus.append(title + ' ' + content)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

mecab_path = 'C:\\mecab\\mecab-ko-dic'
# stopwords file path
stopwords = '../stopwords/stopwordsKor.txt'
pipeline = ptm.Pipeline(ptm.splitter.KoSentSplitter(),
                            ptm.tokenizer.MeCab(mecab_path),
                            ptm.lemmatizer.SejongPOSLemmatizer(),
                            ptm.helper.SelectWordOnly(),
                            ptm.helper.StopwordFilter(file=stopwords))

result = pipeline.processCorpus(corpus)
TaggedDocument = namedtuple('TaggedDocument', 'tags words')

documents=[]
i = 0
for doc in result:
    document = []
    for sent in doc:
        for word in sent:
            document.append(word)
    documents.append(TaggedDocument(['doc_' + str(i)], document))
    i += 1
    if i % 10000 == 0:
        logging.info('Loaded %s documents', i)

algorithm = 'pv_dma'
# ignores all words with total frequency lower than this
vocab_min_count = 10
# word and document vector siz
dim = 100
# window size
window = 5
#number of training epochs
epochs = 20
# initial learning rate
alpha = 0.025
# learning rate will linearly drop to min_alpha as training progresses
min_alpha = 0.001
# number of cores to train on
cores = 2
# number of cores to train on
train = True

output_base_dir='./tmp'

doc2vec = Doc2VecTrainer()
logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', level=logging.INFO)
doc2vec.run(documents, output_base_dir=output_base_dir, vocab_min_count=vocab_min_count,
            num_epochs=epochs, algorithm=algorithm, vector_size=dim, alpha=alpha,
            min_alpha=min_alpha, train=train, window=window, cores=cores)

kmeans_model = KMeans(n_clusters=3, max_iter=100)

'''
X = kmeans_model.fit(d2v_model.docvecs.doctag_syn0)
labels=kmeans_model.labels_.tolist()
l = kmeans_model.fit_predict(d2v_model.docvecs.doctag_syn0)
pca = PCA(n_components=2).fit(d2v_model.docvecs.doctag_syn0)
datapoint = pca.transform(d2v_model.docvecs.doctag_syn0)

label1 = ['#FFFF00', '#008000', '#0000FF', '#800080']
color = [label1[i] for i in labels]
plt.scatter(datapoint[:, 0], datapoint[:, 1], c=color)
centroids = kmeans_model.cluster_centers_
centroidpoint = pca.transform(centroids)
plt.scatter(centroidpoint[:, 0], centroidpoint[:, 1], marker='^', s=150, c='#000000')
plt.show()
'''
