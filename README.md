# lokaal

Je maakt de nodige classes, zodat volgende code
Traject traject1 = new Traject("java");
Traject traject2 = new Traject(".net");
Cursist cursist1 = new Cursist("Felix", "De Vliegher", traject1);
Cursist cursist2 = new Cursist("Koen", "Vanhoutte", traject2);
Cursist cursist3 = new Cursist("Serge", "Vereecke", traject2);
Cursist cursist4 = new Cursist("Freddy", "Himpe", traject1);
Trainer trainer = new Trainer("Hans", "Desmet");
Lokaal lokaal = new Lokaal(11, trainer);
lokaal.cursistToevoegen(cursist1);
// een lokaal heeft een variabel aantal cursisten
lokaal.cursistToevoegen(cursist2);
lokaal.cursistToevoegen(cursist3);
lokaal.cursistToevoegen(cursist4);
System.out.println(lokaal);


volgende output geeft:
Lokaal 11 Hans Desmet
4 cursisten:
Felix De Vliegher volgt java
Koen Vanhoutte volgt .net
Serge Vereecke volgt .net
Freddy Himpe volgt java
