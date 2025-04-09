from datetime import date
from datetime import datetime
import sqlite3
import uvicorn
import logging


def connect_db():
    conn = sqlite3.connect('projetbdd_V3.db')
    return conn


def visualiser_table(data):
    table_name = data.get('table_name')
    if table_name:
        query = f"SELECT * FROM {table_name}"


        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        cursor.close()
        return result


def connect_db():
    conn = sqlite3.connect('projetbdd_V3.db')
    return conn

conn = connect_db()
cursor = conn.cursor()
def creer_medecin(data):
    query = "INSERT INTO Medecin (ID_Medecin,Identifiant, MDP_MED, Mail, Numero_tel, Prenom, Nom, Specialite, Adresse, " \
            "ville, code_postal, Numéro_licence) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = tuple(data.values())
    cursor.execute(query, values)
    conn.commit()



def modifier_medecin(id_medecin, data):
    query = "UPDATE Medecin SET Identifiant=?, MDP_MED=?, Mail=?, Numero_tel=?, Prenom=?, Nom=?, Specialite=?, Adresse=?" \
            ", ville=?, code_postal=?, Numéro_licence=? WHERE ID_Medecin=?"
    values = tuple(data.values()) + (id_medecin,)
    cursor.execute(query, values)
    conn.commit()


def creer_patient(data):
    query = "INSERT INTO Patient (assurance_medicale, ID_Patient, Nom, Prenom, Adresse, ville, code_postal, identifiant," \
            " mdp, liste_rendez_vous_, historique_PDS, historique_Scanner, historique_AU, numéro_securitee_sociale) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = tuple(data.values())
    cursor.execute(query, values)
    conn.commit()


def modifier_patient(id_patient, data):
    query = "UPDATE Patient SET assurance_medicale=?, Nom=?, Prenom=?, Adresse=?, ville=?, code_postal=?, identifiant=?," \
            " mdp=?, liste_rendez_vous_=?, historique_PDS=?, historique_Scanner=?, historique_AU=?, numéro_securitee_sociale=? WHERE ID_Patient=?"
    values = tuple(data.values()) + (id_patient,)

    cursor.execute(query, values)
    conn.commit()


def modifier_patient_receptionniste(id_receptionniste, id_patient, data):
    query_check = "SELECT COUNT(*) FROM Receptionniste_ WHERE ID_receptionniste=?"

    cursor.execute(query_check, (id_receptionniste,))
    count = cursor.fetchone()[0]
    conn.commit()

    if count > 0:

        query_update = "UPDATE Patient SET assurance_medicale=?, Nom=?, Prenom=?, Adresse=?, ville=?, code_postal=?," \
                       " identifiant=?, mdp=?, liste_rendez_vous_=?, historique_PDS=?, historique_Scanner=?, historique_AU=?," \
                       " numéro_securitee_sociale=? WHERE ID_Patient=?"
        values = tuple(data.values()) + (id_patient,)
        cursor.execute(query_update, values)
        conn.commit()
    else:
        print("Réceptionniste non autorisé à modifier le patient.")


def creer_receptionniste(data):
    query = "INSERT INTO Receptionniste_ (ID_receptionniste, Nom, Prenom, Adresse, ville, code_postal, identifiant," \
            " MDP_RECEP, numero_tel, Mail) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = tuple(data.values())
    cursor.execute(query, values)
    conn.commit()

def modifier_receptionniste(id_receptionniste, data):
    query = "UPDATE Receptionniste_ SET Nom=?, Prenom=?, Adresse=?, ville=?, code_postal=?, identifiant=?," \
            " MDP_RECEP=?, numero_tel=?, Mail=? WHERE ID_receptionniste=?"
    values = tuple(data.values()) + (id_receptionniste,)

    cursor.execute(query, values)
    conn.commit()


def supprimer_M_P_R(table, id):
    query = f"DELETE FROM {table} WHERE ID_{table}=?"

    cursor.execute(query, (id,))
    conn.commit()


def ajouter_rdv(data):
    query = "INSERT INTO RDV (ID_RDV, Etat, Date_RDV, ID_Patient, ID_Medecin , ID_Creneau) VALUES (?, ?, ?, ?, ?, ?)"
    values = tuple(data.values())
    cursor.execute(query, values)
    conn.commit()


def modifier_etat_rdv(id_rdv, nouveau_etat_rdv):
    query = "UPDATE RDV SET Etat=? WHERE ID_RDV=?"
    values = (nouveau_etat_rdv, id_rdv)
    cursor.execute(query, values)
    conn.commit()

def annuler_rdv(id_rdv):
    query = "DELETE FROM RDV WHERE ID_RDV=?"
    cursor.execute(query, (id_rdv,))
    conn.commit()

def visualiser_rdv(id_medecin, data):

    query = "SELECT * FROM RDV WHERE ID_Creneau IN (SELECT ID_Creneau FROM Creneau WHERE ID_Medecin=?) AND Date=? AND Etat=?"
    values = (id_medecin, data.get('Date', ''), data.get('Etat', ''))

    cursor.execute(query, values)
    rdvs = cursor.fetchall()
    conn.commit()
    for rdv in rdvs:
        print(rdv)


def visualiser_rdv_medecin(id_medecin):


    query = "SELECT * FROM RDV WHERE ID_Medecin=? "
    values = (id_medecin)
    cursor.execute(query, values)
    rdvs = cursor.fetchall()
    conn.commit()
    for rdv in rdvs:
        print(rdv)


def creer_analyse(data):
    query = "INSERT INTO analyse_d_urine_ (ID_AU, resultat, prix, Methamphetamine, LSD, Heroine, Cocaine, Amphetamine," \
            " Cannabinoides, Antidepress_tricycliques, Paracetamol, ID_Facture, ID_Patient) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = tuple(data.values())
    cursor.execute(query, values)
    conn.commit()


def creer_facture(data):
    query = "INSERT INTO Facture (ID_Facture, Prix_HT, Prix_TTC, TVA, Part_Mutuelle, Frais, Part_Remboursee," \
            " Date, Numéro_de_facture, Numéro_Patient, Numéro_Medecin, ID_receptionniste) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = tuple(data.values())

    cursor.execute(query, values)
    conn.commit()


def modifier_facture(id_facture, data):
    query = "UPDATE Facture SET Prix_HT=?, Prix_TTC=?, TVA=?, Part_Mutuelle=?, Frais=?, Part_Remboursee=?," \
            " Date=?, Numéro_de_facture=?,Numéro_Patient=?,Numéro_Medecin=? WHERE ID_Facture=?"
    values = tuple(data.values()) + (id_facture)
    cursor.execute(query, values)
    conn.commit()



def creer_prescription(data):
    query = "INSERT INTO Prerscription (ID_presc, medicament, quantite, duree) VALUES (?, ?, ?, ?)"
    values = tuple(data.values())

    cursor.execute(query, values)
    conn.commit()


def supprimer_A_F_R(id, table):
    query = f"DELETE FROM {table} WHERE ID_{table}=?"
    cursor.execute(query, (id,))
    conn.commit()


def visualiser_doss_medical_1_consultation(id_patient, id_consult):
    query = "SELECT * FROM Consultation WHERE ID_Patient=? AND ID_Consultation=?"
    values = (id_patient, id_consult)

    cursor.execute(query, values)
    consultation = cursor.fetchone()
    conn.commit()

    if consultation:
        print(consultation)
    else:
        print("Consultation non trouvée pour ce patient avec cet identifiant")


def visualiser_doss_medical(id_patient):
    query = "SELECT * FROM Patient Where ID_Patient = ?"
    values = (id_patient)
    cursor.execute(query,values)
    dossier = cursor.fetchall()
    if dossier:
         return (dossier)
    else:
         return ("error not found")



def visualiser_rdv_journee():
    query = "SELECT * FROM RDV WHERE Date=DATE('now')"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    return result


def ecrire_message(data):
    query = "INSERT INTO Message (ID_message, contenu, ID_Patient) VALUES (?, ?, ?)"
    values = tuple(data.values())
    cursor.execute(query, values)
    conn.commit()

def lire_message(id_medecin):
    query = "SELECT * FROM Message WHERE ID_Medecin=?"
    cursor.execute(query, (id_medecin,))
    result = cursor.fetchall()
    conn.commit()
    return result


def repondre_message(data):
    query = "INSERT INTO Replique (ID_Replique, contenu_rep, ID_Medecin, ID_message) VALUES (?, ?, ?, ?)"
    values = tuple(data.values())

    cursor.execute(query, values)
    conn.commit()


def reporting(data: dict):
    start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
    end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
    cursor.execute("SELECT * FROM Facture WHERE Date BETWEEN ? AND ?", (start_date, end_date))
    facture_data = cursor.fetchall()
    cursor.execute("SELECT * FROM RDV WHERE Date_RDV BETWEEN ? AND ?", (start_date, end_date))
    rdv_data = cursor.fetchall()
    conn.commit()
    patients_count = len(set([rdv['ID_Patient'] for rdv in rdv_data]))
    recettes = sum([facture['Prix_TTC'] for facture in facture_data])
    print(f"Nombre de patients dans la période : {patients_count}")
    print(f"Recettes dans la période : {recettes} euros")


conn = connect_db()
cursor = conn.cursor()


