# provincial-database-nb
Provincial Database of New Brunswick

## Python Dependencies

* Requests
* Flask
* Json
* Oauth
* Datetime

*Note:* using `pip install [package-name]

## Web Access Setup (home network)

sysctl -w net.ipv4.conf.all.route_localnet=1
iptables -t nat -I PREROUTING -p tcp --dport 80 -j DNAT --to 127.0.0.1:5000
iptables -t nat -L
