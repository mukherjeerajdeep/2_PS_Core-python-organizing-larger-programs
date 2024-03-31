import gzip

# instead of this absolute import we can use the below relative import
# absolute
# from demo_reader.util import writer

# Relative
# from ..util import writer

from demo_reader.util.writer import main
from ..util.writer import main
from demo_reader.util.deeper.trans import trans
from ..util.deeper.trans import trans

opener = gzip.open

if __name__ == '__main__':
    main(opener)
    trans()