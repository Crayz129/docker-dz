from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import random

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Генератор случайных чисел</title>
</head>
<body>
    <h1>Генератор случайных чисел</h1>
    <label for='min'>Min:</label>
    <input type='number' id='min' value='1'>
    <label for='max'>Max:</label>
    <input type='number' id='max' value='100'>
    <button onclick='generate()'>Сгенерировать</button>
    <h2 id='result'></h2>
    <script>
        async function generate() {
            let min = document.getElementById('min').value;
            let max = document.getElementById('max').value;
            let response = await fetch(`/random?min=${min}&max=${max}`);
            let data = await response.json();
            document.getElementById('result').innerText = data.random_number || data.error;
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    return html_content

@app.get("/random")
def get_random_number(min: int = 1, max: int = 100):
    if min > max:
        return {"error": "Минимальное значение больше максимального"}
    return {"random_number": random.randint(min, max)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
