from tokenizer_tools.tagset.offset.corpus import Corpus


def find_all(string, sub):
    result = []

    sub_length = len(sub)
    start = 0
    while True:
        idx = string.find(sub, start)
        if idx == -1:
            break

        end = idx + sub_length
        result.append((idx, end))
        start = end

    return result


class EntityDisagreement:
    def check_entity(self, corpus: Corpus, entity_text: str, entity_type: str):
        disagreement_docs = []

        for doc in corpus:
            text = "".join(doc.text)
            sub_slices = find_all(text, entity_text)
            if not sub_slices:
                # have no relationship with the entity
                continue

            for start, end in sub_slices:
                # get entity in region
                entities = doc.get_entities_by_range(start, end)

                if not entities:
                    disagreement_docs.append(doc)
                    break
                elif len(entities) > 1:
                    disagreement_docs.append(doc)
                    break
                elif "".join(entities[0].value) != entity_text or entities[0].entity != entity_type:
                    disagreement_docs.append(doc)
                    break

        return disagreement_docs
