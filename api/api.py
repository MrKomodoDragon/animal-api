from quart import Quart

app = Quart(__name__)

@app.route('/')
async def root():
	return "Hello! This is the animal api made by MrKomodoDragon and tom the bomb :)"


app.run()