# Simple PY port scanner

This scanner is made with python3 and allows you to scan the ports on a certain ip address

## Installation
Does not require any installation, just python3

## Usage
Run the command below on your console

```bash
python3 scanner.py <ip-address>
```

for help run this command:
```bash
python3 scanner.py -h
```
eg:
```bash
python3 scanner.py 192.168.0. -i 1 -f 65535
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Changelog
- Now you can specify the limits of the ports and added '-help' command
- Runs on all the ports from 1-65000, takes some time...
