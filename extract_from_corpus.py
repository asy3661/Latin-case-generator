from pathlib import Path
from document_parser import get_prep_n_pairs
from cltk.data.fetch import FetchCorpus

lat_corpus_downloader = FetchCorpus(language="lat")
lat_corpus_downloader.import_corpus("lat_text_tesserae")

grc_corpus_downloader = FetchCorpus(language="grc")

def append_pairs_to_file(output_path, context, data):

    lines = data.split('\n')
    lines = [f'{context}\t' + line for line in lines]
    contextualized_data = '\n'.join(lines)

    with output_path.open('a') as fh:
        fh.write('\n')
        fh.write(contextualized_data)

def write_progress(place):
    with open('text_processing.txt', 'a') as fh:
        fh.write(place)
        fh.write('\n')

def get_progress(progress_path):
    if Path(progress_path).exists():
        with open(progress_path) as fh:
            progress = fh.readlines()
            progress = [line.strip() for line in progress]
        return progress
    else:
        with open(progress_path, 'w') as fh:
            return ''

def scour_corpus(corpus_path, output_dir_path, language='lat'):
    output_path = output_dir_path / 'prep_noun_pairs.txt'
    progress_path = output_dir_path / 'text_processing.txt'
    processing_progress = get_progress(progress_path)
    for child in corpus_path.iterdir():
        child_str = str(child)
        # print(child_str)
        if child_str in processing_progress:
            print(child_str, 'already processed')
            continue
        else:
            with child.open() as fh:
                text = fh.read()
            print(child_str, 'read')
            pairs = get_prep_n_pairs(text, language=language)
            print('pairs found')
            append_pairs_to_file(output_path, child_str, pairs)
            write_progress(child_str)
            print('data updated')

