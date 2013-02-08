Drawable Growth Charts
======================


What is this?
-------------

This repository aims to provide machine-readable definitions of areas that define data areas on growth chart files (usually PDF files). With this information at hand, software is able to overlay data points and other data on growth chart files and present it to the user.


License
-------

<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US"><img alt="Creative Commons License" style="border:none; float:left; margin:0 1em 1em 0;" src="http://i.creativecommons.org/l/by-nc/3.0/88x31.png" /></a> <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/p2/growth-charts-json" property="cc:attributionName" rel="cc:attributionURL">These formats</a> are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US">Creative Commons Attribution-NonCommercial 3.0 Unported License</a>.


Documentation
-------------

The format of choice is **JSON** and one JSON file defines areas on one source file, usually a PDF growth chart. The basic information element is an **area** object that defines an area in the parent object, which is either a page of the growth chart or another area. Areas define a point of **origin** (x and y), measured from the bottom left of the parent area, and the **size** (width and height), in numbers relative to the parent, which starts at 0,0 and has a size of 1,1.

The format is specified in the [documentation].

An experimental Mac App that reads and writes these formats [is available here][helper].

[documentation]: Format.md
[helper]: https://github.com/p2/growth-charts-helper
