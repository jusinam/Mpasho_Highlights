# MPasho HighLights
Mpasho is a news highlight application that gives access to the users about what is happening worldwide. The application posses news from different sources.

## Author
* Evans Nyambane

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Showcasing news | Navigate through | Read requested news |

## Installation Requirements
* ` python3.6 ` 
* ` pip `
* ` flask `

Get the installation guide [here](https://www.python.org/)

## Set-up
Open your terminal and run:

* ` git clone https://github.com/DjCooGie/Mpasho_Highlights.git `

* ` cd project root directory `

* ` python3.6 -m venv --without-pip virtual ` to create a virtual environment

* ` source virtual/bin/activate ` to activate the virtual environment

* ` curl https://bootstrap.pypa.io/get-pip.py | python `

* ` pip install flask `

* ` deactivate ` to exit the virtual environment

* **`pip install -r requirements.txt`** to download all dependencies in the requirements.txt

Visit the [NEWS API](https://newsapi.org/) website, sign up for a free account and generate an API key. 

Create a .sh (shell)file in your root directory called **start.sh** and in it, type;
* **`export API_KEY="<your-api-key>"`**
* **`python3 manage.py server`** 

In your terminal;

* `chmod +x start.sh` to make the shell file from executable
* `./start.sh` to launch the application

Open **http://127.0.0.1:5000/** on your preffered browser

## Technologies Used
* Python 3.9
* Flask 
* Bootstrap
* Flask-Script
* Jinja2 

#### Known Bugs
No known bugs

#### Collaborate
>Incase of any questions, problems ideas concerning the app, feel free to reach out to me:
>>Github: [Evans Nyambane](https://github.com/DjCooGie)
>>Email: evansonchagwa01@gmail.com

#### License
MIT
&copy;2019 Evans Onchagwa
