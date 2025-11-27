from fpdf import FPDF

# Créer un PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Helvetica", size=12)

quiz_with_answers = """
1. Quel est le role principal de Jest dans React ?
A) Afficher les composants
B) Executer et organiser les tests  (correct)
C) Simuler les clics des utilisateurs
D) Styliser les composants

2. React Testing Library sert principalement a :
A) Verifier la logique des fonctions
B) Tester l'interface utilisateur et les interactions  (correct)
C) Compiler le code React
D) Gerer les routes

3. Quelle fonction permet de simuler un clic sur un bouton ?
A) render()
B) expect()
C) fireEvent.click()  (correct)
D) screen.getByText()

4. Quelle est la fonction qui verifie qu'un element est present dans le DOM ?
A) expect(...).toBeInTheDocument()  (correct)
B) fireEvent.click()
C) render()
D) screen.getByText()

5. Pourquoi utilise-t-on describe() dans Jest ?
A) Pour executer un test unique
B) Pour regrouper et organiser plusieurs tests  (correct)
C) Pour afficher le composant
D) Pour simuler des evenements

6. Quelle est la valeur initiale du compteur dans Counter.jsx si on ecrit useState(0) ?
A) 1
B) 0  (correct)
C) null
D) undefined

7. Que fait fireEvent.click(button) ?
A) Verifie la valeur du compteur
B) Simule un clic utilisateur  (correct)
C) Rend le composant
D) Reinitialise le compteur

8. Que retourne render(<Counter />) ?
A) Une interface visible pour l'utilisateur
B) Une version virtuelle du composant pour le test  (correct)
C) Une erreur si le compteur est a 0
D) Un snapshot CSS

9. Quel package faut-il importer pour utiliser toBeInTheDocument() ?
A) @testing-library/react
B) @testing-library/jest-dom  (correct)
C) react
D) jest

10. Que teste expect(screen.getByText('Compteur : 1')).toBeInTheDocument() ?
A) Que le bouton est clique
B) Que le texte 'Compteur : 1' est visible dans le DOM  (correct)
C) Que le compteur est initialise a 0
D) Que le composant est monte

11. Quel est l'interet principal des tests unitaires ?
A) Tester l'application entiere en condition reelle
B) Verifier le comportement d'une fonction ou d'un composant isole  (correct)
C) Styliser les composants React
D) Optimiser le rendu CSS

12. Quel type de test verifie l'interaction entre plusieurs composants ?
A) Test unitaire
B) Test d'integration  (correct)
C) Test end-to-end
D) Test snapshot

13. Quelle est la commande pour lancer les tests dans un projet CRA ?
A) npm start
B) npm run build
C) npm test  (correct)
D) npm install

14. Pourquoi est-il important de tester les composants React ?
A) Pour ameliorer la vitesse du navigateur
B) Pour eviter les bugs lors des mises a jour  (correct)
C) Pour creer des styles CSS
D) Pour gerer les routes

15. Que fait la fonction reset() dans Counter.jsx ?
A) Augmente le compteur de 1
B) Diminue le compteur de 1
C) Remet le compteur a 0  (correct)
D) Supprime le composant

16. Quelle assertion Jest permet de comparer une valeur ?
A) expect().toBe()  (correct)
B) fireEvent.click()
C) render()
D) screen.getByText()

17. Que fait describe('Counter component', () => {...}) ?
A) Cree un composant Counter
B) Groupe plusieurs tests lies au Counter  (correct)
C) Simule un clic sur le bouton
D) Verifie l'etat initial du compteur

18. Pourquoi utilise-t-on screen.getByText() ?
A) Pour recuperer un element par son texte dans le DOM virtuel  (correct)
B) Pour executer tous les tests
C) Pour initialiser le compteur
D) Pour simuler un clic

19. Que se passe-t-il si un test echoue ?
A) Le test passe automatiquement
B) Jest affiche une erreur et le test est marque comme failed  (correct)
C) Le compteur est reinitialise
D) Le composant disparait

20. Quel est l'avantage principal des tests automatises ?
A) Ils augmentent le poids du fichier JavaScript
B) Ils reduisent les erreurs et assurent la fiabilite du code  (correct)
C) Ils changent le design du composant
D) Ils rendent le code plus rapide
"""

pdf.multi_cell(0, 8, quiz_with_answers)

# Enregistrer le PDF
file_path = "C:/Users/moham/Desktop/Quiz_React_Testing_Avec_Reponses.pdf"
pdf.output(file_path)
file_path
