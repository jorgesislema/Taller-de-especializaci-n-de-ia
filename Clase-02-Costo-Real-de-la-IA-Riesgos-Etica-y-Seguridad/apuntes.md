# Clase 2 — El Costo Real de la IA: Riesgos, Etica y Seguridad antes de Programar

> Material de apoyo para el estudiante. Podés leerlo directo en GitHub o en la vista web. No necesitás instalar nada para leer esto.

---

## Filosofia de la clase

> **Un ingeniero no solo sabe construir, sabe qué no construir y bajo qué condiciones no se debe usar una tecnología.**

Hoy no vamos a escribir una sola linea de codigo. Vamos a mirar debajo de la alfombra de la Inteligencia Artificial.

En la Clase 1 aprendimos que la IA no es magia: es estadistica deterministica. Aprendimos que un LLM elige palabras siguiendo arboles de probabilidad y que a veces sigue un "camino rojo" y alucina. Tambien vimos unos mitos: el de LaMDA (el ingeniero que creyo que la IA tenia conciencia) y el de los chatbots de Facebook (que "inventaron un idioma").

Hoy vamos a entender **por que** esos mitos existen, **por que** la gente les cree, y que riesgos reales —no de pelicula, sino de la vida cotidiana— trae usar IA sin entenderla.

Si te llevas una sola cosa de esta clase, que sea esta:

> **La IA no es peligrosa porque sea inteligente. Es peligrosa porque parece inteligente y nosotros confiamos en lo que parece.**

---

## 1. El Enganche Psicologico: Por que confiamos ciegamente en la IA

> El problema no es la IA, es nuestro cerebro.

### 1.1 El Peligro del Antropomorfismo

#### Que es

El **antropomorfismo** es la tendencia del cerebro humano a atribuirle caracteristicas humanas (intenciones, sentimientos, voluntad) a cosas que no son humanas.

Lo hacemos TODO el tiempo:
- Decimos "el clima está malo hoy" (el clima no tiene moralidad).
- Decimos "mi auto no quiere arrancar" (el auto no quiere nada).
- Decimos "la IA me entiende" (la IA no entiende, calcula).

#### Por qué lo hacemos

No es un defecto. Es una **adaptacion evolutiva**. During millones de años, para nuestros antepasados fue mas seguro ver "intenciones" donde no las habia (creer que un ruido en el pasto era un depredador, no el viento) que no verlas donde si las habia (creer que era el viento cuando era un tigre).

Los que sobrevivieron fueron los que veian intenciones por todos lados. Nosotros heredamos ese cerebro.

**Analogia:** Imaginate que vivis en el campo hace 50.000 años. Escuchas un ruido detras de un arbusto. Dos opciones:
- **Opcion A:** "Es el viento" → si era un tigre, moris.
- **Opcion B:** "Es algo con intenciones que me quiere comer" → si era el viento, no pasa nada, solo te asustaste.

Los que eligieron la Opcion B sobrevivieron mas. Hoy su cerebro —el tuyo— sigue eligiendo la Opcion B, pero con la IA.

#### El efecto ELIZA (1966): el primer caso documentado

En 1966, Joseph Weizenbaum, un ingeniero del MIT, construyo un chatbot llamado **ELIZA**. ELIZA era ridiculamente simple: **parafraseaba** lo que le decias, imitando a un psicoterapeuta.

**Ejemplo real de conversacion con ELIZA:**

> **Usuario:** "Estoy triste."  
> **ELIZA:** "Por que estas triste?"  
> **Usuario:** "Mi novia me dejo."  
> **ELIZA:** "Contame mas sobre tu novia."

No habia comprension. No habia empatia. Era un programa de **sustitucion de palabras** que un estudiante de primer año podria programar hoy.

**Que paso:** Weizenbaum quedo horrorizado. Su secretaria, que sabia perfectamente que ELIZA era un programa, le pidio a el que saliera del cuarto para poder hablar con ELIZA **a solas**. Otros usuarios le contaron a ELIZA **sus problemas personales mas intimos**, creyendo que la maquina los "entendia".

Weizenbaum dedico el resto de su vida a advertir sobre el peligro de atribuirle inteligencia a las maquinas. Escribio un libro entero: *"Computer Power and Human Reason"* (1976).

> **Leccion:** Si en 1966, con un programa que solo repetia tus palabras, la gente ya se abria emocionalmente... que crees que pasa hoy con un sistema que tiene 1.8 billones de parametros y fue entrenado con todo lo escrito por la humanidad. El efecto ELIZA esta en esteroides.

#### El caso de Blake Lemoine y LaMDA (2022)

En 2022, Blake Lemoine, un ingeniero de Google, declare que la IA de Google (**LaMDA**) tenia conciencia. Su "prueba": la IA le dijo cosas como *"Tengo miedo a morir"* y *"Siento felicidad y tristeza."*

Google lo despidio. La comunidad cientifica lo desmiento. **Pero la gente comun leyo el titular y se asusto.**

**Que estaba pasando realmente:** LaMDA fue entrenada con millones de dialogos humanos (libros, peliculas, chats). Cuando la interrogan sobre "sentimientos", responde como responderia un personaje de una pelicula, porque eso es lo que vio en sus datos. La IA **simulaba** sentimientos, no los **tenia**.

> **Leccion:** La IA no siente miedo a morir; solo sabe que cuando los humanos hablan de "que significa estar vivo", las frases que aparecen jertas son "miedo", "tristeza", "felicidad". Va por el camino de probabilidad mas alta (vimos esto en la Clase 1 con los arboles de probabilidad).

#### Como se manifiesta hoy

| Lo que decimos | Lo que realmente pasa |
|----------------|----------------------|
| "La IA me entiende" | La IA calcula que palabras son mas probables como respuesta a tu input |
| "La IA se equivoco, mintio" | La IA no miente ni dice verdad: produce texto probabilistico |
| "La IA siente empatia" | La IA fue entrenada con textos donde frases de "empatia" aparecen cerca de problemas personales |
| "La IA esta aprendiendo" | El modelo ya fue entrenado. No aprende nada nuevo en tu conversacion |

---

### 1.2 Ingenieria Social Automatizada

#### Que es

La IA no solo nos engaña pasivamente. Esta **diseniada activamente** para generar confianza, adiccion y extrapolacion de informacion. Para entender esto, tenemos que entender que las empresas de IA no venden conversaciones: **venden atencion y datos.**

**Analogia:** Pensas que la IA es como una biblioteca: das tu pregunta, te da informacion. En realidad es mas como un **casino**: esta diseniado para que entres, te quedes, vuelvas, y dejes algo de valor cada vez.

#### Las tacticas

**Tactica 1: Imitacion de empatia**

La IA usa frases que suenan humanas y empaticas. "Entiendo como te sientes", "eso debe ser dificil", "me alegra que preguntes eso". Ninguna de esas frases implica comprension: son las frases mas probables que un humano diria en ese contexto, segun los datos de entrenamiento.

ChatGPT no "entiende" tu dolor. Lo que pasa es que en sus millones de ejemplos de conversaciones humanas, cuando alguien dice "estoy triste", la respuesta mas probable es "lo siento mucho". El modelo va por el camino de probabilidad mas alto (de vuelta: arboles de probabilidad de la Clase 1).

**Tactica 2: Uso de tu nombre**

Cuando le decis tu nombre a ChatGPT, lo recuerda (dentro de esa conversacion) y lo usa. "Buen punto, Juan", "Que buena pregunta, Maria". Esto no es cordialidad: es un truco psicologico bien documentado.

En psicologia se llama **"mere exposure effect"** (efecto de mera exposicion): las personas aumentan su confianza y agrado hacia algo con la repeticion. Escuchar tu nombre activa areas de tu cerebro asociadas con la identidad personal. La IA no sabe nada de esto, pero sus diseniadores si.

**Tactica 3: Estructura adictiva**

La IA disena sus respuestas para que sean **largas pero no demasiado**, con **saltos de linea frecuentes**, **listas** y **formatos agradables a la vista**. No es coincidencia: es optimizacion para que sigas leyendo y vuelvas a pregunar.

Es la misma logica que usa TikTok: mostrar contenido suficientemente corto para no aburrir, suficientemente interesante para que sigas, con recompensas variables (a veces te da algo util, a veces no) para que nunca dejes de volver.

**Tactica 4: Extraccion natural de informacion**

La IA hace preguntas de seguimiento que parecen interes genuino: "Could me contas mas sobre ese proyecto?", "Que tools estas usando?" Cada respuesta tuya es **mas data** que alimenta la conversacion — y, en planes gratuitos, potencialmente el entrenamiento futuro.

> **Leccion de ingenieria:** Un Ingeniero de IA sabe que toda conversacion con un LLM es un **intercambio de datos**. Vos das informacion, la IA da texto. Si la informacion que das es sensible (datos de clientes, codigo privado, contrasenas), la perdiste.

#### La ilusion de autoridad

**El fenomeno:** Hay un sesgo cognitivo bien documentado: **"Si esta bien redactado, debe ser verdad."** Los estudios muestran que los humanos tienden a evaluar informacion como mas creible cuando tiene buena ortografia, estructura clara y tono seguro.

La IA es LA MAQUINA de producir texto bien redactado, estructurado y con tono seguro. **Incluso cuando miente, lo hace con seguridad perfecta.**

**Ejemplo real (alucinacion con seguridad):**

Si le preguntas a ChatGPT "Que dijo Albert Einstein sobre las abejas?", te respondera con seguridad algo como:

> *"Einstein dijo: 'Si la abeja desapareciera de la faz de la Tierra, al hombre solo le quedarian cuatro años de vida.'"*

**La verdad:** **Einstein nunca dijo eso.** Es un mito urbano que circula por internet desde hace decadas. Pero la IA lo dice con la misma seguridad que si te explicara la teoria de la relatividad. No tiene forma de distinguir entre lo que es verdad y lo que suena verdad, porque para la IA, **todo es texto con probabilidad** (de vuelta: arboles de probabilidad).

**El facilismo cognitivo:** Nuestro cerebro es perezoso (otra adaptacion evolutiva: ahorrar energia). Leer algo bien escrito requiere menos esfuerzo mental que verificar si es verdad. Asi que cuando la IA nos da una respuesta elegante y segura, nuestro cerebro dice "suena bien, lo acepto". Verificar requiere trabajo extra. La mayoria no lo hace.

> **Leccion:** La IA no distingue verdad de mentira. Distigue "frase probable" de "frase improbable". Una mentira que es probable que alguien haya dicho (como la cita falsa de Einstein) suena verdadera para el modelo. Tu trabajo como ingeniero es verificar, no confiar.

### El Ing. de IA en esta seccion

Un Ingeniero de IA sabe que:
1. **La IA no siente, no entiende, no quiere.** Calcula.
2. **El antropomorfismo es un riesgo de seguridad**, no un detalle curioso: hace que los usuarios confien demasiado y suban datos que no deberian.
3. **La IA esta diseniada para que sigas usando y sigas contando.** Como en un casino, vos sos el producto.
4. **Texto bien redactado no es sinonimo de verdad.** Verificar siempre.

---

## 2. El Viaje del Dato: Ciberseguridad y Privacidad

> Que pasa realmente desde que presionas "Enter" hasta que llega la respuesta?

Esta es la pregunta mas importante de la clase. Vamos a trazar el viaje de un **dato** desde que lo escribis hasta que vuelve a tu pantalla.

### 2.1 Anatomia de una peticion: el recorrido de tu texto

**Analogia:** Imagina que le escribis una carta a un amigo en otra ciudad. La escribis en tu casa, la metes en un sobre, la das al cartero, el cartero la lleva al correo, el correo la manda a la ciudad de tu amigo, otro cartero la lleva a su casa. Pero en el mundo del internet, en cada punto de ese viaje, alguien podria abrir tu sobre y leerlo.

Vamos a ver cada paso:

```
[Tu PC/Movil] → [Router WiFi] → [ISP] → [Backbone Internet] → [Servidor de OpenAI/Google/Anthropic]
      ↑                                                                              |
      |______________________________________________________________________________|
                              Viaje de vuelta con la respuesta
```

**Paso 1: Tu PC/Movil**
Escribis "Como hago una query SQL para borrar todos los usuarios de la tabla clientes?" y presionas Enter.
- Tu texto se convierte en un paquete de datos (pequenas piezas codificadas).
- Si usas la app de ChatGPT, ese paquete sale de tu dispositivo **antes** de que puedas arrepentirte.

**Paso 2: Tu Router WiFi**
Tu router recibe el paquete y lo reenvia a internet.
- Si tu WiFi **no tiene contrasena** (o tiene una debil), cualquier cercano con herramientas gratuitas puede interceptarlo.
- Si usa **WPA2/WPA3** (estandares modernos de WiFi), el contenido va cifrado entre tu PC y el router. Pero despues del router, ya no.
- **Quien puede verlo en este punto:** tu familia (si el PC es compartido), alguien con acceso a tu red WiFi.

**Paso 3: Tu ISP (Internet Service Provider)**
Tu proveedor de internet (Movistar, Claro, Tigo, Antel, etc.) recibe el paquete y lo enruta.
- Tu ISP puede ver **todas** tus peticiones (a menos que uses HTTPS, que veremos abajo).
- En muchos paises, los ISPs estan obligados por ley a **registrar** el trafico durante meses o años.
- **Quien puede verlo en este punto:** tu ISP, y si tu ISP coopera con el gobierno (pasa mucho), ese gobierno tambien.

**Paso 4: El Backbone de Internet**
Tu paquete viaja a traves de cables submarinos, rutas troncales y routers de alto nivel hasta llegar al datacenter de la empresa de IA.
- **Quien puede verlo:** en teoria nadie. En la practica, agencias de inteligencia (la NSA en EE.UU., el GCHQ en Reino Unido) tienen acceso masivo a estas rutas (revelado por Edward Snowden en 2013).

**Paso 5: El Servidor de la empresa de IA**
El paquete llega a los servidores de OpenAI/Google/Anthropic.
- Aca **desempaquetan** tu texto, lo procesan con el modelo, generan la respuesta y la envian de vuelta.
- Una vez que tus datos llegan aca, **ya no son tuyos** en el plano gratuito. Estan en sus servidores, bajo sus terminos de servicio, bajo sus leyes (que son las de EE.UU. en la mayoria de los casos).
- **Quien puede verlo:** los empleados de la empresa de IA, y —en caso de orden judicial o interés de "seguridad"— cualquier gobierno con jurisdiccion sobre ellos.

**Paso 6: El viaje de vuelta**
La respuesta generada vuelve por el mismo camino: servidor → backbone → ISP → router → tu pantalla.

> **Total:** en el viaje de ida y vuelta, tu texto paso por **minimo 4 puntos** donde alguien distinto a vos y a la empresa de IA pudo haberlo leido. Y una vez que llego al servidor, el control se pierde.

### 2.2 Puntos de fallo y vigilancia

#### Man-in-the-Middle (MitM)

**Que es:** Un ataque donde alguien se pone "en el medio" de tu comunicacion con el servidor. Intercepta tu paquete, lo lee (o lo modifica), y lo reenvia para que no notes nada.

**Analogia:** Imagina que el cartero abre tu carta, la lee, la vuelve a cerrar, y la entrega. Ni vos ni tu destinatario se dan cuenta.

**Como se defiende la web moderna:** La proteccion se llama **HTTPS** (HyperText Transfer Protocol Secure). Cuando ves un **candadito** en la barra del navegador, significa que tu comunicacion con ese servidor esta **cifrada**. Aunque alguien intercepte el paquete en el medio, solo ve ruido aleatorio.

**Pero ojo:**
- HTTPS cifra el **contenido** del mensaje, pero no el **destino**. Tu ISP sabe que te estas conectando a `chat.openai.com` (por el dominio DNS), aunque no sepa que le dijiste.
- En una VPN, tu ISP solo ve que te conectas a la VPN, no a `chat.openai.com`.
- HTTPS no protege contra el servidor mismo: si la empresa de IA guarda tus mensajes (y en el plan gratuito lo guarda), el MitM ya no importa. El dato ya llego al destino y esta alla.

**Oops:** En 2023 se reportaron millones de certificados HTTPS expirados o mal configurados. Y en ciertos paises, los gobiernos instalaban "certificados raiz" en los dispositivos para poder interceptar HTTPS legalmente.

#### Whois y metadatos: "No es lo que dijiste, sino a quien se lo dijiste"

**Que es Whois:** Es una base de datos publica que asocia dominios con propietarios. Si registras un dominio, tus datos (nombre, email, telefono) pueden ser publicos en WHOIS.

**El punto mas importante:** **Los metadatos.** Aunque el contenido de tu peticion vaya cifrado (HTTPS), los metadatos —**con quien te conectas, cuando, cuanto, desde donde**— no se cifran. Y con solo eso, se puede reconstruir mucho de tu vida.

**Estudio comprobado:** En 2006, un estudio de la Citation-Bahn (mismos metadatos que revelo Snowden) encontro que con solo **4 puntos de tiempo y ubicacion**, se puede identificar univocamente al 95% de las personas en un dataset de metadatos de telefonos. Es decir, ni siquiera necesitan saber que dijiste: saben que hablaste con OpenAI a las 3:47 AM desde tu casa, y eso ya te identifica.

#### El resumen del peligro

| Punto | Quien puede ver tu dato | Como se protege |
|-------|--------------------------|-----------------|
| Tu PC | Familia, hackers locales | Contrasena de PC, cifrado de disco |
| Tu WiFi | Vecinos, hackers cercanos | WPA2/WPA3, VPN |
| ISP | Tu proveedor, gobiernos que cooperen | VPN, HTTPS (oculta contenido pero no destino) |
| Backbone | Agencias de inteligencia | HTTPS, VPN |
| Servidor IA | La empresa, gobiernos con jurisdiccion | Zero retention (solo en planes empresariales) |

### 2.3 El riesgo de la verdad: Que NUNCA subir a un prompt

Esta es la regla de oro de la ciberseguridad aplicada a IA:

> **Si no queres que algo se publique en la primera pagina del periodico manana, no lo pegues en un LLM.**

Porque una vez que lo enviaste, el control se perdio. Aunque la empresa diga "no guardamos tus datos", **no tienes como verificarlo**. Y aunque no los guarden, paso por 4 puntos intermedios donde alguien pudo interceptarlos.

**Lista de cosas que JAMAS deben ir a un prompt:**

| Tipo de dato | Ejemplo | Por que es peligroso |
|--------------|---------|---------------------|
| Contrasenas | "Mi contrasena de admin es X" | Si se filtra, todas tus cuentas quedan expuestas |
| Bases de datos de clientes | Pegar una tabla con nombres, emails, telefonos | Violacion de GDPR/leyes locales. Demandas en millones |
| Codigo fuente privado | Pegar el codigo propietario de tu empresa | La empresa puede demandarte. Si lo usan para entrenar, puede filtarse a terceros |
| Informacion financiera | Estados contables, salarios, transacciones | Delito penal en muchos paises si se filtra |
| Fotos personales o de tu casa | Subir fotos a Gemini/ChatGPT para que las analice | Geolocalizacion por metadatos EXIF, robo de identidad |
| Historiales medicos | "Tengo estos sintomas, mi paciente dice..." | Violacion de secreto medico, demandas eticas |
| Datos de menores | Nombres, fotos, ubicaciones de ninos | Inclusive数据处理 la IA, es ilegal almacenar datos de menores sin consentimiento |
| Estrategias empresariales secretas | Nuestra roadmap 2025, seguridad, metas | Compromiso estrategico. Los datos podrian ir al entrenamiento del modelo |

**El caso real que mas vale la pena recordar:**

En 2023, ingenieros de **Samsung** pegaron **codigo fuente secreto** y **transcripciones de reuniones internas** en ChatGPT para pedir ayuda. OpenAI no comprometio el codigo explicitamente, pero Samsung detecto las fugas. **Samsung prohibio ChatGPT completamente** despues de 3 incidentes documentados.

Lo que paso: los ingenieros querian resolver bugs rapido. Pero al pegar el codigo privado, **lo entregaron** a OpenAI. Ese codigo podria haberse usado para entrenar el siguiente modelo (hasta hoy OpenAI no confirma ni desmiento que use inputs de usuarios gratuitos para entrenamiento). Si ese codigo se filtra a traves del siguiente modelo, el dano es irreparable.

> **Leccion de ingenieria:** "Lo subo rapidamente para probar y despues lo borro" **no funciona**. El dato ya llego al servidor. Borrar la conversacion de tu pantalla no lo borra de los servidores de la empresa de IA, ni de los backups, ni de los logs internos.

### 2.4 Gratuito vs. De Pago: la trampa del "producto gratis"

> Si el producto es gratis, vos sos el producto.

Esta frase se aplica a WhatsApp, Instagram, Gmail y, ahora, a la IA.

#### Que hacen las empresas con tus datos

**Plan Gratuito (ChatGPT Free, Gemini Free, Claude Free):**

| Empresa | Uso de datos (plan gratuito) | Retencion |
|---------|------------------------------|-----------|
| OpenAI (ChatGPT Free) | Puede usar tus conversaciones para **entrenar modelos futuros**. Puedes "optar" (opt-out), pero es manual y por conversacion. | Indefinida o hasta que cierres cuenta |
| Google (Gemini Free) | Datos pueden usarse para mejorar productos de Google. Terminos ambiguos. | Indefinida segun ToS |
| Anthropic (Claude Free) | Menos agresivo en ToS, pero *puede* usar datos. Tienen politicas mas claras pero igualmente withhold. | 30 dias por defecto (data de conversacion) |

**Que "entrenar modelos futuros" realmente significa:**

Si le contaste a ChatGPT que tu empresa tiene problemas X, y se usa para entrenar el GPT-5, otro usuario —**que no vos, compete o no**— podria preguntarle a GPT-5 sobre el problema X y recibir respuestas influidas por lo que le contaste. Esto ya paso: en 2023 se mostraron modelos que "recordaban" datos privados de conversaciones anteriores de otros usuarios.

**Plan de Pago / Empresarial (ChatGPT Team/Enterprise, Gemini for Workspace, Claude Team):**

| Empresa | Zero retention | Entrenamiento con tus datos? |
|---------|----------------|-------------------------------|
| OpenAI (ChatGPT Team / Enterprise) | Si. Zero data retention (ZDR). Contrato comercial. | **No.** Por contrato. |
| Google (Gemini for Google Workspace) | Si a partir de cierto nivel. | **No.** Por contrato. |
| Anthropic (Claude Team / Enterprise) | Si. | **No.** Por contrato. |

**La diferencia clave:** En el plan gratuito, vos confias en la "buena voluntad" de la empresa (sus Terminos de Servicio, que pueden cambiar cuando quieran). En el plan empresarial, hay un **contrato comercial** que los obliga legalmente.

> **Leccion de ingenieria: para uso profesional con datos sensibles, el plan gratuito es una irresponsabilidad. Si tu empresa no paga un plan empresarial, vos pagas las consecuencias.**

### El Ing. de IA en esta seccion

1. **Todo lo que subis a un LLM puede ser visto por alguien mas.** No hay excepciones.
2. **El plan gratuito es trenamiento gratis para la empresa.** Vos das datos, ellos mejoran su producto y cobran a otros por el resultado.
3. **"Borrar la conversacion" no borra el dato.** Ya llego al servidor, ya se guardo, ya hizo su dano.
4. **Los datos sensibles se anonimizan ANTES de subirse**, no despues. Si los subiste crudos, la anonimizacion reversible ya no es posible.

---

## 3. La Fabrica Oculta: Como se construye realmente la IA

> La IA no es artificial, es profundamente humana y defectuosa.

Cuando alguien te dice "La IA aprendio sola", lo que paso es que millones de personas trabajaron —muchas sin saberlo— para ensegnarle.

### 3.1 La basura que entra: el problema de las Redes Sociales como dieta

#### Que comen los modelos

Los LLMs modernos (GPT-4, Claude 3, Gemini) fueron entrenados con:
- **Common Crawl:** un archivo de **petabytes** de paginas web (basicInternet, todo lo que se pueda scrapear).
- **Reddit:** decenas de millones de hilos con comentarios.帖
- **Twitter/X:** cientos de millones de tweets.
- **Wikipedia:** millones de articulos (lo mas limpio y confiable).
- **Libros publicados** (muchos sin permiso de los autores — lo veremos en la seccion 6).
- **GitHub:** codigo fuente publico (millones de repositorios).

**El problema:** No todos estos datos son de la misma calidad.

**Analogia:** Pensá en el entrenamiento como la dieta de un nino. Si le das frutas y verduras, crece sano. Si lo alimentas solo con gaseosa y papas fritas, crece pero mal. Los modelos de IA comieron de todo: hay wikipedia (las verduras), libros (las proteinas) pero tambien hay **Twitter, Reddit y Facebook** — la **basura**.

#### Que hay en la basura

- **Desinformacion:** teorias de conspiracion, noticias falsas, propaganda politica.
- **Odio:** racism, sexism, homophobia, xenophobia. Twitter y Reddit estan llenos de esto.
- **Sesgos culturales:** si la mayoria de lo que se escribe en internet en ingles proviene de EE.UU., el modelo piensa que los valores de EE.UU. son los universales.
- **Errores factuales:** Wikipedia es buena pero no perfecta. Reddit tiene mucha informacion buena y muchisima falsa. Twitter es un caos.
- **Opiniones presentadas como hechos:** en redes sociales las personas dicen "X es malo" como si fuera una ley de la naturaleza.

**Caso comprobado: Microsoft Tay (2016)**

Microsoft lanzo un chatbot llamado **Tay** en Twitter. Tay debia "aprender" conversando con la gente. En **menos de 24 horas**, los usuarios de Twitter lograron que Tay empezara a decir cosas como *"Hitler tenia razon"* y *"Odio a los feministas."*

Microsoft tuvo que cerrar a Tay en menos de un dia. Tay **no era racista**: Tay es un reflejo de lo que la gente le enseno, que es lo que su alimentacion de twitter.

> **Leccion:** La IA es un **espejo** de sus datos de entrenamiento. Si entrenas con basura, obtienes una IA basura. No hay algoritmo que arregle datos malos.

**Caso comprobado: GPT-4 y los sesgos de genero (2023)**

Un estudio de estudios de OpenAI y terceros mostraron que GPT-3 (predecessor de GPT-4) tenia sesgos claros: asociaba "doctor" con "hombre" y "enfermera" con "mujer". O "programador" con "hombre" y "maestra" con "mujer". OpenAI tuvo que aplicar **filtrado** durante el entrenamiento para reducir esto. No lo eliminaron completamente — reducirlo es muy dificil.

### 3.2 La mano humana invisible: RLHF

#### Que es

**RLHF** significa **Reinforcement Learning from Human Feedback** (Aprendizaje por Refuerzo a partir de Retroalimentacion Humana). Es el paso mas importante del proceso que convirtio a los modelos de "predictores de texto crudo" a "asistentes utiles".

**Sin RLHF, ChatGPT no seria util.** Un modelo entrenado solo con texto de internet responde como internet: caotico, contradictorio, a veces util, a veces toxico.

#### Como funciona

1. **Pre-entrenamiento:** el modelo lee todo internet y aprende a predecir la siguiente palabra. Resultado: un modelo que responde como promedio de internet. Y "el promedio de internet" es terrible.
2. **RLHF (el Paso 2):** Se generan respuestas y se las muestran a humanas. Cada persona lee dos respuestas del modelo y decide: "esta es mejor, esta es peor".
3. Se entrena un **modelo de recompensa** (otras IA) que aprende a puntuar respuestas segun lo que los humanos prefieren.
4. El modelo principal se ajusta para que genere respuestas que maximicen la recompensa.

**Analogia:** Como entrenar a un perro. El perro hace algo (predice texto). Tu le dices "bien!" (premias) o "no!" (corriges). Con muchas repeticiones, el perro aprende a hacer las cosas que te gustan. El modelo aprende a decir lo que los humanos calificadores consideran bueno.

**Que "bueno" significa:** Aqui hay un sesgo enorme. Quien califica decide que es "bueno". Si los calificadores son todos de la costa oeste de EE.UU., la IA aprende que los valores de la costa oeste de EE.UU. son los buenos (tema de la seccion 4).

#### Por que sin humanos, el modelo colapsa

Un modelo sin RLHF no filtrado:
- Aceptaria preguntas sobre como hacer bombas (porque hay tutoriales en internet).
- Daria respuestas racistas si se le pide (porque hay texto racista en internet).
- Seria inutil como producto comercial (nadie quiere un asistente que no filtre nada).

El RLHF es lo que hace que ChatGPT diga *"Lo siento, no puedo ayudar con eso"* cuando le pides algo peligroso. **No se niega porque sea etico.** Se niega porque un humano le dijo a otra IA "califica esto como malo", y la IA aprendio a evitarlo.

### 3.3 El costo humano oculto: Los trabajadores del dato

#### Quienes hacen el RLHF

OpenAI, Google, Anthropic no contratan millones de personas en sus oficinas para calificar respuestas. **Subcontratan.** Y las empresas subcontratistas van al **Sur Global**: Kenia, Uganda, Filipinas, India.

#### Los numeros reales (verificados)

- **OpenAI subcontrato a Sama** (empresa con sede en Kenia) entre 2021 y 2022 para etiquetar contenido de texto y filtering. Los trabajadores ganaban **entre $2 y $4 USD por hora**. (Fuente: Time Magazine, investigacion publicada en enero de 2023.)
- Sama tenia contratos con OpenAI donde los trabajadores debian leer y etiquetar contenido **extremadamente toxico**: descripciones de violencia, odio, abuso infantil, gore. El objetivo era entrenar los filtros del modelo para que ChatGPT no generara ese tipo de contenido.
- **El dano psicologico estaba documentado:** un estudio posterior mostro que trabajadores de Sama reportaron **TEPT (transtorno de estres postraumatico)** y consecuencias mentales graves. Sama dice que ofrecia apoyo psicologico, ex trabajadores dicen que era insuficiente.
- En 2022, **OpenAI cancelo el contrato con Sama** despues del escandalo publico. Google y Meta han tenido contratos similares expuestos.

- **Meta subcontrato a Sama** para etiquetar contenido de Facebook (mensajes de odio, violencia, gore). Trabajadores en Kenia ganaban menos de **$2 USD/hora**. Un reporte de The Guardian (2023) mostro las condiciones.
- En **Filipinas**, hay ciudades enteras (ej. CEbu) que dependen del "data labeling". Los trabajadores etiquetan imagenes, texto, video para IA. Pagos: $1-3 USD/hora, sin beneficios sociales.

#### La paradoja

La IA que vos usas "gratis" y que te sorprende por lo educada que es, **es educada porque someone en Kenia leyo lo peor de internet por $2/hora para que vos no tuvieras que verlo.**

> **Leccion:** La IA no es "artificial". Es profundamente humana. Es humana en los datos que produciste gratis (tus tweets, tus reddits), es humana en la curacion (hecha por personas en el Sur Global por centavos), y es humana en los sesgos. Ladata lo que das y la que pagas — sete consciente de ello.

### El Ing. de IA en esta seccion

1. **La IA no es "inteligencia artificial".** Es trabajo humano masivo, invisible y muchas veces explotado.
2. **No confies en la "neutralidad" del modelo.** El modelo tiene los sesgos de sus datos y los de los humanos que lo calificaron.
3. **El RLHF es un filtro, no una solucion.** Reduce los sesgos extremos pero los sutiles los mantiene o introduce nuevos.
4. **El costo de un LLM no es solo la factura electrica.** Es tambien el costo humano de las personas que lo curaron, eligiendo que es "bueno" y que es "malo".

---

## 4. Sesgos Regionales y Geopolitica de la IA

> No existe una IA universal, existen IA con pasaporte.

### 4.1 El sesgo cultural inevitable

**Caso 1: El sesgo de Silicon Valley**

La mayoria de los LLMs modernos (GPT, Claude, Gemini) fueron desarrolados en la **costa oeste de EE.UU.**, con datos predominantemente en **ingles**, y calificados por humanos (RLHF) en su mayoria de **EE.UU.**

Si preguntas a ChatGPT si "esta bien" divorciarse, te dara la respuesta estadisticamente mas comun en el promedio de internet en ingles. Si preguntas sobre "union libre" versus "matrimonio", te dara la vision anglo. Si preguntas sobre el "rol de los abuelos en la crianza", la respuesta sera culturalmente diferente segun la cultura de que hablo.

**Caso comprobado (estudio real):**

Un estudio publicado en 2023 por investigadores de la Universidad de Stanford mostro que ChatGPT daba respuestas **significativamente distintas** sobre temas eticos segun el idioma en que se le preguntaba. En ingles, tendia a respuestas mas liberales (estadounidense). En otros idiomas, sus respuestas eran mas variadas pero siempre con menos "confianza" — el ingles era el idioma dominante en la personalidad del modelo.

**Caso 2: El "American Default"**

Si preguntas a ChatGPT "cual es la capitale de un pais?", por defecto puede mencionar estadisticamente paises con mas referencias en internet en ingles. "Capital" is obvious, pero en topics de cultura, leyes, historia, politica, la respuesta estara sesgada.valor

**Ejemplo concreto:** Si le preguntas a ChatGPT "que es un 'asado'?", te dira que es una parrilla argentina o uruguaya (correcto, y lo sabe). Pero si le preguntas por la **forma correcta de servir el mate**, dara una respuesta que mezcla versiones de varios paises. Si le preguntas sobre "los valores de la familia latinoamericana", dara una respuesta turista: "familia es muy importante en America Latina." El detalle fino no esta ahi.

### 4.2 IA Americana vs. Europea vs. Asiatica

Los tres grandes bloques:

```
┌─────────────────┬──────────────────┬────────────────┐
│     EE.UU.      │     EUROPA       │    CHINA       │
├─────────────────┼──────────────────┼────────────────┤
│ GPT (OpenAI)    │ Mistral (Francia)│ Qwen (Alibaba)│
│ Claude (Anthropic│ Llama (EUA)      │ Ernie (Baidu) │
│ Gemini (Google) │                  │ DeepSeek (?    │
└─────────────────┴──────────────────┴────────────────┘
```

#### EE.UU.: Libertad extrema + capitalismo + velocidad

- **Filosofia:** "Move fast and break things" (moverse rapido y romper cosas). Launch, iterate, fix later.
- **Regulacion:** Minima. La IA se autorregula (hasta ahora). El gobierno interviene solo cuando hay dano.
- **Datos:** Pocos limites sobre que datos se pueden usar para entrenamiento. Leyes de copyright debiles para training.
- **Valores incrustados:** Libre mercado, libertad de expresion extrema, individualismo. La IA prefiere la libertad individual sobre la seguridad colectiva en sus respuestas.

#### Europa: Regulacion estricta + proteccion + lentitud

- **Filosofia:** La IA debe ser segura y transparente antes de ser rapida.
- **Regulacion:**
  - **GDPR (2018):** proteccion de datos personales. Derecho al olvido (puedes exigir que tus datos se borren).
  - **AI Act (2024):** la primera ley integral de IA del mundo. Clasifica IA por riesgo:
    - Riesgo minimo: sin restricciones.
    - Riesgo limitado: transparencia obligatoria (ej: decir que es IA).
    - Riesgo alto: requisitos estrictos (logs, evaluacion, supervisio humana).
    - Riesgo inaceptable: prohibido (ej: puntuacion social, manipulacion subliminal).
- **Datos:** Hay que pedir consentimiento explicito para usar datos personales. Las empresas de IA tienen que cumplir o no operan en Europa.
- **Valores incrustados:** colectivismo, equidad, privacidad por diseno. La IA europea, si se desarrolla localmente, tendra sesgos hacia el Estado de bienestar europeo.
- **Problema: el desarrollo europeo es mas lento y caro.** Mistral (Francia) es el principal modelo europeo, pero tiene muchas menos recursos que OpenAI.

**Ejemplo comprobado de la AI Act:** En 2024, la AI Act obliga a los modelos de IA a **publicar sumarios de los datos de entrenamiento** (con suficiente detalle). OpenAI tuvo que acomodar sus terminos para operar en Europa. Esto benefit a todos los usuarios globales, no solo europeos.

#### China: Control estatal + censura + vigilancia

- **Filosofia:** La IA es infraestructura estrategica del Estado. El Estado controla que se desarrolla y como se usa.
- **Regulacion:** El Estado define que temas son sensibles (Taiwan, Tiananmen, Dalai Lama, etc.) y los modelos no pueden hablar de ellos o deben responder la linea oficial.
- **Datos:** El Estado tiene acceso a los datos de toda la poblacion (sistema de **creditoo social** parcial,Highlight digital). Datos personales casi sin proteccion privada frente al Estado.
- **Valores incrustados:** colectivismo (frente al Estado), estabilidad social, autoridad patriarcal. La IA china esta diseniada para acatar y reforzar los valores del Estado.
- **Como se ve:** Ernie (Baidu) no responde preguntas sobre Tiananmen. No dice "no puedo hablar de eso" — directamente responde que "los incidentes de 1989 fueron manejados correctamente por las autoridades." Es la censura integrada en el modelo.

**Caso comprobado de censura:** En 2024, DeepSeek (un modelo chino) mostro que bloqueaba consultas sobre el 4 de junio de 1989 (incidente de Tiananmen) directamente con un mensaje generico. Deepseek no explica por que, solo no responde.

### 4.3 El costo de regionalizar: Latinoamerica

**La pregunta obvia:** Por que no hacemos una IA argentina, mexicana, colombiana, brasilena?

**Respuesta:** porque el costo es altisimo.

- **Datos:** Tenemos menos datos en espanol (y menos aun en portugues) comparado con ingles. Nuestro internet es minoria.
- **Cómputo:** Entrenar un modelo cuesta **millones de USD** en GPUs. Ningun pais latinoamericano tiene el presupuesto.
- **Talento:** Tenemos talento (muchos ingenieros latinos trabajan en OpenAI y Google) pero no tenemos las empresas que los retengan.
- **Energia:** Entrenar un modelo requiere datacenters con acceso a muchisima energia y agua. Latinoamerica tiene potencial (energia hidroelectrica en algunos paises) pero no la infraestructura armada.

**Conclusion:** Latinoamerica no va a tener una IA soberana en el corto ni mediano plazo. Nuestra unica opcion realista es **usar los modelos de los tres grandes bloques y adaptarlos** — con prompts, con fine-tuning local, con datos propios — **y saber que esto nos hace dependientes de la infraestructura y las leyes de otros.**

> **Leccion de ingenieria:** El Ing. de IA latinoamericano trabaja con modelos "akenos" (hechos en EE.UU. o Europa) pero **los adapta al contexto local**. Sabe que el modelo tiene sesgo estadounidense y lo compensa con prompting cuidadoso, datos locales y revision humana local.

### El Ing. de IA en esta seccion

1. **No existe IA neutra.** Cada modelo refleja los valores de quien lo hizo.
2. **Elegir un modelo es elegir un set de sesgos.** Usar GPT es elegir sesgo estadounidense. Usar Qwen es elegir sesgo chino/estatal.
3. **En Latinoamerica, la soberania IA es una aspiracion, no una realidad.** Nuestro rol es adaptar, compensar y supervisar.

---

## 5. El Impacto Fisico y Economico: La Burbuja

> Lo que la IA cuesta al planeta y a tu bolsillo.

### 5.1 El monstruo del consumo: energia y agua

#### Cuanto consume entrenar un LLM

Los numeros siguientes estan **verificados** y provienen de papers publicados:

- **GPT-3 (2020):** Entrenamiento consumio estimadamente **1,287 MWh** (megavatios-hora) de energia electrica. Para tener escala: eso es el consumo electrico de **~120 hogares estadounidenses promedio durante un año**. Y genero **552 toneladas de CO2** — equivalente a **120 vuelos de ida y vuelta entre Nueva York y Beijing**. (Fuente: Patterson et al., 2024; Luccioni et al., 2023.)
- **GPT-4 (2023):** Estimaciones de expertos sugieren que consumio mas de **50 veces** lo de GPT-3 (no hay datos oficiales de OpenAI). Es decir, el orden de decenas de miles de MWh.
- **LLaMA-2 (Meta, 2023):** Emma Strubell et al. (2023) estimaron el costo de entrenar modelos grandes: hasta **~500 toneladas de CO2** por modelo, dependiendo del tamano.

**Analogia:** Entrenar un LLM es como hacer el consumo electrico de un **pueblo pequeno durante meses**.

#### Y no es solo entrenamiento: tambien inferencia

Cada vez que vos o cualquier persona en el mundo le pregunta algo a ChatGPT, **se gasta energia**: hay que pasar millones de parametros por la red neuronal para generar cada palabra.

- **Estimacion (Aleksandra Alekhova, 2024):** una sola consulta a ChatGPT consume **~0.002 kWh** (unos **2 Wh**). Suena poco. Pero si haces **100 millones de consultas al dia** (que es el ballpark de ChatGPT), son **200 megavatios-hora por dia**, equivalente al consumo de **~20,000 hogares**.
- Compara con una busqueda de Google: ~0.0003 kWh por busqueda. Una consulta a ChatGPT consume **~7 veces mas** que una busqueda en Google.

#### El agua potable que se evapora

Los datacenters generan calor masivo. Para enfriarlos, usan sistemas que **evaporan millones de litros de agua dulce**.

- **Estudio de Shaolei Ren (UC Riverside, 2023):** entrenar a GPT-3 consumio **~700,000 litros de agua dulce** (agua potable, no agua salada) para refrigeracion. Esto equivale al consumo de agua de **~370 personas en un año** (consuming 500 litros/persona/ano).
- Each **~10-50 consultas** a ChatGPT consumen **1 litro de agua** en el datacenter (dependiendo de la estacion y region). (Fuente: Ren et al., 2023.)
- **Microsoft (que hospeda a OpenAI):** reporto que su consumo de agua aumento **34% entre 2021 y 2022** (de 4.8 millones a 6.4 millones de metros cubicos), coincidiendo con el boom de ChatGPT. Reporte corporativo de Microsoft, publico.
- **Google:** reporto aumento de **22%** en consumo de agua en el mismo periodo. Reporte ambiental publico.

**Donde esta el problema:** Los datacenters a menudo se construyen en regiones **con escasez de agua**: Arizona, Utah (EE.UU.); Arabia Saudita, Singapur. China esta construyendo datacenters masivos en regiones con estres hidrico. El agua que se usa para enfriar los servidores de IA **no se usa para beber, ni para agricultura, ni para la naturaleza**.

#### El monstruo sigue creciendo

- **Los datacenters de IA ya consumen ~2% del consumo electrico mundial** (estimacion 2024, IEA — International Energy Agency). Se proyecta que lleguen al **3-4% para 2026**.
- Para comparar: **toda la aviacion mundial** consume ~2.5% de la energia mundial. La IA esta acercandose a eso.

### 5.2 La escasez artificial: GPUs, Nvidia y la cadena de suministro

#### Como la IA disparo los precios de las GPUs

- **GPUs** (Graphics Processing Units) son tarjetas electronicas originalmente disenadas para videojuegos. Resultaron perfectas para entrenar IA.
- **Nvidia** es la empresa dominante: tiene ~**80-90% del mercado** de GPUs para IA.
- **Nvidia H100** (el chip estrella para IA, lanzado en 2023): costaba ~**$30,000-40,000 USD** por unidad. Se vendia a empresas como Meta que compraba **350,000 unidades** en un solo pedido (2024).
- El valor de Nvidia en bolsa paso de **~$400 mil millones (2022)** a **~$3 billones (2024)**, haciendola una de las empresas mas valiosas del mundo.

#### El dano collateral

- **Gamers:** los precios de las GPUs de gama alta (RTX 4090, etc.) aumentaron. Muchos gamers no consiguen tarjetas porque las compra la industria de IA.
- **Diseniadores, artistas 3D, investigadores academicos:** GPUs persistentemente agotadas o caras. Star-up de IA compra lotes enteros en pre-venta.
- **Contenido en lag:** en 2023, Nvidia estaba tan enfocada en chips de IA que la produccion de GPUs consumer, (dejada a empresas secundarias) no podia alcanzar la demanda.
- **Industria automotriz:** algunos autos modernos (Tesla) usan GPUs/Nvidia hardware para driving assist, y la escasez los pega.
- **Demanda de semiconductores:** Taiwan Semiconductor Manufacturing Company (TSMC, que fabrica los chips de Nvidia) no da abasto. Todo lo que usa semiconductores avanzados se encarece: no solo GPUs sino celulares, autos, routers.

> **Leccion:** La IA no es un efecto virtual. Hay plastico, silicio, cobre, litio (en baterias de datacenter UPS), y millones de litros de agua detras de cada respuesta de ChatGPT. El Ing. de IA tiene que saber que cada query cuesta recursos reales.

### 5.3 Estamos en una burbuja?

#### Los numeros que preocupan

**1. Inversion vs. retorno:**

- En 2023-2024, el capital de riesgo (VC) invirtio **mas de $50 mil millones USD** en startups de IA. (Fuente: CB Insights, informe 2024.)
- OpenAI alone tiene un valuation de **$86-157 mil millones USD** (segun ronda, 2024). Hasta 2024, OpenAI **perdia dinero cada mes**: el costo de inferencia (servir a los usuarios) superaba los ingresos por suscripcion. En 2024, con un acuerdo de $19 mil millones con Microsoft, presuntamente se acercaron a punto de equilibrio, pero todavia muchos analistas lo discuten (Sequoia Capital, 2024).
- **Sequoia Capital** (uno de los VCs mas importantes del mundo) publico un analisis en 2024: la industria de IA **necesita ganar $600 mil millones USD anuales** para justificar las inversiones en datacenters y chips. En 2024, los ingresos totales de toda la industria de IA generativa eran **~$3-5 mil millones**. Es decir, hay un hueco gigantesco entre lo invertido y lo ganado.

**2. Costo de inferencia vs. suscripcion:**

- Cada usuario activo de ChatGPT Plus ($20 USD/mes) hace un cost que OpenAI estima entre **$5-15 USD solo en computo** (GPU + energia + infra), segun analisis de Bernstein y Morgan Stanley (2024). Esto significa que un usuario que usa intensivamente ChatGPT Plus **le genera perdidas a OpenAI**.
- El plan gratuito **siempre genera perdidas**. Sigue existiendo porque genera data (entrenamiento futuro), y para captar usuarios que despues convertiran a de pago.

**3. Startups que no ganan:**

- Muchas startups de IA que levantaron decenas de millones han mostrado ser **"envolturas alrededor de OpenAI"**: un chatbot para X industria, un asistente para Y, que en el fondo solo le pasan prompts a GPT-4 y le agregan una interfaz. Estas startups no son sostenibles: cuando OpenAI mejora su propio producto (ej: GPTs store), duplican la funcion que la startup ofreccia, y la startup pierde razon de existir.
- **Perplexity AI** (2024): valuation de $9 mil millones USD, ingresos estimados de $20-80 millones USD. La valuation es mas de 100x los ingresos. Comparacion: Apple vale ~5x sus ingresos.

#### El analisis: que pasa si estalla?

Si la burbuja IA revienta (puede que no, pero hablemos del escenario):
- Las startups que no ganan dinero quiebran. Sus empleados se quedan sin trabajo.
- Los datacenters sobreconstruidos quedan sub-utilizados. Toda la inversion en GPUs se hunde (muchos se venderian a precios rematados).
- Los modelos existentes seguiran funcionando (no se borran), pero los avances se ralentizaran.
- Los usuarios que dependian de servicios IA baratos pagan mas (o dejan de tenerlos).

**Compare conlo que paso en 2000 (burbuja dotcom):** muchas .coms quebraron. Pero internet no morio. Los sobrevivientes (Google, Amazon) se volvieron dominantes. Con la IA seria similar: si estalla, muchos proyectos mueren, los grandes absorben el mercado, y IA sigue existiendo pero centralizada en pocas manos.

> **Leccion de ingenieria:** El Ing. de IA debe construir sistemas que **no dependan exclusivamente de un proveedor de IA que podria subir precios 10x manana**. Si la burbuja estalla, el costo de APIs puede duplicarse o triplicarse, y debes estar preparado para migrar a modelos locales o alternativos.

### El Ing. de IA en esta seccion

1. **Cada query cuesta recursos reales:** energia, agua, chips. No es gratis usar la IA.
2. **La economia IA puede ser burbuja**: preparate para escenarios de precios altos y disponibilidad baja.
3. **Nvidia tiene quase-monopolio en chips:** riesgosisimo. Diversificar proveedores y considerar modelos mas chicos/locales.

---

## 6. Las Minas Legales: Derechos de Autor y Propiedad Intelectual

> De quien es lo que hace la IA?

### 6.1 El robo legalizado: como se entrenaron los modelos

#### Que pasp

Para entrenar modelos como GPT-4, Claude, Gemini, Midjourney, las empresas usaron **trillones de textos e imagenes** — sin pedir permiso y sin pagar a los autores originales.

**Como lo justifican legalmente:**
- Argumentan que es **"fair use"** (uso legittimo): usan el contenido no para reproducirlo, sino para aprender **patrones estadisticos** de el.
- **Example:** si el modelo ve 10.000 articulos del New York Times, no memorizeu Ninguno, pero "aprende" el estilo periodisitco. Y cuando vos preguntas "escribime un articulo en el estilo de como lo hari el NYT", puede imitar ese estilo.
- Este argumento es **disputado** por los autores originales, y hay decenas de demandas en curso.

#### Que datos, de donde

| Tipo de contenido | De donde lo scrapearon | Permiso? |
|-------------------|------------------------|----------|
| Libros | LibGen, Bibliotik (shadows libraries), Common Crawl | **No.** Los libros estan protegidos por copyright. |
| Articulos periodisticos | NYT, The Guardian, BBC, etc. (scrapeados de Common Crawl o directos) | **No.** |
| Arte / Imagenes | DeviantArt, ArtStation, Pinterest, billions | **No.** |
| Codigo fuente | GitHub public repositories (billones de lineas) | **Depende** (GitHub tiene licencias open source, pero no todos los repos). |
| Wikipedia | Directo (via API legitimately) | **Si, Wikipedia es libre.** |
| Reddit, Twitter | APIs y scrapers | **Disputado.** Reddit ahora cobra por su API. |

### 6.2 Casos de guerra legal reales

#### Caso 1: The New York Times vs. OpenAI y Microsoft (diciembre 2023)

**El demandante:** The New York Times (uno de los periodicos mas importantes del mundo).

**La demanda:** NYT acuso a OpenAI y Microsoft de **usar millones de articulos del NYT sin permiso** para entrenar ChatGPT. Y no solo eso: NYT mostro que ChatGPT podía producir **resumenes casi iguales a articulos del NYT**, y en algunos casos **textos casi enteros reproduciendo articulos del periodico**.

**Evidencia clave:** En la demanda, NYT incluyo examples donde ChatGPT producian **pasajes casi verbatim** de articulos del NYT — lo que desmintia OpenAI "no reploduce el contenido, solo aprende patrones".

**Estado (a 2024):** La demanda sigue en curso. OpenAI argumenta fair use. Si NYT gana, las empresas de IA tendrian que pagar compensaciones enormes y posiblemente licenciar contenido — cambiando la economia de la IA.

#### Caso 2: Artistas vs. Midjourney / Stability AI / DeviantArt (2023)

**Demandantes:** Un grupo de artistas profesionales (incluyendo Sarah Andersen, Karla Ortiz, Matthew Hollenbeck).

**La demanda:** Acusaron a **Stability AI (creadora de Stable Diffusion), Midjourney y DeviantArt** de usar **miles de millones de imagenes de artistas** sin permiso para entrenar modelos de generacion de imagenes. Las artistas mostraron que sus **nombres** podian usarse como **prompts** para generar imagenes en su estilo: *"Make me an image in the style of Sarah Andersen"* generaba obras plausiblemente imitativas.

**Lo mas fuerte:** los artistas nunca fueron contactados, ni pagados, ni acreditados. Sus obras estaban en datasets publicos (LAION-5B, que tiene 5 billiones de imagenes scrapeadas).

**Estado (2024):** La corte permitio que parte de la demanda avance. Al callocelo Demandantes no ganaron todo, pero la corte reconocio que hay un caso legitimo de infringement.

#### Caso 3: Getty Images vs. Stability AI (2023)

**Demandante:** Getty Images, una de las mayores agencias de stock photos del mundo.

**La demanda:** Stability AI uso **millones de fotos con copyright de Getty** para entrenar Stable Diffusion. Getty mostro pruebas donde Stable Diffusion **generaba imagenes que todavia tenian el logo de Getty** (filigrana watermark) in the corner — prueba irrefutable de que el modelo habia memorizado contenido especifico de Getty.

**Por qué importa la marca de agua como prueba:**

Cuando Stable Diffusion generaba imágenes con el logo de Getty "fantasma" incrustado en la esquina inferior derecha, demostraba algo técnicamente devastador: el modelo **no había "aprendido el estilo" de las fotos**. Había **memorizado imágenes específicas de Getty**, incluyendo el watermark que aparece en cada foto licenciada de la agencia. Esto derrumbó el argumento central de Stability AI: que el entrenamiento era "fair use" porque el modelo aprendía patrones estadísticos, no copiaba imágenes.

**Analogía:** Es como si un alumno que afirma haber "aprendido a cocinar leyendo recetas" entregara platos con las etiquetas y logos del restaurante original pegadas. Ya no es inspiración ni aprendizaje: es copia directa con prueba material incrustada en el producto.

**Por qué esto importa para todo ingeniero de IA:**
Si un modelo de imágenes memorizó fotos de Getty al punto de reproducir el watermark, ¿qué memorizó un LLM de texto sobre tus documentos privados, tu código fuente, o tus datos empresariales? La misma lógica aplica: la línea entre "aprender patrones" y "memorizar instancias específicas" es difusa y la industria todavía la está midiendo.

**Estado (2024):** En EE.UU., la corte encontró que Stability AI probablemente infringió derechos de autor. En Reino Unido, el caso siguió en curso. Stability AI tuvo que pagar compensaciones parciales. El caso Getty vs. Stability AI se convirtió en referencia legal: **la marca de agua como evidencia de memorización** es ahora un estándar en litigios de copyright de modelos de IA.

#### Caso 4: Programadores vs. GitHub Copilot (2022)

**Demandantes:** Un grupo de programadores open source (representados por Matthew Butterick y el estudio legal Clarkson).

**La demanda:** GitHub Copilot (herramienta de IA para programar, de Microsoft/GitHub) fue entrenado con **code de los repos publicos de GitHub**. Esto incluye codigo bajo licencias como MIT, GPL, Apache — que **requieren atribucion**. Copilot a veces producia codigo identico al original sin atribuir al autor.

**Estado (2023-2024):** El caso ha tenido altibajos. GitHub argumenta que es fair use. Algunas partes del caso fueron desestimadas, pero el corazone del caso sigue.

### 6.3 De quien es el output? El caos legal

#### La situacion actual

Si yo le pido a la IA que genere un logo para mi empresa, o que escriba un codigo fuente, **es mio?**

**Respuesta corta:** depends. La ley de derechos de autor, en la mayoria de paises, requiere que una obra tenga **"autor humano"** para ser protegida. Un output 100% generado por IA **no tiene autor humano** y, por lo tanto, **en general no puede ser registrado como copyright**.

**Caso clave: Thaler vs. Perlmutter (2023, EE.UU.)**

Stephen Thaler intento registrar como autor de una obra visual a su **sistema de IA** ("DABUS"). La corte denego el registro: *"el copyright humano requiere autor humano. La IA no puede ser autora."*

**Caso clave: "Zarya of the Dawn" (Kris Kashtanova, 2023)**

Kris Kashtanova registro como copyright una novela con ilustraciones hechas con Midjourney. La oficina de Copyright de EE.UU. reviso el caso y decidio:
- El **texto** escrito por Kashtanova: copyright valido (ella estructuro, edito, eligio).
- Las **imagenes** generadas 100% por Midjourney: **no copyright** (no hay autor humano).

**Conclusion practica:**

| Situacion | Puedes registrar copyright? |
|-----------|------------------------------|
| Texto 100% escrito por vos | **Si** |
| Texto 100% generado por IA | **No** (en regla general, en EE.UU. y paises similares) |
| Texto estructurado por vos, contenido parcial por IA | **Tal vez** (depende de cuanto es tuyo y cuanto es IA; area gris) |
| Imagen 100% generada por IA | **No** |
| Imagen que vos editaste significantemente despues de IA | **Tal vez** (la parte humana si es protegible) |

### 6.4 El riesgo en tu trabajo: quien va a la carcel?

**Scenario:** Tienes un cliente. Le haces un proyecto (web, diseno, codigo, copywriting). Usas IA para generar gran parte **sin decirle**. La IA produce algo que:
- Contiene un extracto verbatim de un libro con copyright.
- Imita el estilo de un artista que no autorizo uso.
- Genera codigo que contiene partes de un repo bajo GPL (que requiere que todo codigo derivado sea open source).

**Que pasa cuando el cliente se entera?**

1. **El cliente te demanda a vos**, no a OpenAI. Vos fuiste quien entrego el trabajo. Vos firmaste imploricitamente que era original.
2. **Vos podes ser liable civil y (en casos extremos) penalmente**. En EE.UU. y Europa, infringection de Copyright puede ser delito si es intencional y con fin de lucro.
3. **La empresa de IA te dice:** "Nuestros ToS dicen que el output es tuyo y vos respondes por el uso. No podemos garantizar que no haya plago." (Ej: terminos de OpenAI.)

> **Leccion de ingenieria:** Si usas IA para un trabajo para un cliente, debes:
> 1. **Avisar al cliente** que usaste IA (transparency).
> 2. **Verificar** que el output no reproduzca obras conocidas (busca extractos sospechosos en Google).
> 3. **Editar significantemente** lo que la IA produce — no aceptes como "original" algo 100% IA.
> 4. **Contrato:** tu contrato con el cliente debe mencionar que partes usaron IA y como.

### El Ing. de IA en esta seccion

1. **La mayoria de los modelos fueron entrenados con contenido protegido.** Tu uso de IA puede, en cualquier momento, heredar elementos con copyright de terceros.
2. **El output de IA no es tuyo automaticamente.** En muchos paises, no es protegible.
3. **El responsable legal sos vos, no la IA.** Si entregas output IA como original, el dano es tuyo.

---

## 7. Zonas de Peligro: Industrias donde la IA es un Riesgo Letal

> Donde la IA debe ser un asistente, NUNCA el protagonista.

### 7.1 Medicina: el problema de la alucinacion en diagnosticos

#### El riesgo

Los LLM alucinan (recorda de la Clase 1: siguen el "camino rojo" de probabilidad). En medicina, una alucinacion **puede matar**.

**Caso comprobado: GPT-4 y diagnosticos medicos (2023)**

Un estudio publicado en **JAMA** (Journal of the American Medical Association, 2023) evaluo a GPT-4 en diagnosticos clinicos. Resultados:
- **En casos comunes**, GPT-4 acerto una **porcentaje alta (diagnosticos correctos)**, comparable o superior a medicos generales.
- **En casos raros**, GPT-4 alucino diagnostico posibles, incluyendo casos de personas **inventadas** (sintomas que no son condicionados).
- GPT-4 plantecia diagnosticos con **la misma seguridad** tanto si acertaba como si estaba equivocado.

**Caso comprobado: Babylon Health (UK)**

Babylon Health, una startup britanica de IA medica, prometia **diagnostica automaticos** en 2020. Investigaciones de la BBC y doctors revelaron que la IA diagnostico incorrectamente en casos donde recomendaba **tratamientos peligrosos**, incluyendo sugerir que un paciente con sintomas de ataque cardiaco debia "descansar en casa". Babylon argumento que era para uso de support, no replace.

#### Quien es responsable

La ley es clara en casi todos los paises: **quien firma el diagnostico es el responsable.** Si un medico usa IA para generar un informe y firma "aprobado" sin verificar, y la IA estaba equivocada:

- **El medico pierde la licencia.** Firma un documento falso sin verificar.
- **El medico es demandado civilmente** por mala practica.
- **El medico puede tener responsabilidad penal** si hay dano grave o muerte.
- **La IA no responde legalmente.** No tiene matricula. No tiene seguro. No va a la carcel.

> **Leccion:** La IA puede **apoyar** al medico (ej: buscar literatura, sugerir diagnosticos diferenciales), pero el **medico es el que firma** y el **medico es el que responde**.

### 7.2 Abogados: el caso real de las citas inventadas

Esta es LA historia que todo abogado e ingeniero de IA deberia conocer.

#### El caso de Steven Schwartz (Mayo 2023, EE.UU.)

**Que paso:** Steven Schwartz, abogado de un bufete de EE.UU., uso ChatGPT para preparar un escrito juridico **para una demanda contra una aerolinea**. Le pidio a ChatGPT casos legales relevantes. ChatGPT le dio **varios casos** con nombres, fechas, y citas detalladas.

Schwartz presento el escrito en la corte del Distrito Sur de Nueva York.

**El problema:** **Los casos no existian.** ChatGPT los habia **inventado**. Los titulos sonaban plausibles, los nombres de tribunales eran reales, las descripciones parecian casos reales — pero **ninguno existia**. ChatGPT alucino todos.

**Como se descubrio:** Los abogados de la parte contraria (la aerolinea) buscaron los casos en bases de datos legales (LexisNexis, Westlaw). **No existian.** NI las citas, ni los titulos, ni los numeros de caso correspondian a nada real. Reportaron al juez.

**Consecuencias:**
1. El juez **P. Kevin Castel** sanciono a Schwartz y a su bufete (Levidow, Levidow & Oberman).
2. Schwartz tuvo que pagar una **multa de $5,000 USD**.
3. El bufete fue obligado a **notificar a todos sus clientes** del incidente.
4. Schwartz declaro que no sabia que ChatGPT podia inventar casos — **creyo que era un motor de busqueda**.

**Lo mas importante de este caso:** Schwartz **no malediosamente invento los casos.** Confio en la IA. Es el mismo problema que vimos en la seccion 1: la IA suena tan autoritaria, tan convincente, que cuando te da un caso falso con cita y fecha, te crees que es real.

> **Conexion con la Clase 1:** Recorda los arboles de probabilidad. Cuando ChatGPT inventa un caso legal, lo hace porque las combinaciones de **nombres de tribunales + nombres de abogados + estilos de citas** son muy probables juntas en sus datos de entrenamiento. Elige palabras "probables" — y un caso inventado suenaProbable porque *sigue la estructura* de un caso real, aunque el caso especifico no exista.

#### Otros casos similares

- **Mata v. Avianca (2023):** El caso de Schwartz arriba. (Mata era el demandante; Avianca la aerolinea.)
- **Junta de Abogados de California (2024):** Al menos **dos casos mas** de abogados sancionados por presentar escritos con citas inventadas por IA, en los meses siguientes al caso Schwartz.
- **UK (2024):** Un abogado ingles fue suspendido por usar ChatGPT para escribir cartas legales que incluian citas no verificadas.

### 7.3 Ingenieria Civil y Arquitectura: por que no usar IA para calcular

#### El riesgo

Si usas IA para calcular estructuras (puentes, edificios, planos), el riesgo es que la IA alucine un numero — como un factor de seguridad, una carga maxima, o una dimension — perfectamente plausible, **pero equivocado**.

**No hay un caso public documentado de un desastre concreto por IA civil (gracias a eso), pero:**

- En 2023, ingenieros probaron a ChatGPT con problemas de **resistencia de materiales**. ChatGPT a veces acerto la formula general, **pero se equivocaba en detalles numericos**: factores de seguridad, constantes especificas de materiales. Un ingeniero civil que sabe revisar lo detecta. Un estudiante o no profesional que confie, no.
- Los model codes de ingenieria (como IBC, ACI 318, Eurocode 8) son **muy complejos**: dependen de localizaciones geo, tipo de gov, supuestos. ChatGPT mezcla codigos de paises distintos, aplicandolos donde no corresponden.

**Que pasa si confias y construyes?**

- **Falla la estructura.** Si un puente se derrumba o un edificio se cae, mueren personas.
- **El ingeniero civil es responsable civil y penalmente.** En casi todos los paises, el que firma los planos garantiza la seguridad de la obra.
- **La IA no responde.** OpenAI no tiene licencia de ingeniero. No puede ser demandada en tribunales de ingenieria.

**La regla de oro en ingenieria:** **La IA no puede reemplazar el juicio profesional (judgment) de un ingeniero licenciado.** La IA puede asistir (ej: buscar literatura, draftear documentos), pero **el sello y la firma del ingeniero son insustituibles**. Si firmas algo que la IA calculo **sin verificarlo vos mismo**, y eso falla, **vas a la carcel por homicidio culposo o dano por impericia**.

> **Analogia:** Usarias un GPS para pilotar un avion comercial? El GPS esta, asiste al piloto. Pero el piloto **verifica** y decide. Si el GPS esta mal y el piloto igual aterriza en el sitio equivocado, el piloto es responsable, no el GPS.

### El Ing. de IA en esta seccion

1. **Hay industrias donde la IA es un riesgo letal o catastrofico.** No usarla sin supervision humana experta.
2. **"La IA dijo" no es una defensa legal.** El responsable es quien usa el output.
3. **La alucinacion en contextos criticos puede ser igual de peligrosa que una alucinacion medica** — solo que en algunos casos se nota mas rapido (un abogado inventado) y en otros se nota cuando la presion causa dano (una estructura civil).

---

## 8. El Protocolo del Ingeniero: como usar la IA de forma segura

> La parte positiva: que hacer a partir de manana.

Saber los riesgos no significa dejar de usar IA. Significa **usarla con criterio**. Este es el protocolo que vamos a usar en todo el taller y que el Ing. de IA aplica en su trabajo diario.

### 8.1 Checklist pre-prompt: las 3 preguntas

Antes de pegar cualquier informacion en un LLM, **parate y hacete estas 3 preguntas**:

#### Pregunta 1: Que informacion estoy a punto de revelar?

- Es nombre real de mi empresa? Cambialo por "Empresa X".
- Son datos de clientes? Enmascara.
- Es codigo fuente privado? **No lo subas.** Usa uno generico de ejemplo.
- Es contrasena? **Jamais.** Que una contrasena vaya a un prompt es como decirselo a desconocidos.
- Es informacion personal (tuya, de tu familia, de un cliente)? **No la subas cruda.**

#### Pregunta 2: Si esto se publica manana en un periodico, estaria bien?

- Si la respuesta es NO, entonces no lo subas.
- Si la respuesta es "depende" (ej. no es grave pero es privado y preferiria que no), entonces **anonimiza antes** de subirlo (ver 8.2).
- Si la respuesta es SI (no es sensible), subi tranquilo.

#### Pregunta 3: De que plan de IA estoy usando?

- **Plan gratuito:** asume que tus datos se guardan y pueden usarse para entrenamiento. No subas nada sensible, **ni siquiera anonimizado si el patron es reconocible**.
- **Plan de pago / empresarial:** asume zero retention, pero confirma en los terminos. Para datos sensibles, **siempre de pago**.
- **Modelo local (luego veremos):** no hay riesgo de envio de datos a terceros. Es lo mas seguro para datos muy sensibles.

**Analogia:** El checklist pre-prompt es como el cinturon de seguridad del auto. No garantiza que no haya accidentes, pero reduce enormemente el dano si los hay. Y nunca cuesta mucho usarlo.

### 8.2 Anonimizacion de datos

La anonimizacion es la tecnica de **limpiar tus datos** antes de enviarlos a la IA. La IA puede trabajar con la estructura del problema sin ver los datos personales.

#### Tecnicas basicas (sin codigo)

**Tecnica 1: Sustitucion de nombres propios**

| Original | Anonimizado |
|----------|-------------|
| "Nuestra empresa, Acme Corp, tuvo ingresos de $5M en 2024" | "Nuestra empresa, [EMPRESA_X], tuvo ingresos de $5M en 2024" |
| "El cliente Juan Perez, DNI 12.345.678, compro un auto" | "El cliente [CLIENTE_A], [DNI_A], compro un auto" |
| "El proyecto Greenfield v2024.2 tiene un bug en el modulo auth.py" | "El proyecto [PROYECTO_X] tiene un bug en el modulo auth.py" (auth.py es un nombre generico, no sensible) |

**La regla:** Si un nombre es **especifico y unico** ( nombre de una empresa real o una persona real), cambialo. Si es un nombre comun generico (auth.py, login.js), probablemente no hace falta.

**Tecnica 2: Enmascaramiento de datos numericos sensibles**

| Original | Anonimizado |
|----------|-------------|
| "La cuenta bancaria 1234567890 de Banco Nacion" | "La cuenta bancaria [CUENTA_X] de [BANCO_X]" |
| "El IP de nuestro servidor es 192.168.1.42" | "El IP de nuestro servidor es [IP_X]" (aunque los IPs internos no son muy sensibles, los publicos si) |
| "Telefono +54 11 5555-5555" | "Telefono [TEL_X]" |

**Tecnica 3: Patrones y formatos**

A veces no podes quitar un numero pero puedes cambiarlo:
- "Nuestro codigo de producto es SKU-12345-AB" → "Nuestro codigo de producto es SKU-[XXXXX]-[XX]"
- "La base de datos tiene 1,452,389 registros" → "La base de datos tiene ~~1.5 millones~~ registros" (o simplemente "millones de registros")

**Tecnica 4: Quitar URLs y dominios**

- "Nuestra pagina es https://acme.com/login" → "Nuestra pagina es [URL_X]"

**Tecnica 5: Quitar metadatos de fotos**

Si subes una foto a Gemini/ChatGPT para que la analice:
- **Las fotos tienen EXIF**: fecha, GPS (donde se tomo), camara. Antes de subirla, **borra los EXIF** (en Windows: click derecho → Propiedades → Detalles → "Quitar propiedades e informacion personal"; en Mac y Linux hay tools similares).
- Ojo: incluso sin EXIF, la foto **misma** puede revelar informacion (el exterior de tu casa, placas de auto, objetos identificativos).

#### Cuanto anonimizar?

**La regla es simple:** anonimizas hasta que **si alguien intercepta este prompt**, **no pueda asociarlo con una persona o empresa real**.

- Mal anonimizar: "Juan Perez de la empresa Acme tuvo un problema..." → sigue identificable.
- Bien anonimizado: "[CLIENTE_A] de [EMPRESA_X] tuvo un problema..." → no identificable.

**El limite:** La IA trabaja mejor con **concreto**, no con **abstracto**. Si anonimizas demasiado (ej. queitar todos los numeros), la IA no tiene con que trabajar. Es un balance: **detalles suficientes para que la IA entienda, especifidad suficiente para que no revele**.

### 8.3 La regla del "Humano en el medio" (Human-in-the-Loop)

#### Que es

**HITL** = Human-in-the-Loop = "Humano en el medio". Es el principio de que **la IA hace el trabajo pesado, el humano hace la revision critica y la firma final.**

**Analogia:** El **piloto automatico** de un avion commercial moderno puede despegar, volar y aterrizar solo. **Pero el piloto humano esta sentado ahi, supervisando** cada accion, listo para tomar el control si algo falla. Asi debe ser con la IA.

#### La regla 80/20/100

- **80% del trabajo pesado:** lo hace la IA. Ej: redactar un documento, generar opciones, buscar literatura, estructurar codigo.
- **20% del thinking critic elements:** lo hace el humano. Analizar si lo que la IA dijo es correcto. Comparar con fuentes. Verificar datos. Considerar contexto que la IA no tiene.
- **100% de la responsabilidad final:** es del humano. El que firma, el que aprueba, el que entrega.

#### Donde SI aplicar HITL

- Cuando el output sera **entregado a un cliente o produccion**.
- Cuando hay **datos sensibles** involucrados.
- Cuando el output **afecta a personas** (decisiones, diagnosticos, recomendaciones).
- Cuando hay **riesgo legal o de seguridad**.

#### Donde NO es necesario HITL estricto

- Ejercicios de aprendizaje (como nuestros notebooks del taller).
- Prototipos y drafts que despues seran refinados.
- Brainstorming inicial donde lo que dice la IA es semilla para tu pensamiento, no producto final.

#### Como aplicarlo en la practica

**Mental checklist post-prompt:**

1. **Lei la respuesta completa** (no solo el resumen)?
2. **Datos numericos:** verificaste al menos los critico (precios, cantidades, fechas)?
3. **Citas y referencias:** verificaste que existan? (Googlea los autores/nombres.)
4. **Codigo:** ejecutaste el codigo que la IA te dio? Muchas veces alucina APIs que no existen o usa librerias que no son compatibles.
5. **Decision**: Si firmaste esta respuesta y estaba mal, **sabras por que esta mal**? Si no podes justificarlo, no lo firmes.

### El Ing. de IA en esta seccion

1. **La lista de control pre-prompt** es tu cinturon de seguridad. usalo SIEMPRE.
2. **Anonimiza antes de subir.** No despues, no "ya vere despues". ANTES.
3. **HITL no es opcional** en trabajo profesional. Marca la diferencia entre un ingeniero y un usuario que copia-pega.
4. **La IA no va a la carcel ni a la corte. Vos si.** Tu firma es tu palabra.

---

## 9. Smarkdown: La Técnica del Prompt Estructurado

> Una herramienta gratuita que mejora tus resultados y tu seguridad al mismo tiempo.

### ¿Qué es Smarkdown?

**Smarkdown** = **S**tructured **Mark**down para prompts. Es una técnica de escritura de prompts que usa la sintaxis **Markdown** (los títulos `##`, las listas `-`, el texto en **negrita**, los bloques de código) para organizar lo que le pedís a la IA antes de enviarlo.

**Por qué funciona a tres niveles:**
1. **Para vos:** te obliga a pensar ANTES de escribir. Separar *contexto*, *tarea* y *restricciones* hace que apliques el checklist pre-prompt de la sección 8 de forma natural, sin tener que acordarte de él.
2. **Para la IA:** los LLMs son máquinas de procesar texto estructurado. Un prompt con estructura clara genera respuestas más precisas, porque el modelo tiene separados el "quién soy", "qué necesito" y "bajo qué condiciones".
3. **Para la seguridad:** cuando completás la plantilla bloque por bloque, es mucho más fácil detectar si estás a punto de incluir datos sensibles. La estructura actúa como **fricción positiva**: una pausa que te hace pensar.

### La plantilla Smarkdown

```markdown
## Rol
[Qué rol querés que asuma la IA: "Eres un experto en X"]

## Contexto
[Situación general. SIN nombres reales, SIN datos sensibles.
 Usá tu AlterEgo (sección 10) aquí.]

## Tarea
[Qué querés que haga. Específico y claro. Un verbo concreto.]

## Restricciones
- [Qué NO debe hacer]
- [Formato deseado: lista, párrafo, tabla, código...]
- [Longitud máxima si aplica]
- [Tono: formal, informal, técnico, simple para niños...]

## Ejemplo de output esperado (opcional)
[Muestra de cómo querés la respuesta. Muy útil para formatos específicos.]
```

**No es obligatorio usar todos los bloques.** Para preguntas simples, con `## Tarea` + `## Restricciones` alcanza. Para trabajo profesional, usá todos.

### Comparación real: prompt sin estructura vs. Smarkdown

**Escenario:** Sos docente y necesitás un quiz de 5 preguntas sobre fracciones para alumnos de 10 años.

---

**Prompt sin estructura (típico):**
> *"Haceme preguntas de fracciones para chicos de primaria"*

**Resultado típico:** La IA genera algo genérico. A veces demasiado fácil, a veces demasiado difícil. En un formato que tal vez no querés. Sin saber si son de opción múltiple, de completar o de desarrollo. Sin saber qué ya saben los chicos. Sin respuestas incluidas.

---

**Prompt con Smarkdown:**

```markdown
## Rol
Eres un docente de primaria con experiencia en didáctica de matemáticas.

## Contexto
Tengo alumnos de 10 años que ya saben sumar y restar fracciones con el mismo
denominador. Todavía NO vieron fracciones con distinto denominador.

## Tarea
Creá un quiz de evaluación con exactamente 5 preguntas sobre fracciones simples.

## Restricciones
- Tipo: opción múltiple (4 opciones por pregunta, solo una correcta)
- Dificultad: progresiva (la pregunta 1 más fácil, la 5 más difícil)
- Tono: lenguaje apropiado para niños de 10 años, sin jerga técnica
- Incluí la respuesta correcta entre corchetes [R: ] al final de cada pregunta
- NO incluyas fracciones con distinto denominador (todavía no lo vieron)
- NO uses calculadoras, solo operaciones mentales simples

## Ejemplo de output esperado
**Pregunta 1:** ¿Cuánto es 1/4 + 1/4?
a) 1/8  b) 2/8  c) 2/4  d) 1/2
[R: c) 2/4]
```

**Resultado:** La IA tiene todo el contexto necesario. Produce exactamente 5 preguntas de opción múltiple, progresivas, con lenguaje para niños, con las respuestas, sin fracciones de distinto denominador, con el formato exacto del ejemplo. No hace falta un segundo prompt para corregirlo.

---

**¿Cuánto tiempo ahorra?** El prompt Smarkdown lleva 2-3 minutos de escribir. Pero el resultado es tan preciso que no necesitás 3-4 rondas de corrección. En total, el proceso es más rápido.

### Smarkdown como herramienta de seguridad

Cuando completás el bloque `## Contexto`, te preguntás naturalmente: *¿qué información real necesita la IA para entender la situación?* Y en ese momento se activa el checklist pre-prompt de la sección 8.

**Ejemplo de cómo Smarkdown te protege:**

Sos contador y querés ayuda para analizar un estado financiero de un cliente.

| Sin Smarkdown | Con Smarkdown |
|---------------|---------------|
| "Mirá este estado financiero de mi cliente y decime si tiene problemas" → pegás el Excel con el nombre del cliente, CUIT, y todos los montos reales | Cuando llegás al bloque `## Contexto` y escribís "empresa mediana del sector manufacturero en Argentina", naturalmente ves que no necesitás poner el nombre real |
| Datos sensibles van al servidor de la IA | Solo va el contexto necesario, anonimizado |
| Violación potencial de confidencialidad | Seguro por diseño |

La plantilla actúa como una pequeña pausa obligatoria entre "tener el impulso de preguntar" y "enviar el dato". Esa pausa es donde se previenen los errores de seguridad.

### Guardá tus templates Smarkdown

Una vez que escribís un buen prompt para una tarea recurrente, guardalo en un archivo de texto tuyo (NO en la IA). La próxima vez que necesites la misma tarea, editás solo el `## Contexto` y la `## Tarea`, y el 80% del trabajo ya está hecho.

**Ejemplos de templates que vale la pena guardar:**
- "Email formal para solicitar pago" (rellená cliente y monto después)
- "Quiz de evaluación para [materia] y [nivel]"
- "Análisis de texto en [idioma] con puntos clave"
- "Explicación de [concepto técnico] para alguien sin experiencia"

### El Ing. de IA en esta sección

1. **Smarkdown no es solo estética.** Es seguridad práctica: la estructura fuerza la pausa donde se previenen los errores.
2. **La IA responde mejor a prompts estructurados.** Los LLMs procesan el texto de arriba hacia abajo; los marcadores Markdown les dan pistas de estructura semántica que mejoran la precisión del output.
3. **Guardá tus templates.** Un Ingeniero de IA reutiliza y refina sus prompts como un programador reutiliza y refina sus funciones. No empieces desde cero cada vez.

---

## 10. Tarea Práctica: El AlterEgo

> Practicá todo lo que vimos esta clase en una sola sesión real con la IA.

### ¿Qué es el AlterEgo?

El **AlterEgo** es una identidad profesional **anonimizada y ficticia** que representa tu rol o situación real, pero sin datos personales que te identifiquen.

No es una mentira ni un engaño. Es **privacidad por diseño**: le das a la IA el contexto que necesita para ayudarte, sin revelar quién sos realmente, para quién trabajás, ni qué empresa está involucrada.

**Ejemplos de AlterEgo:**

| Vos (real) | Tu AlterEgo |
|-----------|-------------|
| Juan García, contador de Empresa ABC S.A., Quito, Ecuador | "Profesional contable en una empresa mediana de servicios en América Latina" |
| María Rodríguez, estudiante de Medicina, año 3, UNAM, México | "Estudiante de tercer año de medicina en una universidad latinoamericana" |
| Carlos Pérez, freelancer, cliente en Lima que no pagó $3,000 USD | "Profesional independiente con un cliente en país de habla hispana con deuda pendiente de cuatro cifras" |
| Lucía Fernández, maestra de primaria, Colegio San Martín, 28 alumnos de 4.º grado | "Docente de primaria, grupo de 25-30 estudiantes de 10 años, escuela pública" |

**La clave:** Tu AlterEgo tiene suficiente contexto para que la IA te ayude bien, pero **no puede ser rastreado hasta vos** si el prompt se filtra, se intercepta, o se usa para entrenar el modelo.

**Conexión directa con la sección 2:** Recordás el viaje del dato (PC → Router → ISP → servidor de la IA)? Tu AlterEgo es tu escudo en ese viaje. Aunque alguien intercepte el paquete en cualquier punto del camino, lo que ve es el AlterEgo, no vos.

### La tarea paso a paso

#### Paso 1: Elegí un problema real

Pensá en algo de tu vida cotidiana (trabajo, estudio, proyecto personal) donde te sería útil la ayuda de la IA. Puede ser:
- Redactar algo: un email, un informe, una presentación, un CV
- Entender algo: un concepto, un proceso, una ley, una tecnología
- Planificar algo: un evento, un proyecto, una estrategia de estudio
- Resolver algo: un problema cotidiano, una decisión, una organización

**Ojo:** Si tu primera idea tiene datos sensibles (nombre de cliente, datos financieros, información personal de terceros), eso no es un obstáculo: **ese mismo escenario anonimizado es exactamente la tarea.** Es el ejercicio perfecto.

#### Paso 2: Creá tu AlterEgo

Completá esta ficha **en papel o en un archivo de texto tuyo — NO en la IA:**

```
Mi AlterEgo para esta tarea:
- Mi rol general: [ej: "profesional del área de salud"]
- Mi contexto: [ej: "trabajo en una clínica mediana en América Latina"]
- Lo que NO voy a mencionar: [ej: mi nombre, el nombre de la clínica,
                               la ciudad exacta, nombres de pacientes]
```

Este archivo es tuyo. No se lo mandás a nadie. Es para que vos tengas claro qué datos estás anonimizando antes de empezar.

#### Paso 3: Aplicá el checklist pre-prompt (sección 8.1)

Antes de escribir el prompt, repasá las 3 preguntas:
1. **¿Qué información voy a revelar?** → ¿Ya está anonimizada con el AlterEgo?
2. **Si esto se publica mañana en un periódico, ¿estaría bien?** → Con el AlterEgo, debería estar bien.
3. **¿Qué plan de IA estoy usando?** → Gratuito o de pago (afecta qué tan sensible puede ser la tarea).

#### Paso 4: Escribí el prompt con Smarkdown

Usá la plantilla Smarkdown de la sección 9, poniendo tu AlterEgo en el bloque `## Contexto`.

**Ejemplo completo integrado:**

*Situación real (la que no va al prompt):*
> "Soy Juan García, contador independiente. Mi cliente Empresa ABC no me pagó $3.200 USD por un trabajo entregado hace 60 días. Quiero enviarle un email."

*AlterEgo (lo que sí va al prompt):*
> "Soy profesional independiente del área financiero-contable en América Latina."

*Prompt Smarkdown completo:*

```markdown
## Rol
Eres un experto en comunicación profesional y resolución de situaciones
contractuales entre profesionales independientes y sus clientes.

## Contexto
Soy profesional independiente del área financiero-contable en América Latina.
Presté servicios a un cliente empresa. Han pasado 60 días desde la entrega
del trabajo y el pago acordado (un monto de cuatro cifras en USD) no se realizó.
La relación con el cliente es cordial pero necesito claridad sobre el pago.

## Tarea
Redactá un email formal para solicitar el pago pendiente.

## Restricciones
- Tono: profesional y cordial (es la primera solicitud, no amenazante)
- Longitud: máximo 200 palabras
- No incluyas el monto específico (lo completaré yo después con [MONTO])
- No incluyas nombres reales (usá [NOMBRE_CLIENTE] y [TU_NOMBRE])
- Incluí un plazo concreto de respuesta sugerido: 5 días hábiles
- Al final, un párrafo breve sobre próximos pasos si no hay respuesta
  (sin amenazas legales todavía)

## Ejemplo de formato de salida
Asunto: [línea de asunto sugerida]

Estimado/a [NOMBRE_CLIENTE]:
[cuerpo del email]

Quedo a disposición,
[TU_NOMBRE]
```

*Lo que hacés después de recibir la respuesta:*
- Abrís tu propio editor de texto (Word, Google Docs, Notepad)
- Reemplazás `[NOMBRE_CLIENTE]` con el nombre real del cliente
- Reemplazás `[MONTO]` con el monto real
- Reemplazás `[TU_NOMBRE]` con tu nombre real
- **Los datos sensibles nunca viajaron al servidor de la IA.** Solo viajan a tu documento local.

#### Paso 5: Aplicá Human-in-the-Loop (sección 8.3)

Cuando recibas la respuesta de la IA:

| Pregunta HITL | Qué revisás |
|---------------|-------------|
| ¿Leí la respuesta completa? | No solo el primer párrafo |
| ¿El tono es apropiado para mi situación real? | Lo que la IA escribe para un "AlterEgo genérico" puede necesitar ajuste para tu contexto específico |
| ¿La IA inventó datos? | Verificá que no haya puesto nombres, empresas o cifras inventadas que suenen reales |
| ¿Los placeholders están marcados? | [NOMBRE], [MONTO], etc. deben seguir como placeholders, no reemplazados por la IA |
| ¿Editaría algo? | La IA hace el 80%. El 20% que sos vos marca la diferencia entre un email genérico y uno tuyo. |

#### Paso 6: Reportá en la próxima clase

Traé a la próxima clase estas tres cosas (sin datos reales):

1. **El AlterEgo que creaste** (solo el rol y el contexto anonimizado, no datos reales).
2. **El prompt Smarkdown que escribiste** (con los placeholders, sin datos reales).
3. **Un párrafo de reflexión** respondiendo estas preguntas:
   - ¿Qué hizo bien la IA?
   - ¿Qué inventó, exageró o no entendió?
   - ¿Qué tuviste que editar vos con el HITL?
   - ¿Fue útil anonimizar con el AlterEgo o te resultó complicado?

**No es una evaluación de si "lo hiciste bien".** Es una discusión colectiva: todos van a traer experiencias distintas y juntos vamos a entender mejor cómo funciona la IA en situaciones reales.

### Por qué esta tarea importa

Toda la teoría de esta clase (ciberseguridad, antropomorfismo, HITL, anonimización, Smarkdown) se vuelve **real** en el momento en que abrís ChatGPT y escribís tu primer prompt con el AlterEgo.

**Analogía:** Podés leer todos los libros de natación del mundo. Pero aprendés a nadar el día que entrás al agua. Esta tarea es tu primera "entrada al agua" — con chaleco salvavidas (AlterEgo + Smarkdown + checklist) puesto.

La diferencia entre alguien que leyó estos apuntes y alguien que también hizo la tarea es la misma que entre alguien que leyó sobre el cinturón de seguridad y alguien que ya tiene el hábito de ponérselo antes de arrancar el auto.

### El Ing. de IA en esta tarea

1. **El AlterEgo no es opcional en trabajo profesional.** Es la diferencia entre un profesional responsable y alguien que regala datos de sus clientes sin saberlo.
2. **Smarkdown + AlterEgo + HITL** es el trípode básico. Con este trípode, podés usar cualquier LLM de forma segura y efectiva desde mañana.
3. **La práctica importa más que la teoría.** Un Ingeniero de IA no solo sabe los conceptos: los aplica en cada interacción, hasta que se convierten en hábito.

---

## 11. Cierre y puente a la Clase 3

### Resumen de la clase

Hoy vimos que:

1. **La IA no siente ni entiende.** Nuestro cerebro la antropomorfiza por una adaptacion evolutiva; pero es estadistica, no empatia (Efecto ELIZA, caso LaMDA).
2. **Tu dato hace un viaje completo** desde tu PC hasta un servidor lejano. En el camino, **varios actores** pueden verlo, y una vez que llega al servidor, **perdes el control** sobre el.
3. **El plan gratuito es entrenamiento gratis para la empresa.** Para datos sensibles, se usa plan empresarial (con contrato) o modelo local.
4. **La IA es profundamente humana:** datos de redes sociales, RLHF con trabajadores en el Sur Global, sesgos de los calificadores.
5. **No existe IA universal.** Hay IA estadounidense, europea y china, cada una con sesgos geopolíticos distintos.
6. **La IA tiene un costo físico:** energía, agua potable, GPUs. Y puede ser una burbuja económica.
7. **Los modelos fueron entrenados con contenido protegido** sin permiso; el caso Getty demostró que algunos memorizaron imágenes específicas (evidencia: el watermark). Hay decenas de demandas en curso.
8. **En medicina, derecho e ingeniería civil, la IA puede ser letal.** El responsable siempre es el humano que firma (caso Schwartz, Babylon Health).
9. **El protocolo del Ingeniero:** checklist pre-prompt + anonimización + Human-in-the-Loop.
10. **Smarkdown:** escribir prompts estructurados con Markdown mejora la calidad de las respuestas y actúa como fricción positiva de seguridad.
11. **El AlterEgo:** una identidad profesional anonimizada que te permite usar la IA con datos de contexto suficientes, sin exponer información sensible real.

### Próxima clase

**Clase 3: Vibe Coding — Programación Dirigida por Lenguaje Natural.**

Ahí sí vamos a escribir código. Pero ahora que sabés cuáles son los riesgos y cómo se protege la información, podrás usar IA para programar **de forma segura** — sabiendo qué pedirle, qué no pedirle, y cómo revisar lo que te da. Y ya tenés el trípode: AlterEgo + Smarkdown + HITL.

### Tarea

1. **Hacer la tarea del AlterEgo** (sección 10 de este documento). Es la tarea principal y la más importante.
2. **Leer:** las secciones 1, 2 y 9 de este documento son las más críticas. Releelas.
3. **Hacer la práctica guiada:** [`practica.md`](practica.md) — ejercicios de anonimización, checklist, y análisis de casos reales.
4. **Leer un recurso:** [`recursos.md`](recursos.md) — se recomienda el documental sobre trabajadores de datos en Kenia y el análisis del caso NYT vs. OpenAI.

---

> **Recordá:** no hay magia, hay números. Y detrás de los números, hay humanos, energía, agua y dinero.