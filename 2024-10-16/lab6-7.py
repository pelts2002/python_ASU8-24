class DNASequence:
    def __init__(self, dna_sequence: str):
        """
        Инициализация экземпляра с передачей строковой последовательности ДНК.
        Проверяем, что введенная последовательность является строкой
        """
        if not isinstance(dna_sequence, str):
            raise ValueError("Последовательность ДНК должна быть строкой.")
        
        self._dna_sequence = dna_sequence.replace("\n", "").replace(" ", "").upper()    #убираем пробелы и перевод строк
        self._compressed_sequence = self._compress()    #сжимаем последовательность при инициализации
    
    def _compress(self):    #приватный метод для сжатия ДНК с использованием if,elif,else.
        compressed = 0
        for nuc in self._dna_sequence:
            compressed <<= 2    #сдвиг влево на 2 бита для каждого нуклеотида
            if nuc == 'A':
                compressed |= 0b00  # A -> 00
            elif nuc == 'C':
                compressed |= 0b01  # C -> 01
            elif nuc == 'G':
                compressed |= 0b10  # G -> 10
            elif nuc == 'T':
                compressed |= 0b11  # T -> 11
            else:
                raise ValueError(f"Недопустимый символ в последовательности ДНК: {nuc}")
        return compressed
    
    def decompress(self):   #метод распаковки данных в строку нуклеотидов.Побитово!
        decompressed = []
        compressed_copy = self._compressed_sequence
        for _ in range(len(self._dna_sequence)):
            last_two_bits = compressed_copy & 0b11
            if last_two_bits == 0b00:
                decompressed.append('A')
            elif last_two_bits == 0b01:
                decompressed.append('C')
            elif last_two_bits == 0b10:
                decompressed.append('G')
            elif last_two_bits == 0b11:
                decompressed.append('T')
            compressed_copy >>= 2 
        return ''.join(reversed(decompressed))  #обратно переворачиваем последовательность
    
    def __str__(self):
        return self.decompress()

dna_sequence = """
ctcacctgcgacgtggttggctgtgacgaaatgattgccgagctaccgatcaggcccacc
agagaataaaacacgcagaagtccgaaatattaactaacgcgtgaggaacatccttcacc
caacgcgcagtggtaaacgacacatatcacagctggacctggcccgtttctcaggataga
ttccgcataggatattcgtatacctcttgtgcacttgcgttaccatacaaatcatacacg
atgttgctccaatccagtggggaacaggctctagctgttgcttttaattgtctaccgact
actcaccagtgacaaacagaattattgcggatgtcgttatgctctgttttcatggcatct
gtccgccgtagaaccttttccagcgttctaaagtcgcgcaatggtttttcccgcacaagt
tcctcccggacatctagttctgttaggaaaagatcggagtgagcgcagcactagtcatgc
atcattactatgccaaccaaaacggggtccggcatgagcccctttcgggggccagacgat
aacacaaggtcaatgtggtgagccactgtgaaaaaaagtgcctgtagtagagcttcgaag
attggatgtgcaatcaccggtctatcctttgcatctgacgttgtgtgcccagatgcattc
gtgctctcaatataacaacgggcaggtgttacctacttaagtgtttctatagtctaactt
ttgtcgcagcgccccctccagcactaaactgtaaatgtccaaacttacgtactaagtagt
gttatcggaatacccttataccgccgcggaacaagatgaatacgcgagccatctctagac
cacagataactgacgtgatcgcattggaaaccgacagaggcgattcgcctgttcctaccg
aacggacgccagggtctaggacactttaactcgtaaaataacttgcgtgggaggttacat
gcggcctacctgtcgatcctagtagaggtcgggtgagacc
"""

dna_obj = DNASequence(dna_sequence) #объект класса

print("Распакованная последовательность:", str(dna_obj))

print("Результат распаковки:", dna_obj.decompress())

print("Сжатая последовательность (целое число):", dna_obj._compressed_sequence)