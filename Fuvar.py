from datetime import datetime

class Fuvar:
    
    def __init__(self, line):

        data = line.split(";")

        self._taxi_id = int(data[0])
        self._indulas = datetime.strptime(data[1], '%Y-%m-%d %H:%M:%S')
        self._idotartam = int(data[2])
        self._tavolsag = float(data[3].replace(',', '.'))
        self._viteldij = float(data[4].replace(',', '.'))
        self._borravalo = float(data[5].replace(',', '.'))
        self._fizetes_modja = data[6]

    @property
    def taxi_id(self):
        return self._taxi_id
    
    @taxi_id.setter
    def taxi_id(self, value):
        self._taxi_id = value

    @property
    def indulas(self):
        return self._indulas
    
    @indulas.setter
    def indulas(self, value):
        self._indulas = value
    
    @property
    def idotartam(self):
        return self._idotartam
    
    @idotartam.setter
    def idotartam(self, value):
        self._idotartam = value

    @property
    def tavolsag(self):
        return self._tavolsag
    
    @tavolsag.setter
    def tavolsag(self, value):
        self._tavolsag = value
    
    @property
    def viteldij(self):
        return self._viteldij
    
    @viteldij.setter
    def viteldij(self, value):
        self._viteldij = value

    @property
    def borravalo(self):
        return self._borravalo
    
    @borravalo.setter
    def borravalo(self, value):
        self._borravalo = value
    
    @property
    def fizetes_modja(self):
        return self._fizetes_modja
    
    @fizetes_modja.setter
    def fizetes_modja(self, value):
        self._fizetes_modja = value

    def __str__(self):
        return f"{ self.taxi_id };{ self.indulas };{ self.idotartam };{ self.tavolsag };{ self.viteldij };{ self.borravalo };{ self.fizetes_modja }"