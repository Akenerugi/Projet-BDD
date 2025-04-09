from fastapi import FastAPI, HTTPException
from biblio import *


logging.basicConfig(level=logging.INFO)
app = FastAPI()



@app.post("/visualiser/")
async def visualiser_data(data: dict):
    try:
        table_name = data.get("table_name")
        if not table_name:
            raise HTTPException(status_code=400, detail="Le nom de la table est requis")

        result = visualiser_table(table_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/medecin/")
async def create_medecin(data: dict):
    try:
        creer_medecin(data)
        return {"message": "Médecin créé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/medecin/{id_medecin}")
async def update_medecin(id_medecin: int, data: dict):
    try:
        modifier_medecin(id_medecin, data)
        return {"message": "Médecin mis à jour avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/patient/")
async def create_patient(data: dict):
    try:
        creer_patient(data)
        return {"message": "Patient créé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/patient/{id_patient}")
async def update_patient(id_patient: int, data: dict):
    try:
        modifier_patient(id_patient, data)
        return {"message": "Patient mis à jour avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/receptionniste/{id_receptionniste}/patient/{id_patient}")
async def update_patient_by_receptionniste(id_receptionniste: int, id_patient: int, data: dict):
    try:
        modifier_patient_receptionniste(id_receptionniste, id_patient, data)
        return {"message": "Patient modifié par le réceptionniste avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/receptionniste/")
async def create_receptionniste(data: dict):
    try:
        creer_receptionniste(data)
        return {"message": "Réceptionniste créé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/receptionniste/{id_receptionniste}")
async def update_receptionniste(id_receptionniste: int, data: dict):
    try:
        modifier_receptionniste(id_receptionniste, data)
        return {"message": "Réceptionniste mis à jour avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/delete/{table}/{id}")
async def delete_data(table: str, id: int):
    try:
        supprimer_M_P_R(table, id)
        return {"message": f"Entrée de la table {table} supprimée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rdv/")
async def create_rdv(data: dict):
    try:
        ajouter_rdv(data)
        return {"message": "Rendez-vous créé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/rdv/{id_rdv}")
async def update_rdv(id_rdv: int, nouvel_etat: str):
    try:
        modifier_etat_rdv(id_rdv, nouvel_etat)
        return {"message": "État du rendez-vous mis à jour avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/rdv/{id_rdv}")
async def cancel_rdv(id_rdv: int):
    try:
        annuler_rdv(id_rdv)
        return {"message": "Rendez-vous annulé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/rdv/medecin/{id_medecin}")
async def view_rdv_medecin(id_medecin: str ):
    try:

        result = visualiser_rdv_medecin(id_medecin)
        print(result)
        return {"voici les differents rendez vous du medecin choisi": str(result)}



    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/rdv/")
async def view_rdv_by_criteria(id_medecin: int, date: str, etat: str):
    try:
        data = {"Date": date, "Etat": etat}
        return visualiser_rdv(id_medecin, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyse/")
async def create_analysis(data: dict):
    try:
        creer_analyse(data)
        return {"message": "Analyse créée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/facture/")
async def create_invoice(data: dict):
    try:
        creer_facture(data)
        return {"message": "Facture créée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/facture/{id_facture}")
async def update_invoice(id_facture: int, data: dict):
    try:
        modifier_facture(id_facture, data)
        return {"message": f"Facture {id_facture} modifiée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.delete("/supprimer/{table}/{id}")
async def delete_item(table: str, id: int):
    try:
        supprimer_A_F_R(id, table)
        return {"message": f"Élément de la table {table} avec l'ID {id} supprimé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/consultation/{id_patient}/{id_consult}")
async def view_consultation(id_patient: int, id_consult: int):
    try:
        result = visualiser_doss_medical_1_consultation(id_patient, id_consult)
        return {"consultation": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/rdv/journee/")
async def view_daily_appointments():
    try:
        result = visualiser_rdv_journee()
        return {"rdv_jour": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/message/")
async def write_message(data: dict):
    try:
        ecrire_message(data)
        return {"message": "Message écrit avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/message/{id_medecin}")
async def read_messages(id_medecin: int):
    try:
        result = lire_message(id_medecin)
        return {"messages": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/reponse/")
async def respond_to_message(data: dict):
    try:
        repondre_message(data)
        return {"message": "Réponse envoyée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/reporting/")
async def show_report(data: dict):
    try:
       result = reporting(data)
       return {"voici le reporting de la journée :":result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/visualiser_dossier_Patient")
async def visulalisation_dossier(id_patient: int):
    try:
        result = visualiser_doss_medical(id_patient)
        return {"voici le dossier :":result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


conn = connect_db()
cursor = conn.cursor()




