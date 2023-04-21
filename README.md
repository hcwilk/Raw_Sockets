## Requirements

- Linux
- Python 3.6 or higher

## Usage

- Right now, this is purely for me to learn how to utilze raw sockets in my Linux VM.
- I'll try to expand this to recreate common protocols (TCP,UDP) to better understand how they communicate


### Server

```
sudo python server.py $INTERFACE
```

### Client

```
sudo .python client.py $DESTINATION_MAC_ADDRESS $SOURCE_INTERFACE
```
