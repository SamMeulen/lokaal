from domain.Trajekt import Trajekt
from domain.Trainer import Trainer
from domain.Lokaal import Lokaal
from domain.Cursist import Cursist

trajekt1 = Trajekt("java")
trajekt2 = Trajekt(".net")

cursist1 = Cursist("Felix", "De Vliegher", trajekt1)
cursist2 = Cursist("Serge", "Vereecke", trajekt2)
cursist3 = Cursist("Freddy", "Himpe", trajekt1)
cursist4 = Cursist("Felix", "De Vliegher", trajekt1)

trainer = Trainer("Hans", "Desmet")

lokaal = Lokaal(11, trainer)

lokaal.cusist_toevoegen(cursist1)
lokaal.cusist_toevoegen(cursist2)
lokaal.cusist_toevoegen(cursist3)
lokaal.cusist_toevoegen(cursist4)

lokaal.print_info()
