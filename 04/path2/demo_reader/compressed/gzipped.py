import gzip
from path1.demo_reader.util import writer

opener = gzip.open

if __name__ == '__main__':
    writer.main(opener)