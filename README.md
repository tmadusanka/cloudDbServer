# cloudDbServer

# Setup 
- py -m venv env 
- env\Scripts\activate

-pip install flask 
-pip install firebase_admin 
-pip install requests 

# Run server 
- python app.py

# Generate initail database 
- cd dbGenrate 
- python genDb.py ( this will clean existing database )

# Test
- pip install pytest

- py.test testWeb.py
