import unittest
import tempfile
import os

#################
import sysutils

lipsum = b"""Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Vivamus
eu elit convallis, pellentesque lacus eu, luctus arcu.  In tempus vulputate
tortor, non facilisis mi pharetra quis. Donec dui orci, pharetra non
condimentum vel, feugiat mattis lectus. In nec erat a augue semper varius
euismod nec massa.  Praesent mauris orci, rhoncus ac porttitor sed, molestie
non urna. Phasellus in elit eleifend, egestas dolor non, feugiat dui. Etiam
hendrerit leo ac mollis dignissim. Sed tellus metus, porta a mattis quis,
suscipit eu velit. Sed at elementum sem. In sit amet nisl tempus, tincidunt
augue ac, viverra magna. Ut nec porttitor lorem. Donec scelerisque turpis et
metus consequat ullamcorper.  Phasellus rutrum id ligula in congue."""

lipsum_sha256_checksum\
    = '1191759d52ffe6e17171f385dee4b6015bb1cba5f85b35f3709cfd1c5f8fe69b'

class TestCase(unittest.TestCase):

    def test_checksum(self):

        f = tempfile.NamedTemporaryFile(delete=False)
        f.write(lipsum)
        f.close()

        self.assertTrue(
            sysutils.checksum(f.name) == lipsum_sha256_checksum
        )

        os.unlink(f.name)
