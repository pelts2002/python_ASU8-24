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
    
    def _compress(self):    #приватный метод для сжатия ДНК
        nucleotide_to_binary = {
            'A': 0b00,
            'C': 0b01,
            'G': 0b10,
            'T': 0b11
        }
        
        compressed = 0
        for nuc in self._dna_sequence:
            compressed <<= 2  #сдвиг влево на 2 бита для каждого нуклеотида
            compressed |= nucleotide_to_binary[nuc]  #добавляем новые биты с помощью побитового ИЛИ
        
        return compressed
    
    def decompress(self):   #метод для распаковки данных
        binary_to_nucleotide = {
            0b00: 'A',
            0b01: 'C',
            0b10: 'G',
            0b11: 'T'
        }
        
        decompressed = []
        compressed_copy = self._compressed_sequence
        #обходим последовательность справа налево, извлекая по 2 бита (1 нуклеотид за раз)
        for _ in range(len(self._dna_sequence)):
            # Извлекаем последние 2 бита и получаем нуклеотид
            decompressed.append(binary_to_nucleotide[compressed_copy & 0b11])
            compressed_copy >>= 2  # Сдвигаем число вправо на 2 бита
        
        return ''.join(reversed(decompressed))  # Обратно переворачиваем последовательность
    
    def __str__(self):  #строковое представление распакованной последовательности ДНК.
        return self.decompress()


# Тестирование класса
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