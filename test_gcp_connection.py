from google.cloud import storage

BUCKET_NAME = "emotor-dataset-raw"

def test_connection():
    try:
        client = storage.Client()
        print("✅ Cliente GCP creado correctamente")

        blobs = client.list_blobs(BUCKET_NAME)

        print(f"📂 Contenido del bucket '{BUCKET_NAME}':")
        for i, blob in enumerate(blobs):
            print(" -", blob.name)
            if i >= 10:
                break

        print("\n🎉 Conexión exitosa. Puedes leer el bucket sin problemas.")
    
    except Exception as e:
        print("❌ Error al conectar o listar objetos:")
        print(e)

if __name__ == "__main__":
    test_connection()

