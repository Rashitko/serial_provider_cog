# Serial Cog #
The Serial Cog is a cog for the Up framework which adds the ability to communicate with peripherals via the Serial protocol.

## Installation ##
1. Add the following to `Cogfile.yml`
<pre>
serial_cog:
    pypi: serial-cog
</pre>
2. Run:
<pre>
    up gather
    up register serial_cog
</pre>
If all of the above finishes without error, you are ready to go.

## Usage ##
The Serial Cog adapts the principle of the CommandExecutor. You register action for certain commands and these actions 
will be executed upon receiving the particular command.

### Obtaining reference ###
To obtain reference to the SerialProvider use the following (typically in the `_execute_initialize` method):
```python
self.up.get_module(SerialProvider.__name__)
```

### Initialization ###
During initialization of the Up you are required to set the port and baudrate. To set these attributes use:
```python
serial_provider_module.port = '/dev/some_port' # to set baudrate
serial_provider_module.baud_rate = 9600 # to set baudrate
```

### Start ###
Port is being open in `_execute_start` method. Once the `_execute_start` returns and returns True, the port is open and 
ready to use. Therefore you should make sure the dependent modules will start after the SerialProvider. To do so use
for example the following:
```python
class MyModule(BaseStartedModule):
    LOAD_ORDER = SerialProvider.LOAD_ORDER + 1
    
    # rest of your module
```

### Registering handlers ###
To register handler use the following:
```python
serial_provider.add_handler(cmd_type, handler, payload_size, args)
```
* required  
`cmd_type` - single char used to distinguish between command types  
`handler` - callable which will be called after receiving the command  
* optional  
`payload_size` - int specifying the required size of command payload in bytes, default is 0  
`args` - will be passed to the handler when invoked, default is None

### Sending data ###
To register handler use the following:
```python
serial_provider.send_command(cmd_type, data)
```
* required  
`cmd_type` - single char specifyingthe command type  
* optional  
`data` - bytes which will be transmitted after the cmd_type
