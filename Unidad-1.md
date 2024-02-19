# Objetivo

Conocer los conceptos básicos de Ciencia de Datos

---

# Tema 1.1 - Definición Y Conceptos

==Actualmente estamos recolectando más información que nunca== y esto seguirá avanzando a través del tiempo, un dato[^1] se define como una mínima pieza de información y esta mínima pieza de información se puede extraer de cualquier cosa.

[^1]: Un **[dato](Diccionario.md)** es una unidad mínima de información.

---

## Ciencia de datos

Conjunto de metodologías para absorber datos y obtener conclusiones significativas.

> "Desde los albores de la civilización hasta 2003 se crearon 5 exabytes de información, pero ahora se crea esa cantidad de información cada dos días." - Eric Schmidt, Ex presidente ejecutivo de Google

Cada día se sube más información a internet, _Eric Schmidt_ nos dice que si desde un inicio hubiéramos tenido registro de más información desde un comienzo, la cantidad de información sería inmensa y con la llegada de la tecnología y su evolución, esto está avanzando cada vez más a pasos agigantados.

---

### Casos de estudio

- Machine learning tradicional
- Internet of Things (IoT)
- Deep learning

---

## Entendimiento del negocio

El entendimiento del negocio es comprender el **contexto** que existe acerca del negocio.

Los datos que tenemos alrededor nos pueden ayudar a una buena **toma de decisiones**. Una decisión informada requiere **datos**.

---

### Ejemplo

Tenemos el ejemplo sencillo de buscar información sobre si es zona comercial el lugar para iniciar el negocio de un restaurante. Nosotros deseamos saber que tipo de negocio se trata.

![Dibujo de ejemplo](assets/Drawing%202024-01-31%2012.32.20.excalidraw.png)

Nosotros seguimos un algoritmo diferente en la cabeza para llegar a una respuesta. Todos revisamos la ubicación del restaurante y evaluamos el vecindario. Sin embargo, cada uno de nosotros tiene una medida diferente de que tan lejos revisar para tomar una decisión.

El proceso que nosotros seguimos para obtener nuestra conclusión sobre qué tipo de negocio puede ser, está similar al proceso de [Machine Learning](../../../Engineering/Machine%20Learning.md).

(algoritmo K, vecinos cercanos)

#MachineLearning

---

## Modelo canvas (Modelo de negocios canvas)

![Modelo canvas](assets/Pasted%20image%2020240201123842.png)

El **Modelo Canvas** es una herramienta de gestión estratégica que te permite conocer los aspectos clave de tu negocio y cómo se relacionan entre sí. Este modelo condensa la información más relevante de la empresa en **nueve categorías interconectadas**, lo que facilita la estructuración de un modelo de negocio de manera concisa.

### Ejercicio (Entendimiento del negocio)

1. Describir el modelo de negocio con el modelo canvas de las siguientes empresas:
   - OXXO
   - SAP
   - Liverpool
   - pwc
2. ¿Por qué definieron ese modelo? ¿Qué objetivos persigue ese negocio?

---

## El rol del científico de datos

Es el responsable de guiar un proyecto de ciencia de datos de inicio a fin.

Trabajar directamente con los datos, realizar pruebas estadísticas, aplicar modelos de aprendizaje de máquina y evaluar los resultados.

#### Persona

Existen diversas cosas que debe tener un científico de datos.

##### Conocimientos

- Programación (conocer lenguajes de programación)
- Estadística
- Comunicación (saber transmitir seguridad)
- Visualización de datos (graficación de datos)
- Experiencia (experiencia en el rol)

##### Actitud

- Ser creativo (para programar y encontrar soluciones)
- Tolerancia a los fallos
- Comprender sus herramientas
- Aprecio por la diversidad
- Escepticismo
- Habilidad de la comunicación

---

## ¿Cómo abordar un problema de ciencia de datos?

1. Establecer una línea base de comparación
2. Llevar un registro de actividades realizadas
3. Utiliza conocimiento del dominio en la medida de lo posible
4. Apoyarte en la información relacionada al dominio del problema para la toma de decisiones

---

![Diagrama de tratamiento de información](assets/Pasted%20image%2020240207183636.png)

# Tema 1.2 - Historia

## Cuarta revolución industrial

## Campos de uso

### Banca

### Ciberseguridad

### Riesgo

Para predecir decisiones de riesgo

### Imágenes

### Marketing

### Automatización

# Tema 1.3 - Habilidades De Un Científico De Datos

Existen por lo general cuatro areas de un ingeniero en esta area.

## Data engineer

Esta primer area debe recopilar información y entender lenguajes de programación para mantener la base de datos

## Data analyst

Se encarga de representar los datos

Herramientas:

- Excel o Google Sheets

## Data scientist tools

Herramientas:

- Conocer librerías de Python o R

## Machine learning scientist

Se encarga de hacer predicciones o extrapolar la información

Herramientas:

- Conocer librerías de Python o R

# Tema 1.4 - Técnicas Y Herramientas Para Ciencia De Datos

# Tema 1.5 - Origen De Los Datos

---

# Tema 1.6 - Formatos Y Extracción De Datos

El proceso de extracción de datos comienza con la identificación de las fuentes de datos. ==Se debe tener claro qué datos se necesita y dónde se encuentran.== Las fuentes pueden ser desde documentos, bases de datos hasta en redes sociales y una vez identificado la fuente, debemos saber que método debemos usar.

---

## Desafíos

- Volumen de los datos
- Complejidad de los datos
- Manejo y monitoreo de los errores
- Escalabilidad
- Automatización
- Heterogeneidad de los datos

---
## Extracción vs minería de datos


---

### Extracción

La extracción es solamente recopular datos de distintas fuentes y prepararlos para su análisis o almacenamiento

---

### Minería de datos

Es reconocer patrones, tendencias, ideas o conocimientos valiosos a partir de un conjunto de datos.

La minería de datos a menudo requiere una comprensión profunda del análisis estadístico y el aprendizaje automático.

#### Identificar fuentes de datos

El proceso de extracción de datos comienza en la identificación de las fuentes de datos, o sea de dónde se extrae la información.

#### Fuente de conexión

Luego,

#### Consulta o recuperación

Puede extraerse mediante

#### Transformación y carga de datos

En este paso se convierten los datos a un formato requerido por el destino final para que sea más fácil para su analisis.

## Web scraping

El web scraping se utuliza para recopilar datos de diversas fuentes en línea, como sitios web, de comercio electrónico, sitios de noticias, etc...

## Extracción basada en API

Muchos servicios web proporcionan API que les permiten a los desarrolladores recuperar datos de aplicaciones en un formato estructurado, este consiste en solicitudes HTTP a estas API y luego recuperar datos.
