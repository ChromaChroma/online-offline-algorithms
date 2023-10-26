# De Algen : online-offline-algorithms

This codebase includes the [offline, online algorithms](./src/algorithms) described in the paper of the course Algorithms for Decision Support.
It also includes a [performance_test.py](./src/performance_test.py) module to run iteration of computational performance test and its average cost.
These performance measurements are plotted in box plots using [plotting.py](./src/plotting.py).

Instances that we used and others that can be run are located in the [instances](./instances) directory.
These instance text files are being read and parsed by our [parser](./src/instance_parser.py)

A preview of the general performance of our algorithms can be seen in a sampled plot.
![](./plots/all-algs.png)