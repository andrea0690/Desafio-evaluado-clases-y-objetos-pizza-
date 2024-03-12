from ingredientes import MASA_OPTS, VEGETALES_OPTS, PROTEINAS_OPTS


class Pizza():
   
    proteina    = None
    vegetal_1   = None
    vegetal_2   = None
    masa        = None
    
    @staticmethod
    def validar_opcion(opcion: str , opciones: list):
        if opcion in opciones:
            return True
        else:
            return False
    
    def pedido(self):
        self.proteina = input('''Elija una opcion de proteina: 
                         - Pollo
                         - Vacuno
                         - Carne vegetal
                         ''').lower()
        
        self.vegetal_1 = input('''Ingrese el primer vegetal a elegir: 
                          - Tomate
                          - Aceitunas
                          - Champiñones 
                          ''').lower()
        
        self.vegetal_2 = input ('''Ingrese el segundo vegetal a elegir: 
                           - Tomate
                          - Aceitunas
                          - Champiñones 
                           ''').lower()
        
        self.masa = input( '¿Qué tipo de masa desea?, Tradicional ó delgada: ').lower()
        
        is_valid_proteina  = self.validar_opcion(self.proteina, PROTEINAS_OPTS)
        is_valid_vegetal_1 = self.validar_opcion(self.vegetal_1, VEGETALES_OPTS)
        is_valid_vegetal_2 = self.validar_opcion(self.vegetal_2, VEGETALES_OPTS)
        is_valid_masa      = self.validar_opcion(self.masa, MASA_OPTS)
        
        self.valido = is_valid_proteina and is_valid_vegetal_1 and is_valid_vegetal_2 and is_valid_masa
        
        