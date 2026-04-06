# 📚 CRUD de Útiles Escolares

Este proyecto es una aplicación web básica que implementa un sistema CRUD (Crear, Leer, Actualizar y Eliminar) para gestionar un inventario de útiles escolares.

Fue desarrollado como actividad práctica para comprender el manejo de datos en una aplicación web utilizando Python.

---

## 🚀 Funcionalidades

* ✅ Ver lista de útiles escolares
* ✅ Agregar nuevos productos
* ✅ Editar productos existentes
* ✅ Eliminar productos
* ✅ Mostrar la cantidad disponible
* ✅ Mostrar el precio de cada producto
* ✅ (Nivel medio/avanzado) Manejo de la **marca**
* ✅ (Nivel avanzado) Cálculo del **valor total del inventario**

---

## 🧱 Estructura del Proyecto

* `app.py` → Lógica principal de la aplicación
* `templates/index.html` → Interfaz de usuario
* Lista de productos almacenada en memoria

---

## 🛠️ Tecnologías utilizadas

* Python
* Flask
* HTML
* Bootstrap (para estilos)

---

## 📦 Ejemplo de datos

```python
productos = [
    {"id": 1, "nombre": "Cuaderno", "cantidad": 50, "precio": 2.50, "marca": "Norma"},
    {"id": 2, "nombre": "Lápiz HB", "cantidad": 100, "precio": 0.30, "marca": "Mirado"},
    {"id": 3, "nombre": "Borrador", "cantidad": 80, "precio": 0.50, "marca": "Pelikan"},
]
```

---

## ▶️ Cómo ejecutar el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/zulemasanchezm/Actividad-Crud.git
```

2. Entra a la carpeta del proyecto:

```bash
cd Actividad-Crud
```

3. Ejecuta la aplicación:

```bash
python app.py
```

4. Abre tu navegador en:

```
http://localhost:5000
```

---

## 📊 Funcionalidad avanzada

### 🏷️ Campo "Marca"

Se agregó el atributo **marca** en:

* Lista de productos
* Formulario HTML
* Tabla de visualización

---

### 💰 Valor total del inventario

La aplicación calcula automáticamente el valor total del inventario con la fórmula:

```
total = precio × cantidad
```

Y muestra el resultado al final de la tabla.

---

## ✅ Checklist de la actividad

* ✔️ Mínimo 8 útiles escolares agregados
* ✔️ Aplicación funcional sin errores
* ✔️ CRUD completo operativo
* ✔️ Campo "marca" implementado
* ✔️ Total del inventario calculado

---

## 🎯 Objetivo

Practicar conceptos básicos de desarrollo web como:

* Manipulación de datos
* Formularios
* Renderizado dinámico
* Lógica CRUD

---

## 👨‍💻 Autor

Proyecto realizado como actividad académica.

---
