import h5py

f = h5py.File('datarec.bin', 'r')
print(*f['dataset'])