from pytorch_pretrained_bert.tokenization import (BertTokenizer, BasicTokenizer, WordpieceTokenizer,
                                                  _is_whitespace, _is_control, _is_punctuation)


class TokenizationTest():

    def test_full_tokenizer(self):
        vocab_tokens = [
            "[UNK]", "[CLS]", "[SEP]", "want", "##want", "##ed", "wa", "un", "runn",
            "##ing", ","
        ]
        with open("./tmp/bert_tokenizer_test.txt", "w") as vocab_writer:
            vocab_writer.write("".join([x + "\n" for x in vocab_tokens]))

            vocab_file = vocab_writer.name

        tokenizer = BertTokenizer(vocab_file)
        tokens = tokenizer.tokenize(u"UNwant\u00E9d,running")
        print(tokens)

        print(tokenizer.convert_tokens_to_ids(tokens))

    def test_full_tokenizer_raises_error_for_long_sequences(self):
        vocab_tokens = [
            "[UNK]", "[CLS]", "[SEP]", "want", "##want", "##ed", "wa", "un", "runn",
            "##ing", ","
        ]
        with open("./tmp/bert_tokenizer_test.txt", "w") as vocab_writer:
            vocab_writer.write("".join([x + "\n" for x in vocab_tokens]))
            vocab_file = vocab_writer.name

        tokenizer = BertTokenizer(vocab_file, max_len=10)
        tokens = tokenizer.tokenize(u"the cat sat on the mat in the summer time")
        indices = tokenizer.convert_tokens_to_ids(tokens)
        print(indices)

        tokens = tokenizer.tokenize(u"the cat sat on the mat in the summer time .")
        print(tokenizer.convert_tokens_to_ids)
        print(tokens)

    def test_wordpiece_tokenizer(self):
        vocab_tokens = [
            "[UNK]", "[CLS]", "[SEP]", "want", "##want", "##ed", "wa", "un", "runn",
            "##ing"
        ]

        vocab = {}
        for (i, token) in enumerate(vocab_tokens):
            vocab[token] = i
        tokenizer = WordpieceTokenizer(vocab=vocab)

        print(tokenizer.tokenize("unwanted running"))
        print(tokenizer.tokenize("unwantedX running"))


if __name__ == '__main__':
    tokenization = TokenizationTest()
    tokenization.test_full_tokenizer()
    tokenization.test_full_tokenizer_raises_error_for_long_sequences()
    tokenization.test_wordpiece_tokenizer()