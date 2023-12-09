import openfoamparser as Ofpp
import struct


def parser():
    p = Ofpp.parse_internal_field('data_wage/high_dim/vel3.0/0.1/p')
    print(p.shape)
    p.tofile("pressure_data.bin")