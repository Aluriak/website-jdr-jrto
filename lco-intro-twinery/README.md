



## Harlowe 3.3
pour avoir la dernière version de harlowe, il faut aller chercher les fichiers compilés (`format.js` et `logo.svg`) ici :

    https://github.com/klembot/twinejs/blob/develop/public/story-formats/

Avec par ex:

    wget https://raw.githubusercontent.com/klembot/twinejs/develop/public/story-formats/harlowe-3.3.6/format.js
    wget https://raw.githubusercontent.com/klembot/twinejs/develop/public/story-formats/harlowe-3.3.6/logo.svg

Et les mettre dans `/usr/share/tweego/storyformats/harlowe-3`.

Maintenant, `tweego --list-formats` donne bien harlowe-3 comme 3.3.6.
