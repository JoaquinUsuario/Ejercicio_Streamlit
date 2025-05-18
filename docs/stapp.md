# Documentación de la Aplicación

## ¿Qué es nuestro Dashboard?

Esta aplicación es un dashboard interactivo que permite a los usuarios cargar sus propios archivos CSV y realizar análisis exploratorio de datos de manera sencilla y visual.

## Funcionalidades

### 1. Carga de Datos
- La aplicación acepta archivos en formato CSV
- Interfaz de arrastrar y soltar para subir archivos
- Validación automática del formato de archivo

### 2. Visualización de Datos
- Vista previa de las primeras filas del dataset
- Resumen estadístico completo de los datos
- Visualización de tipos de datos y valores únicos

### 3. Filtrado de Datos
- Selección dinámica de columnas
- Filtrado por valores únicos en cada columna
- Vista previa instantánea de datos filtrados

### 4. Generación de Gráficos
- Creación de gráficos lineales interactivos
- Selección flexible de ejes X e Y
- Visualización automática de tendencias

## Guía de Uso

1. **Carga de Datos**
   - Haga clic en "Choose a CSV file" o arrastre su archivo CSV
   - Espere a que los datos se carguen

2. **Exploración Inicial**
   - Revise la vista previa de datos
   - Examine el resumen estadístico
   - Identifique columnas de interés

3. **Filtrado**
   - Seleccione una columna para filtrar
   - Elija un valor específico
   - Observe los resultados filtrados

4. **Visualización**
   - Seleccione columnas para los ejes X e Y
   - Haga clic en "Generate Plot"
   - Analice el gráfico resultante

## Requisitos Técnicos

- Python 3.6 o superior
- Streamlit 1.32.2
- Pandas 2.2.1
- Matplotlib 3.8.3

## Consejos de Uso

- Asegúrese de que su CSV esté correctamente formateado
- Para mejores resultados, use datos numéricos para la generación de gráficos
- Explore diferentes combinaciones de columnas para descubrir patrones
- Utilice el filtrado para enfocarse en subconjuntos específicos de datos 