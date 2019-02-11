# 1 Cryptonite

__Pregunta: ¿Es suficiente verificar que el dominio es válido?__

No, la clave podría comprometerse si de forma local tenemos algún tipo de malware que pueda robarnos las claves.


# 2 Metamask

Funciona, he recuperado la cuenta en Firefox a través de las 12 palabras.¨

# 3 Geth

Lance la red rinkeby con Geth en modo nodo ligero añadiendo el parámetro --syncmode "light":
$ geth -rinkeby --syncmode "light"
¿Qué diferencia aprecia respecto a la sincronización full (por defecto)?
>Solamente está descargando las cabeceras de los bloques en vez de descargarlos completos.

Ejecute el siguiente comando en otro terminal:
$ du -hs ~/.ethereum/rinkeby/geth/lightchaindata
¿Cuando espacio en disco ocupa el siguiente directorio?
> 32MB 

# 4 Parity

Funcionando, descarga las cabeceras.

# 5 Solidity

Después de asignar un número demasiado grande para un "uint" el valor almacenado en la variable se ha roto en tres y además no representa el número introducido: 
BigNumber { s: 1, e: 39, c: [ 100000000000, 0, 101 ] }

# 6 SOLC

__¿En qué unidad le devuelve el gas?__

======= simpleStorage.sol:SimpleStorage =======
Gas estimation:
construction:
   117 + 66000 = 66117
external:
   add(uint256):	20437
   get():	446
   set(uint256):	20253
