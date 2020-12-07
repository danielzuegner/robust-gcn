# Certifiable Robustness and Robust Training for GCN

<p align="center">
<img src="https://www.in.tum.de/fileadmin/w00bws/daml/robust-gcn/figure_small.png" width="400">
</p>

Implementation of the paper:   
**[Certifiable Robustness and Robust Training for Graph Convolutional Networks](https://arxiv.org/abs/1906.12269)**

by Daniel Zügner and Stephan Günnemann.   
Published at KDD'19, August 2019, Anchorage, USA

Copyright (C) 2019   
Daniel Zügner   
Technical University of Munich    

## Additional resources
[[Paper](https://arxiv.org/pdf/1906.12269.pdf) | [Poster](https://www.in.tum.de/fileadmin/w00bws/daml/robust-gcn/robust_gcn_poster.pdf) | [Slides (KDD 2019)](https://www.in.tum.de/fileadmin/w00bws/daml/robust-gcn/kdd2019_presentation_flattened.pdf)]

## Run the code
 
The fastest way to try our code is to use the Jupyter notebook `demo.ipynb`.

## Requirements
* Python 3.6 or newer
* `numpy`
* `scipy`
* `scikit-learn`
* `pytorch`
* `matplotlib` (for the demo notebook)

`tqdm` is recommended for displaying progress bars.

## Installation
`python setup.py install`

If you just want to add a symbolic link to your package directory run   
`python setup.py develop`
 
## Contact
Please contact zuegnerd@in.tum.de in case you have any questions.


## References
### Datasets
In the `data` folder we provide the following datasets originally published by   
#### Cora
McCallum, Andrew Kachites, Nigam, Kamal, Rennie, Jason, and Seymore, Kristie.  
*Automating the construction of internet portals with machine learning.*   
Information Retrieval, 3(2):127–163, 2000.

and the graph was extracted by

Bojchevski, Aleksandar, and Stephan Günnemann. *"Deep gaussian embedding of   
attributed graphs: Unsupervised inductive learning via ranking."* ICLR 2018.

#### Citeseer
Sen, Prithviraj, Namata, Galileo, Bilgic, Mustafa, Getoor, Lise, Galligher, Brian, and Eliassi-Rad, Tina.   
*Collective classification in network data.*   
AI magazine, 29(3):93, 2008.
#### PubMed
Sen, Prithviraj, Namata, Galileo, Bilgic, Mustafa, Getoor, Lise, Galligher, Brian, and Eliassi-Rad, Tina.   
*Collective classification in network data.*   
AI magazine, 29(3):93, 2008.

### Graph Convolutional Networks
Our implementation of the GCN algorithm is based on the authors' implementation,
available on GitHub [here](https://github.com/tkipf/gcn).

The paper was published as  

Thomas N Kipf and Max Welling. 2017.  
*Semi-supervised classification with graph
convolutional networks.* ICLR (2017).

## Cite
Please cite our paper if you use the model or this code in your own work:

```
@inproceedings{zugner2019robustgcn,
  title={Certifiable Robustness and Robust Training for Graph Convolutional Networks},
  author={Z{\"u}gner, Daniel and G{\"u}nnemann, Stephan},
  booktitle = {Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery \&\#38; Data Mining},
  year={2019},
  publisher = {ACM},
  address = {New York, NY, USA},
location = {Anchorage, United States},
}

```
