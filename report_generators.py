import os

def gen_agg_report(jmx_filename):
    jtl_filename = jmx_filename.split('.')[0] + ".jtl"
    jmx_file_loc = f"jmx/{jmx_filename}"
    jmeter_bin = "jmeter-app\\bin\\jmeter.bat"
    command_jtl = f"{jmeter_bin} -n -t {jmx_file_loc} -l jtl/{jtl_filename}"
    
    os.system(command_jtl)

    aggregate_report_name = jmx_filename.split('.')[0] + "_aggregateReport.csv"
    jmeterCMDPlugin_bin = "jmeter-app\\bin\\JMeterPluginsCMD.bat"
    command_aggregateReport = f"{jmeterCMDPlugin_bin} --generate-csv aggregate_report/{aggregate_report_name} --input-jtl jtl/{jtl_filename} --plugin-type AggregateReport"
    os.system(command_aggregateReport)
    return aggregate_report_name