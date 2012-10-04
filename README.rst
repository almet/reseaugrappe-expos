Generateur de présentations
###########################

Ce petit projet permet de générer des presentations comme celles qui sont
actuellement disponibles sur http://expo.reseaugrappe.org.

Chaque dossier contient un fichier `infos.txt` qui doit lister, comme suit, le nom
de l'auteur de l'image et le titre de sa création::

    Femmes Gourmantché dans leur potager - Julie Bousquet

Les images doivent êtres nommées XX.jpg, ou XX est un nombre. Elles doivent
bien évidemment être dans l'ordre qui corresponds à l'ordre défini dans le
fichier `infos.txt`.

Le dossier contenant les images doit également contenir un fichier
`header.html` qui contient le contenu, au format HTML, qui sera ajouté en haut
de l'éxposition.

Voici comment générer une exposition::

    $ python generator.py fourche-fourchette "De la Fourche à la fourchette" --output=output.html
