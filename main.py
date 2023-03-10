from pathlib import Path
import zipfile

# root_dir = Path('files')

# for i in range(1, 11):
#   filename = str(i) + ".txt"
#   filepath = root_dir / Path(filename)
#   filepath.touch()

root_dir = Path('files')
archive_path = root_dir / Path("archive.zip")

with zipfile.ZipFile("archive_path", "w") as zf:
  for path in root_dir.rglob("*.txt"):
    zf.write(path)
    path.unlink() # remove all single files which are now in archive
  