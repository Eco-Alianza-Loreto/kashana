Kashana
=======

Kashana is an open source logframe manangement tool for planning and evaluating
projects, used and written by `Aptivate <http://aptivate.org/>`_.

Installation
------------

System requirements:

- POSIX-compliant system (tested on Linux)
- Python 2.7
- Node JavaScript platform
- Apache + WSGI
- MySQL
- Recommended at least 1GB of RAM

In the deploy directory, run: ::

    ./bootstrap.py
    ./tasks.py deploy:<environment name>

``<environment name>`` refers to one of the ``local_settings.py.*`` files under ``django/website`` directory.
These contain, amongst other things the details for the MySQL database. So to deploy the ``dev`` environment
you would enter: ::

    ./tasks.py deploy:dev


Usecases
--------
1. A multi-stakeholder and multi-organisation team operates in dozens or hundreds of villages and urban areas across Zambia. They need Android-based support to coordinate their work. They are assessing well-being, using ODK or similar on their tablets / phones. They may also be coordinating the delivery of some services -- perhaps health education, for example. They may be helping people to fill out forms to apply for various types of aid, or to register for different relations with the government bureaucracies. They need to have a well-being assessment tool that tracks the impact of their work and the work of the other development agencies in the area. How do they coordinate their activities? How do they collaborate? How are their documents hosted? Could Kashana be all or part of the solution?
2. Let us imagine that an organisation gets a grant to work with us and their Ghanaian chapter. They would like to provide an inexpensive tool for coordinating the work of their Ghanian chapter via mobile phone or very inexpensive tablet. They also need to show their donors / funders that their work in promoting local participation in Ghana is improving local life outcomes. If Kashana is to help, it needs to provide a way of assessing life impacts (or tracking life impact assessments) as well as coordinating local activities (tasks, calendar, etc. for local teams and a coordinating group).
3. We have a financial tracking system called CASH. The people using CASH want to know how money will be divided up between the different elements of the logframe, and also between the different people who are responsible for spending the money. They are only slightly concerned about tracking impacts within CASH -- as long as the money gets spent and they know what they have to do in order to effectively use their whole budget, they are happy.
4. Various triple-bottom-line companies want to keep track of key performance indicators (outputs) as well as the social and environmental impacts of their work (outcomes), in a way that integrates with their daily work. Kashana might give those small and medium-size ethical businesses a way to manage their workflows and their policies at the same time as tracking impact, in a way that makes it easy to learn and steer. Having a simple way to connect the outputs (what the business is selling) to impacts (of various kinds) within a shared collaboration-support environment (Kashana, the intranet) can let those businesses see what's going on with a minimum of switching back and forth between a dozen different applications or interfaces. Also, it can reduce the need to enter data multiple times.

API
---

All URLS except creation are ``/logframes/<logframe_pk>/<itemtype>/<item id>``
URLS for creation are ``/logframes/<logframe_pk>/<itemtype>``
Actions determined by request type::

   PUT = update
   DELETE = delete
   POST = create

The code to get the logframe exists in ``logframe.views.OverviewMixin``. It's a method called ``get_logframe``.

The code for the backend that does the work on the logframe lives under ``django/website/logframe/api``.

Running Javascript tests
------------------------

If you are using recent Ubuntu, then install npm which will also install nodejs. Because of a name conflict with another package it will be named nodejs instead of node, so you will have to create a symlink yourself (assuming you don't have amateur radio node package installed)::

   sudo ln -s /usr/bin/nodejs /usr/local/bin/node

We'll need phantomjs to run tests::

   sudo npm install -g phantomjs
   sudo npm install -g grunt

Install local dependencies by switching to directory alfie/javascript and running::

   npm install

This will install all the necessary packages including Gulp which we use for
defining and running tasks. Currently following tasks are defined (and at
least somewhat useful)::

   grunt test (runs tests)
   grunt jshint (checks code with JSHint)
   grunt templates (compiles templates to src/lib/templates.js)
   grunt watch (runs JSHint and compiles templates when either change)
   
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

Si está utilizando Ubuntu en version reciente, instale npm que también instalará nodejs. Debido a un conflicto de nombre con otro paquete, se denominará nodejs en lugar de nodo, por lo que tendrá que crear un enlace simbólico usted mismo (suponiendo que no tenga un paquete de nodo de radio amateur instalado):

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
