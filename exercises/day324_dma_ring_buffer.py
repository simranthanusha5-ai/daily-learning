"""Day 324: DMA Descriptor Ring Buffer."""

class RXDescriptor:
    def __init__(self, dma_addr, length):
        self.dma_addr = dma_addr
        self.length = length
        self.ready_by_hw = False

class NICRingBuffer:
    def __init__(self, size=4):
        self.descriptors = [RXDescriptor(i * 1024, 0) for i in range(size)]
        self.head = 0
        self.tail = 0

    def hw_dma_receive(self, packet_bytes):
        desc = self.descriptors[self.tail]
        desc.length = len(packet_bytes)
        desc.ready_by_hw = True
        self.tail = (self.tail + 1) % len(self.descriptors)

    def driver_poll(self):
        desc = self.descriptors[self.head]
        if desc.ready_by_hw:
            desc.ready_by_hw = False
            self.head = (self.head + 1) % len(self.descriptors)
            return desc.length
        return None

if __name__ == "__main__":
    nic = NICRingBuffer(4)
    nic.hw_dma_receive(b"ethernet_frame")
    pkt_len = nic.driver_poll()
    assert pkt_len == 14
    print("Day 324 DMA Ring Buffer tests passed!")
