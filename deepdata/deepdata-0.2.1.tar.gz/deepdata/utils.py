import os
import os.path
import hashlib
import gzip
import tarfile
import zipfile
from tqdm import tqdm


def gen_bar_updater():
    bar = tqdm(total=None)

    def bar_update(count, block_size, total_size):
        if bar.total is None and total_size:
            bar.total = total_size
        progress_bytes = count * block_size
        bar.update(progress_bytes - bar.n)

    return bar_update


def calculate_md5(file, chunk_size=1024 * 1024):
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def check_md5(file, md5=None, **kwargs):
    if not os.path.isfile(file):
        return False
    if md5 is None:
        return True
    return md5 == calculate_md5(file, **kwargs)


def download_url(url, root, filename=None, md5=None):
    """Download a file from a url and place it in root.

    Args:
        url (str): URL to download file from
        root (str): Directory to place downloaded file in
        filename (str, optional): Name to save the file under. If None, use the basename of the URL
        md5 (str, optional): MD5 checksum of the download. If None, do not check
    """
    from six.moves import urllib

    root = os.path.expanduser(root)
    if not filename:
        filename = os.path.basename(url)
    file = os.path.join(root, filename)

    os.makedirs(root, exist_ok=True)

    # check if file is already present locally
    if check_md5(file, md5):
        print('Using downloaded and verified file: ' + file)
    else:  # download the file
        try:
            print('Downloading ' + url + ' to ' + file)
            urllib.request.urlretrieve(
                url, file,
                reporthook=gen_bar_updater()
            )
        except (urllib.error.URLError, IOError) as e:
            if url[:5] == 'https':
                url = url.replace('https:', 'http:')
                print('Failed download. Trying https -> http instead.'
                      ' Downloading ' + url + ' to ' + file)
                urllib.request.urlretrieve(
                    url, file,
                    reporthook=gen_bar_updater()
                )
            else:
                raise e
        # check integrity of downloaded file
        if not check_md5(file, md5):
            raise RuntimeError("File not found or corrupted.")


def list_dir(root, prefix=False):
    """List all directories at a given root

    Args:
        root (str): Path to directory whose folders need to be listed
        prefix (bool, optional): If true, prepends the path to each result, otherwise
            only returns the name of the directories found
    """
    root = os.path.expanduser(root)
    directories = list(
        filter(
            lambda p: os.path.isdir(os.path.join(root, p)),
            os.listdir(root)
        )
    )

    if prefix is True:
        directories = [os.path.join(root, d) for d in directories]

    return directories


def list_files(root, suffix, prefix=False):
    """List all files ending with a suffix at a given root

    Args:
        root (str): Path to directory whose folders need to be listed
        suffix (str or tuple): Suffix of the files to match, e.g. '.png' or ('.jpg', '.png').
            It uses the Python "str.endswith" method and is passed directly
        prefix (bool, optional): If true, prepends the path to each result, otherwise
            only returns the name of the files found
    """
    root = os.path.expanduser(root)
    files = list(
        filter(
            lambda p: os.path.isfile(os.path.join(root, p)) and p.endswith(suffix),
            os.listdir(root)
        )
    )

    if prefix is True:
        files = [os.path.join(root, d) for d in files]

    return files


def extract_archive(from_path, to_path=None, remove_finished=False):
    if to_path is None:
        to_path = os.path.dirname(from_path)

    if from_path.endswith(".tar"):
        with tarfile.open(from_path, 'r') as tar:
            tar.extractall(path=to_path)
    elif from_path.endswith(".tar.gz") or from_path.endswith(".tgz"):
        with tarfile.open(from_path, 'r:gz') as tar:
            tar.extractall(path=to_path)
    elif from_path.endswith(".tar.xz"):
        # .tar.xz archive only supported in Python 3.x
        with tarfile.open(from_path, 'r:xz') as tar:
            tar.extractall(path=to_path)
    elif from_path.endswith(".gz") and not from_path.endswith(".tar.gz"):
        to_path = os.path.join(to_path, os.path.splitext(os.path.basename(from_path))[0])
        with open(to_path, "wb") as out_f, gzip.GzipFile(from_path) as zip_f:
            out_f.write(zip_f.read())
    elif from_path.endswith(".zip"):
        with zipfile.ZipFile(from_path, 'r') as z:
            z.extractall(to_path)
    else:
        raise ValueError("Extraction of {} not supported".format(from_path))

    if remove_finished:
        os.remove(from_path)


def download_and_extract_archive(url, download_root, extract_root=None, filename=None,
                                 md5=None, remove_finished=False):
    download_root = os.path.expanduser(download_root)
    if extract_root is None:
        extract_root = download_root
    if not filename:
        filename = os.path.basename(url)

    download_url(url, download_root, filename, md5)

    archive = os.path.join(download_root, filename)
    print("Extracting {} to {}".format(archive, extract_root))
    extract_archive(archive, extract_root, remove_finished)


def iterable_to_str(iterable):
    return "'" + "', '".join([str(item) for item in iterable]) + "'"


def verify_str_arg(value, arg=None, valid_values=None, custom_msg=None):
    if valid_values is None:
        return value

    if value not in valid_values:
        if custom_msg is not None:
            msg = custom_msg
        else:
            msg = ("Unknown value '{value}' for argument {arg}. "
                   "Valid values are {{{valid_values}}}.")
            msg = msg.format(value=value, arg=arg,
                             valid_values=iterable_to_str(valid_values))
        raise ValueError(msg)

    return value
