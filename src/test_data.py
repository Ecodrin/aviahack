import numpy as np
import h5py 

test_data = np.random.random((16,16,16))

print(test_data)

hp5_file = h5py.File('data.bin', 'w')
hp5_file.create_dataset('dataset', data=test_data)
