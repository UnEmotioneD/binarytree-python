# Using Nodemon with Python

_Nodemon is a utility that monitors changes in your source code and automatically restarts your application. While it's primarily used for Node.js applications, you can also use it to streamline Python development._

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Monitoring Multiple File Extensions](#monitoring-multiple-file-extensions)
- [Creating a Configuration File](#creating-a-configuration-file)
- [Ignoring Files and Directories](#ignoring-files-and-directories)
- [Troubleshooting](#troubleshooting)
- [Conclusion](#conclusion)

---

## Prerequisites

- **Node.js and npm**: Ensure that [Node.js](https://nodejs.org/) and npm are installed on your system.

---

## Installation

Install Nodemon globally using npm:

```zsh
npm install -g nodemon

```

Verify the installation:

```zsh
nodemon -V
```

---

## Basic Usage

To use Nodemon with a Python script, run:

```zsh
nodemon --exec python3 --ext py binary_tree.py
```

Now, Nodemon will restart whenever `.py` file changes.

---

## Monitoring Multiple File Extensions

If your project includes other file types (e.g., `.html`, `.css`) that should trigger a restart, specify them:

```zsh
nodemon --exec python3 --ext py,html,css binary_tree.py
```

---

## Creating a Configuration File

For advanced configurations, create a `nodemon.json` file in your project directory.

## Sample `nodemon.json`

```json
{
  "watch": ["*.py"],
  "ext": "py",
  "ignore": [],
  "exec": "python3 binary_tree.py"
}
```

- `watch`: Files or directories to monitor.
- `ext`: File extensions to watch.
- `ignore`: Path to exclude.
- `exec`: Command to run on changes.

## Running with Configuration File

Simply execute:

```zsh
nodemon
```

Nodemon will use the settings from `nodemon.json`.

---

## Ignoring Files and Directories

Exclude files or directories using the `--ignore` flag:

```zsh
nodemon --exec python3 --ext py --ignore tests/* binary_tree.py
```

Or specify them in `nodemon.json` under the `ignore` key.

---

## Troubleshooting

## Nodemon Command Not Found

if you encounter a "command not found" error:

- Ensure Nodemon is installed globally.
- Add npm global packages to your PATH.
- Alternatively, run Nodemon with `npx`:

```zsh
npx nodemon --exc python3 --ext py binary_tree.py
```

## Changes Not Detected

- Confirm you're in the correct directory.
- Verify the file extensions with `--ext`.
- Check file permissions and paths.

---

## Conclusion

Using Nodemon with Python automates the restart process of your scripts upon code changes, enhancing your development workflow.
Customize Nodemon to fit your project's needs and focus more on coding.

---

Happy coding!
