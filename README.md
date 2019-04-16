
# jetbot_widgets

[![Build Status](https://travis-ci.org/jaybdub/jetbot_widgets.svg?branch=master)](https://travis-ci.org/jaybdub/jetbot_widgets)
[![codecov](https://codecov.io/gh/jaybdub/jetbot_widgets/branch/master/graph/badge.svg)](https://codecov.io/gh/jaybdub/jetbot_widgets)


Jupyter widgets for NVIDIA JetBot

## Installation

You can install using `pip`:

```bash
pip install jetbot_widgets
```

Or if you use jupyterlab:

```bash
pip install jetbot_widgets
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

If you are using Jupyter Notebook 5.2 or earlier, you may also need to enable
the nbextension:
```bash
jupyter nbextension enable --py [--sys-prefix|--user|--system] jetbot_widgets
```
