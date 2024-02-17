# HAL_AUTO_CHECK

## Installation

To install HAL_AUTO_CHECK, follow these steps:

1. Clone this repository:

```bash
   git clone https://github.com/OR9-Systems/HAL_AUTO_CHECK.git
   cd HAL_AUTO_CHECK
```
2. Install the package in editable mode using pip. Depending on your needs, you can install additional dependencies using the following modes:

| Mode         | Description                             |
|--------------|-----------------------------------------|
| .[behave]    | Installs the package with additional dependencies required for Behave testing. |
| .[docs]      | Installs the package with additional dependencies required for generating documentation. |
| .            | Installs the base package requirements. |

For example, to install with Behave dependencies:

```bash
pip install -e .[behave]
```

To install with documentation dependencies:

```bash
pip install -e .[docs]
```

3. Run Post Install Script To Download Selenium iE Packages and make sure internet Explorer is installed

```bash
post-install
```


This will install HAL_AUTO_CHECK in editable mode, allowing you to make changes to the code and immediately see the effects without needing to reinstall the package.

## Requirements

Make sure you have the latest version of pip installed. You can upgrade pip using the following command:

```bash
pip install --upgrade pip
```

## Documentation

For documentation visit the [HAL_AUTO_CHECK Documentation](https://or9-systems.github.io/HAL_AUTO_CHECK/).
