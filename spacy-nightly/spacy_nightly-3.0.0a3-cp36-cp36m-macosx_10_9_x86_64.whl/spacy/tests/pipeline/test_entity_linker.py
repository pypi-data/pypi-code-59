import pytest

from spacy.kb import KnowledgeBase

from spacy import util
from spacy.gold import Example
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
from spacy.tests.util import make_tempdir
from spacy.tokens import Span


@pytest.fixture
def nlp():
    return English()


def assert_almost_equal(a, b):
    delta = 0.0001
    assert a - delta <= b <= a + delta


def test_kb_valid_entities(nlp):
    """Test the valid construction of a KB with 3 entities and two aliases"""
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=3)

    # adding entities
    mykb.add_entity(entity="Q1", freq=19, entity_vector=[8, 4, 3])
    mykb.add_entity(entity="Q2", freq=5, entity_vector=[2, 1, 0])
    mykb.add_entity(entity="Q3", freq=25, entity_vector=[-1, -6, 5])

    # adding aliases
    mykb.add_alias(alias="douglas", entities=["Q2", "Q3"], probabilities=[0.8, 0.2])
    mykb.add_alias(alias="adam", entities=["Q2"], probabilities=[0.9])

    # test the size of the corresponding KB
    assert mykb.get_size_entities() == 3
    assert mykb.get_size_aliases() == 2

    # test retrieval of the entity vectors
    assert mykb.get_vector("Q1") == [8, 4, 3]
    assert mykb.get_vector("Q2") == [2, 1, 0]
    assert mykb.get_vector("Q3") == [-1, -6, 5]

    # test retrieval of prior probabilities
    assert_almost_equal(mykb.get_prior_prob(entity="Q2", alias="douglas"), 0.8)
    assert_almost_equal(mykb.get_prior_prob(entity="Q3", alias="douglas"), 0.2)
    assert_almost_equal(mykb.get_prior_prob(entity="Q342", alias="douglas"), 0.0)
    assert_almost_equal(mykb.get_prior_prob(entity="Q3", alias="douglassssss"), 0.0)


def test_kb_invalid_entities(nlp):
    """Test the invalid construction of a KB with an alias linked to a non-existing entity"""
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=1)

    # adding entities
    mykb.add_entity(entity="Q1", freq=19, entity_vector=[1])
    mykb.add_entity(entity="Q2", freq=5, entity_vector=[2])
    mykb.add_entity(entity="Q3", freq=25, entity_vector=[3])

    # adding aliases - should fail because one of the given IDs is not valid
    with pytest.raises(ValueError):
        mykb.add_alias(
            alias="douglas", entities=["Q2", "Q342"], probabilities=[0.8, 0.2]
        )


def test_kb_invalid_probabilities(nlp):
    """Test the invalid construction of a KB with wrong prior probabilities"""
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=1)

    # adding entities
    mykb.add_entity(entity="Q1", freq=19, entity_vector=[1])
    mykb.add_entity(entity="Q2", freq=5, entity_vector=[2])
    mykb.add_entity(entity="Q3", freq=25, entity_vector=[3])

    # adding aliases - should fail because the sum of the probabilities exceeds 1
    with pytest.raises(ValueError):
        mykb.add_alias(alias="douglas", entities=["Q2", "Q3"], probabilities=[0.8, 0.4])


def test_kb_invalid_combination(nlp):
    """Test the invalid construction of a KB with non-matching entity and probability lists"""
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=1)

    # adding entities
    mykb.add_entity(entity="Q1", freq=19, entity_vector=[1])
    mykb.add_entity(entity="Q2", freq=5, entity_vector=[2])
    mykb.add_entity(entity="Q3", freq=25, entity_vector=[3])

    # adding aliases - should fail because the entities and probabilities vectors are not of equal length
    with pytest.raises(ValueError):
        mykb.add_alias(
            alias="douglas", entities=["Q2", "Q3"], probabilities=[0.3, 0.4, 0.1]
        )


def test_kb_invalid_entity_vector(nlp):
    """Test the invalid construction of a KB with non-matching entity vector lengths"""
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=3)

    # adding entities
    mykb.add_entity(entity="Q1", freq=19, entity_vector=[1, 2, 3])

    # this should fail because the kb's expected entity vector length is 3
    with pytest.raises(ValueError):
        mykb.add_entity(entity="Q2", freq=5, entity_vector=[2])


def test_candidate_generation(nlp):
    """Test correct candidate generation"""
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=1)

    # adding entities
    mykb.add_entity(entity="Q1", freq=27, entity_vector=[1])
    mykb.add_entity(entity="Q2", freq=12, entity_vector=[2])
    mykb.add_entity(entity="Q3", freq=5, entity_vector=[3])

    # adding aliases
    mykb.add_alias(alias="douglas", entities=["Q2", "Q3"], probabilities=[0.8, 0.1])
    mykb.add_alias(alias="adam", entities=["Q2"], probabilities=[0.9])

    # test the size of the relevant candidates
    assert len(mykb.get_candidates("douglas")) == 2
    assert len(mykb.get_candidates("adam")) == 1
    assert len(mykb.get_candidates("shrubbery")) == 0

    # test the content of the candidates
    assert mykb.get_candidates("adam")[0].entity_ == "Q2"
    assert mykb.get_candidates("adam")[0].alias_ == "adam"
    assert_almost_equal(mykb.get_candidates("adam")[0].entity_freq, 12)
    assert_almost_equal(mykb.get_candidates("adam")[0].prior_prob, 0.9)


def test_append_alias(nlp):
    """Test that we can append additional alias-entity pairs"""
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=1)

    # adding entities
    mykb.add_entity(entity="Q1", freq=27, entity_vector=[1])
    mykb.add_entity(entity="Q2", freq=12, entity_vector=[2])
    mykb.add_entity(entity="Q3", freq=5, entity_vector=[3])

    # adding aliases
    mykb.add_alias(alias="douglas", entities=["Q2", "Q3"], probabilities=[0.4, 0.1])
    mykb.add_alias(alias="adam", entities=["Q2"], probabilities=[0.9])

    # test the size of the relevant candidates
    assert len(mykb.get_candidates("douglas")) == 2

    # append an alias
    mykb.append_alias(alias="douglas", entity="Q1", prior_prob=0.2)

    # test the size of the relevant candidates has been incremented
    assert len(mykb.get_candidates("douglas")) == 3

    # append the same alias-entity pair again should not work (will throw a warning)
    with pytest.warns(UserWarning):
        mykb.append_alias(alias="douglas", entity="Q1", prior_prob=0.3)

    # test the size of the relevant candidates remained unchanged
    assert len(mykb.get_candidates("douglas")) == 3


def test_append_invalid_alias(nlp):
    """Test that append an alias will throw an error if prior probs are exceeding 1"""
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=1)

    # adding entities
    mykb.add_entity(entity="Q1", freq=27, entity_vector=[1])
    mykb.add_entity(entity="Q2", freq=12, entity_vector=[2])
    mykb.add_entity(entity="Q3", freq=5, entity_vector=[3])

    # adding aliases
    mykb.add_alias(alias="douglas", entities=["Q2", "Q3"], probabilities=[0.8, 0.1])
    mykb.add_alias(alias="adam", entities=["Q2"], probabilities=[0.9])

    # append an alias - should fail because the entities and probabilities vectors are not of equal length
    with pytest.raises(ValueError):
        mykb.append_alias(alias="douglas", entity="Q1", prior_prob=0.2)


def test_preserving_links_asdoc(nlp):
    """Test that Span.as_doc preserves the existing entity links"""
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=1)

    # adding entities
    mykb.add_entity(entity="Q1", freq=19, entity_vector=[1])
    mykb.add_entity(entity="Q2", freq=8, entity_vector=[1])

    # adding aliases
    mykb.add_alias(alias="Boston", entities=["Q1"], probabilities=[0.7])
    mykb.add_alias(alias="Denver", entities=["Q2"], probabilities=[0.6])

    # set up pipeline with NER (Entity Ruler) and NEL (prior probability only, model not trained)
    sentencizer = nlp.create_pipe("sentencizer")
    nlp.add_pipe(sentencizer)

    ruler = EntityRuler(nlp)
    patterns = [
        {"label": "GPE", "pattern": "Boston"},
        {"label": "GPE", "pattern": "Denver"},
    ]
    ruler.add_patterns(patterns)
    nlp.add_pipe(ruler)

    cfg = {"kb": mykb, "incl_prior": False}
    el_pipe = nlp.create_pipe(name="entity_linker", config=cfg)
    el_pipe.begin_training()
    el_pipe.incl_context = False
    el_pipe.incl_prior = True
    nlp.add_pipe(el_pipe, last=True)

    # test whether the entity links are preserved by the `as_doc()` function
    text = "She lives in Boston. He lives in Denver."
    doc = nlp(text)
    for ent in doc.ents:
        orig_text = ent.text
        orig_kb_id = ent.kb_id_
        sent_doc = ent.sent.as_doc()
        for s_ent in sent_doc.ents:
            if s_ent.text == orig_text:
                assert s_ent.kb_id_ == orig_kb_id


def test_preserving_links_ents(nlp):
    """Test that doc.ents preserves KB annotations"""
    text = "She lives in Boston. He lives in Denver."
    doc = nlp(text)
    assert len(list(doc.ents)) == 0

    boston_ent = Span(doc, 3, 4, label="LOC", kb_id="Q1")
    doc.ents = [boston_ent]
    assert len(list(doc.ents)) == 1
    assert list(doc.ents)[0].label_ == "LOC"
    assert list(doc.ents)[0].kb_id_ == "Q1"


def test_preserving_links_ents_2(nlp):
    """Test that doc.ents preserves KB annotations"""
    text = "She lives in Boston. He lives in Denver."
    doc = nlp(text)
    assert len(list(doc.ents)) == 0

    loc = doc.vocab.strings.add("LOC")
    q1 = doc.vocab.strings.add("Q1")

    doc.ents = [(loc, q1, 3, 4)]
    assert len(list(doc.ents)) == 1
    assert list(doc.ents)[0].label_ == "LOC"
    assert list(doc.ents)[0].kb_id_ == "Q1"


# fmt: off
TRAIN_DATA = [
    ("Russ Cochran captured his first major title with his son as caddie.",
        {"links": {(0, 12): {"Q7381115": 0.0, "Q2146908": 1.0}},
         "entities": [(0, 12, "PERSON")]}),
    ("Russ Cochran his reprints include EC Comics.",
        {"links": {(0, 12): {"Q7381115": 1.0, "Q2146908": 0.0}},
         "entities": [(0, 12, "PERSON")]}),
    ("Russ Cochran has been publishing comic art.",
        {"links": {(0, 12): {"Q7381115": 1.0, "Q2146908": 0.0}},
         "entities": [(0, 12, "PERSON")]}),
    ("Russ Cochran was a member of University of Kentucky's golf team.",
        {"links": {(0, 12): {"Q7381115": 0.0, "Q2146908": 1.0}},
         "entities": [(0, 12, "PERSON"), (43, 51, "LOC")]}),
]
GOLD_entities = ["Q2146908", "Q7381115", "Q7381115", "Q2146908"]
# fmt: on


def test_overfitting_IO():
    # Simple test to try and quickly overfit the NEL component - ensuring the ML models work correctly
    nlp = English()
    nlp.add_pipe(nlp.create_pipe("sentencizer"))

    # Add a custom component to recognize "Russ Cochran" as an entity for the example training data
    ruler = EntityRuler(nlp)
    patterns = [
        {"label": "PERSON", "pattern": [{"LOWER": "russ"}, {"LOWER": "cochran"}]}
    ]
    ruler.add_patterns(patterns)
    nlp.add_pipe(ruler)

    # Convert the texts to docs to make sure we have doc.ents set for the training examples
    train_examples = []
    for text, annotation in TRAIN_DATA:
        doc = nlp(text)
        train_examples.append(Example.from_dict(doc, annotation))

    # create artificial KB - assign same prior weight to the two russ cochran's
    # Q2146908 (Russ Cochran): American golfer
    # Q7381115 (Russ Cochran): publisher
    mykb = KnowledgeBase(nlp.vocab, entity_vector_length=3)
    mykb.add_entity(entity="Q2146908", freq=12, entity_vector=[6, -4, 3])
    mykb.add_entity(entity="Q7381115", freq=12, entity_vector=[9, 1, -7])
    mykb.add_alias(
        alias="Russ Cochran",
        entities=["Q2146908", "Q7381115"],
        probabilities=[0.5, 0.5],
    )

    # Create the Entity Linker component and add it to the pipeline
    entity_linker = nlp.create_pipe("entity_linker", config={"kb": mykb})
    nlp.add_pipe(entity_linker, last=True)

    # train the NEL pipe
    optimizer = nlp.begin_training()
    for i in range(50):
        losses = {}
        nlp.update(train_examples, sgd=optimizer, losses=losses)
    assert losses["entity_linker"] < 0.001

    # test the trained model
    predictions = []
    for text, annotation in TRAIN_DATA:
        doc = nlp(text)
        for ent in doc.ents:
            predictions.append(ent.kb_id_)
    assert predictions == GOLD_entities

    # Also test the results are still the same after IO
    with make_tempdir() as tmp_dir:
        nlp.to_disk(tmp_dir)
        nlp2 = util.load_model_from_path(tmp_dir)
        predictions = []
        for text, annotation in TRAIN_DATA:
            doc2 = nlp2(text)
            for ent in doc2.ents:
                predictions.append(ent.kb_id_)
        assert predictions == GOLD_entities
