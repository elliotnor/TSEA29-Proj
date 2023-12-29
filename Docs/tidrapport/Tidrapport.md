Denna fil är skriven med [MarkDown](https://www.markdownguide.org/basic-syntax/)

Uppdatera tidrapporten **senast** kl 16 varje måndag, enligt Leveranser och deadlines i Lisam.
Glöm inte att även uppdatera tidplanen.

# Tidrapport Grupp 06
Svara på följande frågor i tidrapporten varje vecka:
1. Vilka framsteg har gjorts sedan förra tidrapporten?
2. Finns det några problem?
3. Vad ska göras kommande vecka?

## Tidrapport t o m Vecka 43 (Grupp 06) (rapporteras måndag v44)
1. Den gånga veckan har vi bokat in utlämning av hårdvaran, mer en så har inte gjorts ty kursstart är idag.

2. Vi har för närvarande inga problem ty arbetet börjar idag 30/10-23

3. Kommande vecka ska vi starta igång med projektet: Setup av Raspberry Pi, Kommunikationsmodul, Styrenhet, Manuellt Styrningsprogram och GUI.

## Tidrapport för v44 (Grupp 06) (rapporteras måndag v45)
1. Den gånga veckan har vi implementerat kommunikationsmodulen med bluetooth, kommunikation mellan delsystem, Raspberry Pi setup och styrenheten.

2. Vi har för närvarande problem med styrenheten främst med snurrning sv hjulen. 

3. Kommande vecka ska vi fortsätta med kommunikationsmoduler och styrsystemet. 

## Tidrapport för v45 (Grupp 06) (rapporteras måndag v46)
1. Den gånga veckan har vi fortsatt på kommunikation mellan delsystem, styrenheten och påbörjat sensormodulen.

2. Vi har för närvarande problem med kommunikation då vi bytt från SPI till I2C.  

3. Kommande vecka ska vi fortsätta med kommunikationsmoduler och sensormodulen.

## Tidrapport för v46 (Grupp xx) (rapporteras måndag v47)
1. Den gånga veckan har vi fortsatt på kommunikation mellan delsystem och sensormodulen.

2. Vi har för närvarande problem med hur vi ska sätta upp våra sensorer på roboten.  

3. Kommande vecka ska vi fortsätta med sensormodulen, styrenheten och kartritning.

## Tidrapport för v47 (Grupp xx) (rapporteras måndag v48)
1. Den gågna veckan har vi hunnit med mycket. Jennifer och Elin har gjort kartritningsprogrammet som ritar upp kartan på GUIt. Därefter har vi också påbörjat det autonoma kartläggningprogrammet, där vi skapat en egen algoritm. Jacob, Elliot och Edvard har först och främst felsökt I2Cn då vi inte kunde läsa in rätt värden, men tillslut visade det sig att vi enablade interuppt på ADCn, vilket "störde" resterande interuppt. Jacob och Edvard har gjort funktioner för styrningen, där man kan lägga in avstånd/grader så kör roboten den sträckan/rotationen. Hugo gjorde klart det sista med sensorerna. 

2. Vi har för närvarande inga problem eftersom vi har påbörjat nya delar denna vecka. De utmaningarna vi ser denna vecka är att testköra den autonoma styrningen och att implementera legreringen. Men det ska nog gå bra!

3. Kommande vecka ska vi testköra det automa styrningen och implementera reglering på sensormodulen så att vi kan veta att vi åker längst en vägg. 

## Tidrapport för v48 (Grupp xx) (rapporteras måndag v49)
1. Vilka framsteg har gjorts sedan förra tidrapporten?
Vi har testat roboten i Arenan, och mha testningen har vi implementerat PD-reglering och felsökt samt förbättrat den autonoma styrningen. 

2. Finns det några problem?
Just nu har vi inte hunnit testköra i Arenan, så vi har inte hunnit testa om våra nya implementeringar fungerar. Vi har haft lite problem med den autonoma styrningen, men vi har kommit långt. Just nu kan den projicera rätt karta, men har svårt att hitta hem igen. 

3. Vad ska göras kommande vecka?
Kommande vecka ska vi fortsätta felsöka autonoma styrningen. Vi ska även fortsätta att testa och felsöka roboten. Vi måste också påbörja dokumentationen som ska in nästa vecka. Också kontrollera sensordata så att den inte störs av felstyrningar.

4. Vilken funktionalitet har roboten idag?
Idag kan roboten: styras manuellt, köra en enkel karta och mappa upp rätt karta och kan reglera själv. Alla "moduler är klara" men nu måste vi testa och felsöka! Samt testa att köra på tävlingsbanan.

5. Vilken funktionalitet återstår?
Det som saknas är ett fullt fungerande autonomt styrprogram, samt tesning på samtliga moduler.

6. Beskriv eventuella tekniska problem.
Vi har för närvarande inga tekniska problem som vi fastnat på, däremot har vi inte testkört tillräckligt så problem kan uppstå.

7. Hur mycket tid har ni kvar av budgeterade timmar?
Vi har 960 - 598 = 362 timmar kvar (ca. 60h/person kvar)

8. Hur många timmar har respektive projektmedlem kvar att leverera (för att nå målet på 160 timmar) och hur ska dessa timmar fördelas över respektive kvarvarande veckor?
Redovisa i en tabell i statusrapporten hur många timmar detta blir per person och vecka.
    Redovisa också vilka aktiviteter som respektive person ska arbeta med.
          Nuvarande timmar:       V49:      V50:     V51:
Jennifer:       93                22        23        22
Elin:           88                26        24        22             
Jacob:          96                23        21        20
Edvard:         113               16        16        15
Elliot:         118               8         20        14
Hugo:           90                24        24        23

9. Är arbetsbelastningen jämn i gruppen?
    Om ej, ange orsak och vilken åtgärd ni vidtar.
Arbetsfördelningen är inte helt jämn, men det är något vi kommer se till att korrigera resterande veckor. Den medlemmen med flest timmar, ska vara borta 5 dagar, så han har samlat in timmar som buffert.

10. Beskriv eventuella samarbetsproblem.
Vi har inte haft några sammarbetsproblem!

## Tidrapport för v49 (Grupp xx) (rapporteras måndag v50)
1. De framsteg som har gjorts är att fixa så att bluetooth-kommunikationen fungerar mellan RPi och datorn. Nu kan vi skicka kartan och rita upp den på gränssnittet. Vi har även trådat sökalgoritmen, den körs nu parallellt för att kunna använda bluetooth och algoritmen samtidigt. Alla kommandon för Bluetooth har lagts in. Resterande tid har spenderats på att skriva den tekniska dokumentationen samt användarhandledning. På grund av bort fall från två medlemmar har dokumentationen tagit längre tid. 

2. Finns det några problem?
Just nu finns det inga större problem, förutom att vi måste testköra. Vi har bokat Arenan idag och kommer testa våra nya implementationer. Vi måste justera sökalgoritmen lite, för just nu om kartan inte är korrekt mätt (40x40cm) så kommer roboten tro att den gått längre och lägger till en extra ruta. 

3. Vad ska göras kommande vecka?
Denna vecka ska vi lämna in dokumentationen och få BP5 godkänt. Vi ska skriva klart dokumentationen idag och sen testa roboten och göra finjustreingar. Denna vecka blir det att testa och säkerställa att vår robot uppfyller de krav vi specifierat. 

## Tidrapport för v50 (Grupp xx) (rapporteras måndag v51)
1. De framsteg som har gjort är att vi fått robotens krav godkända. För att bli godkända jobbade vi denna vecka med att förbättra regleringen, testade alla moduler och försökte implementera knapparna. 
2. De problem vi stötte på var främst knappimplementationen, vi behövde därmed tråda hela Bluetooth-modulen men detta skapade flera problem och på grund av tidsbrist så blev detta svårt att fixa. Vi hade också problem med att roboten inte svängde perfekt 90 grader, så vi behövde fixa detta också då det skapade komplikationer vid körningen.
3. Vad ska göras kommande vecka?
V51 ska vi presentera projektet och fixa evenutella kommentarer på tekniska dokumentationen och användarhandledning.
