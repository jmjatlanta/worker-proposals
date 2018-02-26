# Running a bitshares api node

## Introduction

A Bitshares API Node is a `witness_node` instance specially configured to serve applications with data endpoints. Any bitshares application (gateway, explorer, wallet, trading program, etc) interacts with the decentralized network (blockchain) by connecting to one or many api nodes.

If you plan to run a business on top of bitshares you will probably want to own one or several api nodes. Public nodes can be used, but they are very busy and often run old versions. In addition, the more api nodes around the better for the network and end users.

This tutorial is for users that already have `witness_node` compiled successfully.

## Running a basic api node

We have `witness_node` executable and we know we can run it within a terminal. The first thing is to check the options available:

`./programs/witness_node/witness_node --help`

It is important to know which version you are using to know what to expect from a node. Get the version of the node by using the `--version` flag:

`./programs/witness_node/witness_node --version`

The basic api node will run by:

`./programs/witness_node/witness_node --rpc-endpoint "127.0.0.1:8090"`

With the above command you are starting a node that will listen for api calls at port 8090, that originate only on that machine. This can be changed to listen on any IP address within this machine, which could be accessible from the internet, or perhaps just your local area network.

By default, the blockchain directory will be `witness_node_data_dir`. But you may specify a different directory, for example:

`./programs/witness_node/witness_node --rpc-endpoint "127.0.0.1:8090" --data-dir data/my-blockprod`

Depending on your hardware and use purposes of your api node, you will probably start it with some custom parameters, enabling and disabling plugins. This will be explained as we go.

Certain options to the witness_node can be added to the config file or passed on the command line as we did above. Check the default `config.ini` created within the `witness_node_data_dir` that was created the first time you started the witness_node. Reading the config.ini will give you an idea on how you can customize it.
 
A typical node may be started by something like:

`programs/witness_node/witness_node --data-dir data/my-blockprod --rpc-endpoint "127.0.0.1:8090" --max-ops-per-account 10000 --partial-operations true`

Above we limit the operations per account to 1000 to save RAM. This is the default behaviour for newest versions of `witness_node` as a full node needs more than 80GB of RAM to run.

We call an api node a "full node" when it has all the account history from all the accounts in the bitshares blockchain. As the amount of RAM needed is so big and increasing, these kinds of nodes are each becoming more rare.

Look in the terminal for messages like:

```
1256186ms th_a       application.cpp:499           handle_block         ] Got block: #10000 time: 2015-10-13T23:15:42 latency: 73184714186 ms from: cyrano  irreversible: 9976 (-24)
1267475ms th_a       application.cpp:499           handle_block         ] Got block: #20000 time: 2015-10-14T07:37:33 latency: 73154614475 ms from: bitcube  irreversible: 19975 (-25)
```

If you see this, the blockchain is successfully synchronizing. Completing the sync is a long process that depends a lot in your hardware. While you see the blocks coming in the witness node terminal, you that you are on a good track.

## Running a production api node

For a production api node there are several options depending in your OS. A few of them are:

### GNU screen

This is the easy way. Start a `screen` terminal and run your node on it as: https://github.com/bitshares/bitshares-core/wiki/Manage-your-nodes-by-using-gnu-screen

This works but it is not highly recommended. Upon a reboot the node admin will need to run everything again.

### As linux service

In order to run a node by service you need to ...

get documentation

### Docker

get documentation

### Others?

get documentation

## Performance tip

You can improve performance for API nodes by running the following before starting a node:

```
sudo sysctl -w net.core.somaxconn=65535
```

## Secure your websocket connection

get help

## Full classic node

In bitshares a full node is a node that haves all the account history for all the network users. This setup uses a lot of RAM so nodes by default dont run this way anymore. If you want to run a full node start it by:

`command`

## Elasticsearch node

Another way to have all the account history plus improved capability to search throw it than the classic node you can run your node with elasticsearch plugin.

Elasticsearch installation guide can be found at:

https://github.com/bitshares/bitshares-core/wiki/ElasticSearch-Plugin

To start a node with elasticsearch plugin activated use:

`command`

## Run python wrappers

Add something.

NGINX.

## Connecting to your api node

There are 2 ways to connect to your api node:

- By RPC calls.
- By Websocket.

Both of them will return the response in JSON format.

### RPC

RPC calls are one time calls made to the api node each time. You send a command, and the server returns something. The connection ends there.

The easiest way to make these types of calls is by using the curl command line. For example:

`curl command`

Curl can also make calls that include authentication, this is for wallet type applications that need to be logged in to access restricted account data.

Here is how this is done:

`command authenticated curl call`

Curl is not the only option to make rpc calls to the api server. In fact almost all programming languages will offer a built in library or third party addons to make this calls.

It is possible to make rpc calls with php, python, and javascript just to name a few.

### Websocket

From the command line, bitshares developers use the `wscat` tool to connect to an api node. The main difference with using websocket versus rpc calls is that websocket connections remain connected, even after a call is complete. This way, you can "subscribe" to updates, and the server can send the updates in real-time. Lets see how that works with an example. 

Connect to a bitshares node with `wscat`:

`wscat -c wss://bit.btsabc.org/wss`

If you see the following the program is waiting for commands:
```
connected (press CTRL+C to quit)
> 
```

Log in to access restricted apis:

```
```

Subscribe to network events and receive data in real time:
```
example for wscat receiving real time data
```

More on websocket subscriptions here: https://github.com/bitshares/bitshares-core/wiki/Websocket-Subscriptions

For scripting websockets we recommend using `wsdump`, very similar tool as `wscat` but easier to make scripting over it. More info at https://github.com/bitshares/bitshares-core/wiki/Scripting-websockets-easy

The same as with the rpc calls almost all languages will have a built in or addon to work with a websocket.

#### Connect the cli wallet

The `cli_wallet` is part of the `bitshares-core` project and use a websocket address to connect to a node and send/receive data.

Connect the `cli_wallet` to your node with a command like:

`./programs/cli_wallet/cli_wallet -s wss://bit.btsabc.org/wss`

For more info on the command line wallet see: https://github.com/cryptonomex/graphene/wiki/CLI-Wallet-Cookbook
