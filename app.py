from flask import Flask, render_template, request, redirect, url_for
from flask_sqlachemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuración de la base de datos
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelos
class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    equipos = db.relationship('Equipo', backref='marca', lazy=True)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    equipos = db.relationship('Equipo', backref='categoria', lazy=True)

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    costo = db.Column(db.Float, nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipos', methods=['GET', 'POST'])
def equipos():
    equipos = Equipo.query.all()
    marcas = Marca.query.all()
    categorias = Categoria.query.all()

    if request.method == 'POST':
        modelo = request.form['modelo']
        costo = request.form['costo']
        marca_id = request.form['marca_id']
        categoria_id = request.form['categoria_id']
        nuevo_equipo = Equipo(modelo=modelo, costo=costo, marca_id=marca_id, categoria_id=categoria_id)
        db.session.add(nuevo_equipo)
        db.session.commit()
        return redirect(url_for('equipos'))

    return render_template('equipo_list.html', equipos=equipos, marcas=marcas, categorias=categorias)

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    clientes = Cliente.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        nuevo_cliente = Cliente(nombre=nombre, email=email)
        db.session.add(nuevo_cliente)
        db.session.commit()
        return redirect(url_for('clientes'))

    return render_template('cliente_form.html', clientes=clientes)

@app.route('/ventas', methods=['GET', 'POST'])
def ventas():
    equipos = Equipo.query.all()
    clientes = Cliente.query.all()

    if request.method == 'POST':
        equipo_id = request.form['equipo_id']
        cliente_id = request.form['cliente_id']
        nueva_venta = Venta(equipo_id=equipo_id, cliente_id=cliente_id, fecha=request.form['fecha'])
        db.session.add(nueva_venta)
        db.session.commit()
        return redirect(url_for('ventas'))

    return render_template('venta_form.html', equipos=equipos, clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
