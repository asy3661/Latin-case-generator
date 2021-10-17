from pathlib import Path
from document_parser import get_prep_n_pairs

def append_pairs_to_file(path, data):
    with path.open('a') as fh:
        fh.write('\n')
        fh.write(data)


if __name__ == "__main__":
    home = Path.home()
    source_dir = home / 'cltk_data' / 'lat' / 'text' / 'lat_text_tesserae' / 'texts'
    language='lat'
    output_path = Path.cwd() / 'prep_noun_pairs.txt'

    for child in source_dir.iterdir():
        print(str(child))
        with child.open() as fh:
            text = fh.read()
        pairs = get_prep_n_pairs(text, language=language)
        append_pairs_to_file(output_path, pairs)


