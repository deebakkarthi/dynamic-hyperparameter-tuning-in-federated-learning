# New env creation on Linux
```
conda create -n SMAC python=3.10
conda activate SMAC
conda install gxx_linux-64 gcc_linux-64 swig
pip install smac
```

# New env creation on Mac
```
conda create -n SMAC python=3.10
conda activate SMAC
pip install smac
```

Additionally install swig using homebrew
```
brew install swig
```

# Importing old env on Linux
```
conda env create --name envname --file=environments.yml
```

