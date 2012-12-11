#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Copyright (c) 2012 Christian Schwarz
#
#Permission is hereby granted, free of charge, to any person obtaining
#a copy of this software and associated documentation files (the
#"Software"), to deal in the Software without restriction, including
#without limitation the rights to use, copy, modify, merge, publish,
#distribute, sublicense, and/or sell copies of the Software, and to
#permit persons to whom the Software is furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
#LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
#WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import pybindgen, sys

pycastC = pybindgen.Module("pycast")

## create the submodules of pycast
pycastC_errors       = pycastC.add_cpp_namespace("errors")
pycastC_common       = pycastC.add_cpp_namespace("common")
pycastC_methods      = pycastC.add_cpp_namespace("methods")
pycastC_optimization = pycastC.add_cpp_namespace("optimization")

## pycast.errors
pycastC_errors.add_include('"pycast/errors/baseerrormeasure.h"')
pycastC_errors_baseerrormeasure = pycastC_errors.add_class("BaseErrorMeasure")

pycastC_errors_baseerrormeasure.add_constructor(
	[
	    pybindgen.param("int", "minimalErrorCalculationPercentage")
	]
)
pycastC_errors_baseerrormeasure.add_method("initialize", pybindgen.retval('bool'), 
	[
		pybindgen.param("PyObject*", "originalTimeSeries",    transfer_ownership=False),
		pybindgen.param("PyObject*", "calculatedTimesSeries", transfer_ownership=False)
	])

#pycastC_errors_baseerrormeasure.add_method(
#	"local_error", pybindgen.retval("float"),
#	[
#	    pybindgen.param("float", "originalValue"),
#	    pybindgen.param("float", "calculatedValue")
#	]
#)

pycastC.generate(sys.stdout)