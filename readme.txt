### BubbleSort & LinearSearch ###

░░░░░░░░░░░░☼░░░░░░░░░
░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
░░░░░░▐▌░░░░▀▀███████▀
▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒

Por: Rosales Herrera Jonathan Adrian
No. de Cuenta: 317243286
Materia: Computación Concurrente
01/12/2022

─▌█──║─║╔═║─║─╔═╗─
─███─╠═╣╠═║─║─║─║─
─▐█▐─║─║╚═╚═╚═╚═╝─
─▐▐───────────────
─▐▐───────────────

Esta aplicación realiza los algoritmos BubbleSort y LinearSearch a través de un servidor web.

*** MANUAL DE USUARIO***

* Iniciar servidor con Django, en cmd desde la carpeta djangoProyect, ejecutar
        ---> python manage.py runserver

** Acceder a la URL del servidor y agregar los parámetros de la vista "view/nodeCuenta"
        ---> http://127.0.0.1:8000/main/317243489 (Sustituir con número de cuenta a buscar en un rango (317243286, +5_000))
        
        views:
            -- main
            -- concurrente
    
*** Espere mientras carga la ejecución
        --Espera promedio secuencial: s
        --Espera promedio concurrente: 210 s

**** Resultados.
        posición = -1 --> No encontrado
        otro caso, posición en que se encuentra


!!! SUGERENCIA !!!

Modificar  el llamado a las funciones en la linea 43 y 95 de 'views.py' para realizar múltiples intentos de búsqueda sin ordenar,
saltando tiempos de espera. 


▒▒▒▒▒▒▐███████▌▒▒▒▒▒▒▒
▒▒▒▒▒▒▐░▀░▀░▀░▌▒▒▒▒▒▒▒
▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌▒▒▒▒▒▒▒
▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄▒
▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐▒
▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▒▒
░╔╗╔╗╔╗╦╗░╦╗╗╦╔╗╗╔╔╦╗░
░║╦║║║║║║░║║║║║╦╠╣░║░░
░╚╝╚╝╚╝╩╝░╩╚╝╩╚╝╝╚░╩░░
▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▒▒

