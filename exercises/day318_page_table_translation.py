"""Day 318: Two-Level Page Table Translation."""

class MMU:
    def __init__(self):
        self.page_directory = {}

    def map_page(self, vaddr, paddr):
        # 32-bit: 10 bit dir, 10 bit table, 12 bit offset
        pde_idx = (vaddr >> 22) & 0x3FF
        pte_idx = (vaddr >> 12) & 0x3FF
        if pde_idx not in self.page_directory:
            self.page_directory[pde_idx] = {}
        self.page_directory[pde_idx][pte_idx] = (paddr >> 12)

    def translate(self, vaddr):
        pde_idx = (vaddr >> 22) & 0x3FF
        pte_idx = (vaddr >> 12) & 0x3FF
        offset = vaddr & 0xFFF
        if pde_idx in self.page_directory and pte_idx in self.page_directory[pde_idx]:
            frame = self.page_directory[pde_idx][pte_idx]
            return (frame << 12) | offset
        raise MemoryError("Page Fault")

if __name__ == "__main__":
    mmu = MMU()
    mmu.map_page(0x1000200, 0x8000200)
    phys = mmu.translate(0x1000205)
    assert phys == 0x8000205
    print("Day 318 MMU Translation tests passed!")
