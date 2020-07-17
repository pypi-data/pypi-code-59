from tokenizer_tools.tagset.offset.corpus import Corpus

from tokenizer_tools.tagset.offset.diagnose.entity_disagreement import (
    EntityDisagreement,
)


def test_entity_disaggrement(datadir):
    corpus = Corpus.read_from_file(datadir / "corpus.conllx")
    ed = EntityDisagreement()

    result = ed.check_entity(corpus, "清华大学", "NOT_ORG")
    assert len(result) == 2

    result = ed.check_entity(corpus, "清华", "PART_ORG")
    assert len(result) == 2

    result = ed.check_entity(corpus, "读书", "SOME_ENTITY")
    assert len(result) == 2

    result = ed.check_entity(corpus, "清华大学", "ORG")
    assert len(result) == 0
