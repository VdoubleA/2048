2048

============================================================================
      ___          ___                   ___          ___          ___ 
     /__/\        /  /\         ___     /  /\        /  /\        /__/\
    |  |::\      /  /::\       /  /\   /  /:/_      /  /:/        \  \:\
    |  |:|:\    /  /:/\:\     /  /:/  /  /:/ /\    /  /:/          \__\:\
  __|__|:|\:\  /  /:/~/::\   /  /:/  /  /:/ /:/_  /  /:/  ___  ___ /  /::\
 /__/::::| \:\/__/:/ /:/\:\ /  /::\ /__/:/ /:/ /\/__/:/  /  /\/__/\  /:/\:\
 \  \:\~~\__\/\  \:\/:/__\//__/:/\:\\  \:\/:/ /:/\  \:\ /  /:/\  \:\/:/__\/
  \  \:\       \  \::/     \__\/  \:\\  \::/ /:/  \  \:\  /:/  \  \::/
   \  \:\       \  \:\          \  \:\\  \:\/:/    \  \:\/:/    \  \:\
    \  \:\       \  \:\          \__\/ \  \::/      \  \::/      \  \:\
     \__\/        \__\/                 \__\/        \__\/        \__\/
============================================================================


Ez a program a 2020-as évi Matech-verseny második fordulójának előfeladatának megoldásásra készült. A kérdéses probléma a 2048 nevű játék bizonyos állásából a következő 2 hatvány elérésére vonatkozik. A program alapértelmezett beállításai a feladatban meghatározott játékállásra vonatkoznak, de lehetőséget ad másik állások vizsgálatára is.

A program előre definiált eseteket vizsgál, melyek a játék véletleszerű mechanikáit írják le.

A program egy számot használ a kettesek ill. négyesek beadási sorrendjére. Ezt a számot kettes számrendszerben használja fel, olymódon hogy a legkisebb helyiértéken szereplő számjegy az első húzás utáni beadott számot írja le, és így tovább halad a program az egyre nagyobb helyiértékekig. Ha a szám rövidebb mint az adott esetben szükséges lépések száma, a program 0-ás értékekkel tölti fel a szükséges helyiértékeket. A 0-ás számjegy a 2-es beadott értéket jelöli a 1-es pedig a 4-es beadott értéket. Ha más nincs megadva akkor ezt az értéket a program autómatikusan növeli (^c) megszakításig.

Arra az esetre mikor több helyen is szabadul fel lyuk, további szabályok adhatóak meg. A szabály megadását egy megfelelő formátumú string-el lehet elvégezni. Ez a string max. 16 egymástól ';'-vel elválasztott részből áll. Minden rész egy hexadecimális számjeggyel kezdődik, ami azt adja meg hogy hány lyukkal van több az egyértelmű (1db) lyuknál. Így ez az érték a lyukak száma mínusz egy értékű. Ezt a számjegyet görbe zárójelen belül '()' egymástól ','-vel elválasztott hexadecimális számjegypárok követik, közöttük ':' -karakterrel. Minden párban a második számjegy azt jelöli hogy hányadik a '()' előtti számú lyuk előfordulásnál, az első számjegy pedig hogy hova kell lehelyezni az adott értéket. Ha a ':' nélkül önmagában található egy számjegy, az az általános esetet jelöli, melyet felülírnak a számjegypárok. A '()' belül is mindig 0-tól kezdjük a számozást. Ezek alapján ha azt akarjuk hogy mindig az utolsó lyukba tegye a program a beszúrt értéket, akkor a "0(0);1(1);2(2);3(3);4(4);5(5);6(6);7(7);8(8);9(9);A(A);B(B);C(C);D(D);E(E);F(F)" string-et kell megadnunk. Ha pedig például csak azt akarjuk hogy az első alkalommal, amikor három lyuk szabadul fel, a második helyre tegye a beszúrt számot, akkor a "2(1:0)" string-et kell megadnunk.

opciók:
  -c : A kettesek ill. nyégyesek sorrendjét megadó egész szám
  -c0b : A kettesek ill. négyesek sorrendjét megado egész szám kettes számrendszerben
  -o : A kimenet fájlba írása esetén a fájlnév
  -f : Rögzített hossz megadása a sorrendre vonatkozó szám esetán, pl: ha az értéke 2 akkor az első kettő helyiértéket nem növeli
  -n : Megadja hogy hányszor növelje a sorrendre vonatkozó számot.
  -r : A helyzetre vonatkozó formázott string
