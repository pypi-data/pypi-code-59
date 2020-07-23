import sbol2


class DataSheet(sbol2.Identified):

    RDF_TYPE = 'http://examples.org#DataSheet'

    def __init__(self, uri='example'):
        super().__init__(uri=uri,
                         type_uri=DataSheet.RDF_TYPE)


class Analysis(sbol2.TopLevel):

    RDF_TYPE = 'http://examples.org#Analysis'

    def __init__(self, uri=None, model=None):
        super().__init__(uri=uri,
                         type_uri=Analysis.RDF_TYPE)
        self.model = sbol2.ReferencedObject(self, sbol2.SBOL_MODELS, sbol2.SBOL_MODEL,
                                            0, 1, [])
        self.dataSheet = sbol2.OwnedObject(self, 'http://examples.org#dataSheet',
                                           DataSheet, '0', '1', [])


doc = sbol2.Document()
analysis = Analysis('foo')
doc.add(analysis)
analysis.dataSheet = DataSheet('foo')
print(doc.writeString())
