import argparse


def rev_comp(seq):
    c = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return "".join([c[x] for x in seq])


def convert(source, dest):
    data_i = "not found"
    bc_index = None
    with open(source) as i, open(dest, 'w') as o:
        for line in i:
            if data_i == "not found" and line.startswith("[Data]"):
                data_i = "header"
            elif data_i == "header":
                data_i = "found"
                bc_index = line.split(",").index("index2")
            elif data_i == "found":  # Line with barcode
                fields = line.split(",")
                bc2 = fields[bc_index]
                fields[bc_index] = rev_comp(bc2)
                line = ",".join(fields)
            o.write(line)


def main():

    parser = argparse.ArgumentParser(description="Creates illumina samplesheet with the reverse complement of the index2")

    parser.add_argument('source_samplesheet')
    parser.add_argument('edited_samplesheet')

    args = parser.parse_args()
    convert(args.source_samplesheet, args.edited_samplesheet)


if __name__ == "__main__":
    main()
