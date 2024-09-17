# Enciclopedia Wiki

Este proyecto es una implementación de una enciclopedia estilo Wiki. Permite a los usuarios visualizar, crear, buscar y editar entradas de enciclopedia en formato Markdown. A continuación, se detallan las características y el uso del sitio.

## Páginas y Funcionalidades

### 1. Página de Entrada (`/wiki/TITLE`)

- **Descripción**: Muestra el contenido de la entrada de enciclopedia con el título especificado en la URL (`/wiki/TITLE`).
- **Características**:
  - La vista obtiene el contenido de la entrada llamando a la función adecuada.
  - Si la entrada no existe, se muestra una página de error indicando que la página no fue encontrada.
  - Si la entrada existe, se muestra el contenido con el título de la entrada.

### 2. Página de Índice 

- **Descripción**: Muestra una lista de todas las entradas de enciclopedia.
- **Características**:
  - Los nombres de las entradas están enlazados para que los usuarios puedan hacer clic y acceder a cada entrada.

### 3. Búsqueda

- **Descripción**: Permite a los usuarios buscar entradas de enciclopedia.
- **Características**:
  - El usuario puede escribir una consulta en el cuadro de búsqueda.
  - Si la consulta coincide con el nombre de una entrada, se redirige al usuario a esa entrada.
  - Si la consulta no coincide, se muestra una página de resultados de búsqueda con una lista de entradas que contienen la consulta como subcadena.

### 4. Nueva Página

- **Descripción**: Permite a los usuarios crear una nueva entrada en la enciclopedia.
- **Características**:
  - El usuario puede ingresar un título y el contenido en formato Markdown.
  - El usuario puede hacer clic en un botón para guardar la nueva página.
  - Si ya existe una entrada con el título proporcionado, se muestra un mensaje de error.
  - Si no existe, se guarda la entrada y se redirige al usuario a la página de la nueva entrada.

### 5. Página de Edición

- **Descripción**: Permite a los usuarios editar el contenido de una entrada existente.
- **Características**:
  - La página de edición se accede desde un enlace en cada entrada.
  - El contenido Markdown existente se muestra en un área de texto (`textarea`).
  - El usuario puede guardar los cambios, lo que actualiza la entrada y redirige al usuario a la página de la entrada.

### 6. Página Aleatoria

- **Descripción**: Permite al usuario acceder a una entrada aleatoria de la enciclopedia.
- **Características**:
  - Se accede al hacer clic en "Página aleatoria" en la barra lateral.

## Instalación

1. **Clonar el Repositorio**

    ```bash
    git clonehttps://github.com/juanjose23/Wiki.git
    cd wiki
    ```

2. **Instalar Dependencias**

    - Asegúrate de tener Python instalado.
    - Instala las dependencias necesarias (como `markdown2` para la conversión de Markdown a HTML).

    ```bash
    pip3 install markdown2
    ```

3. **Ejecutar el Servidor**

    - Ejecuta el servidor de desarrollo. Dependiendo de la configuración, esto puede hacerse con un comando como:

    ```bash
    python manage.py runserver
    ```

## Uso

1. **Página de Entrada**: Accede a cualquier entrada utilizando la URL `/wiki/TITLE`.

2. **Página de Índice**: Navega por la lista de todas las entradas en la página principal (`index.html`).

3. **Búsqueda**: Utiliza el cuadro de búsqueda para encontrar entradas. Accede a la página de resultados si no hay coincidencias exactas.

4. **Nueva Página**: Crea una nueva entrada accediendo a la opción "Crear nueva página" y guarda el contenido.

5. **Edición**: Edita una entrada existente desde la página de la entrada.

6. **Página Aleatoria**: Accede a una entrada aleatoria desde la opción "Página aleatoria" en la barra lateral.

## Contribuciones

Si encuentras algún error o deseas realizar mejoras, siéntete libre de bifurcar el repositorio y enviar solicitudes de extracción.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
