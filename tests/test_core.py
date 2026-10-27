from rag_kb.core import chunk, retrieve
def test_retrieval():
    assert retrieve("cats", chunk("cats are curious", "x"))[0].source == "x"
