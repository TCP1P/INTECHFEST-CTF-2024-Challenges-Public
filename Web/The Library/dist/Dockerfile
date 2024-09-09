FROM mcr.microsoft.com/dotnet/aspnet:7.0

RUN useradd -m ctf

COPY flag.txt /flag.txt
RUN mv /flag.txt /flag_`cat /proc/sys/kernel/random/uuid`.txt

RUN chown root:root /flag_*.txt
RUN chmod 444 /flag_*.txt

WORKDIR /app/src

COPY src .
RUN chown -R root:root /app
RUN chmod -R 755 /app

RUN chown -R root:root /tmp
RUN chmod -R 700 /tmp

RUN rm -rf System.Diagnostics.Process.dll

ENV COMPlus_EnableDiagnostics=0

USER ctf
ENTRYPOINT ["dotnet", "CRUD.dll", "--urls", "http://*:8181"]
