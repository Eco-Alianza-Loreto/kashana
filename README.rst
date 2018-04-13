Kashana
=======

Kashana es una herramienta de gestión de marco lógico de código abierto para la planificación y evaluación proyectos, usados y escritos por `Aptivate <http://aptivate.org/>` _.

Instalación
------------

Requisitos del sistema:

- Sistema compatible con POSIX (probado en Linux)
- Python 2.7
- Plataforma JavaScript de nodo
- Apache + WSGI
- MySQL
- Se recomienda al menos 1 GB de RAM

En el directorio de implementación, ejecute: ::

    ./bootstrap.py
    ./tasks.py deploy: <nombre del entorno>

``<nombre del entorno>`` hace referencia a uno de los ``local_settings.py.*`` archivos en del directorio ``django / website``.
Estos contienen, entre otras cosas, los detalles de la base de datos MySQL. Entonces, para implementar el entorno ``dev``
ingresarías: ::

    ./tasks.py deploy: dev

Casos de uso
--------
1. Un equipo multiactor y multi-organización opera en docenas o cientos de pueblos y áreas urbanas en todo Zambia. Necesitan soporte basado en Android para coordinar su trabajo. Están evaluando el bienestar, usando ODK o similar en sus tabletas / teléfonos. También pueden estar coordinando la prestación de algunos servicios, tal vez educación sanitaria, por ejemplo. Pueden estar ayudando a las personas a completar formularios para solicitar diversos tipos de ayuda o registrarse para diferentes relaciones con las burocracias gubernamentales. Necesitan tener una herramienta de evaluación de bienestar que rastree el impacto de su trabajo y el trabajo de otras agencias de desarrollo en el área. ¿Cómo coordinan sus actividades? ¿Cómo colaboran? ¿Cómo se alojan sus documentos? ¿Podría Kashana ser todo o parte de la solución?
2. Imaginemos que una organización obtiene una subvención para trabajar con nosotros y su capítulo ghanés. Quieren proporcionar una herramienta económica para coordinar el trabajo de su capítulo de Ghania a través de un teléfono móvil o una tableta muy económica. También necesitan mostrarles a sus donantes / financiadores que su trabajo para promover la participación local en Ghana está mejorando los resultados de la vida local. Si Kashana tiene que ayudar, debe proporcionar una forma de evaluar los impactos de la vida (o hacer un seguimiento de las evaluaciones de impacto de la vida) así como coordinar las actividades locales (tareas, calendario, etc. para los equipos locales y un grupo coordinador).
3. Tenemos un sistema de seguimiento financiero llamado EFECTIVO. Las personas que usan EFECTIVO quieren saber cómo se repartirá el dinero entre los diferentes elementos del marco lógico, y también entre las diferentes personas que son responsables de gastar el dinero. Solo están ligeramente preocupados por el seguimiento de los impactos dentro de EFECTIVO: siempre que gasten el dinero y sepan lo que tienen que hacer para usar de manera efectiva todo su presupuesto, están contentos.
4. Varias empresas triple linea base desean realizar un seguimiento de los indicadores de rendimiento (productos) clave, así como los impactos sociales y ambientales de su trabajo (resultados), de una manera que se integre con su trabajo diario. Es posible que Kashana ofrezca a esas pequeñas y medianas empresas socialmente responsables una forma de administrar sus flujos de trabajo y sus políticas, al mismo tiempo que hace un seguimiento del impacto, de forma que sea fácil de aprender y dirigir. Tener una forma simple de conectar los productos (lo que la empresa está vendiendo) con los impactos (de varios tipos) dentro de un entorno de colaboración compartida (Kashana, la intranet) puede permitir que esas empresas vean lo que está sucediendo con un mínimo de cambio y adelante entre una docena de aplicaciones o interfaces diferentes. Además, puede reducir la necesidad de ingresar datos varias veces.

API
---

Todas las URL excepto la creación son ``/logframes/<logframe_pk>/<itemtype>/<item id>``
Las URL para la creación son ``/logframes/<logframe_pk>/<itemtype>``
Acciones determinadas por tipo de solicitud ::

    PUT = actualización
    DELETE = borrar
    POST = crear

El código para obtener el marco lógico existe en ``logframe.views.OverviewMixin``. Es un método llamado `` get_logframe``.

El código para el backend que hace el trabajo en el marco lógico existe bajo ``django / website / logframe / api``.

Ejecutar pruebas de Javascript
------------------------

Si está utilizando Ubuntu en version reciente, instale npm que también instalará nodejs. Debido a un conflicto de nombre con otro paquete, se denominará nodejs en lugar de nodo, por lo que tendrá que crear un enlace simbólico usted mismo (suponiendo que no tenga un paquete de nodo de radio amateur instalado): ::

    sudo ln-usr / bin / nodejs / usr / local / bin / node

Necesitaremos phantomjs para ejecutar pruebas ::

    sudo npm install -g phantomjs
    sudo npm install -g gruñido

Instale dependencias locales cambiando al directorio alfie / javascript y ejecutando ::

    npm instalar

Esto instalará todos los paquetes necesarios incluyendo Gulp que usamos para
definir y ejecutar tareas. Actualmente se definen las siguientes tareas (y por lo menos algo útil) ::

    grunt test (ejecuta pruebas)
    grunt jshint (verifica el código con JSHint)
    grunt templates (compila plantillas para src / lib / templates.js)
    grunt watch (ejecuta JSHint y compila las plantillas cuando cambia)
