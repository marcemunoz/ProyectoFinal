from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/")
def dashboard():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Dashboard Demo</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #eef3f9;
            }
            .sidebar {
                width: 80px;
                background: #1f3c88;
                height: 100vh;
                color: white;
                float: left;
                padding-top: 20px;
            }
            .sidebar .logo {
                text-align: center;
                margin-bottom: 30px;
                font-weight: bold;
            }
            .sidebar ul {
                list-style: none;
                padding: 0;
            }
            .sidebar li {
                padding: 15px;
                margin: 10px 0;
                text-align: center;
                cursor: pointer;
                font-size: 18px;
            }
            .sidebar li.active,
            .sidebar li:hover {
                background: #304ba3;
                border-radius: 10px;
            }
            .content {
                margin-left: 80px;
                padding: 20px;
            }
            .topbar {
                display: flex;
                justify-content: space-between;
                margin-bottom: 20px;
            }
            .cards {
                display: flex;
                gap: 20px;
            }
            .card {
                background: white;
                padding: 20px;
                border-radius: 10px;
                flex: 1;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            .card.blue {
                background: #2e86de;
                color: white;
            }
            .card .value {
                font-size: 24px;
                margin-top: 10px;
            }
            .bigbox {
                background: white;
                margin-top: 20px;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            .bottom-row {
                display: flex;
                gap: 20px;
                margin-top: 20px;
            }
            .mini {
                flex: 1;
            }
        </style>
    </head>
    <body>
        <div class="sidebar">
            <div class="logo">Dashboard</div>
            <ul>
                <li class="active">📊 Inicio</li>
                <li>⭐ Favoritos</li>
                <li>📁 Proyectos</li>
                <li>💬 Mensajes</li>
                <li>📧 Email</li>
            </ul>
        </div>

        <div class="content">
            <div class="topbar">
                <div></div>
                <div class="user">Natasha Ros</div>
            </div>

            <div class="cards">
                <div class="card blue">
                    <h3>Total amount</h3>
                    <p class="value">$ 17,421.97</p>
                </div>
                <div class="card">
                    <h3>Monthly amount</h3>
                    <p class="value">$ 2,194.20</p>
                </div>
                <div class="card">
                    <h3>Total downloads</h3>
                    <p class="value">1,928,838</p>
                </div>
            </div>

            <div class="bigbox">
                <canvas id="lineChart"></canvas>
            </div>

            <div class="bottom-row">
                <div class="mini card">
                    <h4>Yearly result</h4>
                    <canvas id="barChart"></canvas>
                </div>

                <div class="mini card">
                    <h4>Comparación</h4>
                    <canvas id="pieChart"></canvas>
                </div>
            </div>
        </div>

        <script>
            // Line Chart
            new Chart(document.getElementById("lineChart"), {
                type: "line",
                data: {
                    labels: ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago"],
                    datasets: [{
                        data: [10,25,15,20,35,30,45,40],
                        borderWidth: 2,
                        fill: false
                    }]
                }
            });

            // Bar Chart
            new Chart(document.getElementById("barChart"), {
                type: "bar",
                data: {
                    labels: ["2017","2018","2019","2020","2021"],
                    datasets: [{
                        data: [5,10,6,12,8]
                    }]
                }
            });

            // Pie Chart
            new Chart(document.getElementById("pieChart"), {
                type: "doughnut",
                data: {
                    labels: ["2019","2020"],
                    datasets: [{
                        data: [65,75]
                    }]
                }
            });
        </script>
    </body>
    </html>
    """
    return Response(html_content, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
