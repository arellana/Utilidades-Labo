# 🛠️ Utilidades-Labo

**📌 Scripts útiles para laboratorio**  

Colección de scripts en **Python**, **MATLAB** y algo de **OriginLab**, prácticos para uso en entornos de laboratorio de **física** y análisis de datos, pensados especialmente para iniciantes en la programación.  

---

## 📂 Contenido del Repositorio

- 🌀 **Smooth.py**  
  Script en Python para **suavizar datos** (filtros, suavizado de series de tiempo, etc.).  

- 📈 **ajusteDeDatos_v2.py**  
  Código en Python para **ajustes y modelado de datos** (ej. regresión, calibración).  

- 📊 **multipleData.py**  
  Manejo y procesamiento de **múltiples datasets** simultáneamente (automatización de lecturas, comparación, etc.).  

- 🔬 **practica3-labo.py**  
  Script de apoyo para **prácticas de laboratorio**, incluye cálculos y visualizaciones.  

- 📂 **upperDirectory.py**  
  Herramienta para navegar jerárquicamente directorios (ideal para organizar datasets o estructuras de carpetas).  

- 📐 **Practica3-Osciladores.opj**  
  Proyecto de **OriginLab** asociado a un **experimento de osciladores**, con datos de prueba y análisis de resultados.  
  *(Creado en OriginLab 8.5 y probado en Origin 9)*

  ---

## ⚡ Carpeta: CampoE y potencial

Programas para resolver el **campo electrostático** mediante la **discretización del potencial** en un rectángulo, usando el **método de diferencias finitas**.  

### 📁 Estructura de archivos

- **Mediciones/**  
  Contiene los archivos `Conductorj.txt` (j = 1,2,3), con 3 columnas:  
  - `X`, `Y`: coordenadas espaciales.  
  - `Volt`: tensión medida.  

- **programas/**  
  - ⚙️ `AutorunCampos.py`: ejecuta automáticamente `Campo1.py`, `Campo2.py` o `Campo3.py` según la elección del usuario.  
  - 📐 `Campo.py`: procesa `Conductor1.txt`, genera matrices del campo eléctrico (`Ex1.txt`, `Ey1.txt`) y el potencial, guardados en:
    - `Camposdiscret/` → componentes discretizadas del campo.  
    - `Potenciales/` → potencial electrostático.  
    - `Campos/` → gráficos del campo eléctrico.  
  - 📐 `Campo2.py`, `Campo3.py`: igual a `Campo.py` pero aplicados a `Conductor2.txt` y `Conductor3.txt`.  

- **Potencial1.m**, **Potencial2.m**, **Potencial3.m**  
  Scripts en **MATLAB/Octave** para graficar:  
  - Representaciones 2D del campo eléctrico.  
  - Superficie 3D del potencial electrostático.  

- **Autorun.m**  
  Permite elegir y graficar los resultados de `Campo.py`, `Campo2.py` y `Campo3.py`.  
  *(Nota: puede no funcionar si se ejecuta directamente; en Octave se recomienda usar `octave -f Autorun.m` o abrir desde la aplicación).*  

---

---

## ▶️ Cómo Usar

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/arellana/Utilidades-Labo.git
   cd Utilidades-Labo

2. **Instalar dependencias**
   Instalación de librerías básicas:

   ```bash
   pip install numpy scipy matplotlib pandas
   ```

   ➕ En caso de necesitar otra librería, repetir el comando anterior cambiando el nombre de la librería deseada.

3. **Ejecutar los scripts**

   ```bash
   python Smooth.py
   python ajusteDeDatos_v2.py
   ```

4. **Abrir el archivo de proyecto**

   * `Practica3-Osciladores.opj` puede abrirse con **Origin** u otro software compatible `.opj`.

---

## 📌 Cosas por Hacer

* 📝 Mejorar la documentación dentro de los scripts para mayor claridad.
* 📂 Dividir los scripts por categorías si la colección crece.

---

## 👨‍🔬 Sobre el Repositorio

* **Autor:** Javier Arellana
  Instituto de Astronomía y Física del Espacio (**IAFE**), UBA – CONICET
  Departamento de Física, Facultad de Ciencias Exactas y Naturales, **Universidad de Buenos Aires**

📬 Contacto:

* ✉️ [arellana.javier.e@gmail.com](mailto:arellana.javier.e@gmail.com)
* 📧 [jarellana@iafe.uba.ar](mailto:jarellana@iafe.uba.ar)

---
