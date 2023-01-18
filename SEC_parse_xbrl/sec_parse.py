import csv
import pprint
import pathlib
import collections
import xml.etree.ElementTree as ET

import os
import sys


# get current working directory
cwd = os.getcwd()

# get all files in current working directory
files = os.listdir(cwd)

# get all xbrl files in current working directory
xbrl_files = [f for f in files if f.endswith('.xbrl')]

# get first xbrl file
xbrl_file = xbrl_files[0]

# parse xbrl file
xbrl_obj = xbrl.XBRL(xbrl_file)

# get all facts in xbrl file
facts = xbrl_obj.facts

# get all facts in xbrl file with context ref
facts_with_context = xbrl_obj.facts_with_context

# get all facts in xbrl file with context ref and unit ref
facts_with_context_and_unit = xbrl_obj.facts_with_context_and_unit


sec_directory = pathlib.Path.cwd().joinpath("apple10K")

# define file paths to the documents

file_htm = sec_directory.joinpath('.htm').resolve()
file_cal = sec_directory.joinpath('.xml').resolve()
file_lab = sec_directory.joinpath('.xml').resolve()
file_def = sec_directory.joinpath('.xml').resolve()


storage_list = []
storage_values = {}
storage_gaap = {}


FilingTuple = collections.namedtuple(
    'FilingTuple', ['file_path', 'namespace_root', 'namespace_label'])

files_list = [
    FilingTuple(
        file_cal, r'{http://www.xbrl.org/2003/linkbase}calculationLink', 'calculation'),
    FilingTuple(
        file_def, r'{http://www.xbrl.org/2003/linkbase}definitionLink', 'definition'),
    FilingTuple(
        file_lab, r'{http://www.xbrl.org/2003/linkbase}labelLink', 'label'),
]

avoids = ['linkbase' 'roleRef']
parse = ['label', 'lanelLink', 'labelArc', 'loc',
         'definitionLink', 'definitionArc', 'calculationArc']

lab_list = set()
cal_list = set()

for file in files_list:
    tree = ET.parse(file.file_path)

    elements = tree.findall(file.namespace_element)
