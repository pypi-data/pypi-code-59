import pandas as pd
import jsonlines

def read_io(filepath, source='rasa_nlu.md', target='rasa_nlu'):
    ## available options
    # rasa_nlu.md, rasa_nlu

    if source == 'rasa_nlu.md' and target == 'rasa_nlu':
        
        # from rasa.importers.rasa import RasaFileImporter
        # importer = RasaFileImporter(None, None, [filepath])
        # nludata = await importer.get_nlu_data()
        from typing import Iterable , Text
        from rasa.nlu.training_data import TrainingData
        from rasa.nlu.training_data import loading
        language = 'en'
        training_datas = [loading.load_data(nlu_file, language) for nlu_file in [filepath]]
        nludata = TrainingData().merge(*training_datas)
        nludata.fill_response_phrases()

        #############################################################

        nludata = pd.read_json(nludata.nlu_as_json())
        nludata = pd.DataFrame(nludata['rasa_nlu_data']['common_examples'])

        return nludata
    elif source == 'doccano.jsonl' and target == 'finie':
        dftemp = []
        intent = filepath
        with jsonlines.open(filepath , mode='r') as f:

            _f_jsonlines = []
            for line in f:
                _f_jsonlines.append(line)
            _f_jsonlines = sorted(_f_jsonlines, key=lambda x: x['id']) if 'id' in _f_jsonlines[0] else _f_jsonlines

            for line in _f_jsonlines:
                temp = []
                line_labels = sorted(line['labels'], key=lambda x:x[0])
                for l in line_labels:
                    temp.append({'label': l[2], 'word':line['text'][l[0]:l[1]], 'start':l[0], 'end':l[1]})

                assert line['text'] == " ".join(t['word'] for t in temp)
                dftemp.append((line['text'], temp, intent))

        df = pd.DataFrame(dftemp, columns=['Sentence', 'Labels', 'Intent'])
        return df

def write_io(inputs, filepath, source='finie', target='rasa_nlu.md'):

    if source == 'finie' and target == 'doccano.jsonl':
        df = inputs
        with open(filepath, 'w') as f:
            # {"text": "Peter Blackburn", "labels": [ [0, 15, "PERSON"] ]}
            # {"text": "EU rejects German call to boycott British lamb.", "labels": [ [0, 2, "ORG"], [11, 17, "MISC"], ... ]}
            for idx, row in df.iterrows():
                d = row['Labels']

                temp0 = ''
                temp1 = []
                offset = 0
                token_count = len(d)
                lidx = 0
                while lidx < token_count:
                    l = d[lidx]
                    
                    word = l['word']
                    label = l['label']

                    # temp1.append([offset, offset+len(word), label])
                    temp1.append([l['start'], l['end'], label])
                    
                    if lidx < token_count -1:
                        if l['end'] != d[lidx+1]['start']:
                            temp0 += word + " "
                        else:
                            temp0 += word
                    else:
                        temp0 += word
                    # temp0 += word + " "
                    offset += len(word) +1
                    
                    lidx += 1
                
                temp0 = temp0.strip()
                line = json.dumps({"text":temp0, "labels":temp1})
        
                f.write(line + '\n')
    
    elif source == 'rasa_nlu_ner' and target == 'rasa_nlu.md':
        def generate_entity(token, roles=['to', 'from'], delimiter='-'):
    
            def generate_format(word, entity, role, O='O'):
                
                if entity == O:
                    return word
                
                if role:
                    return f'[{word}]{{"entity":"{entity}", "role":"{role}"}}'
                else:
                    return f'[{word}]{{"entity":"{entity}"}}'
            
            result = None
            
            label = token['label']
            label_parts = label.split(delimiter)
            
            matched_roles = list(set(label_parts) & set(roles) )
            
            if len(matched_roles) == 0:
                result = generate_format(token['word'], label , None)
            elif len(matched_roles) == 1:
                templabel = delimiter.join([l for l in label_parts if l not in matched_roles])
                result = generate_format(token['word'], templabel, matched_roles[0])
            else:
                print(label)
                print(matched_roles)
                assert "Number of matched roles is not 1" == 0
                
            assert result != None
            
            return result

        def write_df_to_file(f, df, keep_examples_without_entity=True):
            
            for entry, group in df.groupby('Intent'):
                f.write('## intent:' + entry + '\n')
                
                if 'Labels' in df.columns:

                    for text in group['Labels'].values:
                        temp = ""
                        for token in text:
                            temp += generate_entity(token) + " "

                        if ']{"entity":"' in temp or keep_examples_without_entity:
                            text = temp
                            f.write('- ' + text.strip() + '\n')
                else:
                    for text in group['Text'].values:
                        f.write('- ' + text.strip() + '\n')
                    
                f.write('\n')

        df = inputs
        with open(filepath,'w') as f:   
            write_df_to_file(f, df)

            if len(df['Intent'].unique()) == 1:
                
                f.write('## intent:' + 'dummy' + '\n')
                f.write('- ' 'dummy 1' + '\n')
                f.write('- ' 'dummy 2' + '\n')
                f.write('- ' 'dummy 3' + '\n')
                f.write('- ' 'dummy 4' + '\n')
                f.write('- ' 'dummy 5' + '\n')
                f.write('- ' 'dummy 6' + '\n')
                f.write('\n')
            
            #     f.write(regexconfig)
            #     f.write('\n')
            pass
    elif source == 'rasa_nlu_base' and target == 'rasa_nlu.md':
        train = inputs
        with open(filepath ,'w') as f:

            for entry, group in train.loc[:60].groupby('Intent'):
                f.write('## intent:' + entry + '\n')
                
                for text in group['Text'].values:
                    f.write('- ' + text.strip() + '\n')
                    
                f.write('\n')

    elif source == 'rasa_story_base' and target == 'rasa_story.md':
        train = inputs
        with open(filepath,'w') as f:
        #     f.write('text1')

            for entry, group in train.groupby('Intent'):
                f.write('## ' + entry + '\n')
                f.write('* ' + entry + '\n')
                f.write('    - utter_group_' + entry + '\n')
                
                f.write('\n')

    elif source == 'rasa_domain_base' and target == 'rasa_domain.md':
        train = inputs

        # http://www.yamllint.com/

        escapecharregex = r'\\.*?\s'
        with open(filepath ,'w') as f:
        #     f.write('text1')

            f.write('intents:\n')
            for entry, group in train.groupby('Intent'):
                f.write('- ' + entry + '\n')
                
            f.write('responses:\n')
            for entry, group in train.groupby('Intent'):
                f.write('  utter_group_' + entry + ':\n')
                
                answer =  group['Answer'].values[0]
                # if("Sizi anlamaya çalışıyorum." in answer):
                #     print(answer)
                #     print(type(answer))
                #     print(re.sub(emojiregex, " ", str(answer)))
                # text = re.sub(escapecharregex, " ", answer)
                text = answer.replace('\\', "\\\\")
                text = text.replace('"', '\\"')
                f.write('  - text: "' + text + '"\n\n')
                
                
            f.write('\n')
            
            f.write('actions:\n')
            f.write('- action_request_example_1\n')
            f.write('\n')
            
            f.write('session_config:\n')
            f.write('  session_expiration_time: 0.0\n')
            f.write('  carry_over_slots_to_new_session: true\n')
            f.write('\n')

def convert_io(inputs, source='finie', target='spacy'):
    
    ## available options
    # finie - spacy
    # spacy - finie

    if source == 'finie' and target == 'spacy':

        if str(type(inputs)) == str(type(pd.DataFrame())):
            df = inputs

        import spacy
        from spacy.lang.tr import Turkish as SpacyTurkish
        from spacy.tokens import Span, Token, Doc

        trnlp = SpacyTurkish()
        sdocs = []
        for idx, row in df.iterrows():
            tokens = [ann['word'] for ann in row['Labels']]
            spaces = [row['Labels'][i]['end'] != row['Labels'][i+1]['start'] for i in range(0, len(tokens)-1)] + [False]

            sdoc = spacy.tokens.doc.Doc(trnlp.vocab, words=tokens, spaces=spaces)
            for idx, ann in enumerate(row['Labels']):
                sdoc.ents += (Span(sdoc, idx, idx+1, label=ann['label']), )
            sdocs.append(sdoc)
        return sdocs

    elif source == 'spacy' and target == 'finie':
        spacy_docs = None
        class_name = None
        class_column_name = 'label'

        if str(type(inputs)) == str(type(['a'])):
            spacy_docs = inputs
        elif str(type(inputs)) == str(type({'a':'b'})):
            if 'spacy' in inputs:
                spacy_docs = inputs['spacy']
            else:
                assert 1 == 0
            if 'label' in inputs:
                class_name = inputs['label']
                class_column_name = 'Label'
            elif 'intent' in inputs:
                class_name = inputs['intent']
                class_column_name = 'Intent'
        
        spacy_docs_temp = [[{'label':t.ent_type_,'word':t.text, 'start': t.idx, 'end': t.idx + len(t.text),} for t in s] for s in spacy_docs]
        df = pd.DataFrame({'Labels':spacy_docs_temp})
        df[class_column_name] = class_name

        return df

    elif source == 'rasa_nlu' and target == 'finie':

        from spacy.lang.tr import Turkish as SpacyTurkish
        from pyspace.nlp.toolkit.spacy import SpacyMatcherEntityUpdater, SpacyPostTokenizer, SpacyTokenizer, SpacyRegexReplaceNormalizer, SpacyWhitespaceNormalizer, SpacyEndPunctuationNormalizer

        df = inputs.copy()

        nlp = SpacyTurkish()
        nlp.tokenizer = lambda x: x
        nlp.add_pipe(SpacyTokenizer(nlp))
        nlp.add_pipe(SpacyPostTokenizer(merge_bool=True))

        finie_formatted_entities = []
        for idx, row in df.iterrows():
            text = row['text']
            entities = row['entities']
            if str(type(entities)) != str(type([])):
                entities = []
                
            doc = nlp(text, component_cfg={"SpacyPostTokenizer": {"posttokenization": entities, }})
            entities = SpacyPostTokenizer.update_entities(entities, doc)

            temp = [e['start'] for e in entities]

            for t in doc:
                if t.idx not in temp:

                    e = {
                        'start': t.idx,
                        'end': t.idx + len(t.text),
                        'value': t.text,
                        'entity': 'O',
                    }
                    entities.append(e)
                    temp.append(e['start'])
            
            entities = sorted(entities, key=lambda x: x['start'])
            for e in entities:
                e['word'] = e['value']
                del e['value']
                e['label'] = e['entity']
                del e['entity']

            finie_formatted_entities.append(entities)
        
        df['Labels'] = finie_formatted_entities
        df = df[['text', 'intent', 'Labels']]
        df.columns = ['Sentence', 'Intent', 'Labels']
        return df

    elif source == 'finie_raw' and target == 'finie':
        from pyspace.nlp.preprocessing.normalizer.xnormalizer import xNormalizer
        
        df = inputs

        temp = []
        for idx, row in df.iterrows():
            text = row['Sentence']
            entities = row['Labels']

            temptext = ''
            tempstart = 0
            for e in entities:

                e['start'] = tempstart
                e['end'] = tempstart + len(e['word'])

                temptext += e['word']

                if e['end'] == len(text):
                    assert temptext == text
                    for e in entities:
                        assert 'start' in e
                    break
                else:
                    if xNormalizer.is_whitespace(text[e['end']]):
                        tempstart = e['end']+1
                        temptext += text[e['end']]
                    else:
                        tempstart = e['end']
        
        return df

    else:
        assert source == 'invalid source type'
        