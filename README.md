# Google Trends Project

---
Date: 2022-09-13

Author: Hongyuan Qiu

About: Coding and Data Collection Take-home Tech Assessment from EonLabs

---


## Installation (Mac)
1. Create a virtual environment using Python 3.8: 
   ```
   python -m venv google_trends_venv
   ```   
2. Activate the virtual environment: 
   ```
   source google_trends_venv/bin/activate
   ```   
3. Install ipykernel which provides the IPython kernel for Jupyter: 
   ```
   pip install ipykernel
   ```
   Note: Skip steps 3-4 if you don't want to use Jupyter Notebook
   
4. Add your virtual environment to Jupyter:
   ```
   python -m ipykernel install --name=google_trends_venv
   ```
   This will print information similar to:
   ```
   Installed kernelspec google_trends_venv in /usr/local/share/jupyter/kernels/google_trends_venv
   ```
5. Go to google_trends_projects folder and intall Python libraries/packages:
   ```
   pip install -r "requirements.txt"
   ```

## Uninstallation (Mac)
#### Deactivate virtual environment
To deactivate the Python virtual environment, you can run in Terminal: 
```
deactivate
```
#### Remove kernel from Jupyter
You can list all the available kernels with:
```
jupyter kernelspec list
```
Uninstall the kernel `google_trends_venv`, you can type:
```
jupyter kernelspec uninstall google_trends_venv
```

## Reference:
1. [File .gitignore reference](https://github.com/github/gitignore/blob/main/Python.gitignore)
2. [Using Virtual Environments in Jupyter Notebook and Python](https://janakiev.com/blog/jupyter-virtual-envs/)
3. [How To Use Virtual Environment And Jupyter Notebook](https://pythoninoffice.com/virtual-environment-and-jupyter-notebook/)
4. [Remove pandas rows with duplicate indices](https://stackoverflow.com/questions/13035764/remove-pandas-rows-with-duplicate-indices)
5. [Access Google Trends Data without a wrapper, or with the API: Python](https://stackoverflow.com/questions/56340866/access-google-trends-data-without-a-wrapper-or-with-the-api-python)
6. [converting daily stock data to weekly-based via pandas in Python](https://stackoverflow.com/questions/34597926/converting-daily-stock-data-to-weekly-based-via-pandas-in-python)
7. [How to deal with SettingWithCopyWarning in Pandas](https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas)
8. [Origin of tokens in Google trends API call](https://stackoverflow.com/questions/42317489/origin-of-tokens-in-google-trends-api-call)