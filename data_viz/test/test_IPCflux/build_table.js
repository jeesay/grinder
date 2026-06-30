import { all, desc, op, table } from 'arquero';

// const { tableFromArrays, tableToIPC } = require('apache-arrow');
// const aq = require('arquero');

// --- ÉTAPE 1 : Créer des données de test ---
const noms = ['Laptop', 'Souris', 'Clavier', 'Ecran', 'Casque'];
const prix = [1200.50, 25.00, 45.00, 350.00, 80.00];
const stock = [10, 50, 30, 15, 20];

// --- ÉTAPE 2 : Transformer en Table Apache Arrow (Format binaire) ---
// Ici, on simule ce que vous recevriez en lisant un fichier .parquet ou .arrow
const arrowTable = tableFromArrays({
    produit: noms,
    prix: prix,
    quantite: stock
});

// Facultatif : Conversion en Buffer binaire (ce qui circulerait sur le réseau)
const binaryBuffer = tableToIPC(arrowTable);
console.log(`Taille du buffer binaire : ${binaryBuffer.length} octets\n`);

// --- ÉTAPE 3 : Charger dans Arquero ---
// Arquero "encapsule" la table Arrow sans copier les données
const dt = aq.fromArrow(arrowTable);

// --- ÉTAPE 4 : Manipuler les données ---
console.log("Tableau initial (Arquero) :");
dt.print();

console.log("\nAnalyse : Produits chers avec valeur du stock :");
dt.derive({ 
    valeur_totale: d => d.prix * d.quantite // Création d'une colonne calculée
  })
  .filter(d => d.prix > 100)               // Filtre
  .select('produit', 'valeur_totale')      // Sélection de colonnes
  .orderby(aq.desc('valeur_totale'))       // Tri
  .print();