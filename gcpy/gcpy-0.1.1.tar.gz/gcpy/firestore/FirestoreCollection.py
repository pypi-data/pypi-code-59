from google.cloud import firestore

from gcpy.firestore.Changes import Changes
from gcpy.firestore.Document import Document

db = firestore.Client()


class FirestoreCollection:
    name = ''
    """
    Collection name
    """

    document_type = Document.__class__
    """
    Document type
    """

    asc = 'ASCENDING'
    desc = 'DESCENDING'

    def _save_list(self, objects_list: list, merge: bool = False):
        """
        Batch save the list of object into collection_to_listen
        tries to save with chunks of 500 items

        :param objects_list: list of objects of type object, each must have an id field
        :param merge: should the object be merged with that is already exists in the database
        """
        collection = self.name
        if not collection or not isinstance(objects_list, list):
            return
        batch = db.batch()
        counter = 0
        for obj in objects_list:
            if counter == 500:
                batch.commit()
                print('Written {} objects into "{}"'.format(counter, collection))
                counter = 0

            doc_id = obj.get('id')
            if doc_id is None:
                continue
            ref = db.collection(collection).document(doc_id)
            batch.set(ref, obj, merge=merge)
            counter += 1

        batch.commit()
        print('Written {} objects into "{}"'.format(len(objects_list), collection))

    def _remove_list(self, objects_id_list: list, merge: bool = False):
        """
        Batch save the list of object into collection_to_listen
        tries to save with chunks of 500 items

        :param objects_list: list of objects of type object, each must have an id field
        :param merge: should the object be merged with that is already exists in the database
        """
        collection = self.name
        if not collection or not isinstance(objects_id_list, list):
            return
        batch = db.batch()
        counter = 0
        for obj_id in objects_id_list:
            if counter == 500:
                batch.commit()
                print('Deleted {} objects into "{}"'.format(counter, collection))
                counter = 0

            ref = db.collection(collection).document(obj_id)
            batch.delete(ref)
            counter += 1

        batch.commit()
        print('Deleted {} objects into "{}"'.format(len(objects_id_list), collection))

    def _save(self,
              obj: object,
              doc_id: str,
              merge: bool = False
              ):
        """
        Saves an object into collection_to_listen

        :param doc_id:
        :param obj: object to save
        :param merge: should the object be merged with that is already exists in the database
        """
        collection = self.name
        print(obj)
        if not collection or not isinstance(obj, object):
            return
        ref = db.collection(collection).document(doc_id)
        result = ref.set(obj, merge=merge)
        return result

    def _get_all(self, limit: int = None):
        ref = db.collection(self.name)
        if limit:
            ref.limit(limit)
        docs = ref.stream()
        return [doc.to_dict() for doc in docs]

    def _get_doc(self, doc_id):
        ref = db.collection(self.name).document(doc_id)
        doc = ref.get().to_dict()
        return doc

    #
    # HANDLING UPDATES

    def changes_from_event(self, event):
        old_data = event.get('oldValue', {}).get('fields', {})
        new_data = event.get('value', {}).get('fields', {})
        return Changes(
            old=self.document_type.changes(old_data),
            new=self.document_type.changes(new_data)
        )
