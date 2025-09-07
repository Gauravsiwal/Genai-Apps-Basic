## Genai Frontend Apps Basic Setup
### Getting Started
* Install VS code
* Install jupyter and python extensions.
* Install python from www.python.org
* While intsalling python make sure to add path in environment.
* open cmd and check python --version

### Pushing files to github from local system
* Download Github Desktop
* Open Github desktop and open current repository (top left)
* Select add and select options from clone repositry, create new repository or add existing repository
* click new repository and add the name of repository.
* Select options to add readme file and licences.
* Add local path to push the files from.
* Make sure to make repository public before commiting (By defualt it is private)

### Open VS code, select the created folder and start working...

### Adding API key to local environment
* open cmd or powershell
* type setx GOOGLE_API_KEY "XXXXXXXXXXXX"
* in python script import os
* key = os.getenv('GOOGLE_API_KEY')
* Make sure to configure the api key on stremalit when deploying (Advance Setup)
