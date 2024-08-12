# Importation des modules et fonctions nécessaires à Flask :
from flask import Flask, render_template, request, redirect, url_for

# Créer une instance de l'application Flask :
app = Flask(__name__)

# Liste de livres initialisée :
books = [
    
    # Ajout de "L'Étranger" à la liste des livres :
    {"id" : 1, "title" : "L'Étranger", "author" : "Albert Camus"},
   
    # Ajout de "1984" à la liste des livres :
    {"id" : 2, "title" : "1984", "author" : "George Orwell"},
    
    # Ajout de "Le petit Prince" à la liste des livres :
    {"id" : 3, "title" : "Le Petit Prince", "author" : "Antoine de Saint-Exupéry"}
]

# Définit une route pour afficher la page d'accueil :
@app.route('/')

# Fonction pour gérer la route de la page d'accueil :
def index():

    # Renvoie le modèle 'index.html' avec les livres :
    return render_template('index.html', books=books)

# Route pour ajouter un livre (GET, POST) :
@app.route('/add_book', methods=['GET', 'POST'])

# Fonction pour ajouter un livre :
def add_book() :

    # Vérifie si la méthode de la requête est POST :
    if request.method == 'POST' :

        # Récupère la valeur du champ de titre soumis :
        title = request.form['title']

        # Récupère la valeur du champ d'auteur soumis :
        author = request.form['author']

        # Nouvel ID attribué au livre ajouté :
        new_id = max([book['id'] for book in books]) + 1

        # Ajout d'un nouveau livre à la liste :
        books.append({"id": new_id, "title": title, "author": author})

        # Redirection vers la page d'accueil :
        return redirect(url_for('index'))

    # Renvoie le modèle 'ajout_livre.html' :
    return render_template('ajout_livre.html')

# Route pour éditer un livre avec un ID spécifique :
@app.route('/edit_book/<int:id>', methods=['GET', 'POST'])

# Fonction pour éditer un livre avec un ID donné :
def edit_book(id) :

    # Livre trouvé dans la liste par ID :
    book = next((book for book in books if book['id'] == id), None)

    # Condition pour vérifier si la méthode de requête est POST :
    if request.method == 'POST' :

        # Mise à jour du titre du livre avec le formulaire :
        book['title'] = request.form['title']

        # Mise à jour de l'auteur du livre avec le formulaire :
        book['author'] = request.form['author']

        # Redirection vers la page d'accueil après édition :
        return redirect(url_for('index'))

    # return render_template('modif_livre.html', book=book) :
    return render_template('modif_livre.html', book=book)

# Route pour supprimer un livre avec un ID spécifique :
@app.route('/delete_book/<int:id>')

# Fonction pour supprimer un livre avec un ID donné :
def delete_book(id) :

    # Utilisation de la variable books déclarée globalement :
    global books

    # Filtrage des livres pour exclure celui avec l'ID donné :
    books = [book for book in books if book['id'] != id]

    # Redirection vers la page d'accueil après la suppression :
    return redirect(url_for('index'))

# Vérifie si le script est exécuté directement :
if __name__ == '__main__' :

    # Lance l'application en mode de débogage :
    app.run(debug=True)