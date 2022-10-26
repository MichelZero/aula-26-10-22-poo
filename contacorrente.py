#
from conta import Conta as C

class ContaCorrente(C):
  def __init__(self, agencia, conta, saldo, limite =100) -> None:
    super().__init__(agencia, conta, saldo)
    self._limite = limite
    
  #get
  @property
  def limite(self):
    return self._limite
  
  def sacar(self, valor):
    if (self.saldo + self.limite) < valor:
      print("saldo insuficiente!")
      return
    self.saldo -= valor
    self.detalhes()