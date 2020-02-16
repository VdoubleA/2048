===========================================================================
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
===========================================================================

Ez a program a 2020-as évi Matech-verseny második fordulójának előfeladatának megoldásásra készült. A kérdéses probléma a 2048 nevű játék bizonyos állásából a következő 2 hatvány elérésére vonatkozik. A program alapértelmezett beállításai a feladatban meghatározott játékállásra vonatkoznak, de lehetőséget ad másik állások vizsgálatára is.

A program előre definiált eseteket vizsgál, melyek a játék véletleszerű mechanikáit írják le.

A program egy számot használ a kettesek ill. négyesek beadási sorrendjére. Ezt a számot kettes számrendszerben használja fel, olymódon hogy a legkissebb helyiértéken szereplő számjegy az első húzás utáni beadott számot írja le, és így tovább halad a program az egyre nagyobb helyiértékekig. Ha a szám rövidebb mint az adott esetben szükséges lépések száma, a program 0-ás értékekkel tölti fel a szükséges helyiértékeket. A 0-ás számjegy a 2-es beadott értéket jelöli a 1-es pedig a 4-es beadott értéket.

Arra az esetre mikor több helyen is szabadul fel lyuk, további szabályok adhatóak meg. A szabály megadását egy megfelelő formátumú string-el lehet elvégezni. 
