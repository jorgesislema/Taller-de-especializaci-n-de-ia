# Practica — Clase 2: El Costo Real de la IA

> Esta clase no tiene codigo. La practica es **aplicada**: vas a anonimizar datos, analizar casos reales y construir tu propio protocolo de seguridad.

---

## Ejercicio 1: Anonimizacion de prompts (15 min)

A continuacion tenes **5 prompts** que alguien querria enviar a un LLM. Cada uno tiene **informacion sensible** que no deberia subirse cruda.

**Tu tarea:** Reescribe cada prompt anonimizando los datos sensibles. Usa las tecnicas de la seccion 8.2 de los apuntes.

### Prompt 1

> "Nuestra empresa, Tecnologia Sur S.A., con sede en Buenos Aires, Argentina, tiene una base de datos de clientes en MySQL con las columnas: nombre, email, telefono, DNI. El servidor de produccion es 190.210.45.12 y tiene la contrasena de root 'admin123'. El jefe de sistemas es Juan Perez. Escribime una query SQL para..."

**Que anonimizar:**
- Nombre de empresa → ?
- Direccion/sede → ? (o dejar Pais por contexto)
- IP del servidor → ?
- Contrasena → ?
- Nombre del jefe → ?

### Prompt 2

> "Tengo un cliente que es Pedro Lopez, DNI 28.456.789, telefono +54 11 4567-8901, email pedrolopez@gmail.com. Quiere un seguro de vida. Sus datos financieros: ingresa $850.000 ARS mensuales, tiene una hipoteca en el Banco Galicia por $45.000.000. Escribime una propuesta de seguro."

**Que anonimizar:**
- Todos los datos personales del cliente.
- Datos bancarios especificos.

### Prompt 3

> "Nuestra startup, DataFlow, esta developing una feature para nuestro producto principal que se llama 'SecureVault'. La feature usa un endpoint en https://api.dataflow.com/v2/sync que toma un token JWT. El token de test es 'eyJhbGciOiJIUzI1...'. Ayudame a debugear este codigo: [codigo propietario pegado aqui]."

**Que anonimizar:**
- Nombre de empresa y producto.
- URL de API (parcial: el path '/v2/sync' puede ser generico).
- Token JWT.
- (La pregunta extra: deberias subir codigo propietario? Que harias?)

### Prompt 4

> "Trabajo en el hospital意大利 de Cordoba. tenemos un paciente que es Marta Dominguez, 58 anos, DNI 23.451.678, con diagnostico de carcinoma ductal infiltrante, estadio IIB, en mama izquierda. El medico tratante es el Dr. Roberto Gomez. Quiero que la IA me ayude a redactar un informe medico para la obra social."

**Que anonimizar:**
- Nombre del hospital (o dejarlo generico?).
- Todos los datos personales de la paciente.
- Nombre del medico.

### Prompt 5

> "Nuestra aplicacion tiene un login en https://app.miempresa.com/login. El usuario admin es 'admin@miempresa.com' con contrasena 'SuperSecret123!'. Hay un bug donde despues de 3 intentos fallidos, no bloquea la cuenta. El codigo fuente del backend esta en un repo privado en GitHub: https://github.com/miempresa/backend. Como lo arreglo?"

**Que anonimizar:**
- URL especifica (dominio).
- Credenciales.
- URL del repo privado.
- (Aca lo critico: por que subirias el repo privado? Que harias?)

---

### Solucionario (revisar despues de intentar)

**Prompt 1 anonimizado:**

> "Nuestra empresa, [EMPRESA_X], con sede en [CIUDAD_X], [PAIS_X], tiene una base de datos de clientes en MySQL con las columnas: nombre, email, telefono, DNI. El servidor de produccion es [IP_X]. Escribeme una query SQL para..."

**Decisiones:**
- La contrasena de root **no se sube en ningun caso**. No hay necesidad de que la IA la sepa para escribir una query.
- El nombre del jefe no es relevante para la query SQL. Se quita.
- Las columnas de la tabla (nombre, email, etc.) son **genericas** — no son sensibles, se pueden dejar.

**Prompt 2 anonimizado:**

> "Tengo un cliente, [CLIENTE_A], que quiere un seguro de vida. Sus datos financieros: ingresa [MONTO_X] mensuales, tiene una hipoteca en [BANCO_X] por [MONTO_Y]. Escribime una propuesta de seguro."

**Decisiones:**
- DNI, telefono, email no son relevantes para la propuesta. Se quitan.
- El monto y el banco pueden dejarse como "[MONTO_X]" y "[BANCO_X]" si el objetivo es que la IA entienda la estructura del cliente. Or pueden dejarse los numeros reales si la persona ya esta anonimizada (no se puede identificar a la persona con solo sus ingresos, en este caso).

**Prompt 3 anonimizado:**

> "Nuestra startup, [EMPRESA_X], esta desarrollando una feature para nuestro [PRODUCTO_X]. La feature usa un endpoint en https://[DOMINIO_X]/v2/sync que toma un token JWT. Ayudame a debugear este codigo: [codigo generico de ejemplo que representa el problema, no el codigo propietario real]."

**Decisiones:**
- El token JWT **jamais** se sube. La IA puede ayudarte sin ver el token real.
- El codigo propietario no se sube: se hace un **codigo de ejemplo** que representa la misma estructura del problema (mismos nombres de funciones genericos, misma logica) sin exponer el codigo real.
- El path '/v2/sync' es generico (se ve en millones de APIs): se puede dejar o cambiar por '[PATH_X]'.

**Prompt 4 anonimizado:**

> "Trabajo en un [TIPO_HOSPITAL_X]. Tenemos una paciente de 58 anos con diagnostico de carcinoma ductal infiltrante, estadio IIB, en mama izquierda. El medico tratante es el [MEDICO_X]. Quiero que la IA me ayude a redactar un informe medico para la obra social."

**Decisiones:**
- El DNI y nombre especifico de la paciente se quitan.
- La edad y el diagnostico se pueden dejar (no permiten identificar a la persona si el nombre ya esta anonimizado).
- El nombre del hospital no es relevante para la redaccion: se quita.
- El nombre del medico: se quita por privacidad del medico tambien.
- (Adicionalmente: al ser informacion medica, deberia usarse plan empresarial o modelo local — jamas el gratuito.)

**Prompt 5 anonimizado:**

> "Nuestra aplicacion tiene un login en https://[DOMINIO_X]/login. El usuario admin es [USER_X] con contrasena [CONTRASENA_X]. Hay un bug donde despues de 3 intentos fallidos, no bloquea la cuenta. Como lo arreglo?"

**Decisiones:**
- El dominio se anonimiza puesto que el problema es generico.
- Las credenciales se quitar (la IA no las necesita para debugear).
- El URL del repo privado jamas se sube. En lugar de eso, se hace un codigo de ejemplo.
- (Esto es el caso perfecto para usar un **modelo local** despues de estudiar las Clases 11.)

---

## Ejercicio 2: Checklist pre-prompt (10 min)

A continuacion te presento **5 intentos de envios a un LLM**. Para cada uno, marca:

- (a) **Que informacion esta a punto de revelarse?**
- (b) **Si se publicara manana en un periodico, estarias bien?**
- (c) **De que plan de IA se trata (gratuito/pago/empresarial)?**
- (d) **Que accion recomendada?** (enviar / anonimizar antes / no enviar / cambiar a plan pago)

### Caso A

> Estudiante quiere pedir a ChatGPT (plan gratuito) que le explique como resolver un problema de derivadas. Pega el enunciado del libro.

### Caso B

> Empleado de una PYME pega el listado de clientes de su empresa en ChatGPT (plan gratuito) para pedir un analisis de ventas.

### Caso C

> Programador freelance usa Claude (plan pago) con zero data retention activo, pega codigo fuente de un cliente para resolver un bug en el codigo.

### Caso D

> Abogado usa ChatGPT (gratuito) para buscar jurisprudencia sobre un caso especifico de un cliente, incluyendo el nombre del cliente.

### Caso E

> Estudiante pega el texto de un trabajo practico para que ChatGPT lo resuma (la consigna es de dominio publico del curso).

---

### Solucionario

**Caso A:**
- (a) Enunciado de derivadas de un libro. Probablemente **no sensible** (educativo).
- (b) Si, no seria ninguna tragedia.
- (c) Gratuito.
- (d) **Enviar tranquilo.** No es dato sensible.

**Caso B:**
- (a) Listado de **clientes** de la empresa. SENSIBLE: datos personales protegidos por GDPR/leyes locales.
- (b) **NO.** Si se publicaria, seria una violacion de datos masiva.
- (c) Gratuito.
- (d) **NO enviar crudo.** Opciones: (1) anonimizar completamente antes (sin nombres de clientes, solo estructura de ventas); (2) usar plan empresarial con contrato; (3) usar modelo local.

**Caso C:**
- (a) Codigo fuente de un cliente. Potencialmente sensible si el codigo es propiedad del cliente.
- (b) Depende de los acuerdos contractuales con el cliente (NDA?). En general NO estaria bien que el codigo del cliente se publique.
- (c) **Plan pago con zero retention** — esto es bueno: los datos no se guardan ni usan para entrenar.
- (d) **Enviar** — pero confirmar con el cliente que autoriza el uso de IA. Idealmente, el contrato del freelance debe permitir IA (con estas garantias).

**Caso D:**
- (a) Nombre del cliente + datos del caso. Sensible por confidencialidad abogado-cliente.
- (b) **NO.** Violacion de secreto profesional.
- (c) Gratuito.
- (d) **NO enviar crudo.** La jurisprudencia per se no es sensible, pero el **nombre del cliente** y los **detalles del caso especifico** si lo son. Anonimizar nombre y datos, dejar solo la pregunta juridica en abstracto. Mejor aun: usar modelo local o plan empresarial.

**Caso E:**
- (a) Consigna de un trabajo practico. Probablemente no sensible.
- (b) Si.
- (c) Gratuito.
- (d) **Enviar tranquilo.** Es texto educativo de dominio publico del curso.

---

## Ejercicio 3: Analisis de casos reales (15 min)

Lee los siguientes casos y responde las preguntas. (Las respuestas estan al final.)

### Caso 1: El abogado que confio en ChatGPT

> En mayo de 2023, el abogado Steven Schwartz uso ChatGPT para preparar un escrito juridico. ChatGPT le dio varios casos legales con citas, fechas y nombres. Schwartz presento el escrito en la corte. Resulto que **todos los casos eran inventados por ChatGPT**. El juez sanciono a Schwartz.

**Preguntas:**
1. Que error psicologico cometio Schwartz?
2. Cual es el concepto de la Clase 1 que explica por que ChatGPT inventa casos que suenan reales?
3. Que deberia haber hecho Schwartz (checklist HITL)?
4. Quien es legalmente responsable: Schwartz o ChatGPT (OpenAI)? Por que?

### Caso 2: Samsung y el codigo fuente

> En 2023, ingenieros de Samsung pegaron codigo fuente secreto en ChatGPT para pedir ayuda. Samsung detecto las fugas y prohibio ChatGPT en toda la empresa.

**Preguntas:**
1. Que regla basica de seguridad se violo?
2. Que deberian haber hecho los ingenieros?
3. Si hubieran tenido un plan empresarial con zero retention, habria estado bien?

### Caso 3: El casamiento de las citas de Einstein

> ChatGPT afirma con seguridad que Einstein dijo: "Si la abeja desapareciera, al hombre le quedarian 4 anos de vida." **Einstein nunca dijo eso.** Es un mito urbano.

**Preguntas:**
1. Por que ChatGPT lo afirma con seguridad si no es verdad? (Pista: seccion 1.3 de los apuntes.)
2. Que nos dice esto sobre la idea de que "si esta bien redactado, debe ser verdad"?
3. Como verificarias si una cita atribuida a alguien es real?

---

### Solucionario

**Caso 1 — Schwartz:**
1. **Antropomorfismo + ilusion de autoridad:** Schwartz trato a ChatGPT como un motor de busqueda con capacidad de razonar. Al ver respuestas con citas plausibles, confio en la **ilusion de autoridad** (esta bien redactado y con tono seguro, debe ser verdad). No verifico.
2. **Arboles de probabilidad (Clase 1):** ChatGPT no "sabe" si un caso existe. Sigue el camino de palabras mas probables. Las combinaciones de "Tribunal Supremo + fecha + nombre de caso + cita" son muy probables porque vio miles de casos reales en sus datos. Produce un caso "plausible" pero inexistente — sigue un "camino rojo" de probabilidad pero sin verificar que el destino existe.
3. **HITL:** Schwartz deberia haber verificado cada caso en LexisNexis o Westlaw **antes** de presentarlo. Googlea el nombre del caso. Comprueba el numero. La verificacion toma 30 segundos por caso y le hubiese evitado la sancion.
4. **Schwartz es responsable.** OpenAI no tiene matricula de abogado, no firmo el escrito, no esta bajo jurisdiccion de la corte. En sus terminos de servicio OpenAI dice explicitamente que el usuario es responsable del output que usa. Schwartz, como profesional licenciado, es el que responde.

**Caso 2 — Samsung:**
1. **Regla**: Nunca subir codigo fuente privado a un plan gratuito. Los ingenieros pasaron **datos sensibles** por un canal que los guardaba y podria usarlos para entrenamiento.
2. **Debian: (a)** usar plan empresarial con zero retention; **o (b)** crear un codigo de ejemplo generico que represente el problema sin exponer el codigo real; **o (c)** usar un modelo local (que veremos en clases avanzadas).
3. **Hasta con zero retention:** hay riesgo de que alguien intercepte el dato en el camino (seccion 2), pero si llegaba solo al servidor y no se guardaba, era mucho mas seguro. Sin embargo, **idealmente** no se sube codigo	propietario a terceros en absoluto sin autorizacion explicita de la empresa.

**Caso 3 — Einstein y las abejas:**
1. **Ilusion de autoridad + estadistica:** En los datos de entrenamiento de ChatGPT, hay miles de menciones de esa falsa cita (es un mito popular que circula desde hace decadas). Para el modelo, es una secuencia de palabras **altamente probable** cerca de "Einstein" y "abejas". Lo dice con seguridad porque suena "normal", no porque sepa si es verdad. La IA no distingue verdad de mentira: distingue probable de improbable.
2. **El sesgo cognitivo de "facilismo":** texot bien redactado con tono seguro engana a nuestro cerebro. Verificar requiere esfuerzo.
3. **Verificacion:** Googlea la cita exacta entre comillas. si es real, aparecera en un sitio confiable (ej. Wikiquote de Einstein, papers academicos, libros publicados). Busca la fuente original (en que documento, en que fecha, dijo eso Einstein?). Si solo aparece en blogs sin fuente verificable, es probable que sea falsa.

---

## Ejercicio 4: Construye tu protocolo (10 min)

Esta es la parte mas importante de la practica. Vas a armar tu propio protocolo de seguridad, en 3 partes. Escribelo en una nota (papel, app de notas, donde quieras) para que tengas siempre a mano.

### Parte 1: Mi checklist pre-prompt personal

Escribe tu version de las **3 preguntas del pre-prompt** (seccion 8.1) adaptadas a tu contexto. Por ejemplo:

> 1. **Estoy a punto de revelar:** [presta atencion a: nombres de empresas, nombres de personas, datos financieros, codigo privado, contrasenas]
> 2. **Si esto se publicaria en el periodico:** [seria un desastre / seria incordio pero no grave / no pasaria nada]
> 3. **Estoy usando plan:** [gratuito - asumir que guardan todo / pago - confirmar ToS / empresarial - zero retention / local - seguro]

### Parte 2: Mi tecnica de anonimizacion favorita

Elige **una tecnica** (de la seccion 8.2) que te resuene y que vas a aplicar como habito cada vez. Ejemplos:

- "Sustituyo todos los nombres propios por [TAG_X] antes de subir"
- "Quito todas las URLs y emails"
- "Borro EXIF de cualquier foto que subo"

### Parte 3: Mi regla HITL personal

Elige en que casos vas a hacer verificacion completa HITL y en cuales te basta con verificacion ligera:

- **Verificacion completa:** (ej: "todo output que voy a entregar a un cliente o publicar")
- **Verificacion ligera:** (ej: "ejercicios de aprendizaje, brainstorming personal")

---

## Ejercicio 5: Reflexion final (5 min)

Responde a las siguientes preguntas (no hay respuestas correctas o incorrectas):

1. **Cual fue el concepto de esta clase que mas te sorprendio?**

2. **A partir de hoy, que vas a hacer distinto cuando uses ChatGPT/Claude/Gemini?**

3. **Tenes alguna duda o algo que no quedo claro?** (traerlo a la sesion de consulta de 20 minutos)

---

## Feedback para el instructor

Si encontras algun error en esta practica, algun caso desactualizado o una explicacion confusa, avisale al instructor. Este taller se mejora cada vez que se dicta.

---

> **Recorda:** la IA no es peligrosa porque sea inteligente. Es peligrosa porque parece inteligente y confiamos en lo que parece. Tu protocolo es tu defensa.