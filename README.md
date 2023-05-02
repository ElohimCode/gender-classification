# Gender Classification 


### Task
```A gender classification model trained using gender datasets from kaggle. It was trained using tensorflow pipeline```

### Summary
---
Gender classification is an aspect of computer vision and it has application in engineering and computer science.
The model is built using tensorflow pipeline with n_epoch=10.

**Author**: Johnbull Vitowanu (Software Engr)

**Input Data**

*Image Number*: 11649 files (Kaggle gender validation dataset)

*Number of classes*: 2 classes (female, male).

**Architecture**
```
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 254, 254, 16)      448       
                                                                 
 max_pooling2d (MaxPooling2D  (None, 127, 127, 16)     0         
 )                                                               
                                                                 
 conv2d_1 (Conv2D)           (None, 125, 125, 32)      4640      
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 62, 62, 32)       0         
 2D)                                                             
                                                                 
 conv2d_2 (Conv2D)           (None, 60, 60, 16)        4624      
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 30, 30, 16)       0         
 2D)                                                             
                                                                 
 flatten (Flatten)           (None, 14400)             0         
                                                                 
 dense (Dense)               (None, 256)               3686656   
                                                                 
 dense_1 (Dense)             (None, 1)                 257       
                                                                 
=================================================================
Total params: 3,696,625
Trainable params: 3,696,625
Non-trainable params: 0
_________________________________________________________________
```

**Accuracy Result on Test data**
```
tf.Tensor(0.92409533, shape=(), dtype=float32) tf.Tensor(0.955542, shape=(), dtype=float32) tf.Tensor(0.9401042, shape=(), dtype=float32)
```


### Installation
- Clone the repository
- Get python IDLE installed
- Upgrade pip with ```python -m pip install --upgrade pip```
- Activate virtual environment to manage the packages
-  Run *pip numpy, matplotlib, opencv-python tensorflow*
- Run main.py ```py main.py```

### Project Structure
```
├── .gitignore                      # Git use it to ignore file while tracking files
├── README.md                       # readme file
└── Gender-Classification
    ├── colab
    │   ├── datasets                # gender datasets  - sub-directory (female, male)
    │   ├── logs                    # log directory for n_poch=5
    │   ├── modells                 # model directory trained with n_poch=5
    │   ├── classification.ipynb    # Colab file used to train the model
    │   ├── main.py                 # main file
    │   └── utils               # Funct5ions to create plots in bokeh
    │  
    ├── logs                        # log directory for n_poch=5
    └── models                      # model directory trained with n_poch=5

```

### Miscellaneous
- ```__init__.py``` convert the folder to python package

