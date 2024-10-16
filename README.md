# DarkSocialAnalytics

## Descripción del Proyecto

**DarkSocialAnalytics** es un proyecto de análisis de datos que tiene como objetivo analizar el comportamiento de los usuarios en diferentes plataformas de redes sociales y su nivel de adicción. A través de este proyecto, se exploran diferentes métricas como el tiempo de uso, la satisfacción de los usuarios y las razones detrás del uso excesivo de redes sociales.

Este análisis incluye un **Análisis Exploratorio de Datos (EDA)** y visualizaciones avanzadas utilizando **Plotly**, con gráficos interactivos como **Treemaps** y gráficos de barras personalizados inspirados en los estándares de presentación profesional.

---

## Estructura del Proyecto

La estructura de carpetas sigue las mejores prácticas de organización para proyectos de **Data Science**:

```plaintext
DarkSocialAnalytics/
│
├── data/
│   ├── processed/                         # Datos procesados listos para su análisis
│   │   └── cleaned_TimeWasters_SocialMedia.csv
│   └── raw/                               # Datos en crudo sin procesar
│       └── TimeWasters_SocialMedia.csv
│
├── notebooks/                             # Jupyter Notebooks con el análisis
│   ├── eda.ipynb                          # Análisis Exploratorio de Datos (EDA)
│   └── visualizations.ipynb               # Visualizaciones avanzadas
│
├── outputs/                               # Resultados y gráficos generados
│   └── age_distribution.png               # Gráfico de distribución de edad
│
├── scripts/                               # Scripts de Python
│   ├── data_cleaning.py                   # Script para limpieza de datos
│   └── __pycache__/                       # Archivos temporales generados por Python
│
├── venv/                                  # Entorno virtual para el proyecto
├── .gitignore                             # Archivos y carpetas ignoradas por Git
├── README.md                              # Descripción del proyecto
└── requirements.txt                       # Dependencias del proyecto
```

## Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
```

### 2. Crear y Activar un Entorno Virtual
```bash
# Crear entorno virtual
python -m venv env

# Activar entorno virtual
# En Unix/macOS:
source env/bin/activate
# En Windows:
env\Scripts\activate
```

### 3. Instalar las Dependencias
```bash
pip install -r requirements.txt
```

## Uso del Proyecto

### 1. Limpieza de Datos
El script `data_cleaning.py` en la carpeta `scripts/` se encarga de la limpieza de datos:
```bash
python scripts/data_cleaning.py
```

Este script procesa el archivo `TimeWasters_SocialMedia.csv` (ubicado en `data/raw/`) y genera un archivo limpio `cleaned_TimeWasters_SocialMedia.csv` en la carpeta `data/processed/`.

### 2. Análisis Exploratorio de Datos (EDA)
Para ejecutar el notebook de análisis exploratorio:
```bash
jupyter notebook notebooks/eda.ipynb
```

### 3. Visualizaciones
Para acceder a las visualizaciones avanzadas (incluyendo gráficos interactivos de Plotly):
```bash
jupyter notebook notebooks/visualizations.ipynb
```

## Resultados Clave

- **Distribución de Usuarios por Plataforma**: Gráfico de barras mostrando la distribución de usuarios en Instagram, Facebook, YouTube y TikTok.
- **Nivel de Adicción por Género**: Treemap visualizando niveles de adicción entre hombres y mujeres en diferentes plataformas.
- **Distribución de Edad**: Gráfico de distribución de edad (`age_distribution.png`) mostrando la demografía de usuarios.

## Contribución

Para contribuir al proyecto:

1. Haz un fork del repositorio
2. Crea una nueva rama:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -am 'Añadir nueva funcionalidad'
   ```
4. Sube los cambios a tu rama:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Crea un nuevo Pull Request
