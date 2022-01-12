from Fuvar import Fuvar

class Fuvarok:
    def __init__(self, file_name):
        self._fuvar_list = []

        with open(file_name, "r", encoding="utf-8") as file:
            self.first_line_of_file = file.readline()

            lines = file.readlines()

            for line in lines:
                self._fuvar_list.append(Fuvar(line))

    @property
    def fuvar_list(self):
        return self._fuvar_list
    
    def get_fuvars_by_id(self, id):
        return list(filter(lambda fuvar: fuvar.taxi_id == id, self._fuvar_list))
    
    def get_sum_of_money(self, my_list):
        return sum(fuvar.viteldij + fuvar.borravalo for fuvar in my_list)

    def statistic(self):
        dict = {}
        for fuvar in self._fuvar_list:
            if fuvar.fizetes_modja in dict: 
                dict[fuvar.fizetes_modja] += 1
            else:
                dict[fuvar.fizetes_modja] = 1
        return dict

    def get_all_km(self):
        return sum(fuvar.tavolsag for fuvar in self._fuvar_list)

    def get_longest_fuvar(self):
        return max(self._fuvar_list, key = lambda fuvar: fuvar.idotartam)
    
    def write_errors(self):
        with open("hibak.txt", "w", encoding="utf-8") as file:
            error_list = list(filter(lambda fuvar: (fuvar.idotartam > 0 and fuvar.viteldij > 0) and fuvar.tavolsag == 0, self._fuvar_list))
            error_list.sort(key = lambda fuvar: fuvar.indulas)
                
            text = self.first_line_of_file
            for fuvar in error_list:
                text += str(fuvar)
            
            file.write(text)

        print("8.feladat: hibak.txt")