from pyrogram import Client, filters

api_id = 8241732
api_hash = "a32dd346ca8392af581b02402e31924a"
device_model = "daniUB"

app = Client("my_account", api_id=api_id, api_hash=api_hash, device_model=device_model,
                    plugins=dict(root="plugins")).run()




if __name__ == "__main__":
    try:
        app.run()
    except:
        pass