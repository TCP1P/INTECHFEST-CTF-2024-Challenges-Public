trafic-capture-conf:
	docker network create challenges -d bridge --subnet 192.168.133.0/24
sync:
	~/go/bin/ctfify gzcli --sync
start:
	~/go/bin/ctfify gzcli --run-script start
stop:
	~/go/bin/ctfify gzcli --run-script stop
register-all-user:
	~/go/bin/ctfify gzcli --create-teams "https://docs.google.com/spreadsheets/d/fake/gviz/tq?tqx=out:csv"
send-email:
	~/go/bin/ctfify gzcli --create-teams-and-send-email "https://docs.google.com/spreadsheets/d/fake/gviz/tq?tqx=out:csv"
