import gzip
import shutil
import os
import urllib.request




def download_data(url, out_path, uncompress=False):

    if uncompress:
        download_data_and_uncompress(url, out_path)
        return

    filename = os.path.basename(url)
    out_file = os.path.join(out_path, filename)

    if os.path.exists(out_file):
        return
    
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    urllib.request.urlretrieve(url, out_file)

    return out_file


def download_data_and_uncompress(url, out_path):
    if not url.endswith('.gz'):
        raise ValueError("URL must point to a .gz file if uncompress is True")

    filename = os.path.basename(url)
    gz_file = os.path.join(out_path, filename)
    out_file = os.path.join(out_path, filename[:-3])  # remove .gz

    if os.path.exists(out_file):
        return

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    urllib.request.urlretrieve(url, gz_file)
    uncompress_gz(gz_file, out_file)
    os.remove(gz_file)

    return out_file


def uncompress_gz(gz_path, out_path):
    with gzip.open(gz_path, 'rb') as f_in:
        with open(out_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)