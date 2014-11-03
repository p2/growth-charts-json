Drawable Growth Charts
======================

This repository aims to provide machine-readable definitions for growth chart files (usually PDF files). With this information at hand, software is able to overlay data points and other data on growth chart files and present it to the user.


License
-------

<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US"><img alt="Creative Commons License" style="border:none; float:left; margin:0 1em 1em 0;" src="http://i.creativecommons.org/l/by-nc/3.0/88x31.png" /></a> <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/p2/growth-charts-json" property="cc:attributionName" rel="cc:attributionURL">These formats</a> are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US">Creative Commons Attribution-NonCommercial 3.0 Unported License</a>.


Documentation
-------------

The format of choice is **JSON** and one JSON file defines areas on one source file, usually a PDF growth chart. The basic information element is an **area** object that defines an area in the parent object, which is either a page of the growth chart or another area. Areas define a point of **origin** (x and y), measured from the bottom left of the parent area, and the **size** (width and height), in numbers relative to the parent, which starts at 0,0 and has a size of 1,1.

**Read the full [documentation]**.

An experimental Mac App that reads and writes these formats [is available here][helper].
A Python script that downloads all PDF files belonging to the JSON files is included and can be used as follows to download all PDF files into an existing directory `PDF`:

```bash
python download_pdf.py PDF
```


Statistics Sources
------------------

There are a lot of sources for percentile statistics out there and it is desireable to identify them easily. This can be done with a simple acronym and by specifying the year. Here are the currently used acronyms for the statistics present in this repository:

* **WHO.2006**  
  For the [WHO] charts for [kids 0 - 5 years][who-kid] of age from the year 2006 and for [kids 5 - 10/19 years][who-teen] of age from the year 2007. The 2007 WHO sources supplement the 2006 sources so there's no need to separate these into two acronyms.
* **CDC-infants.2000**  
  For the [CDC] charts for kids 0 - 36 months of age from the year 2000
* **CDC.2000**  
  For the [CDC] charts for kids 2 - 20 years of age from the year 2000. The two CDC sources overlap at age 2 to 3 with differing data so they have to be separated.


Units
=====

These are the units that should be used on charts, the bold one being the preferred one. They should be represented in the JS object notation form, e.g. **length.centimeter**.

### length

* **centimeter**
* meter
* inch
* feet

### weight
* **kilogram**
* pound

### age
* **month**
* year
* day

### bmi
* **kilogram-per-square-meter**


Data Types
==========

A data type unsurprisingly describes the type of data that is being represented. These should be used:

* **bodylength** for body length/height, uses **length** units
* **bodyweight** for body weight, uses **weight** units
* **headcircumference** for head circumference, uses **length** units
* **bmi** for the Body Mass Index (BMI), uses **bmi** unit
* **age** for the age of the child; this can be relative, e.g. when used in the context of a measurement. Uses **age** unit
* **date** usually used in context, e.g. in a measurement-set it means the date of the measurement
* **patient.name** For the child's name (this can be used to designate data areas)
* **patient.record_id** For the child's EHR id


Acknowledgements
----------------

This work was supported by a fellowship from the [Swiss National Science Foundation][snf].


[documentation]: Format.md
[helper]: https://github.com/p2/growth-charts-helper
[WHO]: http://www.who.int/
[who-kid]: http://www.who.int/childgrowth/standards/en/
[who-teen]: http://www.who.int/growthref/en/
[cdc]: http://www.cdc.gov/growthcharts/cdc_charts.htm
[snf]: http://www.snf.ch/
