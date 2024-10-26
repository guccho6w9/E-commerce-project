# E-commerce-project

## Inicia el proyecto 

_Lo primero que deberas hacer es clonar el repositorio en tu maquina. Para eso después de que ya hayas creado un repositorio local deberas ejecutar los siguientes comandos_

```sh
git clone https://github.com/guccho6w9/E-commerce-project.git
```

_Verifica que estes en la rama main del proyecto. Una vez ya estes en la main es necesario que levantes el front para eso abre una terminal y ejecuta los siguientes comandos:_

```sh
cd frontend

python main.py
```

_Tambien puedes buscar el archivo y una vez en el mismo inicias el Run Python File._

_El siguiente paso para levantar el proyecto es levantar el backend_

```sh
cd backend

uvicorn backend.api:app --reload
```

## Intalación sqlAlchemy y psycopg2

```sh
pip install SQLAlchemy psycopg2
```

