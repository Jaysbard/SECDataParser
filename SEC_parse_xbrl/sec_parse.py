import csv
import pprint
import pathlib
import collections
import xml.etree.ElementTree as ET

# define our working directory

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
