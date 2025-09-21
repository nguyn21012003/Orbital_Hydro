# Introduction 

Orbital Hydro is a tool for visualize the orbital of hydrogen atom. 

## Installation

Firstly, create virtual environment for python by using 

```bash
python -m venv env
.\env\Scripts\Activate.ps1
```
If using Linux
```bash
python -m venv env
source .\env\Scripts\Activate.ps1
```

Next, install the requirements.txt by using

```bash
pip install -r requirements.txt
```

## Usage

```bash
python orbital.py
```
You can visual the orbital by via gnuplot

```bash
gnuplot load "drawGP.gnuplot"
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Demo 



<img src="./imgs/310.png" alt="isolated" width="200"/>
<img src="./imgs/321.png" alt="isolated" width="200"/>
<img src="./imgs/320.png" alt="isolated" width="200"/>
