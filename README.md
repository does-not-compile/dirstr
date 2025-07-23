# DIRSTR

## Summary

This script exports your directory structure as a string. Exemplary output:

```text
.
└── app
    ├── api
    │   └── v1
    │       └── endpoints
    ├── core
    ├── models
    ├── services
    └── tests
```


## Usage:

`python -m dirstr <path-to-directory> --folders-only --exclude=folder1,folder2`

- use the optional `--folders-only` flag to exclude files
- use the optional `--exclude=folder1,folder2` flag to exclude specific folders (e.g. `.venv,.git.` note there are NO spaces between the foldernames!)
- if no path is given as argument, it will use the cwd (i.e., ".").

You can also copy it to your bin directory to use as command in your terminal of choice directly. I.e., for macOS:

```
chmod +x dirstr.py
sudo mv dirstr.py /usr/local/bin/dirstr
```

After these commands, you can run the `dirstr` command from anywhere.
