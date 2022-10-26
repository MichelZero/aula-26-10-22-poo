#
from abc import ABC, abstractmethod

class Conta(ABC):
  def __init__(self, agencia, conta, saldo) -> None
    self._agencia = agencia
    self._conta = conta
    self._saldo = saldo
    
  #get
  @property
  def agencia(self):
    return self._agencia
  
  @property
  def conta(self):
    return self._conta
  
  @property
  def saldo(self):
    return self._saldo
  
  #set
  @saldo.setter
  def saldo(self, valor):
    if not isinstance(valor, ((int, float))):
      raise ValueError("Valor precisa ser numérico")
    self._saldo = valor
    
  def depositar(self, valor):
    if not isinstance(valor, ((int, float))):
      raise ValueError("Valor precisa ser numérico")
    self._saldo += valor
    
  @abstractmethod
  def sacar(self, valor):
    pass
  
  def detalhes(self):
    print(f"agencia:{self.agencia}", end=' ')
    print(f"conta:{self.conta}", end=' ')
    print(f"saldo:{self.saldo}")