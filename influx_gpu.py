#!/usr/bin/python
import csv
import subprocess

output = []

def parse_csv(file):

    #data = []
    #csv_f = csv.reader(file)
    #for row in csv_f:
     #   data.append(row)

    data = [line.split(',') for line in file.splitlines()]

    headers = sanitize(data.pop(0))

    tag_count = 3
    #Tags
    for gpu_object in data:
        tags = sanitize(gpu_object[:tag_count])
        metrics = gpu_object[tag_count:]

        header_string = "gpu"

        for index, tag in enumerate(tags):
            header_string += ",{header}={tag}".format(tag=tag, header=headers[index])



        for index, metric in enumerate(metrics):
            out_string = header_string
            out_string += ",metric={header}".format(header=headers[index + tag_count])
            out_string += " "
            out_string += "value={metric}".format(metric=cleanMetric(metric))

            output.append(out_string)

#Remove spaces and whitespace from all members of an array
def sanitize(array):
    to_return = []
    for item in array:
        item = item.strip()
        item = item.replace(" ", "-")
        to_return.append(item)

    return to_return

#Cleans a metric for display
def cleanMetric(metric):
    metric = metric.strip()
    metric = float(metric)
    return metric

if __name__ == '__main__':
    nvidia_smi_path = "nvidia-smi"
    nvidia_smi_query = ("--query-gpu="
                        "name,"
                        "uuid,"
                        "pci.bus_id,"
                        "temperature.gpu,"
                        "utilization.gpu,"
                        "utilization.memory,"
                        "power.draw,clocks.sm,"
                        "clocks.mem,"
                        "clocks.gr")

    nvidia_smi_format = "--format=csv,nounits"
    try:
        smi_output = subprocess.check_output([nvidia_smi_path, nvidia_smi_query, nvidia_smi_format])
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    parse_csv(smi_output)

    for string in output:
        print(string)
