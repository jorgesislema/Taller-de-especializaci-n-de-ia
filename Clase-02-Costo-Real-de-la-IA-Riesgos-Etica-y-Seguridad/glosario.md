# Glosario — Clase 2

> Terminos de esta clase, en lenguaje sencillo, con analogia. Si una palabra te traba, veni aca.

---

## A

### Anonimizacion
**Limpiar datos** antes de enviarlos a la IA. Como usar un seudonimo: cambias nombres reales por "Cliente A", "Empresa X", numeros de telefono por "XXX-XXX". La IA puede trabajar con la estructura del dato sin ver la informacion personal.

### Antropomorfismo
**Atribuirle caracteristicas humanas a algo que no es humano.** Cuando decis "la IA me entiende" o "la IA me quiere ayudar", estas antropomorfizando. La IA no entiende ni quiere nada. Calcula. Es el tema central de esta clase.

### API (Application Programming Interface)
Una **ventanilla** por donde tu programa le pide cosas al programa de otro. Como cuando vas al banco: no entras a la boveda, le pedis al cajero (la API) lo que necesitas, y el te lo trae. Las APIs de IA te dejan usar un modelo desde tu propio programa.

---

## B

### Burbuja economica
Cuando **el dinero invertido en algo supera por mucho lo que eso realmente genera**. Como cuando todos compran entradas a un concierto en reventa creyendo que el precio va a subir, pero el concierto no vale eso. Muchos analistas se preguntan si la IA esta en burbuja hoy.

---

## C

### Cifrado (Encryption)
**Codificar un mensaje** para que solo el destinatario pueda leerlo. Como meter una carta en una caja fuerte con llave: aunque alguien la intercepte en el camino, no puede leerla sin la llave. HTTPS usa cifrado.

### Cifrado de extremo a extremo (E2EE)
**Cifrado donde solo el emisor y el receptor tienen la llave.** Ni siquiera la empresa que transmite el mensaje puede leerlo. WhatsApp lo usa. Pero ojo: cuando le escribis a ChatGPT, NO hay cifrado de extremo a extremo entre vos y OpenAI. Ellos pueden leer tu mensaje.

---

## D

### Datos de entrenamiento
El **conjunto de textos, imagenes, codigos** que se le muestran a la IA para que aprenda patrones. Como la biblioteca del aprendiz de panadero: si la biblioteca solo tiene libros de pan dulce, la IA no va a saber hacer pan frances.

### Deepfake
**Contenido falso generado por IA** que parece real. Puede ser un video donde alguien dice algo que nunca dijo, o una foto de un lugar que no existe. Como un disfraz digital perfecto.

---

## E

### Efecto ELIZA
Un fenomeno de los anos 60: un chatbot simple que **parafraseaba** lo que le decias hizo que usuarios le contaran sus problemas personales, creyendo que los "entendia". El efecto sigue hoy: le atribuimos empatia a la IA porque su texto suena empatico.

### Embedding (ver Clase 1)
Representacion de texto como numeros (vectores). Lo veremos en profundidad en la Clase 12.

---

## G

### GDPR (General Data Protection Regulation)
La **ley de proteccion de datos mas estricta del mundo** (Europa, 2018). Obliga a las empresas a pedir permiso para usar tus datos, dejarte borrarlos, y explicar para que los usan. Si una empresa no cumple, la multan fuerte.

### GPU (Graphics Processing Unit)
Una **tarjeta disenada para hacer muchos calculos a la vez**. Nacio para videojuegos, pero resulto perfecta para entrenar IA. Nvidia domina el mercado. Sin GPUs, no hay ChatGPT.

---

## H

### HTTPS
La version **segura** de HTTP (el protocolo con que tu navegador habla con los servidores web). La "S" es de "Secure": usa cifrado para que nadie pueda leer lo que viaja entre tu PC y el servidor. Si ves el candadito en la barra del navegador, es HTTPS.

### Human-in-the-Loop (HITL)
**Humano en el medio.** Un sistema donde la IA trabaja pero un humano revisa y aprueba antes de que el resultado se use. Como un piloto automatico: el avion vuela solo, pero el piloto humano supervisa y toma el control si algo falla.

---

## I

### Inferencia
Cuando un modelo de IA **ya entrenado** recibe un input y genera un output. Como un cocinero que ya aprendio la receta y ahora cocina pedidos. La inferencia es lo que pasa cada vez que le escribis a ChatGPT.

### ISP (Internet Service Provider)
Tu **proveedor de internet** (Movistar, Claro, Tigo, etc.). Es por donde pasan todos tus datos antes de llegar a internet. Puede ver (y en algunos paises, registrar) lo que envias.

---

## L

### LLM (ver Clase 1)
Modelo de Lenguaje Grande. Programa entrenado con miles de millones de textos que predice la siguiente palabra.

---

## M

### Man-in-the-Middle (MitM)
**Ataque donde alguien se mete en el medio** de tu comunicacion con un servidor. Como un cartero que abre tus cartas, las lee, y las vuelve a cerrar antes de entregarlas. Por eso existe HTTPS: para que aunque alguien se meta en el medio, no pueda leer nada.

### Modelo (ver Clase 1)
El resultado de entrenar una IA con datos. El "cerebro ya entrenado".

---

## N

### Nvidia
La empresa que **fabrica las GPUs mas potentes del mundo**. Sin sus chips, la IA moderna no existiria. Su valor en bolsa paso de ~$400 mil millones a ~$3 billones entre 2023 y 2025.

---

## O

### OpenAI
La empresa detras de **ChatGPT y GPT-4**. Fundada en 2015 como organizacion sin fines de lucro, se convirtio en empresa con fines de lucro en 2019. Su modelo de negocio: suscripciones + APIs.

### Output (Salida)
Lo que la IA **produce**: texto, imagen, codigo. El resultado despues de procesar tu input.

---

## P

### Parametro (ver Clase 1)
Un peso ajustable dentro de un modelo. GPT-4 tiene estimados ~1.8 billones de parametros.

### Privacidad diferencial
Tecnica que **agrega ruido matematico** a los datos para que no se pueda identificar a ninguna persona especifica, pero el conjunto sigue siendo util para entrenar. Como mezclar tintas: sabes que hay rojo y azul, pero no puedes separarlas de nuevo.

### Prompt (Entrada)
Lo que vos le **escribis** a la IA. Tu mensaje, tu pregunta, tu instruccion.

---

## R

### Ransomware
**Software malicioso** que cifra tus archivos y te pide un rescate (ransom) para desbloquearlos. Algunos ransomwares modernos usan IA para escribir mensajes de rescate mas convincentes.

### RLHF (Reinforcement Learning from Human Feedback)
Entrenamiento con feedback humano. Humanos califican respuestas del modelo ("buena" / "mala"). El modelo aprende a generar respuestas que los humanos prefieren. Es lo que hace que ChatGPT sea "educado" y "util".

### Rotacion de datos (Data Retention)
**Cuanto tiempo guarda una empresa tus datos.** "Zero retention" = no guardan nada despues de responder. "30 dias" = guardan 30 dias. "Indefinido" = guardan para siempre (y probablemente para entrenar).

---

## S

### Sesgo (Bias)
Una **inclinacion sistematica** en los datos o el modelo. Si entrenas una IA solo con textos en ingles de EE.UU., va a tener sesgo cultural estadounidense. Como un juez que solo conoce las leyes de su pais: no puede juzgar justamente casos de otros paises.

### Sombra (Shadow AI)
Cuando empleados de una empresa **usan IA sin que la empresa lo sepa ni lo autorice**. Como tener un empleado fantasma que decide cosas por tu espalda. Es un riesgo enorme de seguridad corporativa.

### SSL/TLS
Los protocolos de **cifrado** que usa HTTPS. Son las reglas matematicas que garantizan que tu mensaje viaje cifrado entre tu PC y el servidor.

---

## T

### Token (ver Clase 1)
Trozo minimo de texto convertido en numero.

### ToS (Terms of Service / Terminos de Servicio)
El **contrato** que aceptas (sin leer) cuando te registras en un servicio. Ahi dice que pueden hacer con tus datos. En planes gratuitos de IA, casi siempre dice que pueden usar tus datos para entrenar.

---

## V

### VPN (Virtual Private Network)
Un **tunel cifrado** entre tu PC y un servidor lejano. Tu ISP no ve que haces, solo ve que estas conectado a la VPN. No te hace invisible, pero protege tu trafico de miradas locales.

---

> Falta algun termino? Avisale al instructor para agregarlo.