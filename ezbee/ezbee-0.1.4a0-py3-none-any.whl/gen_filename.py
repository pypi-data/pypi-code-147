"""Generate a feasible filename for a given file name by adding extra number."""
from pathlib import Path
from random import sample
from string import ascii_lowercase


def gen_filename(filename, sep="_", rand=False):
    """Generate a feasible filename for a given file name by adding extra number.

    >>> gen_filename('gen_filename.py')
    'gen_filename_01.py'
    >>> len(gen_filename('gen_filename.py', rand=True))
    23
    """
    # filename = str(filename)

    # file_path = Path(filename).absolute()
    file_path = Path(filename)
    if not file_path.exists():
        return filename

    parent = file_path.parent
    stem = file_path.stem
    suffix = file_path.suffix
    elm = 0
    while elm < 99 and not rand:
        elm += 1
        extra = f"{elm:02d}"
        f_name = f"{stem}{sep}{extra}{suffix}"
        if not (parent / f_name).exists():
            break
    else:
        extra = "".join(sample(ascii_lowercase, 7))
    f_name = f"{stem}{sep}{extra}{suffix}"

    return (parent / f_name).as_posix()
