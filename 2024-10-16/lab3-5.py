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
            'A': '00',
            'C': '01',
            'G': '10',
            'T': '11'
        }           #последовательность => бинарный вид
        binary_string = ''.join([nucleotide_to_binary[nuc] for nuc in self._dna_sequence])

        compressed = int(binary_string, 2)  #из бинарной строки в целое число
        return compressed
    
    def decompress(self):   #метод для распаковки данных
        binary_to_nucleotide = {
            '00': 'A',
            '01': 'C',
            '10': 'G',
            '11': 'T'
        }    #из целого число обратно в бинарную строку
        binary_string = bin(self._compressed_sequence)[2:].zfill(len(self._dna_sequence) * 2)
        
        decompressed = ''.join([binary_to_nucleotide[binary_string[i:i+2]]  #разбиваем бинарную строку по 2 символа и декодируем
                                for i in range(0, len(binary_string), 2)])
        return decompressed
    
    def __str__(self):  #представляем строкой
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