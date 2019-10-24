# nparser
Nginx error log parser.

This project provides a clean parsing of nginx error logs, produced by the
[`error_log`](https://nginx.org/en/docs/ngx_core_module.html#error_log) directive (not
access logs). The implementation is based on
[this](https://stackoverflow.com/a/26125951) stackoverflow answer.


## Installation
```sh
git clone git@github.com:MyMusicTaste/nparser.git
cd nparser
pip install -e .
```

## USAGE

```python
from nparser import parse_line

entry = parse_line('2019/10/01 07:16:38 [warn] 70#0: *3 [lua] balancer.lua:718: redistributeIndices(): [ringbalancer 4] redistributed indices, size=10000, dropped=10000, assigned=0, left unassigned=10000, context: ngx.timer')
print(entry.message)
```


## License
MIT, see `LICENSE.txt`.
