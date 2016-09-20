# pyconjp2016
Start hacking finance data with Python  

[PyCon JP 2016 Talk#024](https://pycon.jp/2016/ja/schedule/presentation/24/) driller@patraqushe  

* Slide  
    en: https://www.slideshare.net/secret/sOATcrXj9gB7MG  
    ja: TBD

* [Docker image](https://hub.docker.com/r/driller/docker-pyconjp2016/)  
    This image doesn't include packages related to Excel.

    ### Usage Example

    * Linux or docker-machine(Docker Toolbox)
  ```
  git clone https://github.com/drillan/pyconjp2016.git
  docker run -d --name pycon -p 8888:8888 -v $PWD/pyconjp2016:/notebooks driller/docker-pyconjp2016
  ```

  * Docker for Windows
  ```
  git clone https://github.com/drillan/pyconjp2016.git
  docker run -d --name pycon -p 8888:8888 -v %CD%/pyconjp2016:/notebooks driller/docker-pyconjp2016
  ```

---
# Sample code and files

* Some code is redundant due to:  
    * Python 2/3 support  
    * Offline mode  
* No license limitations   

---
## Case1-1: Implement Monte-Carlo Simulation in Excel Function

1. Input formula into a Cell to generate random number with geometric Brownian motion(it satisfies the following stochastic differential equation)

    ![$$dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$$](https://wikimedia.org/api/rest_v1/media/math/render/svg/22a084f84c78d0ae6983fd7283004f412f42757b)

2. Copy above formula count of sample paths

3. Classify the result into bin

4. Count the number of each bins then visualize 

---
## Case1-2: Implement Monte-Carlo Simulation in VBA

* Very long code(especially histogram)

* When changing the layout of an Excel sheet, you have to change all the addresses of related cells(can handle by "name manager" partially)

* Very slow

---
## [Case1-3](http://nbviewer.jupyter.org/github/drillan/pyconjp2016/blob/master/Case1-3.ipynb): Implement Monte-Carlo Simulation in Python

* Very short code(especially histogram)

* No need to consider data storage

* Faster than VBA

---
## [Case-1-4](http://nbviewer.jupyter.org/github/drillan/pyconjp2016/blob/master/Case1-4.ipynb): Correlation between Economic indicator and exchange rate and stock price

* Open Economic indicator & Stock price Excel file @ vdata.Nikkei.com through pandas 
  * Economic indicator
     * Real Gross Domestic Product
     * Diffusion Index
  * Currency Pair : USD/JPY
  * Stock: Nikkei Index

* Visualize by seaborn

---
## [Case1-5](http://nbviewer.jupyter.org/github/drillan/pyconjp2016/blob/master/Case1-5.ipynb): Relationship ETF/J-REIT purchases and stock prices

* Open Excel files from BOJ site using pandas

* Load TSE REIT index and stock index price data from k-db site
  * Stock Indices
    * TOPIX
    * JPX400
    * Nikkei225

* Visualize relationship using seaborn

---
## [Case1-6](Case1-6_7): Download stock prices and store into Excel cells

* xlwings features
  * Calling Python from Excel
  * Put pandas DataFrame data into Excel cells
  * Uses syntax close to VBA

* Get stock prices using pandas_datareader

---
## [Case1-7](Case1-6_7): Create User Defined Function by Python, and use it as Excel function

* Windows only
* Install add-in
* Call function written in Python like an Excel function   
* Fetch Excel Range(multiple cells) as array data(pandas or Numpy) in UDF function
* Input multiple return values into Excel Range(multiple cells)

---
## [Case2-1](http://nbviewer.jupyter.org/github/drillan/pyconjp2016/blob/master/Case2-1_2.ipynb): Use DatetimeIndex

* pandas.date_range is very useful to create continuous data  
* Advantage of DatetimeIndex :
  * Specify various types when selecting a location  
    * datetime.date, datetime.datetime, datetime.time, str, int and so on…
  * Able to parse most known formats(similar to parsing by dateutil.parser)
  * Allows slicing into year, month, etc
  * Handles missing values  

---
## [Case2-2](http://nbviewer.jupyter.org/github/drillan/pyconjp2016/blob/master/Case2-1_2.ipynb): Create OHLC data and covert time range

* Not that easy to create OHLC
* Convert time-series data into frequencies using the .resample() method
* .resample() performs resampling operations during frequency conversion
  * Daily, Weekly, 30minute, 1hour, Quarter, etc
* There are tips to convert between different OHLC data representations

---
## [Case2-3](http://nbviewer.jupyter.org/github/drillan/pyconjp2016/blob/master/Case2-3.ipynb): Compute the last trading day by CustomBusinessDay class

* Import holiday data from YAML file  
* Select the 2nd friday of evey month using pandas.date_range(feq='WOM-2FRI')  
* Skip holidays using the CustomBusinessDay class  

---
## [Case3-1](http://nbviewer.jupyter.org/github/drillan/pyconjp2016/blob/master/Case3-1.ipynb): Create own magic command

* Search stock price using "line magic", and output it to IPython.display.Iframe  
* Paste data in various formats into notebook cells using "cell magic" , and convert it into a pandas DataFrame  
* Save frequently used commands to a file and re-use them using %load_ext  

---
## [Case3-2](http://nbviewer.jupyter.org/github/drillan/pyconjp2016/blob/master/Case3-2.ipynb): ipywidgets is the easiest way to create a UI  

* Easy to implement a UI using the ipywidgets.interact decorator  
* Automatically creates UI controls for function arguments  
  * bool: check box 
  * Int: slider
* Creates interactive visualization of moving averages and Bollinger-Bands  


