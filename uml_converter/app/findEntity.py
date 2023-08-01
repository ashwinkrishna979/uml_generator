import nltk
import pandas as pd
import pickle
import os


def findEntity(text):
    
    word2index={'RB': 0, 'WDT': 1, 'PRP$': 2, 'NN': 3, 'IN': 4, 'VBZ': 5, 'CC': 6, 'JJS': 7, 'RBR': 8, 'MD': 9, 'NNS': 10, 'VBN': 11, 'VB': 12, 'DT': 13, 'TO': 14, 'JJR': 15, 'PRP': 16, 'WP': 17, 'VBD': 18, 'RP': 19, 'JJ': 20, 'WRB': 21, 'CD': 22, 'VBG': 23, 'VBP': 24, 'PDT': 25}
    label2index={'none': 0, 'u': 1, 'a': 2}
    test_sentence = str(text).lower().split()
    test_sentence = nltk.pos_tag(test_sentence)
    test_sentence=[i[1] for i in test_sentence]
    test_sentence=[word2index.get(word, 0) for word in test_sentence ]

    c=[]
    count=0
    for word in test_sentence:
        c.append(count)
        count+=1

    data_dict = {
        'ind': c,
        'feat': test_sentence,
    }
    
    dataset = pd.DataFrame(data_dict,index=None)
    model_path = os.path.join(os.path.dirname(__file__), 'knn_model.sav')

    loaded_model = pickle.load(open(model_path, 'rb'))

    output=loaded_model.predict(dataset)

    return output


