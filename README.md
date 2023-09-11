## book-taipingshan-room-helper

### Remove the mistakenly uploaded idea dictionary from the GitHub repository
```
// 1. List the files in the cache 
git ls-files

// 2. Remove the file that is not required
git rm -r --cached .idea
git commit -m "remove idea dictionary"

// 3. Manually delete the idea dictionary on Github 
```

### Requirement
1. pip3 install selenium
2. pip3 install webdriver-manager
3. pip3 install beautifulsoup4

### Anaconda command
1. conda create -n {env-name} python={version}
   * create another virtual environment
   * EX: conda create -n py27env python=2*
2. conda create -n {env-name} --clone root
   * copy current environment
   * EX: conda create -n py27env --clone root
3. conda remove -n {env-name} --all
   * remove specific virtual environment
   * EX: conda remove -n py27env --all
4. conda activate {env-name}
   * switch to another virtual environment
   * EX: activate py27env
5. conda deactivate
   * go back python environment
6. conda info
   * check current conda version
7. conda info -e
   * check all virtual environment you created
8. conda list
   * the installed package in current environment

### Reference
* [How to get text with Selenium WebDriver in Python](https://stackoverflow.com/questions/20996392/how-to-get-text-with-selenium-webdriver-in-python)
* [Selenium wait.until to check ajax request finished is throw error](https://stackoverflow.com/questions/32572313/selenium-wait-until-to-check-ajax-request-finished-is-throw-error)
* [Getting the return value of Javascript code in Selenium](https://stackoverflow.com/questions/5585343/getting-the-return-value-of-javascript-code-in-selenium)
* [Action Chains in Selenium Python](https://www.geeksforgeeks.org/action-chains-in-selenium-python/) 
* [Pandas merge](http://violin-tao.blogspot.com/2017/06/pandas-2-concat-merge.html)

[comment]: <> (### Note)

[comment]: <> (#### 內建隱含的變數)

[comment]: <> (1. \_\_name__)

[comment]: <> (   * 其意義是「模組名稱」，如果該檔案是被引用，其值會是模組名稱；但若該檔案是&#40;透過命令列&#41;直接執行，其值會是 \_\_main__)
