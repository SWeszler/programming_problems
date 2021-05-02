# Implement a buffered file reader

# This class is given.
class BlockReader:

    def Read4096(self, buf):
        """
        Reads the next 4096 bytes from a file, copies it into the given buffer. 

        Returns the actual number of bytes read.
        This will equal 4096 except when it has reached the end-of-file. 
        """
        bytes_read = 0
        return bytes_read


class ArbitraryReader:
    def __init__(self):
       self.reader = BlockReader()

    def Read(self, buf, bytes_to_read):
        """
        Reads the next |bytes_to_read| bytes, and copies it into the given buffer.
        Returns the actual number of bytes read.
        """
        bytes_read = 0

        while bytes_to_read > 0:
            bytes_read = self.reader.Read4096(buf)
            buf += bytes_read

        return bytes_read


ar = ArbitraryReader()
width = 4
height = 4
buf = 0
bytes_read = ar.Read(width * height * 4)
          
	
