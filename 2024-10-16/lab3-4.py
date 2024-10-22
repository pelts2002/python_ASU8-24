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
        compressed = ''.join([nucleotide_to_binary[nuc.upper()] for nuc in self._dna_sequence])
        return compressed
    
    def decompress(self):   #метод для распаковки данных
        binary_to_nucleotide = {
            '00': 'A',
            '01': 'C',
            '10': 'G',
            '11': 'T'
        }    #разбиваем бинарную строку по 2 символа и декодируем
        decompressed = ''.join([binary_to_nucleotide[self._compressed_sequence[i:i+2]] 
                                for i in range(0, len(self._compressed_sequence), 2)])
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