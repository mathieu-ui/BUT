# Comment configurer le routeur rb750gr3 de chez Mikrotik

> Voici comment configurer le routeur Mikrotik tout en respectant le cahier des charges. (Les photos sont communes avec Timothée Fulop car nous avons réalisé la configuration du routeur en binôme).

1. Tout d'abord, si jamais vous ne parvenez pas a entré a vous conecter sur le routeur, ou que vous en avez besoin, voici la procedure de renitialisation :
   * Tout d'abord vous devez appuyer sur le bouton "RES".
  
    <IMG SRC="./BUT/tree/main/sae12-mathieu-iut-beziers-main/Routeur/img/routeur_1 (15).jpg" height="250px" width="auto">

   * Puis branchez l'alimentation du routeur et attendre jusqu'à ce que la LED "USR" clignotte.
  
    <IMG SRC="./BUT/tree/main/sae12-mathieu-iut-beziers-main/Routeur/img/routeur_1 (16).jpg" height="250px" width="auto">

2. Branchez votre PC sur le port eth2 et la connexion au réseau externe sur eth1. 


    <IMG SRC="./BUT/tree/main/sae12-mathieu-iut-beziers-main/Routeur/img/routeur_1 (17).jpg" height="250px" width="auto">
3. Ensuite connectez vous à l'interface gräce au logiciel WinBox ou sur un navigateur en allant sur l'IP par défaut du routeur (192.168.88.1).


    <IMG SRC="./BUT/tree/main/sae12-mathieu-iut-beziers-main/Routeur/img/routeur_1 (11).jpg" height="250px" width="auto">

4. Un fois connecté, on vous demande de créér un mot de passe puis vous arrivez sur une fenêtre de configuration, dans notre cas on a mis une IP du routeur correspondante au réseau sur lequel il est connecté, la passerelle de ce réseau, changez l'IP du routeur et la configuration du serveur DHCP. On rapelle que pour accéder a internet on doit mettre le routeur en mode NAT.


    <IMG SRC="./BUT/tree/main/sae12-mathieu-iut-beziers-main/Routeur/img/routeur_1 (14).jpg" height="250px" width="auto">

5. Un fois cela fai,t il faut rajouter les routes vers les autres réseaux, il existe plusieurs métodes, comme utiliser des protocoles comme RIP ou les mettre manuellement. Dans notre cas on les a ajouté manuellement dans l'onglet Routes qui est lui-même dans l'onglet IP.


    <IMG SRC="./BUT/tree/main/sae12-mathieu-iut-beziers-main/Routeur/img/routeur_1 (21).jpg" height="250px" width="auto">

6. Une fois tout cela de fait, si vous essayez de ping une machine dans un autre réseau, il y a de grandes chances qu'il n'y ait pas réponse. Dans ce cas il faut modifier les règles du firewall, pour notre cas sur le routeur le problème viens de la règle numéro 11 qui bloque tout les réseaux non DSTNAT, en la désactivant, tous les problèmes devraient être réglés.


    <IMG SRC="./BUT/tree/main/sae12-mathieu-iut-beziers-main/Routeur/img/routeur_1 (18).jpg" height="250px" width="auto">

7. Voici ce que donne notre montage sur un schéma :


<IMG SRC="./BUT/tree/main/sae12-mathieu-iut-beziers-main/Routeur/img/archi2.png" height="250px" width="auto">

-----
## Un autre élément

Un autre élément qui peut poser problème est le switch, le principale erreur qui peut être faite est l'attribution des VLAN qui peut être erronée ou l'utilisation du mode TRUNK sur un PC qui par nature ne le supporte pas.
