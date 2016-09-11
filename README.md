# pyconjp2016
Start Python for Finance Data Analysis  
[PyCon JP 2016 Talk#024](https://pycon.jp/2016/ja/schedule/presentation/24/) driller@patraqushe  
[Slide](http://TBD)

---
## [Case1-1](Case1-1_2.xlsm): Implement Monte-Carlo Simulation in Excel Function

1. Input formula into a cell to generate random number with geometric Brownian motion(it satisfies the following stochastic differential equation)

    ![$$dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$$](https://wikimedia.org/api/rest_v1/media/math/render/svg/22a084f84c78d0ae6983fd7283004f412f42757b)

2. Copy above formula count of sample paths

3. Classify the result into bin

4. Count the number of each bin 

5. Visualize

---
## [Case1-2](Case1-1_2.xlsm): Implement Monte-Carlo Simulation in VBA

* Very long code(especially histogram)

* Need to change all corresponding cell addresses for changing sheet layout( can handle by “name manager” partially)

* Very slow

---
## [Case1-3](Case1-3.ipynb): Implement Monte-Carlo Simulation in Python

* Very short code(especially histogram)

* No need to consider data store location

* Faster than VBA

---
## [Case-1-4](Case1-4.ipynb): Correlation between Economic indicator and exchange rate and stock price

* Open Economic indicator & Stock price Excel file @ vdata.Nikkei.com through pandas 
  * Economic indicator
     * Real Gross Domestic Product
     * Diffusion Index
  * Currency Pair : USD/JPY
  * Stock: Nikkei Index

* Visualize by seaborn

---
## [Case1-5](Case1-5.ipynb): Relationship ETF/J-REIT purchases and stock prices

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
  * Using a syntax that is close to VBA

* Get stock prices using pandas_datareader

---
## [Case1-7](Case1-6_7): Create User Defined Function by Python, and use it as Excel function

* Windows only
* Install add-in
* Call function which is written by python as Excel function 
* Fetch Excel range(multiple cells) as array data(pandas or Numpy) in UDF function
* Input multiple return values into Excel range(multiple cells)

---
## [Case2-1](Case2-1_2.ipynb): Use DatetimeIndex

* Very useful pandas.date_range for creating continuous data
* Advantage of DatetimeIndex :
  * Specify various types
    * datetime.date, datetime.datetime, datetime.time, str, int and so on…
  * Handle uncertain notation(similar to parsing by dateutil.parser)
  * Slice into year, month etc
  * Handle "missing value"

---
## [Case2-2](Case2-1_2.ipynb): Create OHLC data and covert time range

* Not so easy to create OHLC
* Convert time-series data into frequency by .resample() method
* .resample() performing resampling operations during frequency conversion
  * Daily, Weekly, 30minute, 1hour, Quarter, etc
* Use techniques to convert OHLC data into OHLC data

---
## [Case2-3](Case2-3.ipynb): Compute the last trading day by CustomBusinessDay class

* Import yaml format holiday data
* Generate the 2nd Friday of the month by pandas.date_range(freq=‘WOM-2FRI‘)
* Skip holidays when calculate using CustomBusinessDay class

---
## [Case3-1](Case3-1.ipynb): Create own magic command

* Search stock price by "line magic", and output it to IPython.display.Iframe
* Paste various format data into notebook cell by "cell magic", and convert into pandas DataFrame
* Save often used command with .py extension, and call it by %load_ext

---
## [Case3-2](Case3-2.ipynb): Use ipywidgets

* Easy to implement UI by ipywidges.interact decorator
* Autogenerate UI controls for function argument
  * bool: check box 
  * Int: slider
* Create interactive visualization of moving average and Bollinger-Bands

