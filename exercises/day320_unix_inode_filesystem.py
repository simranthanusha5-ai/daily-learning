"""Day 320: Unix Inode Filesystem."""

class Inode:
    def __init__(self, inode_num, is_dir=False):
        self.inode_num = inode_num
        self.is_dir = is_dir
        self.direct_blocks = []
        self.size = 0

class MiniUnixFS:
    def __init__(self):
        self.inodes = [Inode(0, is_dir=True)] # Root inode 0
        self.data_blocks = {}
        self.next_block = 0

    def write_file(self, filename, data: bytes):
        ino = Inode(len(self.inodes), is_dir=False)
        blk_id = self.next_block
        self.next_block += 1
        self.data_blocks[blk_id] = data
        ino.direct_blocks.append(blk_id)
        ino.size = len(data)
        self.inodes.append(ino)
        return ino.inode_num

    def read_file(self, inode_num):
        ino = self.inodes[inode_num]
        return b"".join(self.data_blocks[b] for b in ino.direct_blocks)

if __name__ == "__main__":
    fs = MiniUnixFS()
    ino = fs.write_file("test.txt", b"Unix Inode Architecture")
    assert fs.read_file(ino) == b"Unix Inode Architecture"
    print("Day 320 Unix Inode FS tests passed!")
