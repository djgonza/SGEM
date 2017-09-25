class Factura (object):

    def __init__(self, base_imponible,iva,descuento):
       self.base_imponible = base_imponible;
       self.iva = iva;
       self.descuento = descuento;

    def base_con_descuento(self):
        return self.base_imponible - self.base_imponible * self.descuento / 100

    def total_iva_incluido(self):
        return self.base_con_descuento()+(self.base_con_descuento()*self.iva/100)
