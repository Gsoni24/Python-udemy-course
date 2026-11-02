from tkinter import filedialog, Tk
from collections import Counter
import os
from dataclasses import dataclass

@dataclass
class Stats:
    folder: str 
    num_files: int
    total_size_mb: float
    most_common_types: list[tuple[str, int]]


def analyse_folder() -> Stats | None:
    root: Tk = Tk()
    root.withdraw()
    folder_path: str = filedialog.askdirectory(title='Select a folder to analyse')
    
    if not folder_path:
        print('No folder selected')
        return None

    file_count: int = 0 
    total_size: float = 0 
    extension_counter: Counter[str] = Counter()

    for current_dir, subdirs, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.startswith('.'): #not show the hidden files
                continue

            file_count += 1
             
            full_path: str = os.path.join(current_dir, filename)

            try:
                file_size: int = os.path.getsize(full_path)
                total_size += file_size
            except OSError:
                continue

            
            name, extension = os.path.splitext(filename)
            if extension:
                extension_counter[extension.lower()] += 1
    
    total_size_mb: float = round(total_size / (1024 * 1024), 2)
    most_common_extensions: list[tuple[str, int]] = extension_counter.most_common(5)

    return Stats(
        folder = os.path.abspath(folder_path),
        num_files = file_count,
        total_size_mb = total_size_mb,
        most_common_types= most_common_extensions,
    )


def main() -> None:
    stats: Stats | None = analyse_folder()

    if stats:
        print(f'Folder: {stats.folder}')
        print(f'Number of files: {stats.num_files}')
        print(f'Total size (MB): {stats.total_size_mb}')
        print('Most common file types.')
        for ext, count in stats.most_common_types:
            print(f'{ext}: {count} files')
    else:
        print('No folder selected...')


if __name__ == '__main__':
    main()
