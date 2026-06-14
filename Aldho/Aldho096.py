class LUCIUS:
    def __init__(self, nilai):
        self.data = nilai
        self.shape = self._ukuran()
        self.dtype = self._tipe_data()

    def _ukuran(self):
        ukuran = []
        temp = self.data

        while isinstance(temp, list):
            ukuran.append(len(temp))
            temp = temp[0]

        return tuple(ukuran)

    def _tipe_data(self):
        temp = self.data

        while isinstance(temp, list):
            temp = temp[0]

        return temp.__class__.__name__

    def format_matrix(self):
        return "\n".join(map(str, self.data)) + "\n"

    def lucipose(self):
        if len(self.shape) != 2:
            raise ValueError(
                "Transpose saat ini hanya didukung untuk matriks 2 dimensi.")

        hasil = [
            [baris[kolom] for baris in self.data]
            for kolom in range(self.shape[1])
        ]

        return LUCIUS(hasil)

    def __repr__(self):
        teks = [
            self.format_matrix(),
            f"Tipe Data = {self.dtype}",
            f"Ukuran = {self.shape}"
        ]
        return "\n".join(teks)