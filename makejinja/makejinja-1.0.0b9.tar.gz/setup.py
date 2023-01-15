# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['makejinja']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=3.1.2,<4.0.0',
 'pyyaml>=6.0,<7.0',
 'rich-click>=1.6.0,<2.0.0',
 'typed-settings[click]>=2.0.1,<3.0.0']

extras_require = \
{':python_version < "3.11"': ['tomli>=2.0.1,<3.0.0']}

entry_points = \
{'console_scripts': ['makejinja = makejinja.cli:main']}

setup_kwargs = {
    'name': 'makejinja',
    'version': '1.0.0b9',
    'description': 'Automatically generate files based on Jinja templates. Use it to easily generate complex Home Assistant dashboards!',
    'long_description': '# makejinja\n\n**Note:** Development happens in the [beta branch](https://github.com/mirkolenz/makejinja/tree/beta).\n\nmakejinja can be used to automatically generate files from [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/templates/).\nThis allows you to load variables from external files or create repeating patterns via loops.\nIt is conceptually similar to [gomplate](https://github.com/hairyhenderson/gomplate), but is built on Python and Jinja instead of Go.\nA use case for this tool is generating config files for [Home Assistant](https://www.home-assistant.io/):\nUsing the same language that the built-in templates use, you can greatly simplify your configuration.\n\nA concrete example for Home Assistant can be found in the [tests directory](./tests/data)\n\n## Features\n\n- Recursively convert nested directories containing template files. One can even specify a pattern to specify relevant files in a folder.\n- Load data files containing variables to use in your Jinja templates from YAML, TOML, and Python files.\n- Use custom functions in your Jinja templates by loading custom filters and/or globals.\n- Easily load all extensions bundled with Jinja (custom extensions are not yet supported).\n- Tailor the whitespace behavior to your needs.\n- Use custom delimiters for Jinja blocks/comments/variables.\n- Modify _all_ init options for the Jinja environment and even run custom hooks after the environment has been created.\n\n## Installation\n\nmakejinja is available via `pip` and can be installed via\n\n`pip install makejinja`\n\nBeware that depending on other packages installed on your system via pip, there may be incompatibilities.\nThus, we advise leveraging [`pipx`](https://github.com/pypa/pipx) instead:\n\n`pipx install makejinja`\n\nAlternatively, the application can also be used via Docker.\nWe automatically publish an image at `ghcr.io/mirkolenz/makejinja`.\nTo use it, mount a folder to the container and pass the command options via the environment variable `cmd`.\nFor example, to process files in `./data/input` and render them to `./data/output` while using the extension `jinja2.ext.do`, you could run:\n\n`docker run --rm -it -v $(pwd)/data:/data -e args="/data/input /data/output --extension jinja2.ext.do" ghcr.io/mirkolenz/makejinja@latest`\n\n## Usage\n\nIn its default configuration, makejinja searches the input folder recursively for files ending in `.jinja`.\nAlso, we copy all contents (except raw template files) of the input folder to the output folder and remove the `.jinja` ending during the render process.\nTo get an overview of the remaining options, we advise you to run `makejinja --help`:\n\n<!-- echo -e "\\n```txt\\n$(COLUMNS=120 poetry run makejinja --help)\\n```" >> README.md -->\n\n```txt\n\n Usage: makejinja [OPTIONS] INPUT_FOLDER OUTPUT_FOLDER\n\n╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮\n│ *    input_folder       DIRECTORY  Path to a folder containing template files. It is passed to Jinja\'s               │\n│                                    FileSystemLoader when creating the environment.                                   │\n│                                    [default: None]                                                                   │\n│                                    [required]                                                                        │\n│ *    output_folder      DIRECTORY  Path to a folder where the rendered templates are stored. makejinja preserves the │\n│                                    relative paths in the process, meaning that you can even use it on nested         │\n│                                    directories.                                                                      │\n│                                    [default: None]                                                                   │\n│                                    [required]                                                                        │\n╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮\n│ --help          Show this message and exit.                                                                          │\n╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n╭─ Input File Handling ────────────────────────────────────────────────────────────────────────────────────────────────╮\n│ --pattern             TEXT  Glob pattern to search for files in input_folder. Accepts all pattern supported by       │\n│                             fnmatch. If a file is matched by this pattern and does not end with the specified        │\n│                             jinja-suffix, it is copied over to the output_folder. Note: Do not add a special suffix  │\n│                             used by your template files here, instead use the jinja-suffix option.                   │\n│                             [default: **/*]                                                                          │\n│ --jinja-suffix        TEXT  File ending of Jinja template files. All files with this suffix in input_folder matched  │\n│                             by pattern are passed to the Jinja renderer. Note: Should be provided with the leading   │\n│                             dot.                                                                                     │\n│                             [default: .jinja]                                                                        │\n╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n╭─ Jinja Environment Options ──────────────────────────────────────────────────────────────────────────────────────────╮\n│ --data             PATH  Load variables from yaml/yaml files for use in your Jinja templates. The defintions are     │\n│                          passed to Jinja\'s render function. Can either be a file or a folder containg files. Note:   │\n│                          This option may be passed multiple times to pass a list of values. If multiple files are    │\n│                          supplied, beware that previous declarations will be overwritten by newer ones.              │\n│ --globals          PATH  You can import functions/varibales defined in .py files to use them in your Jinja           │\n│                          templates. Can either be a file or a folder containg files. Note: This option may be passed │\n│                          multiple times to pass a list of files/folders. If multiple files are supplied, beware that │\n│                          previous declarations will be overwritten by newer ones.                                    │\n│ --filters          PATH  Jinja has support for filters (e.g., [1, 2, 3] | length) to easily call functions. This     │\n│                          option allows you to define custom filters in .py files. Can either be a file or a folder   │\n│                          containg files. Note: This option may be passed multiple times to pass a list of            │\n│                          files/folders. If multiple files are supplied, beware that previous declarations will be    │\n│                          overwritten by newer ones.                                                                  │\n│ --extension        TEXT  Extend Jinja\'s parser by loading the specified extensions. An overview of the built-in ones │\n│                          can be found on the project website. Currently, only those built-in filters are allowed.    │\n│                          Note: This option may be passed multiple times to pass a list of values.                    │\n╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n╭─ Jinja Whitespace Control ───────────────────────────────────────────────────────────────────────────────────────────╮\n│ --lstrip-blocks            --no-lstrip-blocks              The lstrip_blocks option can also be set to strip tabs    │\n│                                                            and spaces from the beginning of a line to the start of a │\n│                                                            block. (Nothing will be stripped if there are other       │\n│                                                            characters before the start of the block.) Refer to the   │\n│                                                            Jinja docs for more details.                              │\n│                                                            [default: lstrip-blocks]                                  │\n│ --trim-blocks              --no-trim-blocks                If an application configures Jinja to trim_blocks, the    │\n│                                                            first newline after a template tag is removed             │\n│                                                            automatically (like in PHP). Refer to the Jinja docs for  │\n│                                                            more details.                                             │\n│                                                            [default: trim-blocks]                                    │\n│ --keep-trailing-newline    --no-keep-trailing-newline      By default, Jinja also removes trailing newlines. To keep │\n│                                                            single trailing newlines, configure Jinja to              │\n│                                                            keep_trailing_newline. Refer to the Jinja docs for more   │\n│                                                            details.                                                  │\n│                                                            [default: no-keep-trailing-newline]                       │\n╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n╭─ Jinja Delimiters ───────────────────────────────────────────────────────────────────────────────────────────────────╮\n│ --block-start-string           TEXT  [default: {%]                                                                   │\n│ --block-end-string             TEXT  [default: %}]                                                                   │\n│ --comment-start-string         TEXT  [default: {#]                                                                   │\n│ --comment-end-string           TEXT  [default: #}]                                                                   │\n│ --variable-start-string        TEXT  [default: {{]                                                                   │\n│ --variable-end-string          TEXT  [default: }}]                                                                   │\n╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n╭─ Output File Handling ───────────────────────────────────────────────────────────────────────────────────────────────╮\n│ --copy-tree              --no-copy-tree                If your input_folder containes additional files besides Jinja │\n│                                                        templates, you may want to copy them to output_folder as      │\n│                                                        well. This operation maintains the metadata of all files and  │\n│                                                        folders, meaning that tools like rsync will treat them        │\n│                                                        exactly like the original ones. Note: Even if set to          │\n│                                                        no-copy-tree, files that are matched by your provided pattern │\n│                                                        within input_folder are still copied over. In both cases, a   │\n│                                                        file\'s metadata is untouched. The main difference is that     │\n│                                                        with copy-tree, folders keep their metadata while matched     │\n│                                                        files are copied to newly-created subfolders that differ in   │\n│                                                        their metadata.                                               │\n│                                                        [default: copy-tree]                                          │\n│ --remove-jinja-suffix    --no-remove-jinja-suffix      Decide whether the specified jinja-suffix is removed from the │\n│                                                        file after rendering.                                         │\n│                                                        [default: remove-jinja-suffix]                                │\n│ --skip-empty             --no-skip-empty               Some Jinja template files may be empty after rendering (e.g., │\n│                                                        if they only contain macros that are imported by other        │\n│                                                        templates). By default, we do not copy such empty files. If   │\n│                                                        there is a need to have them available anyway, you can adjust │\n│                                                        that.                                                         │\n│                                                        [default: skip-empty]                                         │\n╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n```\n',
    'author': 'Mirko Lenz',
    'author_email': 'mirko@mirkolenz.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mirkolenz/makejinja',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
