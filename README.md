# Sistema gestor de alumnos UNSAM
Contexto teorico. ![link](https://github.com/AdrianPerez0306/gestorAlumnos/blob/42ace063c036c55184657ba6f19447c937ccb2e3/TP%20Base%20de%20datos%202024%20UNSAM.pdf)

## Instalación :hammer_and_wrench: 
Este desarrolo fue realizado en un entorno de `OS debian ubuntu 22.04`, [`python 3.11`](https://www.pgadmin.org/) en adelante, [`PostgreSQL`](https://www.postgresql.org/) con [`PgAdmin`](https://www.pgadmin.org/).

`Python on Ubuntu 22.04`
```bash
sudo apt update
sudo apt install python3
```
```bash
python3 --version
```
```bash
python3 pip install pandas
```
`PostgreSQL`
Acorde a [`PostgreSQL`](https://www.postgresql.org/download/linux/ubuntu/):
```bash
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
```
`PgAdmin`
Acorde a [`PostgreSQL`](https://www.postgresql.org/download/linux/ubuntu/):
```bash
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
```

Una vez tenemos instalado `python`, podemos comenzar el preprocesado. Partiendo del archivo [`raw-data.csv`](preprocessing/raw-data.csv) tenemos labels/columnas de la siguiente forma:

![image](https://github.com/user-attachments/assets/27a3ff0b-410a-4128-adc2-1f1714e79533)

Abrimos [`preprocessing.py`](preprocessing/preprocessing.py) y ejecutamos el script:
```bash
python preprocessing.py
```
Esto generara una serie de `archivos.csv`, que corresponden a los datos necesarios para realizar la carga dentro del sistema `PostgreSQL`
NOTA: Dentro script `preprocessing.py` se encuentra el path donde se descargaran los archivos. MODIFICAR ESTE PATH SEGUN SU O.S

![image](https://github.com/user-attachments/assets/a36596e0-0898-4533-9ef2-7624dd4ab945)

Una vez ejecutado, en el `path` que haya configurado en el script `preprocessing.py`, deberian aparecer una serie de archivos:

![image](https://github.com/user-attachments/assets/9d63581d-5389-4f5b-9fb0-9c8134cf3d9c)

Una vez con estos archivos en la carpeta correspondiente, procedemos a abrir `PgAdmin`. A partir de aqui hay 2 caminos posibles:

### 1 - Construccion del sistema de base de datos desde querys.
#### Pasos a seguir
##### a) Crear un server en PgAdmin.

![image](https://github.com/user-attachments/assets/3a22f8bb-34f5-4b8f-a55d-aeaa2466b365)

Determinar el nombre del server.

![image](https://github.com/user-attachments/assets/6d289825-8848-495f-bfe2-e0e0ec9668ba)

Una vez creado el server deberia verse un panel como el siguiente:

![image](https://github.com/user-attachments/assets/f413e971-1a44-4d10-9789-6a8ddee8bc7e)

Con el server ya creado procedemos a utilizar la query tool que provee `PostgreSQL`:
![image](https://github.com/user-attachments/assets/7bc8605f-209c-4888-a69e-d092fec69446)
![image](https://github.com/user-attachments/assets/dc254c26-a05d-4f2e-af2e-e15b8c49ddc9)


##### b) Ejecutar querys.
Una vez en el panel de querys, procedemos a ejecutar las querys. 
i) Ejecutar todos los querys en el folder `procedures_calls`
IMPORTANTE: Si quiere ejecutar las `procedures_calls` primero debe copiar los archivos dentro de `procedures` y ejecutarlos dentro de la query tool.

  `call_init` -> `call_load_column` -> `call_load_alumnos`
  Una vez ejecutados los querys, deberia estar creadas las tablas y cargados los datos de los archivos correspondientes.
  A partir de aqui, ya se pueden realizar consultas.
  
![image](https://github.com/user-attachments/assets/4b53691a-54c0-4a78-8cfc-3573c5f7b54d)


### 2 - Importar el archivo `SERVER.json`.
Dentro de `pgAdmin` seleccionar `Tools`-> `Import/Export server` -> Seleccionar `SERVER.json` ->  

Si es la primera vez que corremos el proyecto, nos va a crear un montón de ejemplos de cómo testear, en caso contrario nos va abre el ambiente de desarrollo de cypress que tiene la siguiente pinta:

![video](video/cypress2022.gif)

En la primera pantalla nos muestra los archivos de tests que escribimos, los clickeamos y abre un navegador y empieza a correr nuestros tests. Pero ¡ojo! tenemos que tener nuestra aplicación levantada para poder correr los tests

¿Y cómo se hace eso ?

```bash
npm run start
```

Una vez levantado podemos correr el comando `open` de cypress, pero antes debemos modificar el archivo *cypress.config.js* para que la url base de los tests sea `localhost:3000` (puerto en el cual levantamos nuestra app).

```js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  video: false,
  e2e: {
    // We've imported your old cypress plugins here.
    // You may want to clean this up later by importing these.
    setupNodeEvents(on, config) {
      return require('./cypress/plugins/index.js')(on, config)
    },
    baseUrl: 'http://localhost:3000',
  },
})
```

ponemos `video` en `false` para que no grabe los tests 

### Cómo se escribe un test

Vamos a seguir usando los `describe` y `it` de jest y los hooks cómo  `before, beforeAll, beforeEach` , solo que ahora utilizaremos el objeto `cy` que nos va a permitir testear

```javascript
/// <reference types="Cypress" />

const MILLAS_SELECTOR = '[data-testid=millas]'
const KMS_SELECTOR = '[data-testid=kms]'
const ERROR_SELECTOR = '[data-testid=error]'

describe('Caso feliz', () => {
  before(() => {
    cy.visit('/')
  })
  it('escribimos un numero positivo de millas a convertir', () => {
    cy.get(MILLAS_SELECTOR)
      .type(10).should('have.value', '10')
  })
  it('y se tranforma a kilometros', () => {
    cy.get(KMS_SELECTOR).contains('16,093')
  })

})
describe('Caso 0', () => {
  before(() => {
    cy.visit('/')
  })
  it('escribimos 0 en las millas a convertir', () => {
    cy.get(MILLAS_SELECTOR)
      .type(0).should('have.value', '0')
  })
  it('y en los kilometros vemos 0', () => {
    cy.get(KMS_SELECTOR).contains('0')
  })

})
describe('Caso alfabetico', () => {
  before(() => {
    cy.visit('/')
  })
  it('escribimos un valor que no es un numero en el input', () => {
    cy.get(MILLAS_SELECTOR)
      .type('1.*-*/*').should('have.value', '1.*-*/*')
  })
  it('y aparece un cartel de error avisandonos que no es un input valido', () => {
    cy.get(ERROR_SELECTOR)
  })

})
```

Separamos los describes por *flujos* de nuestra aplicación y hacemos uso de `data-testid` para no acoplarnos a los atributos de html.

La línea `/// <reference types="Cypress" />` a comienzo de nuestro archivo de tests activa nuestro IDE para que utilice sugerencias sobre las funcionalidades de cypress.

La funciones que usamos de cypress son:

- `cy.visit` => para visitar una url de nuestra aplicación
- `cy.get` => obtenemos un elemento del DOM en base a un selector
- `cy.type` => escribimos en un input

## ¿Y Github Actions? :construction_worker_man: 

Bueno cypress en su [pagina](https://docs.cypress.io/guides/guides/continuous-integration.html#Setting-up-CI) nos comenta cómo integrar con nuestro CI de turno, estos test e2e.

Nosotros nos basamos en [este archivo](https://github.com/cypress-io/cypress-example-kitchensink/blob/master/.github/workflows/chrome-headless.yml) para crear el nuestro, borrando código redudante y demás yerbas.

Pero como hemos vimos antes,tenemos que tener la aplicación corriendo para poder testearla.... y ¿cómo hacemos eso en CI?

Fácil, creamos dentro de nuestro `package.json` los siguientes comandos:

```json
{
  "cy:open": "cypress open",
  "cy:run": "cypress run",
  "cy:ci": "start-server-and-test start 3000 cy:run",
  "cy:verify": "cypress verify",
}
```

- `npm run cy:ci` levanta nuestra aplicación y espera a que este completamente levantada para seguir al próximo paso (usamos una biblioteca llamada start-server-and-test para esperar)

para instalar `start-server-and-test` : `npm install wait-on -D`

- `yarn run cy:ci` corre nuestros tests en modo Continuous Integration
- `yarn run cy:verify` chequea la instalación de CI en el ambiente
