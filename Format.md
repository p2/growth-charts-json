Describing Growth Charts
========================

With this format it is possible to describe plot- and text-areas on growth chart PDFs so computer programs can **use existing growth chart PDFs** to plot data.

The file is in the **JavaScript Object Notation (JSON) format** and defines metadata allowing identification of a specific growth chart as well as unlimited plot and text areas that can be used to represent data. While it is possible to describe a multi-page PDF it is recommended that one file describes a one page PDF document. The reason for this is that for the sake of filter-ability, the file defines the _gender_ for which the chart is applicable as a top-level property.


The JSON File
=============

The JSON file encapsulates a dictionary with these root-level attributes:

* `source` _string_  
  The URL to the growth chart file. Ideally, the file this points to should not change over time.
* `name` _string_  
  How you want to name the chart, ideally kept short. The text should be in the language used on the chart, if feasible. You can provide different JSON files describing the same PDF in different languages. An example would be **Boys, 0-24 Months**.
* `sourceName` _string_  
  A name for the source, e.g. **World Health Organization**.
* `sourceAcronym` _string_  
  The acronym for the source, ideally very short, e.g. **WHO** or **CDC**. May be the same as _sourceName_.
* `description` _string_  
  A description of the chart in general, intended for presentation to humans. See the _name_ attribute for notes on localization.
* `gender` _number_ (0, 1 or 2)  
  The gender found in the page(s) of this chart. Can be `0` (zero) for **both** or unknown, `1` for **male** or `2` for **female**.
* `areas` _array_  
  An array containing all top level areas shown on any page in the chart. See below.

#### Example ####

```javascript
{
  "source": "http://www.cdc.gov/growthcharts/data/who/grchrt_boys_24hdcirc-l4w_rev90910.pdf",
  "sourceName": "World Health Organization",
  "sourceAcronym": "WHO",
  "name": "Boys, 0-24 Months ",
  "description": "Boys 0-24 Months (Head for Age, Weight for Length)",
  "gender": 1,
  "areas": [<area>, <area>, <area>, <area>]
}
```


Areas
-----

Areas are the most interesting part on the chart and there are several subtypes of areas available, explained below. In general an area defines:

* `type` _string_  
  The type of the area, can be one of the following:
  * **plot** An area that plots data
  * **text** An area that displays text
  * **data** An area that displays data, usually a sub-form of "text"
  * **measurementsetcollection** Contains measurement set rows, comparable to HTML `<table>`
  * **measurementset** An area that contains text/data/value areas that describe data in one measurement set, comparable to an HTML table row `<tr>`.

* `rect` _string_  
  A description of the area rectangle, in the form `{{x,y},{width,height}}`. The numbers are relative to the parent area, which can be a page of the chart or a parent area. The origin {0,0} is at the **bottom left**. The parent has **width and height of 1**.

* `page` _number_
  The page of the document on which the area lives. If left out applies to all pages.

* `outline` _string_ (optional)  
  A path that follows the actual area outline, as a series of points, in the coordinate system of the area itself. It can be used, for example, to guide which parts of the area can be filled with a color, as opposed to just filling the rectangular shape defined in `rect`. At least 3 points are required, formatted like `{x,y};{x,y};...`.
  
  * The decimal separator is the point `.`
  * The x and y values are separated by comma `,` and enclosed in curly brackets `{}`
  * The points are separated by the semicolon `;`


### Plot Areas ###

Areas that define plot areas with an x and y axis. Plot areas can also have pre-drawn percentile (or Z-score) lines, and for that they can identify the source of their percentile lines:

* `axes` _dictionary_ (_string_: _dictionary_)  
  One **plot axis** for the **x** and one for the **y** axis, see below
*  `statsSource`  _string_  
  Should identify the source of the percentiles shown on the chart, for example **WHO.2006**. See the [README] for commonly used identifiers.


#### Plot Axes ####

Each axis defines:

* `from` _number_  
  The value in _unit_ at the left (x) or bottom (y) edge of the plot area
* `to` _number_  
  The value in _unit_ at the right (x) or top (y) edge of the plot area
* `unit` _string_  
  The unit the numerical values are representing, e.g. _"length.centimeter"_. See the [README] for commonly used units.
* `dataType` _string_  
  The data type being represented, e.g. _"bodyweight"_. See the [README] for commonly used data types.

#### Example ####

```javascript
{
	"type" : "plot",
	"rect" : "{{0.1798588,0.4466636},{0.6261412,0.4217345}}",
	"outline" : "{0,-0.043};{1,-0.043};{1,0.453};{0,1.04}",
	"axes" : {
		"x" : {
			"from" : 0
			"to" : 24,
			"unit" : "age.month",
			"dataType" : "age",
		},
		"y" : {
			"from" : 30
			"to" : 53,
			"unit" : "length.centimeter",
			"dataType" : "headcircumference",
		}
	},
	"statsSource" : "WHO.2006"
}
```


Text Areas
----------

A text area draws a string. For simplicity reasons when dealing with font sizes, any chart's wider edge is assumed to be 11 inches (27.94 cm) wide at 100% display size, making it 792 points. The attributes are:

* `fontSize` _number_ (optional)  
  The size is in points (_DTP points/PostScript points_) as if the chart were of US Letter (8.5" x 11") size. This means a 72pt font would occupy one inch if displayed at 100% and 792pt is the wider edge of a page.
* `fontName` _string_ (optional)


### Data Areas ###

A data area is usually used to draw a data string, for example the patient name or a single measurement. Additionally to the text area attributes it also defines:

* `dataType` _string_  
  The type of data to be drawn in the area, represented in JS object notation, for example **patient.name**. See the [README] for commonly used data types.


### Measurement Sets ###

Some PDFs might predefine a table-like area where one can input sets of measurements. We can define such an area in the following manner:

1. Define a `measurementsetcollection` area that encompasses the whole area, similar to an HTML `<table>` element.
2. For each row of measurement sets, define a `measurementset` area, similar to an HTML `<tr>` element.
3. Define the individual cells as `data` areas.

Software should now be capable of deciding which measurement sets to use (usually the latest _x_) and fill the table accordingly. Of course you can define more rows than are actually visible on the PDF, just how some people would jot down more measurements below the fields if there is no more space.

#### Example ####

```javascript
{
	"type" : "measurementsetcollection",
	"rect" : "{{0.357183,0.08936869},{0.534817,0.06606185}}",
	"areas" : [
		{
			"type" : "measurementset",
			"rect" : "{{0,0},{1,0.18}}",
			"areas" : [
				{
				"type" : "data",			
				"dataType" : "date",
				"rect" : "{{0,0},{0.142,1}}"
				},
				{
				"type" : "data",
				"dataType" : "age",
				"rect" : "{{0.1446,0},{0.11,1}}"
				},
				{
				"type" : "data",
				"dataType" : "bodyweight",
				"rect" : "{{0.2585,0},{0.132,1}}"
				}
			]
		},
		{...measurementset...},
		{...measurementset...}
	]
}
```


[README]: README.md
