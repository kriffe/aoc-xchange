#!/usr/bin/env python
# coding: utf-8

r"""Exporting multiple shapes to IGES"""

import logging

from OCC import BRepPrimAPI

from OCCDataExchange.iges import IgesExporter
from OCCDataExchange import path_from_file

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s :: %(levelname)6s :: %(module)20s :: %(lineno)3d :: %(message)s')

# First create a simple shape to export
box_shape = BRepPrimAPI.BRepPrimAPI_MakeBox(50, 50, 50).Shape()
sphere_shape = BRepPrimAPI.BRepPrimAPI_MakeSphere(20).Shape()

# Export to IGES
filename = path_from_file(__file__, "./models_out/result_export_multi.iges")
my_iges_exporter = IgesExporter(filename, format="5.3")
my_iges_exporter.add_shape(box_shape)
my_iges_exporter.add_shape(sphere_shape)
my_iges_exporter.write_file()
