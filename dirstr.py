import os
import sys


def folder_structure_to_string(
    folder_path, prefix="", folders_only=False, exclude_folders=[]
):
    lines = []
    items = sorted(os.listdir(folder_path))

    # Filter out excluded folders and files if folders_only is True
    filtered_items = []
    for item in items:
        item_path = os.path.join(folder_path, item)
        if item in exclude_folders:
            continue
        if folders_only and not os.path.isdir(item_path):
            continue
        filtered_items.append(item)

    for index, item in enumerate(filtered_items):
        item_path = os.path.join(folder_path, item)
        connector = "├── " if index < len(filtered_items) - 1 else "└── "
        lines.append(f"{prefix}{connector}{item}")
        if os.path.isdir(item_path):
            extension = "│   " if index < len(filtered_items) - 1 else "    "
            lines.extend(
                folder_structure_to_string(
                    item_path, prefix + extension, folders_only, exclude_folders
                )
            )
    return lines


def export_folder_structure(folder_path, folders_only=False, exclude_folders=[]):
    folder_name = os.path.basename(folder_path.rstrip("/\\"))
    structure = [folder_name]
    structure.extend(
        folder_structure_to_string(
            folder_path, folders_only=folders_only, exclude_folders=exclude_folders
        )
    )
    return "\n".join(structure)


def main():
    folders_only = "--folders-only" in sys.argv
    exclude_folders = []
    folder_path = "."

    for arg in sys.argv[1:]:
        if arg == "--folders-only":
            continue
        elif arg.startswith("--exclude="):
            exclude_folders.extend(arg.split("=")[1].split(","))
        else:
            folder_path = arg

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    print(export_folder_structure(folder_path, folders_only, exclude_folders))


if __name__ == "__main__":
    main()
