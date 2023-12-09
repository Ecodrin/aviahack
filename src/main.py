import shutil
import os
from file_enumerate import enumerate
from file_downenumerate import downenumerate
from data_loader import loader


def main():
    loader()
    enumerate()
    downenumerate()


if __name__ == '__main__':
    main()
