# auto-generated content
from collections import OrderedDict
from enum import Enum


class NodeType(Enum):
    ACTOR = 'Actor'
    BIBLIOGRAPHY = 'Bibliography'
    CYCLE = 'Cycle'
    INVENTORY = 'Inventory'
    ORGANISATION = 'Organisation'
    SITE = 'Site'
    SOURCE = 'Source'
    TERM = 'Term'


class SchemaType(Enum):
    ACTOR = 'Actor'
    BIBLIOGRAPHY = 'Bibliography'
    COMPLETENESS = 'Completeness'
    CYCLE = 'Cycle'
    EMISSION = 'Emission'
    INFRASTRUCTURE = 'Infrastructure'
    INPUT = 'Input'
    INVENTORY = 'Inventory'
    MEASUREMENT = 'Measurement'
    ORGANISATION = 'Organisation'
    PRACTICES = 'Practices'
    PRODUCT = 'Product'
    PROPERTY = 'Property'
    SITE = 'Site'
    SOURCE = 'Source'
    TERM = 'Term'


class Actor:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Actor'
        self.fields['name'] = ''
        self.fields['firstName'] = ''
        self.fields['lastName'] = ''
        self.fields['orcid'] = ''
        self.fields['scopusID'] = ''
        self.fields['primaryInstitution'] = ''
        self.fields['city'] = ''
        self.fields['country'] = None
        self.fields['email'] = ''
        self.fields['website'] = None
        self.fields['dataPrivate'] = None


class BibliographyDocumentType(Enum):
    BILL = 'bill'
    BOOK = 'book'
    BOOK_SECTION = 'book_section'
    CASE = 'case'
    COMPUTER_PROGRAM = 'computer_program'
    CONFERENCE_PROCEEDINGS = 'conference_proceedings'
    ENCYCLOPEDIA_ARTICLE = 'encyclopedia_article'
    FILM = 'film'
    GENERIC = 'generic'
    HEARING = 'hearing'
    JOURNAL = 'journal'
    MAGAZINE_ARTICLE = 'magazine_article'
    NEWSPAPER_ARTICLE = 'newspaper_article'
    PATENT = 'patent'
    REPORT = 'report'
    STATUTE = 'statute'
    TELEVISION_BROADCAST = 'television_broadcast'
    THESIS = 'thesis'
    WEB_PAGE = 'web_page'
    WORKING_PAPER = 'working_paper'


class Bibliography:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Bibliography'
        self.fields['name'] = ''
        self.fields['documentDOI'] = ''
        self.fields['title'] = ''
        self.fields['arxivID'] = ''
        self.fields['isbn'] = ''
        self.fields['issn'] = ''
        self.fields['scopus'] = ''
        self.fields['ssrn'] = ''
        self.fields['mendeleyID'] = ''
        self.fields['documentType'] = ''
        self.fields['authors'] = []
        self.fields['outlet'] = ''
        self.fields['year'] = None
        self.fields['volume'] = None
        self.fields['issue'] = None
        self.fields['chapter'] = ''
        self.fields['pages'] = ''
        self.fields['publisher'] = ''
        self.fields['city'] = ''
        self.fields['editors'] = []
        self.fields['institutionPub'] = []
        self.fields['websites'] = []
        self.fields['dateAccessed'] = None
        self.fields['abstract'] = ''


class Completeness:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Completeness'
        self.fields['fertilizer'] = None
        self.fields['soilAmendments'] = None
        self.fields['pesticides'] = None
        self.fields['water'] = None
        self.fields['electricityFuel'] = None
        self.fields['productsCoProducts'] = None
        self.fields['cropResidue'] = None
        self.fields['manureCompostManagement'] = None


class CycleFunctionalUnitMeasure(Enum):
    _1_HA = '1 ha'
    RELATIVE = 'relative'


class CycleDataState(Enum):
    AGGREGATED = 'aggregated'
    ORIGINAL = 'original'
    RECALCULATED = 'recalculated'


class Cycle:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Cycle'
        self.fields['name'] = ''
        self.fields['description'] = ''
        self.fields['site'] = None
        self.fields['defaultSource'] = None
        self.fields['endDate'] = None
        self.fields['startDate'] = None
        self.fields['cycleDuration'] = None
        self.fields['treatment'] = ''
        self.fields['treatmentDescription'] = ''
        self.fields['functionalUnitMeasure'] = ''
        self.fields['functionalUnitDetails'] = ''
        self.fields['dataCompleteness'] = None
        self.fields['inputs'] = []
        self.fields['emissions'] = []
        self.fields['products'] = []
        self.fields['practices'] = None
        self.fields['dataState'] = ''
        self.fields['dataVersions'] = None
        self.fields['dataPrivate'] = None


class EmissionSdDefinition(Enum):
    CYCLES = 'cycles'
    FARMS = 'farms'
    REPLICATIONS = 'replications'
    SITES = 'sites'


class Emission:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Emission'
        self.fields['term'] = None
        self.fields['description'] = ''
        self.fields['value'] = None
        self.fields['relDays'] = None
        self.fields['sd'] = None
        self.fields['sdDefinition'] = ''
        self.fields['startDate'] = None
        self.fields['endDate'] = None
        self.fields['emissionDuration'] = None
        self.fields['properties'] = []
        self.fields['recalculated'] = None
        self.fields['method'] = None
        self.fields['methodDescription'] = ''
        self.fields['methodTier'] = None
        self.fields['characterisation'] = None
        self.fields['source'] = None


class Infrastructure:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Infrastructure'
        self.fields['name'] = ''
        self.fields['term'] = None
        self.fields['startDate'] = None
        self.fields['endDate'] = None
        self.fields['lifespan'] = None
        self.fields['inputs'] = []
        self.fields['source'] = None


class InputSdDefinition(Enum):
    CYCLES = 'cycles'
    FARMS = 'farms'
    REPLICATIONS = 'replications'
    SITES = 'sites'


class Input:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Input'
        self.fields['term'] = None
        self.fields['description'] = ''
        self.fields['value'] = None
        self.fields['relDays'] = None
        self.fields['sd'] = None
        self.fields['sdDefinition'] = ''
        self.fields['currency'] = ''
        self.fields['price'] = None
        self.fields['cost'] = None
        self.fields['properties'] = []
        self.fields['recalculated'] = None
        self.fields['method'] = None
        self.fields['methodDescription'] = ''
        self.fields['inventory'] = None
        self.fields['source'] = None


class InventoryDataState(Enum):
    AGGREGATED = 'aggregated'
    ORIGINAL = 'original'
    RECALCULATED = 'recalculated'


class Inventory:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Inventory'
        self.fields['name'] = ''
        self.fields['timestamp'] = None
        self.fields['versionDetails'] = ''
        self.fields['cycle'] = None
        self.fields['product'] = None
        self.fields['functionalUnitMeasure'] = ''
        self.fields['functionalUnitQuantity'] = None
        self.fields['inventoryTable'] = []
        self.fields['dataState'] = ''
        self.fields['dataVersions'] = None
        self.fields['dataPrivate'] = None


class Measurement:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Measurement'
        self.fields['term'] = None
        self.fields['method'] = None
        self.fields['methodDescription'] = ''
        self.fields['date'] = ''
        self.fields['time'] = ''
        self.fields['units'] = ''
        self.fields['value'] = None
        self.fields['sd'] = None
        self.fields['depthUpper'] = None
        self.fields['depthLower'] = None
        self.fields['source'] = None


class Organisation:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Organisation'
        self.fields['name'] = ''
        self.fields['boundary'] = None
        self.fields['area'] = None
        self.fields['latitude'] = None
        self.fields['longitude'] = None
        self.fields['streetAddress'] = ''
        self.fields['city'] = ''
        self.fields['addressRegion'] = ''
        self.fields['country'] = None
        self.fields['postOfficeBoxNumber'] = ''
        self.fields['postalCode'] = ''
        self.fields['startDate'] = None
        self.fields['endDate'] = None
        self.fields['dataPrivate'] = None


class Practices:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Practices'
        self.fields['croppingDuration'] = None
        self.fields['shortFallowPeriod'] = None
        self.fields['shortFallowCrop'] = None
        self.fields['longFallowPeriod'] = None
        self.fields['longFallowCrop'] = None
        self.fields['rotationDuration'] = None
        self.fields['orchardDuration'] = None
        self.fields['previousProduct'] = None
        self.fields['aquacultureManagement'] = []
        self.fields['biodiversity'] = []
        self.fields['cropEstablishment'] = []
        self.fields['cropResidueManagement'] = None
        self.fields['dairyManagement'] = []
        self.fields['landUseManagement'] = []
        self.fields['waterRegime'] = None


class ProductSdDefinition(Enum):
    CYCLES = 'cycles'
    FARMS = 'farms'
    REPLICATIONS = 'replications'
    SITES = 'sites'


class Product:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Product'
        self.fields['term'] = None
        self.fields['description'] = ''
        self.fields['value'] = None
        self.fields['relDays'] = None
        self.fields['sd'] = None
        self.fields['sdDefinition'] = ''
        self.fields['currency'] = ''
        self.fields['price'] = None
        self.fields['revenue'] = None
        self.fields['economicValueShare'] = None
        self.fields['properties'] = []
        self.fields['recalculated'] = None
        self.fields['method'] = None
        self.fields['methodDescription'] = ''
        self.fields['destination'] = None
        self.fields['source'] = None


class PropertyValueType(Enum):
    AUTO = 'auto'
    BOOLEAN = 'boolean'
    NUMBER = 'number'
    STRING = 'string'


class Property:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Property'
        self.fields['term'] = None
        self.fields['key'] = None
        self.fields['value'] = None
        self.fields['valueType'] = ''
        self.fields['iri'] = None
        self.fields['sd'] = None
        self.fields['source'] = None


class SiteSiteType(Enum):
    BUILDING = 'building'
    CROPLAND = 'cropland'
    NATURAL_VEGETATION = 'natural vegetation'
    PERMANENT_PASTURE = 'permanent pasture'
    POND = 'pond'


class SiteDataState(Enum):
    AGGREGATED = 'aggregated'
    ORIGINAL = 'original'
    RECALCULATED = 'recalculated'


class Site:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Site'
        self.fields['siteType'] = ''
        self.fields['name'] = ''
        self.fields['description'] = ''
        self.fields['organisation'] = None
        self.fields['defaultSource'] = None
        self.fields['boundary'] = None
        self.fields['area'] = None
        self.fields['latitude'] = None
        self.fields['longitude'] = None
        self.fields['country'] = None
        self.fields['region'] = None
        self.fields['subRegion'] = None
        self.fields['subSubRegion'] = None
        self.fields['subSubSubRegion'] = None
        self.fields['subSubSubSubRegion'] = None
        self.fields['startDate'] = None
        self.fields['endDate'] = None
        self.fields['measurements'] = []
        self.fields['infrastructure'] = []
        self.fields['practices'] = []
        self.fields['dataState'] = ''
        self.fields['dataVersions'] = None
        self.fields['dataPrivate'] = None


class Source:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Source'
        self.fields['name'] = ''
        self.fields['bibliography'] = None
        self.fields['metaAnalysisBibliography'] = None
        self.fields['doiHESTIA'] = ''
        self.fields['uploadDate'] = None
        self.fields['uploadBy'] = None
        self.fields['validationDate'] = None
        self.fields['validationBy'] = []
        self.fields['intendedApplication'] = ''
        self.fields['studyReasons'] = ''
        self.fields['intendedAudience'] = ''
        self.fields['comparativeAssertions'] = None
        self.fields['design'] = ''


class TermTermType(Enum):
    ANIMALPRODUCT = 'animalProduct'
    AQUACULTUREMANAGEMENT = 'aquacultureManagement'
    BIODIVERSITY = 'biodiversity'
    BUILDING = 'building'
    CHARACTERISATION = 'characterisation'
    CROP = 'crop'
    CROPESTABLISHMENT = 'cropEstablishment'
    CROPPRODUCT = 'cropProduct'
    CROPPROTECTION = 'cropProtection'
    CROPRESIDUEMANAGEMENT = 'cropResidueManagement'
    CROPSUPPORT = 'cropSupport'
    DAIRYMANAGEMENT = 'dairyManagement'
    DESTINATION = 'destination'
    ECOREGION = 'ecoregion'
    ELECTRICITY = 'electricity'
    EMISSION = 'emission'
    FUEL = 'fuel'
    INORGANICFERTILIZER = 'inorganicFertilizer'
    IRRIGATION = 'irrigation'
    LANDUSEMANAGEMENT = 'landUseManagement'
    LIVEANIMAL = 'liveAnimal'
    LIVEAQUATICSPECIES = 'liveAquaticSpecies'
    MACHINERY = 'machinery'
    MATERIAL = 'material'
    MEASUREMENT = 'measurement'
    MODEL = 'model'
    ORGANICFERTILIZER = 'organicFertilizer'
    PESTICIDEAI = 'pesticideAI'
    PESTICIDEBRANDNAME = 'pesticideBrandName'
    PROCESSEDFOOD = 'processedFood'
    PROPERTY = 'property'
    REGION = 'region'
    RESOURCEUSE = 'resourceUse'
    SEED = 'seed'
    SOILAMENDMENT = 'soilAmendment'
    SOILTYPE = 'soilType'
    WATER = 'water'
    WATERREGIME = 'waterRegime'


class Term:
    def __init__(self):
        self.fields = OrderedDict()
        self.fields['type'] = 'Term'
        self.fields['termType'] = ''
        self.fields['name'] = ''
        self.fields['shortName'] = ''
        self.fields['synonyms'] = []
        self.fields['definition'] = ''
        self.fields['description'] = ''
        self.fields['units'] = ''
        self.fields['subClassOf'] = []
        self.fields['defaultProperties'] = []
        self.fields['dependentVariables'] = []
        self.fields['independentVariables'] = []
