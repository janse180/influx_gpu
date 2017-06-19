# InfluxDB Nvidia GPU Parser
## Matt Jansen
This script parses GPU data from Nvidia SMI and outputs it to stdout in the InfluxDB line protocol format. Adding metrics is as simple as updating the 'nvidia_smi_query' string.

GPUs are tagged with the following:
* GPU Name
* GPU UUID
* GPU PCI Slot ID
* Metric Name

A seperate influx entry is created for each of the following metrics per GPU:
* GPU Temperature
* GPU Power Draw
* GPU Core Utilization
* GPU Memory Utilization
* GPU Core Clock Speed 
* GPU Memory Clock Speed 
* GPU Core Streaming Multiprocessor Clock Speed 

Example usage with telegraf: 
```
 [[inputs.exec]]
  commands = ["/influx_gpu.py"]

  data_format = "influx"
```

Example output with Three GPUs:
```
gpu,name=GeForce-GTX-1070,uuid=GPU-3697a48a-fd1b-25fd-90ad-6a4361b5d032,pci.bus_id=0000:01:00.0,metric=temperature.gpu value=76.0
gpu,name=GeForce-GTX-1070,uuid=GPU-3697a48a-fd1b-25fd-90ad-6a4361b5d032,pci.bus_id=0000:01:00.0,metric=utilization.gpu-[%] value=100.0
gpu,name=GeForce-GTX-1070,uuid=GPU-3697a48a-fd1b-25fd-90ad-6a4361b5d032,pci.bus_id=0000:01:00.0,metric=utilization.memory-[%] value=100.0
gpu,name=GeForce-GTX-1070,uuid=GPU-3697a48a-fd1b-25fd-90ad-6a4361b5d032,pci.bus_id=0000:01:00.0,metric=power.draw-[W] value=128.81
gpu,name=GeForce-GTX-1070,uuid=GPU-3697a48a-fd1b-25fd-90ad-6a4361b5d032,pci.bus_id=0000:01:00.0,metric=clocks.current.sm-[MHz] value=1885.0
gpu,name=GeForce-GTX-1070,uuid=GPU-3697a48a-fd1b-25fd-90ad-6a4361b5d032,pci.bus_id=0000:01:00.0,metric=clocks.current.memory-[MHz] value=3802.0
gpu,name=GeForce-GTX-1070,uuid=GPU-3697a48a-fd1b-25fd-90ad-6a4361b5d032,pci.bus_id=0000:01:00.0,metric=clocks.current.graphics-[MHz] value=1885.0
gpu,name=GeForce-GTX-1070,uuid=GPU-a33f2be0-02f1-f7d3-edef-2a96edabade1,pci.bus_id=0000:02:00.0,metric=temperature.gpu value=82.0
gpu,name=GeForce-GTX-1070,uuid=GPU-a33f2be0-02f1-f7d3-edef-2a96edabade1,pci.bus_id=0000:02:00.0,metric=utilization.gpu-[%] value=100.0
gpu,name=GeForce-GTX-1070,uuid=GPU-a33f2be0-02f1-f7d3-edef-2a96edabade1,pci.bus_id=0000:02:00.0,metric=utilization.memory-[%] value=100.0
gpu,name=GeForce-GTX-1070,uuid=GPU-a33f2be0-02f1-f7d3-edef-2a96edabade1,pci.bus_id=0000:02:00.0,metric=power.draw-[W] value=128.46
gpu,name=GeForce-GTX-1070,uuid=GPU-a33f2be0-02f1-f7d3-edef-2a96edabade1,pci.bus_id=0000:02:00.0,metric=clocks.current.sm-[MHz] value=1898.0
gpu,name=GeForce-GTX-1070,uuid=GPU-a33f2be0-02f1-f7d3-edef-2a96edabade1,pci.bus_id=0000:02:00.0,metric=clocks.current.memory-[MHz] value=3802.0
gpu,name=GeForce-GTX-1070,uuid=GPU-a33f2be0-02f1-f7d3-edef-2a96edabade1,pci.bus_id=0000:02:00.0,metric=clocks.current.graphics-[MHz] value=1898.0
gpu,name=GeForce-GTX-1070,uuid=GPU-66cd0dab-c205-e576-8de8-0f74e4d605d3,pci.bus_id=0000:03:00.0,metric=temperature.gpu value=62.0
gpu,name=GeForce-GTX-1070,uuid=GPU-66cd0dab-c205-e576-8de8-0f74e4d605d3,pci.bus_id=0000:03:00.0,metric=utilization.gpu-[%] value=100.0
gpu,name=GeForce-GTX-1070,uuid=GPU-66cd0dab-c205-e576-8de8-0f74e4d605d3,pci.bus_id=0000:03:00.0,metric=utilization.memory-[%] value=100.0
gpu,name=GeForce-GTX-1070,uuid=GPU-66cd0dab-c205-e576-8de8-0f74e4d605d3,pci.bus_id=0000:03:00.0,metric=power.draw-[W] value=126.26
gpu,name=GeForce-GTX-1070,uuid=GPU-66cd0dab-c205-e576-8de8-0f74e4d605d3,pci.bus_id=0000:03:00.0,metric=clocks.current.sm-[MHz] value=1936.0
gpu,name=GeForce-GTX-1070,uuid=GPU-66cd0dab-c205-e576-8de8-0f74e4d605d3,pci.bus_id=0000:03:00.0,metric=clocks.current.memory-[MHz] value=3802.0
gpu,name=GeForce-GTX-1070,uuid=GPU-66cd0dab-c205-e576-8de8-0f74e4d605d3,pci.bus_id=0000:03:00.0,metric=clocks.current.graphics-[MHz] value=1936.0
```

