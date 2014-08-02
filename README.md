camouflage
==========
Camouflage is a Python module to hide/unhide sensitive data in your work. Its main application is to protect your credentials embedded in your code when you share it with your collaborators.

Usage
-----
Apart the target file you want to modify, you also need to make a config file in JSON (Support for other formats like YAML, XML, CSV will be added in future) to help know Camouflage what you want to hide.

JSON file should be in the following format:
```JSON
{
    "string you want to hide": "description or identifier"
    ...
}
```

To hide, run
```Shell
$ python3 camouflage.py *targetfilename* --hide --config configfile.json
```

To unhide, run
```Shell
$ python3 camouflage.py *targetfilename* --unhide --config configfile.json
```

If you don't provide --config option, it'll use ./camouflage.json by default. --hide is optional, too.

Manual
------
```Shell
usage: camouflage.py [-h] [-s | -u] [-c CONFIG] target

Camouflage

positional arguments:
  target                Specify the target file

optional arguments:
  -h, --help            show this help message and exit
  -s, --hide            Hide stuff
  -u, --unhide          Unhide stuff
  -c CONFIG, --config CONFIG
                        Specify the config file (Default is ./camouflage.json)
```