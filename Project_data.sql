BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "analyse_d_urine_" (
	"ID_AU"	CHAR(10) NOT NULL,
	"resultat"	VARCHAR(255) NOT NULL,
	"prix"	DECIMAL(10, 2) NOT NULL,
	"Methamphetamine"	CHAR(1) NOT NULL,
	"LSD"	CHAR(1) NOT NULL,
	"Heroine"	CHAR(1) NOT NULL,
	"Cocaine"	CHAR(1) NOT NULL,
	"Amphetamine"	CHAR(1) NOT NULL,
	"Cannabinoides"	CHAR(1) NOT NULL,
	"Antidepress_tricycliques"	CHAR(1) NOT NULL,
	"Paracetamol"	CHAR(1) NOT NULL,
	"ID_Facture"	CHAR(10),
	"ID_Patient"	CHAR(10) ,
	FOREIGN KEY("ID_Patient") REFERENCES "Patient"("ID_Patient"),
	FOREIGN KEY("ID_Facture") REFERENCES "Facture"("ID_Facture"),
	CONSTRAINT "ID_analyse_d_urine__ID" PRIMARY KEY("ID_AU")
);
CREATE TABLE IF NOT EXISTS "Creneau" (
	"ID_Creneau"	CHAR(10) NOT NULL,
	"statut_Creneau"	CHAR(1) NOT NULL,
	CONSTRAINT "ID_Creneau_ID" PRIMARY KEY("ID_Creneau")
);
CREATE TABLE IF NOT EXISTS "Facture" (
	"ID_Facture"	CHAR(10) NOT NULL,
	"Prix_HT"	DECIMAL(10, 2) NOT NULL,
	"Prix_TTC"	DECIMAL(10, 2) NOT NULL,
	"TVA"	DECIMAL(5, 2) NOT NULL,
	"Part_Mutuelle"	DECIMAL(10, 2) NOT NULL,
	"Frais"	DECIMAL(10, 2) NOT NULL,
	"Part_Remboursee"	DECIMAL(10, 2) NOT NULL,
	"Date"	DATE NOT NULL,
	"Numéro_de_facture"	CHAR(10) NOT NULL,
	"Numéro_Patient"	CHAR(10) NOT NULL,
	"Numéro_Medecin"	CHAR(10) NOT NULL,
	"ID_receptionniste"	CHAR(10),
	FOREIGN KEY("ID_receptionniste") REFERENCES "Receptionniste_"("ID_receptionniste"),
	CONSTRAINT "ID_Facture_ID" PRIMARY KEY("ID_Facture")
);
CREATE TABLE IF NOT EXISTS "Message" (
	"ID_message"	CHAR(10) NOT NULL,
	"contenu"	VARCHAR(255) NOT NULL,
	"ID_Patient"	CHAR(10) ,
	FOREIGN KEY("ID_Patient") REFERENCES "Patient"("ID_Patient"),
	CONSTRAINT "ID_Message_ID" PRIMARY KEY("ID_message")
);
CREATE TABLE IF NOT EXISTS "Medecin" (
	"ID_Medecin"	CHAR(10) NOT NULL,
	"Identifiant"	VARCHAR(50) NOT NULL,
	"MDP_MED"	VARCHAR(50) NOT NULL,
	"Mail"	VARCHAR(100) NOT NULL,
	"Numero_tel"	VARCHAR(15) NOT NULL,
	"Prenom"	VARCHAR(50) NOT NULL,
	"Nom"	VARCHAR(50) NOT NULL,
	"Specialite"	VARCHAR(50) NOT NULL,
	"Adresse"	VARCHAR(255) NOT NULL,
	"ville"	VARCHAR(50) NOT NULL,
	"code_postal"	VARCHAR(10) NOT NULL,
	"Numéro_licence"	VARCHAR(20) NOT NULL,
	CONSTRAINT "ID_Medecin_ID" PRIMARY KEY("ID_Medecin")
);
CREATE TABLE IF NOT EXISTS "Patient" (
	"assurance_medicale"	VARCHAR(50) NOT NULL,
	"ID_Patient"	CHAR(10) NOT NULL,
	"Nom"	VARCHAR(50) NOT NULL,
	"Prenom"	VARCHAR(50) NOT NULL,
	"Adresse"	VARCHAR(255) NOT NULL,
	"ville"	VARCHAR(50) NOT NULL,
	"code_postal"	VARCHAR(10) NOT NULL,
	"identifiant"	VARCHAR(50) NOT NULL,
	"mdp"	VARCHAR(50) NOT NULL,
	"liste_rendez_vous_"	VARCHAR(255) NOT NULL,
	"historique_PDS"	VARCHAR(255) NOT NULL,
	"historique_Scanner"	VARCHAR(255) NOT NULL,
	"historique_AU"	VARCHAR(255) NOT NULL,
	"numéro_securitee_sociale"	VARCHAR(20) NOT NULL,
	"Numero_tel"	VARCHAR(15) NOT NULL,
	CONSTRAINT "ID_Patient_ID" PRIMARY KEY("ID_Patient")
);
CREATE TABLE IF NOT EXISTS "Prescription" (
	"ID_presc"	CHAR(10) NOT NULL,
	"medicament"	VARCHAR(255) NOT NULL,
	"quantite"	INT NOT NULL,
	"duree"	INT NOT NULL,
	"ID_Facture"	CHAR(10) ,
	"ID_Medecin"	CHAR(10) ,
	"ID_Scanner"	CHAR(10) ,
	"ID_PDS"	CHAR(10) ,
	"ID_AU"	CHAR(10) ,
	FOREIGN KEY("ID_Medecin") REFERENCES "Medecin"("ID_Medecin"),
	FOREIGN KEY("ID_Facture") REFERENCES "Facture"("ID_Facture"),
	FOREIGN KEY("ID_AU") REFERENCES "analyse_d_urine_"("ID_AU"),
	FOREIGN KEY("ID_Scanner") REFERENCES "scanner"("ID_Scanner"),
	FOREIGN KEY("ID_PDS") REFERENCES "prise_de_sang"("ID_PDS"),
	CONSTRAINT "ID_Prescription_ID" PRIMARY KEY("ID_presc")
);
CREATE TABLE IF NOT EXISTS "prise_de_sang" (
	"prix"	FLOAT NOT NULL,
	"ID_PDS"	CHAR(10) NOT NULL,
	"Quantite_prelevee"	FLOAT NOT NULL,
	"substance_analyse"	VARCHAR(255) NOT NULL,
	"resultat"	VARCHAR(1) NOT NULL,
	"Hematis"	FLOAT NOT NULL,
	"Hemoglobine"	FLOAT NOT NULL,
	"Hematocrite"	FLOAT NOT NULL,
	"Leucosytes"	FLOAT NOT NULL,
	"Polynucleaires_neutrophiles"	FLOAT NOT NULL,
	"Polynuclaire_eosinophiles"	FLOAT NOT NULL,
	"Polynucleaire_Basophiles"	FLOAT NOT NULL,
	"Lymphocytes"	FLOAT NOT NULL,
	"Monocytes"	FLOAT NOT NULL,
	"ID_Facture"	CHAR(10),
	"ID_Patient"	CHAR(10) ,
	FOREIGN KEY("ID_Patient") REFERENCES "Patient"("ID_Patient"),
	FOREIGN KEY("ID_Facture") REFERENCES "Facture"("ID_Facture"),
	CONSTRAINT "ID_prise_de_sang_ID" PRIMARY KEY("ID_PDS")
);
CREATE TABLE IF NOT EXISTS "gere2" (
	"ID_Medecin"	CHAR(10) ,
	"ID_RDV"	CHAR(10) ,
	FOREIGN KEY("ID_Medecin") REFERENCES "Medecin"("ID_Medecin"),
	FOREIGN KEY("ID_RDV") REFERENCES "RDV"("ID_RDV"),
	CONSTRAINT "ID_gere2_ID" PRIMARY KEY("ID_RDV","ID_Medecin")
);
CREATE TABLE IF NOT EXISTS "modifie_les_donnees" (
	"ID_Patient"	CHAR(10) NOT NULL,
	"ID_receptionniste"	CHAR(10) NOT NULL,
	"donnees_modifiees"	VARCHAR(255) NOT NULL,
	"date"	DATE NOT NULL,
	FOREIGN KEY("ID_Patient") REFERENCES "Patient"("ID_Patient"),
	FOREIGN KEY("ID_receptionniste") REFERENCES "Receptionniste_"("ID_receptionniste"),
	CONSTRAINT "ID_modifie_les_donnees_ID" PRIMARY KEY("ID_Patient","ID_receptionniste")
);
CREATE TABLE IF NOT EXISTS "Organise" (
	"ID_RDV"	CHAR(10) ,
	"ID_receptionniste"	CHAR(10) ,
	FOREIGN KEY("ID_RDV") REFERENCES "RDV"("ID_RDV"),
	FOREIGN KEY("ID_receptionniste") REFERENCES "Receptionniste_"("ID_receptionniste"),
	CONSTRAINT "ID_Organise_ID" PRIMARY KEY("ID_receptionniste","ID_RDV")
);
CREATE TABLE IF NOT EXISTS "RDV" (
    "ID_RDV" CHAR(10) NOT NULL,
    "Etat" CHAR(50) NOT NULL,
    "Date_RDV" DATE NOT NULL,
    "ID_Patient" CHAR(10) ,
    "ID_Medecin" CHAR(10) ,
    "ID_Creneau" CHAR(10) ,
    FOREIGN KEY ("ID_Patient") REFERENCES "Patient"("ID_Patient"),
    FOREIGN KEY ("ID_Creneau") REFERENCES "Creneau"("ID_Creneau"),
    FOREIGN KEY ("ID_Medecin") REFERENCES "Medecin"("ID_Medecin"),
    CONSTRAINT "ID_RDV_ID" PRIMARY KEY("ID_RDV")
);
CREATE TABLE IF NOT EXISTS "recoit" (
	"ID_Patient"	CHAR(10) ,
	"ID_Replique"	CHAR(10) ,
	FOREIGN KEY("ID_Replique") REFERENCES "Replique"("ID_Replique"),
	FOREIGN KEY("ID_Patient") REFERENCES "Patient"("ID_Patient"),
	CONSTRAINT "ID_recoit_ID" PRIMARY KEY("ID_Replique","ID_Patient")
);
CREATE TABLE IF NOT EXISTS "Receptionniste_" (
	"ID_receptionniste"	CHAR(10) NOT NULL,
	"Nom"	VARCHAR(50) NOT NULL,
	"Prenom"	VARCHAR(50) NOT NULL,
	"Adresse"	VARCHAR(255) NOT NULL,
	"ville"	VARCHAR(50) NOT NULL,
	"code_postal"	VARCHAR(10) NOT NULL,
	"identifiant"	VARCHAR(50) NOT NULL,
	"MDP_RECEP"	VARCHAR(50) NOT NULL,
	"numero_tel"	VARCHAR(15) NOT NULL,
	"Mail"	VARCHAR(100) NOT NULL,
	CONSTRAINT "ID_Receptionniste__ID" PRIMARY KEY("ID_receptionniste")
);
CREATE TABLE IF NOT EXISTS "Replique" (
	"ID_Replique"	CHAR(10) NOT NULL,
	"contenu_rep"	VARCHAR(255) NOT NULL,
	"ID_Medecin"	CHAR(10)  ,
	"ID_message"	CHAR(10)  ,
	FOREIGN KEY("ID_Medecin") REFERENCES "Medecin"("ID_Medecin"),
	FOREIGN KEY("ID_message") REFERENCES "Message"("ID_message"),
	CONSTRAINT "ID_Replique_ID" PRIMARY KEY("ID_Replique")
);
CREATE TABLE IF NOT EXISTS "scanner" (
	"ID_Scanner"	CHAR(10) NOT NULL,
	"machine"	VARCHAR(50) NOT NULL,
	"image"	VARCHAR(255) NOT NULL,
	"compte_rendu_resultat"	VARCHAR(255) NOT NULL,
	"prix"	FLOAT NOT NULL,
	"Verre_depoli"	VARCHAR(1) NOT NULL,
	"Crazy_paving"	VARCHAR(1) NOT NULL,
	"Condensation"	VARCHAR(1) NOT NULL,
	"Topographie_lesionnelle_global"	VARCHAR(1) NOT NULL,
	"Micronodules_centrolobulaires"	VARCHAR(1) NOT NULL,
	"Condensation_systematise"	VARCHAR(1) NOT NULL,
	"secretions_endobronchiques"	VARCHAR(1) NOT NULL,
	"Epanchement_pericardique_"	VARCHAR(1) NOT NULL,
	"Anomalie_cardiaque"	VARCHAR(1) NOT NULL,
	"Anomalie_vasculaire"	VARCHAR(1) NOT NULL,
	"ID_Facture"	CHAR(10),
	"ID_Patient"	CHAR(10) ,
	FOREIGN KEY("ID_Patient") REFERENCES "Patient"("ID_Patient"),
	FOREIGN KEY("ID_Facture") REFERENCES "Facture"("ID_Facture"),
	CONSTRAINT "ID_scanner_ID" PRIMARY KEY("ID_Scanner")
);
INSERT INTO "Medecin" ("ID_Medecin","Identifiant","MDP_MED","Mail","Numero_tel","Prenom","Nom","Specialite","Adresse","ville","code_postal","Numéro_licence") VALUES ('1','benjamin.c123','benji.974','benjamin.comte@orange.fr','0692 65 43 21','Benjamin','COMTE','Chirurgien testiculaire','12 rue de la connerie ','Saint-Denis','97421','440 123'),
 ('2','chantal.a123','chant.440','chantal.comte@orange.fr','0692 88 10 72','Chantal','AGATHE','Cardiologue','11 rue des dattiers','Bras-Panon','97412','440 456'),
 ('3','matteo.h123','matt.110','matteo.hoareau@orange.fr','0692 78 94 56','Matteo','HOAREAU','Pediatre','14 rue des bouffons ','Saint-Andrés','97440','440 789');
INSERT INTO "Patient" ("assurance_medicale","ID_Patient","Nom","Prenom","Adresse","ville","code_postal","identifiant","mdp","liste_rendez_vous_","historique_PDS","historique_Scanner","historique_AU","numéro_securitee_sociale","Numero_tel") VALUES ('Groupama','1','COMTE','Quentin','3 allée Jacques Laloë','Ivry-Sur-Seine','94200','quentin.c','quentin123','1','0','0','0','20031307','0692 20 27 09'),
 ('Maif','2','CHANEL','Bastien','44 rue raspail','Ivry-Sur-Seine','94200','bastien.c','bastien123','2','0','0','0','20030110','0607 12 34 56'),
 ('Axa','3','KOK','Steffy','44 rue raspail','Ivry-Sur-Seine','94200','steffy.k','steffy123','1','0','0','0','20020212','0708 56 78 90');
INSERT INTO "Receptionniste_" ("ID_receptionniste","Nom","Prenom","Adresse","ville","code_postal","identifiant","MDP_RECEP","numero_tel","Mail") VALUES ('1','VERROLLE','Camille','5 rue du trou perdu','Miniac Morvan','35 000','camille.v23','camille.verrolle123','0617 12 34 56','camille.verrolle@ipsa.fr'),
 ('2','CLAIN','Leslie','12 rue Maurice Gunsbourg','Saint-Paul','97417','leslie.c23','leslie.clain123','0692 12 34 56','leslie.clain@orange.fr'),
 ('3','AGATHE','Anna','4 rue du bonheur ','Saibt-Pierre','97420','anna.a23','anna.agathe123','0692 23 45 67','anna.agathe@wannadoo.fr');
COMMIT;
