import openfoamparser as Ofpp
import h5py 

U = Ofpp.parse_internal_field('data_wage/high_dim/vel3.0/0.1/U')
p = Ofpp.parse_internal_field('data_wage/high_dim/vel3.0/0.1/p')
T = Ofpp.parse_internal_field('data_wage/high_dim/vel3.0/0.1/T')
rho = Ofpp.parse_internal_field('data_wage/high_dim/vel3.0/0.1/rho')


h5f = h5py.File('U_data.hdf5', 'w')
h5f.create_dataset('dataset', data=U)

h5f = h5py.File('U_data.hdf5', 'w')
h5f.create_dataset('dataset', data=p)

h5f = h5py.File('U_data.hdf5', 'w')
h5f.create_dataset('dataset', data=T)

h5f = h5py.File('U_data.hdf5', 'w')
h5f.create_dataset('dataset', data=rho)
