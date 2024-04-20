# gRPC-TicTacToe
Tic Tac Toe game using gRPC, where server manages games and client plays.
This game uses gRPC, so that client could run function, which is stored on server.

## To start, open first terminal window in current directory and run:
```bash
python3 src/server.py <server_port>
```
- For example
```bash
python3 src/server.py 9999
```
## Open second terminal for the first player and run:
```bash
python3 src/client.py <server_ip>:<server_port>
```
- For example
```bash
python3 src/server.py localhost:9999
```

## For the second player run previous command
