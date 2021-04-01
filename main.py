import create_dir as cd
import report_generators as rg
import convert_to_html as cth
import os

cd.create_dir()
filename = "demo_opencart.jmx"
csvfilename = rg.gen_agg_report(filename)
cth.convert_to_html(csvfilename)