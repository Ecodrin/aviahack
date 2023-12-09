import h5py
import numpy as np

test_data = np.random.random((16,16,16))

f = h5py.File("data.bin", "w")
dset = f.create_dataset("mydataset", data=test_data)