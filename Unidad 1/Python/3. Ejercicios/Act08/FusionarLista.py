class FusionarLista:

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def fusionar(self):
        nuevo = []
        for i in range(len(self.list1)):
            nuevo.append([self.list1[i], self.list2[i]])
        return nuevo