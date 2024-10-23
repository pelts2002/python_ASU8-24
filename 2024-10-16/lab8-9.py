import sys

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
                compressed |= 0b00 
            elif nuc == 'C':
                compressed |= 0b01 
            elif nuc == 'G':
                compressed |= 0b10
            elif nuc == 'T':
                compressed |= 0b11 
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
            compressed_copy >>= 2  #сдвигаем число вправо на 2 бита
        return ''.join(decompressed[::-1])  #возвращаем последовательность в правильном порядке с помощью обратного среза
    
    def __str__(self):
        return self.decompress()


    def print_memory_usage(self):   #метод для вывода оригинального и сжатого размера 
        original_size = sys.getsizeof(self._dna_sequence)  
        compressed_size = sys.getsizeof(self._compressed_sequence)  
        print(f"Оригинальный размер последовательности: {original_size} байт(а)")
        print(f"Сжатый размер последовательности: {compressed_size} байт(а)")


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

dna_obj = DNASequence(dna_sequence) #создаем объект класса

dna_obj.print_memory_usage()    #выводим оригинальный и сжатый размер

print("Распакованная последовательность:", str(dna_obj))