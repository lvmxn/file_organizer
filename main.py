import shutil
from pathlib import Path
from config import FILE_CATEGORIES


def sort(path_str):
    path = Path(path_str)
    for file in path.iterdir():
        if file.is_file():
            if file.is_file():
                ext = file.suffix.lower()
                moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    category_folder = path / category
                    category_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), category_folder / file.name)
                    moved = True
                    break

            if not moved:
                other_folder = path / "Other"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file), other_folder / file.name)


sort(input("folder path \n"))
